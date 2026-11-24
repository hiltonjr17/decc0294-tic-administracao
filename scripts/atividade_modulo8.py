#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
 ATIVIDADE DO MODULO 8 - Painel de indicadores
 DECC0294 - Tecnologia da Informacao e Comunicacao Aplicada a Administracao
 UFMA - Curso de Administracao - 2026.2
=============================================================================

O QUE ESTE ARQUIVO E
    Um unico script que monta o painel do seu projeto em HTML, a partir de um
    formulario de indicadores e de uma serie exportada do banco. O painel e
    autocontido: abre em qualquer navegador, sem internet e sem instalar nada.

COMO USAR (peca ao agente, no opencode desktop)

    1) "execute atividade_modulo8.py com o comando iniciar"
       Cria entregas/modulo8-indicadores.csv com as colunas do painel.

    2) Preencha um indicador por linha. Destinatario e decisao vao na
       primeira linha de indicador e valem para o painel inteiro.

    3) Exporte a serie do grafico com o script do modulo 7:
       "execute atividade_modulo7.py com o comando sql SELECT categoria, valor ..."
       O resultado sai em saidas/consulta-N.csv, com duas colunas.

    4) "execute atividade_modulo8.py com o comando painel saidas/consulta-N.csv"
       Gera entregas/painel.html. Opcoes depois do arquivo:
         linha ou barras      forma do grafico (sem opcao, o script escolhe:
                              linha quando a primeira coluna e periodo)
         destaque=Nome        categoria pintada em vinho, as demais em cinza
         qualquer outro texto titulo do grafico

    5) "execute atividade_modulo8.py com o comando conferir"
       Valida o formulario e o painel.

    6) "execute atividade_modulo8.py com o comando b1"
       Percorre os modulos 6, 7 e 8 e diz o que falta para a entrega B1.

    Formulario da versao anterior, sem as colunas novas:
       "execute atividade_modulo8.py com o comando atualizar"

    Sem nenhum comando, o script imprime estas instrucoes.

A REGRA QUE O SCRIPT APLICA
    Indicador sem formula, comparacao, polaridade ou fonte e recusado. Numero
    solto nao informa, e numero sem origem nao e verificavel.

Nao precisa instalar nada. Roda com o Python que ja vem com o ambiente.
=============================================================================
"""

import csv
import html
import os
import re
import shutil
import sys
import unicodedata
from datetime import datetime

# Quando o script esta na pasta scripts/ do repositorio, as pastas de trabalho
# (dados/, entregas/, saidas/, prompts/) ficam um nivel acima. Copiado para a
# raiz do projeto do aluno, o script roda onde esta, sem mudanca.
_AQUI = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(_AQUI) == "scripts":
    os.chdir(os.path.dirname(_AQUI))

# Texto preenchido pelo aluno pode ter caractere que o console nao exibe.
try:
    sys.stdout.reconfigure(errors="replace")
except (AttributeError, ValueError):
    pass

SEP = ";"
INDICADORES = "entregas/modulo8-indicadores.csv"
PAINEL = "entregas/painel.html"
RELATORIO = "entregas/B1-relatorio.md"

COLUNAS = ["indicador", "titulo_conclusao", "formula", "valor", "unidade",
           "periodo", "comparacao", "valor_comparacao", "polaridade", "fonte",
           "consulta", "destinatario", "decisao"]

VINHO = "#8D0333"
DOURADO = "#D4B277"
TEAL = "#0AB0AB"
# Verde-azulado escurecido para texto: 5,2:1 sobre branco (WCAG 2.2, 1.4.3
# pede 4,5:1). O #0AB0AB da identidade tem 2,7:1 e serve so para area.
TEAL_TEXTO = "#087A76"
CINZA = "#BDBDBD"

EXEMPLO = [
    "Custo por atendimento",
    "O custo por atendimento na unidade Centro e 40% maior que a media das demais",
    "custo total da unidade / atendimentos concluidos",
    "17,66",
    "R$ por atendimento",
    "jan a ago de 2026",
    "media das demais unidades",
    "12,58",
    "menor melhor",
    "Tabela base do projeto.db, filtrada por custo maior que zero",
    "consulta-1.sql",
    "Secretario municipal de administracao",
    "Manter, concentrar ou abrir unidades de atendimento",
]

MESES = {"jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
         "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12}


def titulo(t):
    print()
    print("=" * 74)
    print(" " + t)
    print("=" * 74)


def normalizar(t):
    """Minusculas, sem acento e com espacos simples."""
    t = unicodedata.normalize("NFKD", str(t or ""))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", t).strip().lower()


_MILHAR = re.compile(r"-?[1-9]\d{0,2}(\.\d{3})+")


def _limpo(v):
    return str(v or "").strip().replace("R$", "").replace("%", "").replace(" ", "").strip()


def coluna_com_ponto_de_milhar(valores, sep):
    """Decide pela coluna inteira se o ponto separa milhar.

    Vale quando a coluna usa virgula decimal, ou quando o arquivo e separado
    por ponto e virgula e todo valor com ponto tem o formato 12.480 ou 1.234.567.
    """
    valores = [_limpo(v) for v in valores]
    if any("," in v for v in valores) and sep != ",":
        return True
    com_ponto = [v for v in valores if "." in v]
    return sep == ";" and bool(com_ponto) and all(_MILHAR.fullmatch(v) for v in com_ponto)


def numero(v, milhar=False):
    if v is None:
        return None
    t = str(v).strip().replace("R$", "").replace("%", "").strip()
    if not t:
        return None
    if milhar and _MILHAR.fullmatch(t.replace(" ", "")):
        t = t.replace(" ", "").replace(".", "")
    elif re.match(r"^-?\d{1,3}(\.\d{3})+,\d+$", t):
        t = t.replace(".", "").replace(",", ".")
    elif re.match(r"^-?\d+,\d+$", t):
        t = t.replace(",", ".")
    elif re.match(r"^-?\d{1,3}(,\d{3})+\.\d+$", t):
        t = t.replace(",", "")
    try:
        return float(t)
    except ValueError:
        return None


def ler_tabela(caminho):
    """Devolve (cabecalho, linhas) ou (None, None) se nao conseguir ler."""
    bruto = None
    for cod in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            with open(caminho, encoding=cod) as f:
                bruto = f.read()
            break
        except (UnicodeDecodeError, LookupError):
            continue
    if bruto is None:
        return None, None
    linhas_txt = bruto.splitlines()
    primeira = linhas_txt[0] if linhas_txt else ""
    contagens = {d: primeira.count(d) for d in (";", ",", "\t", "|")}
    sep = max(contagens, key=contagens.get)
    if contagens[sep] == 0:
        return None, None
    leitor = csv.DictReader(linhas_txt, delimiter=sep)
    linhas = list(leitor)
    cab = [(c or "").strip() for c in (leitor.fieldnames or [])]
    global SEPARADOR_LIDO
    SEPARADOR_LIDO = sep
    return cab, linhas


SEPARADOR_LIDO = None


def ler_csv(caminho):
    return ler_tabela(caminho)[1]


def ler_polaridade(t):
    """'maior', 'menor', 'nenhuma' ou None quando o texto nao e reconhecido."""
    n = normalizar(t).replace("quanto ", "").replace(",", "").replace(" e ", " ")
    if n in ("maior melhor", "maior o melhor", "maior"):
        return "maior"
    if n in ("menor melhor", "menor o melhor", "menor"):
        return "menor"
    if n in ("nao se aplica", "nao aplica", "nenhuma", "neutra", "neutro"):
        return "nenhuma"
    return None


TEXTO_POLARIDADE = {"maior": "quanto maior, melhor",
                    "menor": "quanto menor, melhor",
                    "nenhuma": "polaridade nao se aplica"}


def iniciar():
    titulo("MODULO 8 - CICLO 8.3 - FORMULARIO DO PAINEL")
    os.makedirs("entregas", exist_ok=True)
    if os.path.exists(INDICADORES):
        print()
        print("O arquivo ja existe: " + INDICADORES)
        print("Se ele foi criado pela versao anterior do script, peca:")
        print('  "execute atividade_modulo8.py com o comando atualizar"')
        return 0
    with open(INDICADORES, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=SEP)
        w.writerow(COLUNAS)
        w.writerow(EXEMPLO)
        for _ in range(3):
            w.writerow([""] * len(COLUNAS))
    print()
    print("Formulario criado em: " + INDICADORES)
    print()
    print("COMO PREENCHER, um indicador por linha")
    print()
    print("  indicador           Nome curto. Ex.: custo por atendimento")
    print("  titulo_conclusao    A frase que o leitor deve levar. Afirmativa, com o")
    print("                      numero dentro. Minimo de 25 caracteres.")
    print("  formula             Como o numero e calculado, em palavras.")
    print("                      Ex.: custo total / atendimentos concluidos")
    print("  valor               O numero apurado.")
    print("  unidade             R$, %, dias, atendimentos.")
    print("  periodo             O intervalo coberto. Ex.: jan a ago de 2026")
    print("  comparacao          Contra o que se compara: meta, periodo anterior,")
    print("                      media das demais unidades.")
    print("  valor_comparacao    O numero da comparacao.")
    print("  polaridade          maior melhor, menor melhor ou nao se aplica.")
    print("                      Define a cor da variacao no painel.")
    print("  fonte               De que tabela saiu e com que filtro.")
    print("  consulta            O arquivo .sql do modulo 7 que produziu o numero.")
    print("  destinatario        Cargo de quem le o painel. So na primeira linha.")
    print("  decisao             A decisao que o painel sustenta. So na primeira linha.")
    print()
    print("Sao necessarios tres indicadores. A primeira linha e exemplo: substitua.")
    return 0


def atualizar():
    """Acrescenta ao formulario as colunas que faltam, sem apagar nada."""
    titulo("MODULO 8 - ATUALIZACAO DO FORMULARIO")
    if not os.path.exists(INDICADORES):
        print()
        print("Nao encontrei " + INDICADORES + ". Execute o comando 'iniciar'.")
        return 1
    cab, linhas = ler_tabela(INDICADORES)
    if cab is None:
        print()
        print("Nao consegui ler " + INDICADORES + ".")
        return 1
    faltam = [c for c in COLUNAS if c not in cab]
    if not faltam:
        print()
        print("O formulario ja tem todas as colunas. Nada foi alterado.")
        return 0
    copia = "entregas/modulo8-indicadores-anterior.csv"
    shutil.copyfile(INDICADORES, copia)
    extras = [c for c in cab if c and c not in COLUNAS]
    with open(INDICADORES, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=SEP)
        w.writerow(COLUNAS + extras)
        for l in linhas:
            w.writerow([(l.get(c) or "") for c in COLUNAS + extras])
    print()
    print("Colunas acrescentadas: " + ", ".join(faltam))
    print("Copia do arquivo anterior: " + copia)
    print()
    print("Preencha as colunas novas e gere o painel de novo.")
    return 0


def carregar():
    """Devolve (indicadores, erros, avisos, painel_info)."""
    info = {"destinatario": "", "decisao": ""}
    if not os.path.exists(INDICADORES):
        return None, ["nao encontrei " + INDICADORES + ". Execute o comando 'iniciar'."], [], info
    cab, linhas = ler_tabela(INDICADORES)
    if linhas is None:
        return None, ["nao consegui ler " + INDICADORES + "."], [], info
    erros, avisos, indicadores = [], [], []
    faltam = [c for c in COLUNAS if c not in cab]
    if faltam:
        erros.append("o formulario nao tem as colunas %s. Peca: 'execute "
                     "atividade_modulo8.py com o comando atualizar'." % ", ".join(faltam))
        return [], erros, avisos, info
    destinos, decisoes = [], []
    for i, l in enumerate(linhas, start=2):
        nome = (l.get("indicador") or "").strip()
        if not nome:
            continue
        if nome == EXEMPLO[0] and (l.get("titulo_conclusao") or "").strip() == EXEMPLO[1]:
            erros.append("linha %d: a linha de exemplo continua no arquivo" % i)
            continue
        campos = {c: (l.get(c) or "").strip() for c in COLUNAS}
        if len(campos["titulo_conclusao"]) < 25:
            erros.append("linha %d: titulo_conclusao vazio ou curto demais. Escreva a "
                         "frase afirmativa que o leitor deve levar." % i)
        if numero(campos["valor"]) is None:
            erros.append("linha %d: valor precisa ser um numero" % i)
        for obrig in ("formula", "unidade", "periodo", "comparacao", "fonte"):
            if not campos[obrig]:
                erros.append("linha %d: %s esta vazio. Indicador sem %s nao entra no painel."
                             % (i, obrig, obrig))
        if numero(campos["valor_comparacao"]) is None:
            erros.append("linha %d: valor_comparacao precisa ser um numero" % i)
        pol = ler_polaridade(campos["polaridade"])
        if pol is None:
            erros.append("linha %d: polaridade precisa ser 'maior melhor', 'menor melhor' "
                         "ou 'nao se aplica'" % i)
        campos["_pol"] = pol
        if campos["destinatario"]:
            destinos.append(campos["destinatario"])
        if campos["decisao"]:
            decisoes.append(campos["decisao"])
        indicadores.append(campos)
    if len(indicadores) < 3:
        erros.append("sao necessarios tres indicadores, e ha %d." % len(indicadores))
    if destinos:
        info["destinatario"] = destinos[0]
        if len(set(normalizar(d) for d in destinos)) > 1:
            avisos.append("ha mais de um destinatario no formulario. O painel usa o da "
                          "primeira linha: " + destinos[0])
    if decisoes:
        info["decisao"] = decisoes[0]
        if len(set(normalizar(d) for d in decisoes)) > 1:
            avisos.append("ha mais de uma decisao no formulario. O painel usa a da "
                          "primeira linha.")
    return indicadores, erros, avisos, info


def variacao(campos):
    v = numero(campos["valor"])
    c = numero(campos["valor_comparacao"])
    if v is None or c is None or c == 0:
        return None
    return 100.0 * (v - c) / abs(c)


def fmt(v):
    if v is None:
        return "-"
    if abs(v - round(v)) < 1e-9 and abs(v) < 1e15:
        return "{:,}".format(int(round(v))).replace(",", ".")
    return "{:,.2f}".format(v).replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def fmt_pct(v):
    return ("%+.1f%%" % v).replace(".", ",")


def sentido(var, pol):
    """Texto e cor da variacao, a partir da polaridade declarada."""
    if var is None:
        return "", "#555555"
    # O texto vai para o painel, pagina em UTF-8: por isso leva acento.
    if abs(var) < 0.05:
        return "sem varia\u00e7\u00e3o", "#555555"
    if pol == "nenhuma" or pol is None:
        return fmt_pct(var), "#555555"
    favoravel = (var > 0) == (pol == "maior")
    if favoravel:
        return fmt_pct(var) + " favor\u00e1vel", TEAL_TEXTO
    return fmt_pct(var) + " desfavor\u00e1vel", VINHO


def chave_periodo(s):
    """Tupla (ano, mes, dia) quando o texto e um periodo reconhecido."""
    t = normalizar(s)
    m = re.match(r"^(\d{4})$", t)
    if m:
        return (int(m.group(1)), 0, 0)
    m = re.match(r"^(\d{4})-(\d{1,2})(?:-(\d{1,2}))?(?:[ t].*)?$", t)
    if m and 1 <= int(m.group(2)) <= 12:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3) or 0))
    m = re.match(r"^(?:(\d{1,2})/)?(\d{1,2})/(\d{4})$", t)
    if m and 1 <= int(m.group(2)) <= 12:
        return (int(m.group(3)), int(m.group(2)), int(m.group(1) or 0))
    m = re.match(r"^([a-z]{3})[a-z]*\.?[/ -]?(?:de )?(\d{4})$", t)
    if m and m.group(1) in MESES:
        return (int(m.group(2)), MESES[m.group(1)], 0)
    return None


def barras_svg(serie, rotulo, destaque):
    if not serie:
        return ""
    maximo = max(v for _, v in serie) or 1
    alt_barra, espaco = 34, 14
    larg, marg_esq = 900, 250
    altura = len(serie) * (alt_barra + espaco) + 20
    partes = ['<svg viewBox="0 0 %d %d" role="img" aria-label="%s">'
              % (larg, altura, html.escape(rotulo))]
    for i, (cat, val) in enumerate(serie):
        y = 10 + i * (alt_barra + espaco)
        comp = (larg - marg_esq - 120) * (max(val, 0) / maximo)
        if destaque is None:
            cor = VINHO
        else:
            cor = VINHO if normalizar(cat) == destaque else CINZA
        partes.append('<text x="%d" y="%d" class="cat">%s</text>'
                      % (marg_esq - 12, y + 23, html.escape(str(cat)[:34])))
        partes.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="%s"></rect>'
                      % (marg_esq, y, max(comp, 1), alt_barra, cor))
        partes.append('<text x="%.1f" y="%d" class="val">%s</text>'
                      % (marg_esq + max(comp, 1) + 10, y + 23, fmt(val)))
    partes.append("</svg>")
    return "\n".join(partes)


def linha_svg(serie, rotulo, destaque):
    if not serie:
        return ""
    larg, alt = 900, 360
    esq, dir_, topo, base = 70, 40, 40, 300
    valores = [v for _, v in serie]
    vmax = max(max(valores), 0)
    vmin = min(min(valores), 0)
    if vmax == vmin:
        vmax = vmin + 1
    n = len(serie)
    passo = (larg - esq - dir_) / max(n - 1, 1)

    def px(i):
        return esq + (i * passo if n > 1 else (larg - esq - dir_) / 2)

    def py(v):
        return base - (v - vmin) / (vmax - vmin) * (base - topo)

    partes = ['<svg viewBox="0 0 %d %d" role="img" aria-label="%s">'
              % (larg, alt, html.escape(rotulo))]
    partes.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#999" stroke-width="1.5"></line>'
                  % (esq, py(0), larg - dir_, py(0)))
    partes.append('<text x="%d" y="%.1f" class="eixo">0</text>' % (esq - 10, py(0) + 5))
    pontos = " ".join("%.1f,%.1f" % (px(i), py(v)) for i, (_, v) in enumerate(serie))
    partes.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="3"></polyline>'
                  % (pontos, VINHO))
    a_cada = 1 if n <= 12 else (n + 11) // 12
    for i, (cat, v) in enumerate(serie):
        x, y = px(i), py(v)
        em_destaque = destaque is not None and normalizar(cat) == destaque
        partes.append('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"></circle>'
                      % (x, y, 7 if em_destaque else 4, DOURADO if em_destaque else VINHO))
        if n <= 12 or i in (0, n - 1) or em_destaque:
            partes.append('<text x="%.1f" y="%.1f" class="val" text-anchor="middle">%s</text>'
                          % (x, y - 12, fmt(v)))
        if i % a_cada == 0 or i == n - 1:
            partes.append('<text x="%.1f" y="%d" class="per">%s</text>'
                          % (x, base + 30, html.escape(str(cat)[:12])))
    partes.append("</svg>")
    return "\n".join(partes)


def ler_opcoes(args):
    """Separa forma, destaque e titulo do grafico nos argumentos do painel."""
    forma, destaque, resto = None, None, []
    for a in args:
        n = normalizar(a)
        if n in ("linha", "barras", "barra"):
            forma = "linha" if n == "linha" else "barras"
        elif n.startswith("destaque="):
            destaque = n.split("=", 1)[1].strip().strip('"').strip("'") or None
        else:
            resto.append(a)
    return forma, destaque, " ".join(resto).strip()


def painel(args):
    titulo("MODULO 8 - CICLO 8.3 - GERACAO DO PAINEL")
    indicadores, erros, avisos, info = carregar()
    if erros:
        print()
        print("PROBLEMAS QUE PRECISAM SER CORRIGIDOS (%d):" % len(erros))
        for e in erros:
            print("  - " + e)
        print()
        print("O painel nao foi gerado.")
        return 1

    serie, rotulo, forma, destaque = [], "", None, None
    if args:
        linhas = ler_csv(args[0])
        if linhas is None:
            print()
            print("Nao consegui ler a serie em " + args[0])
            return 1
        colunas = list(linhas[0].keys()) if linhas else []
        if len(colunas) < 2:
            print()
            print("A serie precisa de duas colunas: categoria e valor.")
            return 1
        milhar = coluna_com_ponto_de_milhar([l.get(colunas[1]) for l in linhas],
                                            SEPARADOR_LIDO)
        for l in linhas:
            v = numero(l.get(colunas[1]), milhar)
            if v is not None:
                serie.append((str(l.get(colunas[0]) or "").strip(), v))
        forma, destaque, rotulo_dado = ler_opcoes(args[1:])
        rotulo = rotulo_dado or "%s por %s" % (colunas[1], colunas[0])
        chaves = [chave_periodo(c) for c, _ in serie]
        temporal = bool(serie) and all(k is not None for k in chaves)
        if temporal:
            serie = [s for _, s in sorted(zip(chaves, serie), key=lambda x: x[0])]
            if forma is None:
                forma = "linha"
        else:
            if forma == "linha":
                avisos.append("a primeira coluna nao foi reconhecida como periodo "
                              "(use 2026-01, 01/2026 ou jan/2026). A linha segue a ordem "
                              "do arquivo.")
            else:
                serie.sort(key=lambda x: -x[1])
                forma = "barras"
        if destaque and not any(normalizar(c) == destaque for c, _ in serie):
            avisos.append("a categoria do destaque (%s) nao esta na serie. Nenhuma "
                          "categoria foi destacada." % destaque)
            destaque = None
        pequenos = [c for c, v in serie if abs(v - round(v)) < 1e-9 and 0 < v < 5]
        if pequenos:
            avisos.append("a serie tem valor inteiro menor que 5 em: %s. Se for contagem "
                          "de pessoas, agregue a categoria ou retire do painel, porque "
                          "celula pequena permite identificar a pessoa."
                          % ", ".join(pequenos[:5]))

    cartoes = []
    for c in indicadores:
        texto_var, cor = sentido(variacao(c), c["_pol"])
        cartoes.append("""
    <article class="cartao">
      <span class="rot">%s</span>
      <p class="numero">%s <span class="un">%s</span></p>
      <p class="comp">contra %s: <strong>%s</strong> <span class="var" style="color:%s">%s</span></p>
      <p class="conc">%s</p>
      <p class="periodo">%s &middot; %s</p>
    </article>""" % (
            html.escape(c["indicador"]), html.escape(c["valor"]), html.escape(c["unidade"]),
            html.escape(c["comparacao"]), html.escape(c["valor_comparacao"]), cor,
            html.escape(texto_var), html.escape(c["titulo_conclusao"]),
            html.escape(c["periodo"]), TEXTO_POLARIDADE.get(c["_pol"], "")))

    linhas_fonte = "\n".join(
        "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
        % (html.escape(c["indicador"]), html.escape(c["formula"]),
           html.escape(c["periodo"]), html.escape(c["fonte"]),
           html.escape(c["consulta"] or "-"))
        for c in indicadores)

    grafico = ""
    if serie:
        if forma == "linha":
            desenho = linha_svg(serie, rotulo, destaque)
            nota = ("Linha na ordem do periodo, com o eixo vertical a partir de zero. "
                    "Cada ponto traz o valor escrito.")
        else:
            desenho = barras_svg(serie, rotulo, destaque)
            nota = "Barras ordenadas da maior para a menor, com base no zero."
        if destaque and forma == "linha":
            nota += " O ponto maior marca o periodo que o titulo discute."
        elif destaque:
            nota += " A categoria em destaque e a que o titulo discute. As demais servem de contexto."
        grafico = """
  <section class="bloco">
    <h2>%s</h2>
    <div class="grafico">%s</div>
    <p class="nota">%s</p>
  </section>""" % (html.escape(rotulo), desenho, nota)

    destinatario = info["destinatario"] or "a definir (coluna destinatario do formulario)"
    decisao = info["decisao"] or "a definir (coluna decisao do formulario)"

    doc = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Painel do projeto - DECC0294</title>
<style>
  :root{--vinho:%s;--dourado:%s;--teal:%s}
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:"Segoe UI",Calibri,Arial,sans-serif;color:#333;background:#f2f2f2;padding:0 0 48px}
  header{background:var(--vinho);color:#fff;padding:26px 40px 22px}
  header h1{font-size:26px;font-weight:700}
  header p{margin-top:6px;font-size:15px;color:#f1d9e2}
  .filete{height:10px;background:var(--dourado)}
  main{max-width:1060px;margin:26px auto;padding:0 20px}
  .destinatario{background:#faf7f8;border:1px solid var(--dourado);padding:14px 18px;margin-bottom:22px;font-size:15px;line-height:1.5}
  .cartoes{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
  .cartao{background:#fff;border:1px solid #e0e0e0;border-top:5px solid var(--vinho);padding:18px 20px}
  .cartao .rot{font-size:13px;font-weight:700;letter-spacing:1px;color:var(--vinho);text-transform:uppercase}
  .cartao .numero{font-size:38px;font-weight:700;color:#1a1a1a;margin-top:6px;line-height:1.1}
  .cartao .un{font-size:15px;font-weight:400;color:#666}
  .cartao .comp{font-size:14px;margin-top:8px;color:#555}
  .cartao .var{font-weight:700}
  .cartao .conc{font-size:15px;margin-top:12px;line-height:1.4;color:#1a1a1a}
  .cartao .periodo{font-size:13px;margin-top:10px;color:#666}
  .legenda-cor{font-size:13px;color:#555;margin-top:10px}
  .bloco{background:#fff;border:1px solid #e0e0e0;padding:22px 24px;margin-top:22px}
  .bloco h2{font-size:19px;color:var(--vinho);margin-bottom:16px}
  .grafico svg{width:100%%;height:auto}
  .grafico .cat{font-size:15px;fill:#333;text-anchor:end}
  .grafico .val{font-size:15px;fill:#1a1a1a;font-weight:700}
  .grafico .per{font-size:15px;fill:#333;text-anchor:middle}
  .grafico .eixo{font-size:15px;fill:#666;text-anchor:end}
  .nota{font-size:13px;color:#666;margin-top:12px}
  table{width:100%%;border-collapse:collapse;font-size:14px}
  th{background:var(--vinho);color:#fff;text-align:left;padding:9px 10px;font-weight:700}
  td{padding:8px 10px;border-bottom:1px solid #eee;vertical-align:top}
  tr:nth-child(even) td{background:#fafafa}
  footer{max-width:1060px;margin:22px auto 0;padding:0 20px;font-size:13px;color:#666}
</style>
</head>
<body>
<div class="filete"></div>
<header>
  <h1>Painel do projeto</h1>
  <p>DECC0294 &middot; Tecnologia da Informacao e Comunicacao Aplicada a Administracao &middot; UFMA</p>
  <p>Atualizado em %s</p>
</header>
<main>
  <div class="destinatario">
    <strong>Destinatario deste painel:</strong> %s<br>
    <strong>Decisao que ele sustenta:</strong> %s
  </div>
  <div class="cartoes">%s
  </div>
  <p class="legenda-cor">A variacao compara o valor com a referencia ao lado. Favor\u00e1vel ou
  desfavor\u00e1vel segue a polaridade declarada de cada indicador, e a palavra repete o que a cor mostra.</p>%s
  <section class="bloco">
    <h2>De onde vem cada numero</h2>
    <table>
      <thead><tr><th>Indicador</th><th>Formula</th><th>Periodo</th><th>Fonte e filtro</th><th>Consulta</th></tr></thead>
      <tbody>
%s
      </tbody>
    </table>
  </section>
</main>
<footer>
  Gerado em %s pelo script atividade_modulo8.py a partir de entregas/modulo8-indicadores.csv.
  Os numeros vieram das consultas registradas no modulo 7 e podem ser refeitos a partir
  dos arquivos .sql citados.
</footer>
</body>
</html>
""" % (VINHO, DOURADO, TEAL,
       datetime.now().strftime("%d/%m/%Y as %H:%M"),
       html.escape(destinatario), html.escape(decisao),
       "".join(cartoes), grafico, linhas_fonte,
       datetime.now().strftime("%d/%m/%Y"))

    os.makedirs("entregas", exist_ok=True)
    with open(PAINEL, "w", encoding="utf-8") as f:
        f.write(doc)

    if not info["destinatario"] or not info["decisao"]:
        avisos.append("destinatario ou decisao em branco no formulario. O painel mostra "
                      "'a definir' ate o ciclo 8.4.")

    print()
    print("Indicadores no painel: %d" % len(indicadores))
    if serie:
        print("Grafico: %s, com %d %s" % (forma, len(serie),
                                          "periodos" if forma == "linha" else "categorias"))
    else:
        print("Grafico: nenhum (nao foi informada a serie)")
    print()
    print("Painel gerado em: " + PAINEL)
    if avisos:
        print()
        print("PONTOS PARA VOCE REVER (%d):" % len(avisos))
        for a in avisos:
            print("  - " + a)
    print()
    print("PROXIMOS PASSOS")
    print("  Abra o arquivo no navegador e confira: os numeros batem com as consultas?")
    print("  Para mudar destinatario, decisao ou qualquer numero, edite o formulario e")
    print("  gere o painel de novo. Nao edite o painel.html: ele e regravado.")
    print("  Depois: 'execute atividade_modulo8.py com o comando conferir'")
    return 0


def conferir():
    titulo("MODULO 8 - CONFERENCIA DO PAINEL")
    indicadores, erros, avisos, info = carregar()

    if not os.path.exists(PAINEL):
        erros.append("nao encontrei " + PAINEL + ". Execute o comando 'painel'.")
    elif os.path.exists(INDICADORES) and \
            os.path.getmtime(INDICADORES) > os.path.getmtime(PAINEL) + 1:
        avisos.append("o formulario foi alterado depois da ultima geracao do painel. "
                      "Gere o painel de novo.")

    if indicadores is not None and not erros:
        if not info["destinatario"]:
            avisos.append("o destinatario ainda nao foi preenchido no formulario "
                          "(coluna destinatario, primeira linha)")
        if not info["decisao"]:
            avisos.append("a decisao ainda nao foi preenchida no formulario "
                          "(coluna decisao, primeira linha)")
    if indicadores:
        for c in indicadores:
            if not c["consulta"]:
                avisos.append("o indicador '%s' nao aponta o arquivo de consulta que o "
                              "produziu" % c["indicador"])
            elif not os.path.exists("saidas/" + c["consulta"]):
                avisos.append("nao encontrei saidas/%s, citado pelo indicador '%s'"
                              % (c["consulta"], c["indicador"]))

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
    print("Indicadores validos: %d" % (len(indicadores) if indicadores else 0))
    if erros:
        return 1
    print()
    print("PROXIMO PASSO")
    print('  "execute atividade_modulo8.py com o comando b1"')
    return 0


ITENS_B1 = [
    ("Perguntas formuladas (modulo 6)",
     ["entregas/modulo6-ciclo1-perguntas.md"]),
    ("Perfil da base (modulo 6)",
     ["entregas/modulo6-ciclo2-perfil.md"]),
    ("Tratamento de ausentes e atipicos (modulo 6)",
     ["entregas/modulo6-tratamento.csv"]),
    ("Log de verificacao (modulo 6)",
     ["entregas/modulo6-log-verificacao.csv"]),
    ("Banco povoado (modulo 7)", ["projeto.db"]),
    ("Modelo das tabelas (modulo 7)",
     ["entregas/modulo7-ciclo2-modelo.md"]),
    ("Consultas registradas (modulo 7)",
     ["entregas/modulo7-consultas.csv"]),
    ("Juncao validada (modulo 7)",
     ["entregas/modulo7-ciclo4-juncao.md"]),
    ("Reconstrucao de grafico (modulo 8)",
     ["entregas/modulo8-ciclo1-reconstrucao.md"]),
    ("Escolha de formas (modulo 8)",
     ["entregas/modulo8-ciclo2-formas.md"]),
    ("Painel (modulo 8)", [PAINEL]),
]


def _ler(caminho):
    try:
        with open(caminho, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _sha_da_ref(ref):
    """SHA de uma referencia do git, em arquivo solto ou em packed-refs."""
    solto = os.path.join(".git", *ref.split("/"))
    if os.path.exists(solto):
        return _ler(solto).strip() or None
    for l in _ler(os.path.join(".git", "packed-refs")).splitlines():
        partes = l.strip().split(" ")
        if len(partes) == 2 and partes[1] == ref:
            return partes[0]
    return None


def info_git():
    """Situacao da publicacao, lida dos arquivos da pasta .git."""
    d = {"repo": os.path.isdir(".git"), "remoto": None, "ramo": None,
         "local": None, "no_github": None, "ultimo_commit": None}
    if not d["repo"]:
        return d
    m = re.search(r'\[remote "origin"\][^\[]*?url\s*=\s*(\S+)',
                  _ler(os.path.join(".git", "config")), re.DOTALL)
    if m:
        d["remoto"] = m.group(1)
    cabeca = _ler(os.path.join(".git", "HEAD")).strip()
    if cabeca.startswith("ref:"):
        ref = cabeca[4:].strip()
        d["ramo"] = ref.rsplit("/", 1)[-1]
        d["local"] = _sha_da_ref(ref)
        d["no_github"] = _sha_da_ref("refs/remotes/origin/" + ref[len("refs/heads/"):])
    for l in reversed(_ler(os.path.join(".git", "logs", "HEAD")).splitlines()):
        m = re.search(r"> (\d{9,11}) [+-]\d{4}\t", l)
        if m:
            d["ultimo_commit"] = int(m.group(1))
            break
    return d


def situacao_publicacao(caminhos):
    g = info_git()
    if not g["repo"]:
        return False, ("Esta pasta nao e um repositorio do git. Abra a pasta do projeto "
                       "no GitHub Desktop.")
    if not g["remoto"]:
        return False, "Publique o repositorio no GitHub Desktop: Publish repository."
    if not g["no_github"]:
        return False, ("O repositorio tem endereco no GitHub, mas nenhum envio foi "
                       "registrado. No GitHub Desktop, clique em Push origin.")
    if g["local"] != g["no_github"]:
        return False, ("O ultimo commit desta pasta nao esta no GitHub. No GitHub Desktop, "
                       "clique em Push origin (ou Fetch origin e depois Push origin).")
    if g["ultimo_commit"]:
        alterados = [c for c in caminhos
                     if os.path.exists(c) and os.path.getmtime(c) > g["ultimo_commit"] + 2]
        if alterados:
            return False, ("Arquivo alterado depois do ultimo commit: %s. Faca o commit "
                           "e o Push origin." % ", ".join(alterados[:3]))
    return True, "Publicado em %s. O ultimo commit (%s) esta no GitHub." % (
        g["remoto"], (g["local"] or "")[:7])


def conferir_b1():
    titulo("MODULO 8 - CONFERENCIA DA ENTREGA B1")
    itens, presentes = [], []
    for rotulo, caminhos in ITENS_B1:
        achado = next((c for c in caminhos if os.path.exists(c)), None)
        if achado:
            presentes.append(achado)
            tamanho = os.path.getsize(achado)
            ok = tamanho > 200
            det = ("Encontrado: %s (%d bytes)." % (achado, tamanho)) if ok else \
                  ("%s existe mas esta quase vazio." % achado)
        else:
            ok, det = False, "Nao encontrei " + " nem ".join(caminhos)
        itens.append((ok, rotulo, det))

    _, erros, _, info = carregar()
    if erros:
        ok_d, det_d = False, "O formulario tem problemas. Rode o comando conferir."
    elif info["destinatario"] and info["decisao"]:
        ok_d, det_d = True, "Para: %s." % info["destinatario"]
    else:
        ok_d, det_d = False, ("Preencha as colunas destinatario e decisao na primeira "
                              "linha do formulario e gere o painel de novo.")
    itens.append((ok_d, "Destinatario e decisao declarados (modulo 8)", det_d))
    if os.path.exists(INDICADORES):
        presentes.append(INDICADORES)

    # O relatorio e gravado antes de conferir a publicacao, porque ele tambem
    # faz parte da entrega: se foi gravado agora ou se o aluno o editou depois
    # do ultimo commit, a publicacao fica pendente. Ele nao traz a publicacao,
    # e assim nao muda quando o b1 roda de novo depois do Push.
    ok_r = sum(1 for i in itens if i[0])
    anterior = _ler(RELATORIO) if os.path.exists(RELATORIO) else ""
    nome = "Nome e matricula: ______________________________"
    m = re.search(r"^Nome e matricula:.*$", anterior, re.MULTILINE)
    if m and "____" not in m.group(0):
        nome = m.group(0).rstrip()
    corpo = ["Situacao: %d de %d itens concluidos." % (ok_r, len(itens)), "",
             "| Item | Situacao | Observacao |", "|---|---|---|"]
    for ok, rotulo, det in itens:
        corpo.append("| %s | %s | %s |" % (rotulo, "concluido" if ok else "pendente", det))
    corpo += ["", "A publicacao do repositorio e conferida na tela pelo comando b1,",
              "depois do Push origin.", "",
              "## Conferido por mim", "", nome, "",
              "Declaro que os numeros do painel foram conferidos contra as consultas",
              "registradas, que cada indicador declara a sua fonte, e que o painel nao",
              "contem dado pessoal identificavel de terceiro.", ""]
    cab = ["# Relatorio da entrega B1", "",
           "Modulo 8. DECC0294, UFMA, Curso de Administracao.",
           "Gerado em %s pelo script atividade_modulo8.py."
           % datetime.now().strftime("%d/%m/%Y as %H:%M"), ""]
    sem_data = re.sub(r"^Gerado em .*$", "", anterior, flags=re.MULTILINE)
    novo = "\n".join(cab + corpo)
    if sem_data != re.sub(r"^Gerado em .*$", "", novo, flags=re.MULTILINE):
        os.makedirs("entregas", exist_ok=True)
        with open(RELATORIO, "w", encoding="utf-8") as f:
            f.write(novo)
        msg_r = "Relatorio gravado em: " + RELATORIO
    else:
        msg_r = "Relatorio sem mudanca: " + RELATORIO
    presentes.append(RELATORIO)

    ok_p, det_p = situacao_publicacao(presentes)
    todos = itens + [(ok_p, "Repositorio publicado", det_p)]

    print()
    for ok, rotulo, det in todos:
        print(("  [OK]    " if ok else "  [FALTA] ") + rotulo)
        print("           " + det)
    ok_n = sum(1 for i in todos if i[0])
    print()
    print("Concluidos: %d de %d." % (ok_n, len(todos)))
    print()
    print(msg_r)
    if "____" in nome:
        print("Abra o relatorio e escreva nome e matricula na linha indicada.")
        print("O b1 preserva essa linha quando roda de novo.")
    if ok_n < len(todos):
        print()
        print("Resolva os itens pendentes e execute 'b1' de novo.")
        return 1
    print()
    print("Entrega B1 completa e publicada.")
    return 0


def main():
    args = sys.argv[1:]
    cmd = (args[0].strip().lower() if args else "")
    if cmd in ("iniciar", "criar", "start"):
        return iniciar()
    if cmd in ("atualizar", "migrar"):
        return atualizar()
    if cmd in ("painel", "gerar"):
        return painel(args[1:])
    if cmd in ("conferir", "validar", "check"):
        return conferir()
    if cmd in ("b1", "entrega", "bloco"):
        return conferir_b1()
    print(__doc__)
    print("Comandos disponiveis:")
    print("  python atividade_modulo8.py iniciar                     cria o formulario")
    print("  python atividade_modulo8.py atualizar                   acrescenta colunas novas")
    print("  python atividade_modulo8.py painel saidas/serie.csv     gera o painel")
    print("  python atividade_modulo8.py conferir                    valida o painel")
    print("  python atividade_modulo8.py b1                          confere a entrega B1")
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
