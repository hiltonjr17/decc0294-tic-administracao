#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
 ATIVIDADE DO MODULO 9 - Automacao de documentos
 DECC0294 - UFMA - Curso de Administracao - 2026.2
=============================================================================

O QUE ESTE ARQUIVO E
    Um unico script que separa a parte fixa do seu documento das variaveis
    que mudam a cada execucao, gera um documento por linha da tabela, e mede
    se a automacao compensa.

COMO USAR (peca ao agente, no opencode desktop)

    1) "execute atividade_modulo9.py com o comando iniciar"
       Cria o modelo em prompts/modulo9-modelo.md, a tabela de variaveis em
       dados/modulo9-variaveis.csv e o formulario de medicao em
       entregas/modulo9-fluxo.csv

    2) Adapte o modelo ao seu documento e preencha tres linhas de variaveis.

    3) "execute atividade_modulo9.py com o comando gerar"
       Produz um documento por linha em saidas/, so com o texto que fica
       entre a linha "## Documento" e a linha "---" do modelo. Avisa variavel
       sem valor, coluna sem uso e colchete que nao segue a regra de nome
       (maiusculas de A a Z, algarismos e sublinhado).

    4) "execute atividade_modulo9.py com o comando conferir"
       Valida a medicao, calcula em quantas execucoes o investimento se paga,
       ja descontado o tempo de manutencao, e gera entregas/modulo9-relatorio.md

    Sem nenhum comando, o script imprime estas instrucoes.

A REGRA QUE O SCRIPT APLICA
    Ganho declarado sem os tres tempos nao conta. O tempo manual e estimado
    (lembrado da ultima execucao). O tempo automatizado e o de construcao sao
    medidos. Variavel usada no modelo sem coluna correspondente na tabela
    interrompe a geracao, porque o documento sairia com o marcador no lugar
    do valor.

Nao precisa instalar nada. Roda com o Python que ja vem com o ambiente.
=============================================================================
"""

import csv
import os
import re
import sys
import unicodedata
from datetime import date

# Quando o script esta na pasta scripts/ do repositorio, as pastas de trabalho
# (dados/, entregas/, saidas/, prompts/) ficam um nivel acima. Copiado para a
# raiz do projeto do aluno, o script roda onde esta, sem mudanca.
_AQUI = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(_AQUI) == "scripts":
    os.chdir(os.path.dirname(_AQUI))

SEP = ";"
MODELO = os.path.join("prompts", "modulo9-modelo.md")
VARIAVEIS = os.path.join("dados", "modulo9-variaveis.csv")
FLUXO = os.path.join("entregas", "modulo9-fluxo.csv")
RELATORIO = os.path.join("entregas", "modulo9-relatorio.md")

COLS_FLUXO = ["item", "valor", "observacao"]
ITENS_FLUXO = [
    ("tempo_manual_minutos", "", "estimado: quanto a tarefa levava por execucao, antes"),
    ("tempo_automatizado_minutos", "", "medido: quanto leva agora, incluindo conferencia"),
    ("tempo_construcao_minutos", "", "medido: quanto voce gastou construindo o fluxo"),
    ("execucoes_por_ano", "", "quantas vezes a tarefa e feita por ano"),
    ("manutencao_minutos_por_ano", "", "estimado: minutos por ano para ajustar o fluxo"),
    ("passo_irreversivel", "", "onde o fluxo se torna irreversivel"),
    ("o_que_se_confere", "", "no maximo dois itens"),
    ("cargo_responsavel", "", "o cargo, nao a pessoa"),
    ("se_a_conferencia_falhar", "", "o que se faz"),
]

TEXTO_MODELO = """# Modelo de documento

Responsavel por este modelo: PREENCHER
Ultima revisao: PREENCHER

## Regra para dado ausente

Se alguma variavel vier vazia, escrever NAO INFORMADO no lugar e acrescentar
um aviso no inicio do documento listando os campos faltantes.

## Documento

RELATORIO MENSAL DE [AREA]
Periodo de referencia: [MES_REFERENCIA]
Unidade: [UNIDADE]

No periodo de referencia foram registrados [QUANTIDADE] atendimentos, contra
a meta de [META] estabelecida para o periodo. O custo total apurado foi de
R$ [CUSTO_TOTAL].

Observacao do responsavel: [OBSERVACAO]

Elaborado por [RESPONSAVEL] em [DATA_ELABORACAO].

---

COMO ADAPTAR ESTE MODELO

1. Substitua o texto entre "## Documento" e "---" pelo seu documento real.
   So esse trecho entra nos documentos gerados. Responsavel, data de revisao
   e regra para dado ausente ficam apenas aqui no modelo.
2. Troque por marcadores entre colchetes tudo que muda a cada execucao.
3. Use nomes descritivos, em maiusculas, sem acento e sem espaco:
   [MES_REFERENCIA] e nao [X1], [mes] ou [MÊS].
4. Nenhum numero fixo dentro do texto: meta e valor de referencia sao variaveis.
5. Cada marcador precisa de uma coluna com o mesmo nome em
   dados/modulo9-variaveis.csv
"""

PADRAO_MARCADOR = re.compile(r"\[([A-Z0-9_]{2,})\]")
# Qualquer trecho entre colchetes na mesma linha. Ficam de fora o link de
# Markdown ([texto](endereco)) e a caixa de selecao ([ ] ou [x]).
PADRAO_COLCHETE = re.compile(r"\[([^\[\]\n]{1,60})\](?!\()")


def titulo(t):
    print()
    print("=" * 74)
    print(" " + t)
    print("=" * 74)


def sem_acento(txt):
    txt = unicodedata.normalize("NFKD", txt or "")
    return "".join(c for c in txt if not unicodedata.combining(c))


def corpo_do_documento(texto):
    """Devolve (corpo, achou_secao).

    O corpo e o trecho entre a linha "## Documento" e a linha "---" que
    antecede COMO ADAPTAR ESTE MODELO. Sem a linha "## Documento", usa todo o
    texto acima de COMO ADAPTAR ESTE MODELO, como nas versoes anteriores.
    """
    acima = texto.split("COMO ADAPTAR ESTE MODELO")[0]
    linhas = acima.splitlines()
    inicio = None
    for i, l in enumerate(linhas):
        if l.strip().lower().rstrip(":") in ("## documento", "##documento"):
            inicio = i + 1
            break
    achou = inicio is not None
    if achou:
        linhas = linhas[inicio:]
    # retira linhas vazias e a linha --- do fim
    while linhas and linhas[-1].strip() in ("", "---"):
        linhas.pop()
    while linhas and not linhas[0].strip():
        linhas.pop(0)
    return "\n".join(linhas) + "\n", achou


def marcadores(texto):
    corpo, _ = corpo_do_documento(texto)
    return sorted(set(PADRAO_MARCADOR.findall(corpo)))


def nao_reconhecidos(corpo):
    """Trechos entre colchetes que nao seguem a regra de nome do marcador."""
    achados = []
    for m in PADRAO_COLCHETE.findall(corpo):
        if PADRAO_MARCADOR.fullmatch("[%s]" % m):
            continue
        if m.strip().lower() in ("", "x"):
            continue
        sugestao = re.sub(r"[^A-Z0-9_]", "", sem_acento(m).upper().strip()
                          .replace(" ", "_").replace("-", "_"))
        achados.append((m, sugestao))
    vistos, unicos = set(), []
    for m, s in achados:
        if m not in vistos:
            vistos.add(m)
            unicos.append((m, s))
    return unicos


def iniciar():
    titulo("MODULO 9 - CICLO 9.2 - CRIACAO DO MODELO")
    for p in ("prompts", "dados", "entregas", "saidas"):
        os.makedirs(p, exist_ok=True)
    criados = []

    if not os.path.exists(MODELO):
        with open(MODELO, "w", encoding="utf-8") as f:
            f.write(TEXTO_MODELO)
        criados.append(MODELO)

    if not os.path.exists(VARIAVEIS):
        cols = marcadores(TEXTO_MODELO)
        with open(VARIAVEIS, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=SEP)
            w.writerow(cols)
            for _ in range(3):
                w.writerow([""] * len(cols))
        criados.append(VARIAVEIS)

    if not os.path.exists(FLUXO):
        with open(FLUXO, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=SEP)
            w.writerow(COLS_FLUXO)
            for item, valor, obs in ITENS_FLUXO:
                w.writerow([item, valor, obs])
        criados.append(FLUXO)

    print()
    if criados:
        print("CRIADO:")
        for c in criados:
            print("  + " + c)
    else:
        print("Todos os arquivos ja existiam. Nada foi sobrescrito.")

    print()
    print("PROXIMOS PASSOS")
    print()
    print("  1. Abra " + MODELO + ", preencha responsavel e data e, entre as")
    print("     linhas '## Documento' e '---', ponha o seu documento real, trocando")
    print("     por marcadores entre colchetes tudo que muda.")
    print()
    print("  2. Ajuste as colunas de " + VARIAVEIS + " para os marcadores que")
    print("     voce usou, apague as linhas vazias e preencha tres linhas com")
    print("     casos reais.")
    print()
    print("  3. Peca: \"execute atividade_modulo9.py com o comando gerar\"")
    return 0


def gerar():
    titulo("MODULO 9 - CICLO 9.2 - GERACAO DOS DOCUMENTOS")
    if not os.path.exists(MODELO):
        print()
        print("Nao encontrei " + MODELO + ". Execute o comando 'iniciar'.")
        return 1
    if not os.path.exists(VARIAVEIS):
        print()
        print("Nao encontrei " + VARIAVEIS + ". Execute o comando 'iniciar'.")
        return 1

    texto = open(MODELO, encoding="utf-8-sig").read()
    corpo, achou_secao = corpo_do_documento(texto)
    usados = marcadores(texto)
    estranhos = nao_reconhecidos(corpo)

    if not achou_secao:
        print()
        print("AVISO: o modelo nao tem a linha '## Documento'. Todo o texto acima de")
        print("COMO ADAPTAR ESTE MODELO vai para os documentos, inclusive responsavel,")
        print("data de revisao e regra para dado ausente. Escreva '## Documento' na")
        print("linha que antecede o titulo do seu documento.")

    def _txt(v):
        # Campos a mais que o cabecalho chegam como lista, sob a chave None.
        return " ".join(v) if isinstance(v, list) else (v or "")

    linhas, a_mais = [], []
    with open(VARIAVEIS, newline="", encoding="utf-8-sig") as f:
        leitor = csv.DictReader(f, delimiter=SEP)
        for l in leitor:
            extras = l.pop(None, None)
            if extras and any(_txt(x).strip() for x in extras):
                a_mais.append((leitor.line_num, extras))
            if any(_txt(v).strip() for v in l.values()):
                linhas.append(l)

    if a_mais:
        print()
        print("AVISO: linhas de " + VARIAVEIS + " com mais campos que o cabecalho.")
        print("Os valores a mais foram ignorados:")
        for n, extras in a_mais:
            print("  - linha %d: %s" % (n, "; ".join(_txt(x) for x in extras)))
        print("Confira se falta coluna no cabecalho ou se sobrou separador ';'.")

    if not linhas:
        print()
        print("A tabela de variaveis esta vazia. Preencha ao menos tres linhas.")
        return 1

    colunas = [c for c in linhas[0].keys() if c]
    faltando = [m for m in usados if m not in colunas]
    sobrando = [c for c in colunas if c not in usados]

    if faltando:
        print()
        print("O modelo usa marcadores que nao tem coluna na tabela:")
        for m in faltando:
            print("  - [%s]" % m)
        print()
        print("Acrescente essas colunas em " + VARIAVEIS + " ou corrija o nome no")
        print("modelo. A geracao foi interrompida: sem isso o documento sairia com")
        print("o marcador cru no lugar do valor.")
        return 1

    if sobrando:
        print()
        print("Colunas da tabela que o modelo nao usa (pode ser erro de digitacao):")
        for c in sobrando:
            print("  - %s" % c)

    if estranhos:
        print()
        print("AVISO: colchetes que o script nao reconhece como marcador. Eles vao sair")
        print("no documento sem substituicao. O nome do marcador usa so maiusculas de")
        print("A a Z, algarismos e sublinhado, com dois caracteres ou mais:")
        for m, sug in estranhos:
            if len(sug) >= 2:
                print("  - [%s]   escreva [%s]" % (m, sug))
            else:
                print("  - [%s]" % m)
        print("Se o colchete faz parte do texto e nao e marcador, ignore este aviso.")

    os.makedirs("saidas", exist_ok=True)
    gerados, avisos_totais = [], 0

    for i, l in enumerate(linhas, 1):
        doc = corpo
        vazias = []
        for m in usados:
            v = (l.get(m) or "").strip()
            if not v:
                v = "NAO INFORMADO"
                vazias.append(m)
            doc = doc.replace("[%s]" % m, v)
        if vazias:
            aviso = ("> AVISO: os campos a seguir vieram sem valor e foram preenchidos "
                     "com NAO INFORMADO: %s\n\n" % ", ".join(vazias))
            doc = aviso + doc
            avisos_totais += 1
        destino = os.path.join("saidas", "documento-%d.md" % i)
        with open(destino, "w", encoding="utf-8") as f:
            f.write(doc)
        gerados.append((destino, vazias))

    print()
    print("DOCUMENTOS GERADOS (%d):" % len(gerados))
    for destino, vazias in gerados:
        marca = "  + %s" % destino
        if vazias:
            marca += "   (%d campo(s) sem valor)" % len(vazias)
        print(marca)

    print()
    print("Marcadores usados no modelo: %d" % len(usados))
    print("Documentos com campo faltando: %d" % avisos_totais)
    print("Colchetes nao reconhecidos: %d" % len(estranhos))
    print()
    print("PROXIMO PASSO")
    print("  Leia os tres documentos. Alguma frase ficou sem sentido? E onde o")
    print("  modelo precisa de ajuste na parte fixa.")
    print("  Depois: \"execute atividade_modulo9.py com o comando conferir\"")
    return 0


def conferir():
    titulo("MODULO 9 - CICLO 9.4 - CONFERENCIA E MEDICAO")
    if not os.path.exists(FLUXO):
        print()
        print("Nao encontrei " + FLUXO + ". Execute o comando 'iniciar'.")
        return 1

    with open(FLUXO, newline="", encoding="utf-8-sig") as f:
        dados = {(l.get("item") or "").strip(): (l.get("valor") or "").strip()
                 for l in csv.DictReader(f, delimiter=SEP)}

    erros = []
    numeros = {}
    for campo in ("tempo_manual_minutos", "tempo_automatizado_minutos",
                  "tempo_construcao_minutos", "execucoes_por_ano"):
        bruto = dados.get(campo, "").replace(",", ".")
        try:
            numeros[campo] = float(bruto)
            if numeros[campo] < 0:
                erros.append("%s nao pode ser negativo" % campo)
        except ValueError:
            erros.append("%s precisa ser um numero de minutos" % campo)

    if numeros.get("execucoes_por_ano") == 0:
        erros.append("execucoes_por_ano precisa ser maior que zero")

    # Manutencao: linha acrescentada em nov. 2026. Arquivo criado antes nao a
    # tem. Sem valor, o calculo considera zero e avisa.
    manut_informada = True
    bruto = dados.get("manutencao_minutos_por_ano", "").replace(",", ".")
    if not bruto:
        manut_informada = False
        numeros["manutencao_minutos_por_ano"] = 0.0
    else:
        try:
            numeros["manutencao_minutos_por_ano"] = float(bruto)
            if numeros["manutencao_minutos_por_ano"] < 0:
                erros.append("manutencao_minutos_por_ano nao pode ser negativo")
        except ValueError:
            erros.append("manutencao_minutos_por_ano precisa ser um numero de minutos")

    for campo in ("passo_irreversivel", "o_que_se_confere", "cargo_responsavel",
                  "se_a_conferencia_falhar"):
        if len(dados.get(campo, "")) < 10:
            erros.append("%s esta vazio ou curto demais" % campo)

    if "equipe" in dados.get("cargo_responsavel", "").lower() and \
            len(dados.get("cargo_responsavel", "")) < 25:
        erros.append("cargo_responsavel: 'a equipe' nao e um cargo. Nomeie a funcao.")

    gerados = [f for f in os.listdir("saidas")
               if re.match(r"^documento-\d+\.md$", f)] if os.path.isdir("saidas") else []
    if len(gerados) < 3:
        erros.append("faltam documentos gerados: sao %d de 3. Execute 'gerar'."
                     % len(gerados))

    print()
    if erros:
        print("PROBLEMAS QUE PRECISAM SER CORRIGIDOS (%d):" % len(erros))
        for e in erros:
            print("  - " + e)
        print()
        print("O relatorio nao foi gerado.")
        return 1

    manual = numeros["tempo_manual_minutos"]
    automat = numeros["tempo_automatizado_minutos"]
    constr = numeros["tempo_construcao_minutos"]
    por_ano = numeros["execucoes_por_ano"]
    manut_ano = numeros["manutencao_minutos_por_ano"]
    manut_exec = manut_ano / por_ano
    economia = manual - automat - manut_exec

    print("Nenhum problema encontrado.")
    if not manut_informada:
        print("AVISO: manutencao_minutos_por_ano sem valor. O calculo considera zero.")
        print("  Acrescente ao arquivo a linha manutencao_minutos_por_ano;N; com N em")
        print("  minutos por ano, se ela nao existir.")
    print()
    print("  Tempo manual por execucao (estimado):  %.0f min" % manual)
    print("  Tempo automatizado por execucao:       %.0f min" % automat)
    print("  Manutencao por execucao:               %.0f min" % manut_exec)
    print("  Economia liquida por execucao:         %.0f min" % economia)
    print("  Investimento na construcao:            %.0f min" % constr)

    if economia <= 0:
        equilibrio = None
        print()
        print("  A automacao nao economiza tempo por execucao, descontada a manutencao.")
        print("  O metodo serve para descobrir isso antes de investir mais tempo. Se")
        print("  a automacao ainda se justifica, o argumento passa a ser a reducao de")
        print("  erro, com o erro que ela evita descrito no relatorio.")
    else:
        equilibrio = constr / economia
        anos = equilibrio / por_ano
        print("  Execucoes ate o investimento se pagar: %.1f" % equilibrio)
        print("  Ou seja, cerca de %.1f ano(s) na frequencia informada." % anos)
        print("  Economia anual estimada: %.0f min (%.1f h)"
              % (economia * por_ano, economia * por_ano / 60.0))

    gerar_relatorio(dados, numeros, economia, equilibrio, gerados, manut_informada)
    print()
    print("Relatorio gerado em: " + RELATORIO)
    print()
    print("ULTIMO PASSO")
    print("  Abra o relatorio e escreva a frase para a chefia: o que era, o que e")
    print("  agora, e em quanto tempo o investimento se paga.")
    return 0


def gerar_relatorio(dados, numeros, economia, equilibrio, gerados, manut_informada=True):
    L = ["# Fluxo automatizado", "",
         "Modulo 9. DECC0294, UFMA, Curso de Administracao.",
         "Gerado em %s pelo script atividade_modulo9.py." % date.today().strftime("%d/%m/%Y"),
         "", "Nome e matricula: ______________________________", "",
         "## Medicao", "", "| Item | Valor |", "|---|---|"]
    manut = numeros["manutencao_minutos_por_ano"]
    L.append("| Tempo manual por execucao (estimado) | %.0f min |" % numeros["tempo_manual_minutos"])
    L.append("| Tempo automatizado por execucao (medido) | %.0f min |" % numeros["tempo_automatizado_minutos"])
    if manut_informada:
        L.append("| Manutencao por ano (estimada) | %.0f min |" % manut)
    else:
        L.append("| Manutencao por ano | NAO INFORMADO, considerado 0 |")
    L.append("| Economia liquida por execucao | %.0f min |" % economia)
    L.append("| Investimento na construcao (medido) | %.0f min |" % numeros["tempo_construcao_minutos"])
    L.append("| Execucoes por ano | %.0f |" % numeros["execucoes_por_ano"])
    if equilibrio is not None:
        L.append("| Execucoes ate se pagar | %.1f |" % equilibrio)
        L.append("| Economia anual estimada | %.1f h |"
                 % (economia * numeros["execucoes_por_ano"] / 60.0))
    L += ["", "## Documentacao do fluxo", "",
          "### O que entra e de onde vem", "", "ESCREVA AQUI os arquivos de insumo, "
          "com a origem de cada um e quem os disponibiliza.", "", "- ", "",
          "### A sequencia de comandos", "",
          "ESCREVA AQUI a ordem dos comandos e o que cada um produz.", "", "1. ", "",
          "### Ponto de conferencia", "",
          "- Passo irreversivel: %s" % dados.get("passo_irreversivel", ""),
          "- O que se confere: %s" % dados.get("o_que_se_confere", ""),
          "- Cargo responsavel: %s" % dados.get("cargo_responsavel", ""),
          "- Se a conferencia falhar: %s" % dados.get("se_a_conferencia_falhar", ""), "",
          "### O que fazer quando da errado", "",
          "ESCREVA AQUI os dois ou tres defeitos previsiveis e o que fazer em cada caso.",
          "", "- ", "",
          "## Documentos gerados", ""]
    for g in sorted(gerados):
        L.append("- saidas/%s" % g)
    L += ["", "## Frase para a chefia", "",
          "ESCREVA AQUI em uma frase: o que era, o que e agora, e em quanto tempo o",
          "investimento se paga.", "", "> ", "",
          "## Comparacao com a estimativa do modulo 1", "",
          "ESCREVA AQUI: o ganho que voce estimou la bate com o calculado agora? "
          "O que explica a diferenca?", "", "> ", "",
          "---", "", "## Declaracao de uso de inteligencia artificial", "",
          "Ferramenta e modelo usados: ______________________________", "",
          "O modelo com variaveis esta em prompts/ e os documentos gerados em saidas/.",
          "O tempo manual e a manutencao sao estimativas minhas. O tempo automatizado",
          "e o de construcao foram medidos por mim.", ""]
    os.makedirs("entregas", exist_ok=True)
    with open(RELATORIO, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


def main():
    cmd = (sys.argv[1].strip().lower() if len(sys.argv) > 1 else "")
    if cmd in ("iniciar", "criar", "start"):
        return iniciar()
    if cmd in ("gerar", "produzir"):
        return gerar()
    if cmd in ("conferir", "validar", "check"):
        return conferir()
    print(__doc__)
    print("Comandos disponiveis:")
    print("  python atividade_modulo9.py iniciar    cria modelo, variaveis e medicao")
    print("  python atividade_modulo9.py gerar      produz um documento por linha")
    print("  python atividade_modulo9.py conferir   valida a medicao e gera o relatorio")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)
    except KeyboardInterrupt:
        print()
        print("Interrompido.")
        sys.exit(1)
