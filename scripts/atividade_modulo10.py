#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
 ATIVIDADE DO MODULO 10 - Pesquisa e analise qualitativa
 DECC0294 - UFMA - Curso de Administracao - 2026.2
=============================================================================

O QUE ESTE ARQUIVO E
    Um unico script que organiza a ficha de fontes da comparacao setorial,
    prepara a dupla codificacao das respostas abertas, mede a concordancia
    entre as duas codificacoes e confere a entrega B2.

COMO USAR (peca ao agente, no opencode desktop)

    1) "execute atividade_modulo10.py com o comando fontes"
       Cria entregas/modulo10-fontes.csv, a ficha da comparacao setorial.

    2) "execute atividade_modulo10.py com o comando codificar dados/RESPOSTAS.csv"
       Sorteia vinte respostas e cria entregas/modulo10-codificacao.csv com
       duas colunas vazias: a sua e a do agente.

    3) Preencha a sua coluna sem olhar mais nada. Depois peca ao agente para
       preencher a dele, informando o livro de codigos e dizendo para nao
       consultar a sua coluna.

    4) "execute atividade_modulo10.py com o comando concordancia"
       Calcula a concordancia percentual e o kappa de Cohen, com a
       concordancia observada e a esperada ao acaso, e lista os casos
       divergentes.

    5) "execute atividade_modulo10.py com o comando conferir fontes"
       Valida so a ficha de fontes (ciclo 10.2), sem gerar o relatorio.

    6) "execute atividade_modulo10.py com o comando conferir"
       Valida a ficha de fontes, o livro de codigos e a codificacao, e gera
       o relatorio entregas/modulo10-relatorio.md.

    7) "execute atividade_modulo10.py com o comando b2"
       Percorre os modulos 9 e 10 e diz o que falta para a entrega B2.

    Sem nenhum comando, o script imprime estas instrucoes.

A REGRA QUE O SCRIPT APLICA
    Fonte sem endereco, sem ano e sem a definicao do indicador e recusada.
    Categorizacao sem dupla codificacao e opiniao sobre as respostas.
    Categorias sao comparadas sem diferenca de maiusculas, espacos extras e
    acentos: a mesma palavra escrita com ou sem acento conta como uma so.

Nao precisa instalar nada. Roda com o Python que ja vem com o ambiente.
=============================================================================
"""

import csv
import os
import random
import re
import sys
import unicodedata
from datetime import date, datetime

# Quando o script esta na pasta scripts/ do repositorio, as pastas de trabalho
# (dados/, entregas/, saidas/, prompts/) ficam um nivel acima. Copiado para a
# raiz do projeto do aluno, o script roda onde esta, sem mudanca.
_AQUI = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(_AQUI) == "scripts":
    os.chdir(os.path.dirname(_AQUI))

SEP = ";"
FONTES = os.path.join("entregas", "modulo10-fontes.csv")
CODIFICACAO = os.path.join("entregas", "modulo10-codificacao.csv")
LIVRO = os.path.join("entregas", "modulo10-livro-de-codigos.md")
RELATORIO = os.path.join("entregas", "modulo10-relatorio.md")
B2 = os.path.join("entregas", "B2-relatorio.md")

COLS_FONTES = ["organizacao", "orgao_publicador", "publicacao", "ano", "endereco",
               "definicao_do_indicador", "valor_extraido"]
COLS_COD = ["n", "resposta", "categoria_aluno", "categoria_agente", "divergencia_examinada"]

AMOSTRA = 20
MINIMO_CONCORDANCIA = 70.0
MINIMO_FONTES = 2

TEXTO_LIVRO = """# Livro de codigos

Modulo 10, ciclo 10.3. DECC0294, UFMA, Curso de Administracao.

Nome e matricula: ______________________________

Base analisada: PREENCHER (arquivo, numero de respostas, periodo)

## Como este livro foi construido

PREENCHER: as categorias vieram da leitura das respostas, da literatura, ou
das duas? Quantas respostas voce leu antes de definir?

## Categorias

Quatro ou cinco nesta pratica, e no maximo sete. Com mais de sete, a mesma
pessoa ja tem dificuldade de aplicar as definicoes sempre do mesmo modo.
Mantenha o formato do titulo: tres cerquilhas, numero, ponto e nome.

### 1. NOME DA CATEGORIA

Definicao: PREENCHER, em uma frase.

Entram, por exemplo:
- PREENCHER
- PREENCHER

Nao entra, por exemplo:
- PREENCHER (e por que nao entra)

### 2. NOME DA CATEGORIA

Definicao: PREENCHER

Entram, por exemplo:
- PREENCHER
- PREENCHER

Nao entra, por exemplo:
- PREENCHER

### 3. NOME DA CATEGORIA

Definicao: PREENCHER

Entram, por exemplo:
- PREENCHER
- PREENCHER

Nao entra, por exemplo:
- PREENCHER

### 4. NOME DA CATEGORIA

Definicao: PREENCHER

Entram, por exemplo:
- PREENCHER
- PREENCHER

Nao entra, por exemplo:
- PREENCHER

## Teste das duas regras

Exaustiva: toda resposta cabe em alguma categoria? Se muitas caem em "outros",
falta categoria.

Mutuamente exclusiva: nenhuma resposta cabe em duas ao mesmo tempo? Se cabe,
falta dizer na definicao onde fica o caso de fronteira.

## Ajustes feitos depois da dupla codificacao

PREENCHER: quais definicoes foram corrigidas, e por causa de qual divergencia.
"""


def titulo(t):
    print()
    print("=" * 74)
    print(" " + t)
    print("=" * 74)


def ler_csv(caminho):
    bruto = None
    for cod in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            with open(caminho, encoding=cod) as f:
                bruto = f.read()
            break
        except (UnicodeDecodeError, LookupError):
            continue
    if bruto is None:
        return None
    primeira = bruto.splitlines()[0] if bruto.splitlines() else ""
    contagens = {d: primeira.count(d) for d in (";", ",", "\t", "|")}
    sep = max(contagens, key=contagens.get)
    if contagens[sep] == 0:
        return None
    return list(csv.DictReader(bruto.splitlines(), delimiter=sep))


def criar_fontes():
    titulo("MODULO 10 - CICLO 10.2 - FICHA DE FONTES")
    os.makedirs("entregas", exist_ok=True)
    if os.path.exists(FONTES):
        print()
        print("O arquivo ja existe: " + FONTES)
        return 0
    with open(FONTES, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=SEP)
        w.writerow(COLS_FONTES)
        for _ in range(MINIMO_FONTES):
            w.writerow([""] * len(COLS_FONTES))
    print()
    print("Ficha criada em: " + FONTES)
    print()
    print("COMO PREENCHER, uma linha por organizacao comparada")
    print("(a sua e uma comparavel, no minimo. Pode acrescentar linhas.)")
    print()
    print("  organizacao              A organizacao a que o numero se refere.")
    print("  orgao_publicador         Quem publica o dado. Nao e a mesma coisa.")
    print("  publicacao               Nome do relatorio, pesquisa ou base.")
    print("  ano                      O ano a que o dado se refere, com quatro digitos.")
    print("  endereco                 O endereco da fonte que voce abriu.")
    print("  definicao_do_indicador   Como aquela fonte define o indicador.")
    print("                           E aqui que aparece a divergencia de medida.")
    print("  valor_extraido           O numero que voce leu na fonte aberta.")
    print()
    print("Antes de preencher, escreva o indicador que voce vai comparar:")
    print("numerador, denominador e periodo. Sem isso qualquer numero encontrado")
    print("parece servir.")
    print()
    print("Depois de preencher:")
    print('  "execute atividade_modulo10.py com o comando conferir fontes"')
    return 0


def codificar(args):
    titulo("MODULO 10 - CICLO 10.3 - PREPARACAO DA DUPLA CODIFICACAO")
    if not args:
        print()
        print("Faltou o arquivo. Uso: codificar dados/RESPOSTAS.csv")
        return 1
    caminho = args[0]
    if not os.path.exists(caminho):
        print()
        print("Nao encontrei " + caminho)
        return 1

    linhas = ler_csv(caminho)
    if not linhas:
        print()
        print("Nao consegui ler o arquivo, ou ele nao tem linhas.")
        return 1

    colunas = list(linhas[0].keys())
    alvo = None
    if len(args) > 1 and args[1] in colunas:
        alvo = args[1]
    else:
        melhor = -1
        for c in colunas:
            textos = [(l.get(c) or "").strip() for l in linhas]
            media = sum(len(t) for t in textos) / max(len(textos), 1)
            if media > melhor:
                melhor, alvo = media, c

    respostas = [(l.get(alvo) or "").strip() for l in linhas]
    respostas = [r for r in respostas if len(r) > 10]
    if len(respostas) < AMOSTRA:
        print()
        print("Encontrei apenas %d respostas com texto na coluna '%s'."
              % (len(respostas), alvo))
        print("A dupla codificacao precisa de %d. Confira se a coluna esta certa:"
              % AMOSTRA)
        print("colunas disponiveis: " + ", ".join(colunas))
        print("Para escolher outra: codificar %s NOME_DA_COLUNA" % caminho)
        return 1

    random.seed(42)
    amostra = random.sample(respostas, AMOSTRA)

    os.makedirs("entregas", exist_ok=True)
    if os.path.exists(CODIFICACAO):
        print()
        print("O arquivo ja existe: " + CODIFICACAO)
        print("Nada foi sobrescrito. Para recomecar, renomeie o arquivo atual.")
        return 0

    with open(CODIFICACAO, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=SEP)
        w.writerow(COLS_COD)
        for i, r in enumerate(amostra, 1):
            w.writerow([i, r, "", "", ""])

    if not os.path.exists(LIVRO):
        with open(LIVRO, "w", encoding="utf-8") as f:
            f.write(TEXTO_LIVRO)

    print()
    print("Coluna de respostas usada: '%s'" % alvo)
    print("Respostas com texto encontradas: %d" % len(respostas))
    print("Amostra sorteada: %d" % AMOSTRA)
    print()
    print("CRIADO:")
    print("  + " + CODIFICACAO)
    print("  + " + LIVRO + " (se ainda nao existia)")
    print()
    print("PROXIMOS PASSOS, NESTA ORDEM")
    print()
    print("  1. Leia as %d respostas da amostra em %s, sem categorizar."
          % (AMOSTRA, CODIFICACAO))
    print()
    print("  2. Escreva o livro de codigos em " + LIVRO)
    print("     (quatro ou cinco categorias, sem nenhum campo PREENCHER)")
    print()
    print("  3. Preencha a coluna categoria_aluno, sem consultar mais nada.")
    print()
    print("  4. Peca ao agente: 'leia o livro de codigos em %s e preencha a coluna" % LIVRO)
    print("     categoria_agente de %s. Nao consulte a coluna" % CODIFICACAO)
    print("     categoria_aluno: ela precisa ficar independente da sua.'")
    print()
    print("  5. \"execute atividade_modulo10.py com o comando concordancia\"")
    return 0


def concordancia(imprimir=True):
    if not os.path.exists(CODIFICACAO):
        if imprimir:
            print()
            print("Nao encontrei " + CODIFICACAO + ". Execute o comando 'codificar'.")
        return None

    # ler_csv aceita o arquivo salvo pelo Excel, em outra codificacao ou com
    # outro separador.
    linhas = [l for l in (ler_csv(CODIFICACAO) or [])
              if (l.get("resposta") or "").strip()]

    preenchidas = [l for l in linhas
                   if norm(l.get("categoria_aluno")) and norm(l.get("categoria_agente"))]
    iguais = [l for l in preenchidas
              if norm(l.get("categoria_aluno")) == norm(l.get("categoria_agente"))]
    divergentes = [l for l in preenchidas if l not in iguais]
    taxa = 100.0 * len(iguais) / len(preenchidas) if preenchidas else 0.0

    categorias = {}
    usos_agente = {}
    for l in preenchidas:
        c = norm(l.get("categoria_aluno"))
        categorias[c] = categorias.get(c, 0) + 1
        a = norm(l.get("categoria_agente"))
        usos_agente[a] = usos_agente.get(a, 0) + 1

    # Kappa de Cohen (Cohen, 1960): kappa = (Po - Pe) / (1 - Pe).
    # Po e a proporcao de respostas com a mesma categoria nas duas colunas.
    # Pe e a concordancia esperada ao acaso: para cada categoria, a proporcao
    # de uso pelo aluno vezes a proporcao de uso pelo agente, somadas.
    n = len(preenchidas)
    po = len(iguais) / float(n) if n else 0.0
    pe = 0.0
    if n:
        for c in set(categorias) | set(usos_agente):
            pe += (categorias.get(c, 0) / float(n)) * (usos_agente.get(c, 0) / float(n))
    kappa = (po - pe) / (1.0 - pe) if n and pe < 1.0 else None

    if imprimir:
        titulo("MODULO 10 - CICLO 10.3 - CONCORDANCIA")
        print()
        print("  Respostas na amostra:         %d" % len(linhas))
        print("  Codificadas nas duas colunas: %d" % len(preenchidas))
        print("  Concordancias:                %d" % len(iguais))
        print("  Divergencias:                 %d" % len(divergentes))
        print("  Taxa de concordancia:         %.1f%%" % taxa)
        print()
        if n:
            print("  Concordancia observada (Po):  %d / %d = %.3f" % (len(iguais), n, po))
            print("  Esperada ao acaso (Pe):       %.3f" % pe)
            if kappa is None:
                print("  Kappa de Cohen:               nao calculavel (os dois usaram")
                print("                                uma unica categoria)")
            else:
                print("  Kappa de Cohen:               (%.3f - %.3f) / (1 - %.3f) = %.2f"
                      % (po, pe, pe, kappa))
            print()
            print("  Uso de cada categoria (voce / agente):")
            for c in sorted(set(categorias) | set(usos_agente)):
                print("    %-28s %2d / %2d" % (c, categorias.get(c, 0), usos_agente.get(c, 0)))
            print()
        if len(preenchidas) < AMOSTRA:
            print("  Faltam %d resposta(s) para completar a dupla codificacao."
                  % (AMOSTRA - len(preenchidas)))
            print()
        if taxa < MINIMO_CONCORDANCIA and preenchidas:
            print("  Abaixo de %.0f%%: ha definicoes no livro de codigos que deixam a mesma"
                  % MINIMO_CONCORDANCIA)
            print("  resposta caber em mais de uma categoria. O resultado e comum na primeira")
            print("  rodada. Examine cada divergencia e corrija a DEFINICAO da categoria.")
            print("  A categoria ja atribuida a cada caso fica como estava.")
            print()
        if divergentes:
            print("CASOS DIVERGENTES:")
            for l in divergentes:
                print()
                print("  #%s  voce: %-22s agente: %s"
                      % (l.get("n"), l.get("categoria_aluno"), l.get("categoria_agente")))
                print("      %s" % (l.get("resposta") or "")[:100])
            print()
            print("Para cada um, escreva na coluna divergencia_examinada qual definicao")
            print("estava ambigua e o que voce mudou nela.")

    return {"linhas": linhas, "preenchidas": preenchidas, "iguais": iguais,
            "divergentes": divergentes, "taxa": taxa, "categorias": categorias,
            "usos_agente": usos_agente, "po": po, "pe": pe, "kappa": kappa}


def norm(v):
    """Minusculas, sem acentos e com espacos simples, para comparar categorias."""
    t = unicodedata.normalize("NFKD", (v or "").strip().lower())
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", t)


def validar(so_fontes=False):
    """Confere as entregas sem imprimir. Devolve erros, avisos, fontes e dados."""
    erros, avisos = [], []
    fontes = []

    if not os.path.exists(FONTES):
        erros.append("nao encontrei " + FONTES + ". Execute o comando 'fontes'.")
    else:
        for i, l in enumerate(ler_csv(FONTES) or [], start=2):
            if not (l.get("organizacao") or "").strip():
                continue
            campos = {c: (l.get(c) or "").strip() for c in COLS_FONTES}
            for obrig in ("orgao_publicador", "publicacao", "endereco",
                          "definicao_do_indicador", "valor_extraido"):
                if not campos[obrig]:
                    erros.append("fontes, linha %d: %s esta vazio" % (i, obrig))
            if not re.match(r"^\d{4}$", campos["ano"]):
                erros.append("fontes, linha %d: ano precisa ter quatro digitos" % i)
            if len(campos["definicao_do_indicador"]) < 20:
                erros.append("fontes, linha %d: definicao_do_indicador curta demais. "
                             "E nela que aparece a diferenca de medida." % i)
            if campos["endereco"] and not re.search(r"(https?://|www\.)", campos["endereco"]):
                avisos.append("fontes, linha %d: o endereco nao parece um link" % i)
            fontes.append(campos)

        if len(fontes) < MINIMO_FONTES:
            erros.append("a comparacao precisa de pelo menos %d organizacoes, e ha %d."
                         % (MINIMO_FONTES, len(fontes)))
        anos = set(f["ano"] for f in fontes if f["ano"])
        if len(anos) > 1:
            avisos.append("os anos das fontes divergem (%s). A comparacao continua "
                          "possivel, mas a ressalva precisa estar escrita."
                          % ", ".join(sorted(anos)))
        definicoes = set(f["definicao_do_indicador"].lower()[:40] for f in fontes)
        if len(definicoes) > 1:
            avisos.append("as definicoes do indicador nao sao identicas entre as fontes. "
                          "Declare isso na comparacao.")

    if so_fontes:
        return erros, avisos, fontes, None

    dados = concordancia(imprimir=False)
    if dados is None:
        erros.append("nao encontrei " + CODIFICACAO + ". Execute o comando 'codificar'.")
    else:
        if len(dados["preenchidas"]) < AMOSTRA:
            erros.append("a dupla codificacao esta incompleta: %d de %d respostas."
                         % (len(dados["preenchidas"]), AMOSTRA))
        if dados["taxa"] < MINIMO_CONCORDANCIA:
            sem_exame = [l for l in dados["divergentes"]
                         if len((l.get("divergencia_examinada") or "").strip()) < 15]
            if sem_exame:
                erros.append("concordancia de %.1f%% com %d divergencia(s) sem exame "
                             "registrado. Escreva qual definicao estava ambigua."
                             % (dados["taxa"], len(sem_exame)))

    if not os.path.exists(LIVRO):
        erros.append("nao encontrei " + LIVRO)
    else:
        texto = open(LIVRO, encoding="utf-8").read()
        pend = texto.count("PREENCHER")
        if pend:
            erros.append("o livro de codigos ainda tem %d campo(s) marcado(s) como "
                         "PREENCHER" % pend)
        n_cat = len(re.findall(r"^### \d+\.", texto, re.MULTILINE))
        if n_cat < 4:
            avisos.append("o livro tem %d categoria(s). Menos de quatro costuma "
                          "significar categorias largas demais." % n_cat)
        elif n_cat > 7:
            avisos.append("o livro tem %d categorias. Com mais de sete, a aplicacao "
                          "das definicoes tende a variar." % n_cat)

    return erros, avisos, fontes, dados


def conferir(args=None):
    so_fontes = bool(args) and norm(args[0]) == "fontes"
    if so_fontes:
        titulo("MODULO 10 - CICLO 10.2 - CONFERENCIA DA FICHA DE FONTES")
    else:
        titulo("MODULO 10 - CONFERENCIA DAS ENTREGAS")
    erros, avisos, fontes, dados = validar(so_fontes)

    print()
    if erros:
        print("PROBLEMAS QUE PRECISAM SER CORRIGIDOS (%d):" % len(erros))
        for e in erros:
            print("  - " + e)
    else:
        print("Nenhum problema encontrado.")
    if avisos:
        print()
        print("PONTOS PARA VOCE REVER (%d):" % len(avisos))
        for a in avisos:
            print("  - " + a)

    print()
    print("Organizacoes na ficha: %d (minimo de %d)" % (len(fontes), MINIMO_FONTES))
    if dados:
        print("Concordancia: %.1f%%" % dados["taxa"])
        if dados["kappa"] is not None:
            print("Kappa de Cohen: %.2f" % dados["kappa"])

    if so_fontes:
        print()
        if erros:
            print("Corrija as linhas indicadas e execute 'conferir fontes' de novo.")
            return 1
        print("Ficha aprovada. Escreva a comparacao em "
              + os.path.join("entregas", "modulo10-ciclo2-comparacao.md") + ".")
        print("O relatorio do modulo e gerado pelo 'conferir', depois do ciclo 10.3.")
        return 0

    if erros:
        print()
        print("O relatorio nao foi gerado. Corrija e execute 'conferir' de novo.")
        return 1

    gerar_relatorio(fontes, dados, avisos)
    print()
    print("Relatorio gerado em: " + RELATORIO)
    print()
    print("PROXIMO PASSO")
    print('  "execute atividade_modulo10.py com o comando b2"')
    return 0


def gerar_relatorio(fontes, dados, avisos):
    L = ["# Relatorio do modulo 10", "",
         "Pesquisa e analise qualitativa. DECC0294, UFMA.",
         "Gerado em %s pelo script atividade_modulo10.py." % date.today().strftime("%d/%m/%Y"),
         "", "Nome e matricula: ______________________________", "",
         "## Comparacao setorial", "",
         "Indicador comparado (numerador, denominador, periodo):", "", "> ", "",
         "| Organizacao | Orgao | Publicacao | Ano | Valor |", "|---|---|---|---|---|"]
    for f in fontes:
        L.append("| %s | %s | %s | %s | %s |"
                 % (f["organizacao"], f["orgao_publicador"], f["publicacao"],
                    f["ano"], f["valor_extraido"]))
    L += ["", "### Definicao usada por cada fonte", ""]
    for f in fontes:
        L.append("- **%s**: %s" % (f["organizacao"], f["definicao_do_indicador"]))
        L.append("  Fonte: %s" % f["endereco"])
    L += ["", "### Ressalva sobre a comparacao", "",
          "ESCREVA AQUI se os anos ou as definicoes divergem, e o que isso limita "
          "na conclusao.", "", "> ", ""]

    if dados:
        L += ["## Analise qualitativa", "",
              "| Item | Valor |", "|---|---|",
              "| Respostas na amostra | %d |" % len(dados["linhas"]),
              "| Dupla codificacao completa | %d |" % len(dados["preenchidas"]),
              "| Concordancias | %d |" % len(dados["iguais"]),
              "| Divergencias | %d |" % len(dados["divergentes"]),
              "| Taxa de concordancia | %.1f%% |" % dados["taxa"],
              "| Concordancia observada (Po) | %.3f |" % dados["po"],
              "| Concordancia esperada ao acaso (Pe) | %.3f |" % dados["pe"],
              "| Kappa de Cohen | %s |" % ("%.2f" % dados["kappa"]
                                          if dados["kappa"] is not None
                                          else "nao calculavel"), "",
              "### Distribuicao das categorias", "",
              "| Categoria | Respostas | Percentual |", "|---|---|---|"]
        total = len(dados["preenchidas"]) or 1
        for c, q in sorted(dados["categorias"].items(), key=lambda x: -x[1]):
            L.append("| %s | %d | %.0f%% |" % (c, q, 100.0 * q / total))
        L += ["", "### Divergencias examinadas", ""]
        for l in dados["divergentes"]:
            L.append("- **#%s** voce: %s / agente: %s" %
                     (l.get("n"), l.get("categoria_aluno"), l.get("categoria_agente")))
            L.append("  Resposta: %s" % (l.get("resposta") or "")[:160])
            L.append("  Exame: %s" % (l.get("divergencia_examinada") or "PREENCHER"))
        L.append("")

    if avisos:
        L += ["## Pontos marcados pelo script", ""]
        L += ["- %s" % a for a in avisos]
        L.append("")
    L += ["---", "", "## Declaracao de uso de inteligencia artificial", "",
          "Ferramenta e modelo usados: ______________________________", "",
          "As fontes da comparacao foram abertas e lidas por mim. A codificacao da",
          "coluna do aluno foi feita por mim, sem consultar a do agente.", ""]
    os.makedirs("entregas", exist_ok=True)
    with open(RELATORIO, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


ITENS_B2 = [
    ("Decomposicao da tarefa (modulo 9)",
     [os.path.join("entregas", "modulo9-ciclo1-decomposicao.md")]),
    ("Modelo com variaveis (modulo 9)", [os.path.join("prompts", "modulo9-modelo.md")]),
    ("Ponto de conferencia declarado (modulo 9)",
     [os.path.join("entregas", "modulo9-ciclo3-conferencia.md")]),
    ("Fluxo medido (modulo 9)", [os.path.join("entregas", "modulo9-relatorio.md")]),
    ("Sintese em camadas (modulo 10)",
     [os.path.join("entregas", "modulo10-ciclo1-sintese.md")]),
    ("Ficha de fontes (modulo 10)", [FONTES]),
    ("Comparacao escrita (modulo 10)",
     [os.path.join("entregas", "modulo10-ciclo2-comparacao.md")]),
    ("Livro de codigos (modulo 10)", [LIVRO]),
    ("Dupla codificacao (modulo 10)", [CODIFICACAO]),
    ("Resumo legislativo conferido (modulo 10)",
     [os.path.join("entregas", "modulo10-ciclo4-legislacao.md")]),
]


def info_git():
    d = {"remoto": None, "commits": 0}
    logs = os.path.join(".git", "logs", "HEAD")
    if os.path.exists(logs):
        with open(logs, encoding="utf-8", errors="replace") as f:
            linhas = [l for l in f.read().splitlines() if "\t" in l]
        d["commits"] = sum(1 for l in linhas
                           if l.split("\t", 1)[1].strip().startswith("commit"))
    cfg = os.path.join(".git", "config")
    if os.path.exists(cfg):
        with open(cfg, encoding="utf-8", errors="replace") as f:
            m = re.search(r'\[remote "origin"\][^\[]*?url\s*=\s*(\S+)', f.read(), re.DOTALL)
            if m:
                d["remoto"] = m.group(1)
    return d


def conferir_b2():
    titulo("MODULO 10 - CONFERENCIA DA ENTREGA B2")
    itens = []
    for rotulo, caminhos in ITENS_B2:
        achado = next((c for c in caminhos if os.path.exists(c)), None)
        if achado:
            tam = os.path.getsize(achado)
            ok = tam > 200
            det = ("Encontrado: %s (%d bytes)." % (achado, tam)) if ok else \
                  ("%s existe mas esta quase vazio." % achado)
        else:
            ok, det = False, "Nao encontrei " + " nem ".join(caminhos)
        itens.append((ok, rotulo, det))

    # A conferencia do modulo 10 precisa passar sem problemas, e o relatorio
    # gerado por ela precisa existir.
    erros, _avisos, _fontes, _dados = validar()
    if erros:
        itens.append((False, "Conferencia do modulo 10 aprovada",
                      "O comando conferir aponta %d problema(s). Execute 'conferir' "
                      "e corrija o que ele indicar." % len(erros)))
    elif not os.path.exists(RELATORIO):
        itens.append((False, "Conferencia do modulo 10 aprovada",
                      "Sem problemas, mas %s nao existe. Execute 'conferir'." % RELATORIO))
    else:
        itens.append((True, "Conferencia do modulo 10 aprovada",
                      "Sem problemas. Relatorio em %s." % RELATORIO))

    g = info_git()
    itens.append((bool(g["remoto"]), "Repositorio publicado",
                  ("Publicado em: " + g["remoto"]) if g["remoto"]
                  else "Publique o repositorio antes de entregar."))

    print()
    for ok, rotulo, det in itens:
        print(("  [OK]    " if ok else "  [FALTA] ") + rotulo)
        print("           " + det)
    ok_n = sum(1 for i in itens if i[0])
    print()
    print("Concluidos: %d de %d." % (ok_n, len(itens)))

    L = ["# Relatorio da entrega B2", "",
         "Modulo 10. DECC0294, UFMA, Curso de Administracao.",
         "Gerado em %s pelo script atividade_modulo10.py."
         % datetime.now().strftime("%d/%m/%Y as %H:%M"), "",
         "Situacao: %d de %d itens concluidos." % (ok_n, len(itens)), "",
         "| Item | Situacao | Observacao |", "|---|---|---|"]
    for ok, rotulo, det in itens:
        L.append("| %s | %s | %s |" % (rotulo, "concluido" if ok else "pendente", det))
    L += ["", "## Conferido por mim", "",
          "Nome e matricula: ______________________________", "",
          "Declaro que as fontes da comparacao foram abertas por mim, que as citacoes",
          "normativas foram conferidas na fonte oficial, e que as respostas abertas",
          "usadas estao anonimizadas.", ""]
    os.makedirs("entregas", exist_ok=True)
    with open(B2, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print()
    print("Relatorio gravado em: " + B2)
    if ok_n < len(itens):
        print()
        print("Resolva os pendentes e execute 'b2' de novo antes de publicar.")
        return 1
    print()
    print("Entrega B2 completa. No GitHub Desktop, faca o commit com a mensagem")
    print("'entrega B2' e depois o push (Push origin).")
    return 0


def main():
    args = sys.argv[1:]
    cmd = norm(args[0]) if args else ""
    if cmd == "fontes":
        return criar_fontes()
    if cmd == "codificar":
        return codificar(args[1:])
    if cmd == "concordancia":
        return 0 if concordancia() is not None else 1
    if cmd in ("conferir", "validar", "check"):
        return conferir(args[1:])
    if cmd in ("b2", "entrega", "bloco"):
        return conferir_b2()
    print(__doc__)
    print("Comandos disponiveis (peca ao agente: \"execute atividade_modulo10.py com o")
    print("comando ...\"):")
    print("  fontes                    cria a ficha da comparacao")
    print("  conferir fontes           confere so a ficha de fontes")
    print("  codificar dados/X.csv     sorteia a amostra e cria o livro de codigos")
    print("  concordancia              mede a concordancia e o kappa")
    print("  conferir                  confere tudo e gera o relatorio")
    print("  b2                        confere a entrega B2")
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
