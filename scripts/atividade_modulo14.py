"""
Atividade do modulo 14 - Produto digital e gestao agil
DECC0294 - Tecnologia da Informacao e Comunicacao Aplicada a Administracao
UFMA - Curso de Administracao

O QUE ESTE SCRIPT FAZ

Ele cria a ficha do produto, o backlog e o registro do teste com usuario,
ordena as historias por valor sobre esforco, diz o que cabe na versao 1,
grava um produto de partida e confere se a entrega do encontro esta completa.

O PRODUTO DESTE MODULO

Uma pagina HTML unica, entregas/produto.html, que abre com duplo clique, sem
servidor e sem biblioteca externa. Quem escreve a pagina e o agente, uma
historia de usuario por vez. O comando partida grava uma pagina minima para
quem travar.

Nao usa biblioteca externa, nao acessa a rede e nao usa modelo de linguagem.

COMO USAR (peca ao agente do opencode que execute cada comando)

  python atividade_modulo14.py produto
      Cria entregas/ficha-produto.md com as quatro perguntas do ciclo 14.1.

  python atividade_modulo14.py backlog
      Cria entregas/backlog.csv com as colunas exigidas.

  python atividade_modulo14.py priorizar
      Confere o formato das historias e dos criterios de aceite, ordena por
      valor sobre esforco e diz o que cabe na versao 1.
      Grava saidas/backlog-priorizado.md.

  python atividade_modulo14.py partida
      Grava em entregas/produto.html uma pagina minima (pedido de material),
      com formulario, validacao de entrada e mensagem de erro. Nao sobrescreve
      produto.html que ja exista.

  python atividade_modulo14.py teste
      Cria entregas/registro-teste.md para o teste com usuario do ciclo 14.4.

  python atividade_modulo14.py conferir
      Confere as entregas do encontro: ficha, backlog priorizado, produto.html
      e registro do teste.

ORDEM: produto -> backlog -> priorizar -> construir (ou partida) -> teste -> conferir.

A REGRA DO CRITERIO DE ACEITE

Ele precisa poder ser verificado por outra pessoa, sem voce por perto.
"Funcionar bem" nao e criterio. "O arquivo gerado abre com as cinco colunas
na ordem definida" e.
"""

import csv
import os
import sys

# Quando o script esta na pasta scripts/ do repositorio, as pastas de trabalho
# (dados/, entregas/, saidas/, prompts/) ficam um nivel acima. Copiado para a
# raiz do projeto do aluno, o script roda onde esta, sem mudanca.
_AQUI = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(_AQUI) == "scripts":
    os.chdir(os.path.dirname(_AQUI))

PASTA_SAIDAS = "saidas"
PASTA_ENTREGAS = "entregas"
FICHA = os.path.join(PASTA_ENTREGAS, "ficha-produto.md")
BACKLOG = os.path.join(PASTA_ENTREGAS, "backlog.csv")
TESTE = os.path.join(PASTA_ENTREGAS, "registro-teste.md")
PRIORIZADO = os.path.join(PASTA_SAIDAS, "backlog-priorizado.md")
PRODUTO = os.path.join(PASTA_ENTREGAS, "produto.html")

MIN_HISTORIAS = 5
MAX_HISTORIAS = 10
ESFORCO_DA_VERSAO_1 = 8

USUARIOS_VAGOS = ["os gestores", "gestores", "a equipe", "equipe", "o setor", "setor",
                  "os servidores", "servidores", "todos", "a organizacao", "a empresa",
                  "os funcionarios", "funcionarios", "os usuarios", "usuarios", "o publico"]

CRITERIOS_VAGOS = ["funcionar bem", "funcionar", "ficar bom", "ficar bonito", "estar rapido",
                   "ser facil", "ser intuitivo", "ficar pronto", "estar ok", "rodar",
                   "ficar legal", "atender o usuario", "ser util"]

# Inicio da parte "quero ..." que descreve a solucao (um elemento de tela) em
# vez da acao que a pessoa quer realizar. Comparado depois de normalizar.
SOLUCOES = ["um botao", "uma tela", "um menu", "uma aba", "uma janela", "um icone",
            "uma pagina", "um site", "um aplicativo", "um app", "um sistema",
            "um painel", "um dashboard", "um campo", "um formulario", "um link"]

CABECALHO_BACKLOG = ["id", "historia", "criterio_de_aceite", "valor", "esforco", "na_versao_1"]

EXEMPLO_BACKLOG = [
    ["EXEMPLO - apague esta linha",
     "Como assistente da divisao de pessoal, quero gerar a escala do mes a partir da planilha de plantoes, para nao redigitar 40 linhas por mes",
     "A pagina mostra uma linha por servidor com as colunas nome, data e turno, e recusa data fora do mes com mensagem",
     "5", "3", "sim"],
]

TEXTO_FICHA = """# Ficha do produto

## 1. O usuario
usuario_cargo: (o cargo de quem vai usar. Nao vale "os gestores" nem "a equipe")
quem_mais_ocuparia_esse_lugar: (quem faria isso na sua ausencia)

## 2. O caminho atual
passos_hoje: (o que a pessoa faz hoje, em passos, separados por ponto e virgula)
tempo_por_execucao_minutos: (quanto tempo leva hoje, em minutos)
frequencia: (quantas vezes por semana ou por mes)

## 3. O que muda
o_que_a_pessoa_deixa_de_fazer: (o que sai do trabalho dela com o produto)
sinal_de_que_funcionou: (o que voce vai observar para saber que ajudou. Com numero, se possivel)

## 4. O escopo da versao 1
o_que_entra: (o que a versao 1 resolve, do comeco ao fim de um caso)
o_que_fica_de_fora: (o que foi cortado para caber. Nada se perde: vai para o backlog)
"""

TEXTO_TESTE = """# Registro do teste com usuario

## A tarefa
quem_testou: (o cargo de quem testou, ou "colega da turma, no papel de [cargo]")
tarefa_dada: (a tarefa concreta, escrita, que a pessoa recebeu)
tempo_ate_concluir_minutos: (ou NAO CONCLUIU)

## O que aconteceu
Escreva uma linha por achado, no formato: descricao | bloqueio ou incomodo

achado_1: (onde a pessoa travou e o que ela tentou) | (bloqueio ou incomodo)
achado_2: | ()
achado_3: | ()

## O que a pessoa esperava
expectativa_frustrada: (o que ela achou que ia acontecer e nao aconteceu)

## A proxima versao
historias_criadas: (os ids das historias novas que voce colocou no backlog)
o_que_entra_na_versao_2: (o que vem primeiro, e por que)

## Retrospectiva
o_que_atrapalhou_a_construcao: (o que voce faria diferente na proxima)
"""


TEXTO_PARTIDA = r"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Pedido de material - produto de partida</title>
<style>
body{font-family:"Segoe UI",Arial,sans-serif;max-width:760px;margin:24px auto;padding:0 16px;color:#222}
h1{color:#8D0333;font-size:26px}
.instrucao{background:#f6f2f3;border-left:6px solid #8D0333;padding:10px 14px;font-size:15px;line-height:1.45}
.aviso{font-size:13px;color:#666}
label{display:block;margin-top:14px;font-weight:600}
input{font-size:16px;padding:5px 8px;width:260px}
.erro{color:#b00020;font-size:14px;margin-left:8px}
button{margin-top:16px;font-size:16px;padding:7px 18px;background:#8D0333;color:#fff;border:0;cursor:pointer}
#saldo{margin-top:18px;font-size:17px;font-weight:600}
table{border-collapse:collapse;margin-top:12px;width:100%}
th,td{border-bottom:1px solid #ddd;padding:6px 8px;text-align:left}
th{background:#8D0333;color:#fff}
</style>
</head>
<body>
<h1>Pedido de material</h1>
<div class="instrucao">
<b>Para que serve:</b> registrar pedidos de papel e acompanhar o saldo do almoxarifado.<br>
<b>O que entra:</b> o material e a quantidade pedida, em n&uacute;mero inteiro.<br>
<b>O que sai:</b> a lista dos pedidos registrados e o saldo atualizado.<br>
<b>Quando aparecer erro:</b> leia a mensagem em vermelho ao lado do campo, corrija e clique de novo em Registrar.
</div>
<p class="aviso">Produto de partida gravado por atividade_modulo14.py. Troque t&iacute;tulo, campos e regras pelos do seu backlog, uma hist&oacute;ria por vez. Os pedidos ficam s&oacute; nesta aba e somem quando ela &eacute; fechada.</p>
<form id="pedido" novalidate>
  <label for="material">Material</label>
  <input id="material" autocomplete="off"><span class="erro" id="erro-material"></span>
  <label for="quantidade">Quantidade (resmas)</label>
  <input id="quantidade" autocomplete="off"><span class="erro" id="erro-quantidade"></span>
  <br><button type="submit">Registrar</button>
</form>
<p id="saldo"></p>
<table><thead><tr><th>Material</th><th>Quantidade</th><th>Saldo depois do pedido</th></tr></thead>
<tbody id="lista"></tbody></table>
<script>
var SALDO_INICIAL = 40;
var UNIDADE = "resmas";
var saldo = SALDO_INICIAL;

function mostrarSaldo() {
  document.getElementById("saldo").textContent = "Saldo dispon\u00edvel: " + saldo + " " + UNIDADE + ".";
}

function erro(campo, mensagem) {
  document.getElementById("erro-" + campo).textContent = mensagem;
}

function registrar(evento) {
  evento.preventDefault();
  erro("material", "");
  erro("quantidade", "");
  var material = document.getElementById("material").value.trim();
  var texto = document.getElementById("quantidade").value.trim();
  var ok = true;
  var quantidade = 0;

  // validacao sintatica: campo preenchido, tipo e formato
  if (material === "") { erro("material", "Informe o material."); ok = false; }
  if (texto === "") {
    erro("quantidade", "Informe a quantidade."); ok = false;
  } else if (!/^[0-9]+$/.test(texto)) {
    erro("quantidade", "A quantidade precisa ser um n\u00famero inteiro."); ok = false;
  } else {
    quantidade = parseInt(texto, 10);
    // validacao semantica: o valor faz sentido para a operacao
    if (quantidade <= 0) {
      erro("quantidade", "A quantidade precisa ser maior que zero."); ok = false;
    } else if (quantidade > saldo) {
      erro("quantidade", "Saldo dispon\u00edvel de " + saldo + " " + UNIDADE + "."); ok = false;
    }
  }
  if (!ok) { return; }

  saldo = saldo - quantidade;
  var linha = document.createElement("tr");
  [material, String(quantidade), String(saldo)].forEach(function (valor) {
    var celula = document.createElement("td");
    celula.textContent = valor;
    linha.appendChild(celula);
  });
  document.getElementById("lista").appendChild(linha);
  document.getElementById("pedido").reset();
  mostrarSaldo();
}

document.getElementById("pedido").addEventListener("submit", registrar);
mostrarSaldo();
</script>
</body>
</html>
"""


def normalizar(t):
    t = (t or "").strip().lower()
    for de, para in (("á", "a"), ("à", "a"), ("ã", "a"), ("â", "a"), ("é", "e"),
                     ("ê", "e"), ("í", "i"), ("ó", "o"), ("õ", "o"), ("ô", "o"),
                     ("ú", "u"), ("ç", "c")):
        t = t.replace(de, para)
    return t


def vazio(valor):
    if not valor:
        return True
    t = str(valor)
    while "(" in t and ")" in t:
        i, j = t.index("("), t.index(")")
        if j < i:
            break
        t = t[:i] + t[j + 1:]
    return t.replace("|", " ").strip() == ""


def num(valor):
    t = str(valor or "").strip().replace(",", ".")
    try:
        return float(t)
    except ValueError:
        return None


def ler_campos(caminho):
    campos = {}
    if not os.path.exists(caminho):
        return campos
    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            bruta = linha.strip()
            if not bruta or bruta.startswith("#") or bruta.startswith("|"):
                continue
            if ":" in bruta:
                chave, valor = bruta.split(":", 1)
                chave = chave.strip().lower().replace(" ", "_")
                if chave and " " not in chave:
                    campos[chave] = valor.strip()
    return campos


# ---------------------------------------------------------------- comandos

def cmd_produto():
    os.makedirs(PASTA_ENTREGAS, exist_ok=True)
    if os.path.exists(FICHA):
        print("A ficha ja existe em", FICHA)
        return
    with open(FICHA, "w", encoding="utf-8") as f:
        f.write(TEXTO_FICHA)
    print("Ficha criada em", FICHA)
    print()
    print("O usuario precisa ser um cargo. O script recusa 'os gestores', 'a equipe'")
    print("e qualquer grupo, porque produto sem usuario definido nao tem como ser testado.")


def cmd_backlog():
    os.makedirs(PASTA_ENTREGAS, exist_ok=True)
    if os.path.exists(BACKLOG):
        print("O backlog ja existe em", BACKLOG)
        return
    with open(BACKLOG, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(CABECALHO_BACKLOG)
        for linha in EXEMPLO_BACKLOG:
            w.writerow(linha)
    print("Backlog criado em", BACKLOG)
    print()
    print("Formato da historia: Como [cargo], quero [acao], para [resultado].")
    print("valor e esforco: numeros de 1 a 8. A versao 1 comporta esforco somado de %d." % ESFORCO_DA_VERSAO_1)
    print("Escreva de %d a %d historias." % (MIN_HISTORIAS, MAX_HISTORIAS))


def cmd_partida():
    os.makedirs(PASTA_ENTREGAS, exist_ok=True)
    if os.path.exists(PRODUTO):
        print("O produto ja existe em", PRODUTO)
        print("Nada foi gravado, para nao apagar o seu trabalho. Se quiser recomecar,")
        print("renomeie o arquivo atual e rode o comando de novo.")
        return
    with open(PRODUTO, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXTO_PARTIDA)
    print("Produto de partida gravado em", PRODUTO)
    print()
    print("Abra com duplo clique na pasta entregas. A pagina registra pedidos de papel")
    print("com saldo de 40 resmas e recusa campo vazio, quantidade que nao e numero")
    print("inteiro, zero e pedido acima do saldo, com mensagem ao lado do campo.")
    print("Construa sobre ela a primeira historia do seu backlog, uma por vez.")


def cmd_teste():
    os.makedirs(PASTA_ENTREGAS, exist_ok=True)
    if os.path.exists(TESTE):
        print("O registro ja existe em", TESTE)
        return
    with open(TESTE, "w", encoding="utf-8") as f:
        f.write(TEXTO_TESTE)
    print("Registro criado em", TESTE)
    print()
    print("Fique calado enquanto a pessoa tenta. Cada ajuda sua apaga um problema")
    print("que o produto tem, e que vai aparecer de novo com o proximo usuario.")


def ler_backlog(problemas):
    if not os.path.exists(BACKLOG):
        print("O backlog nao existe. Rode: python atividade_modulo14.py backlog")
        sys.exit(1)
    with open(BACKLOG, "r", encoding="utf-8-sig", newline="") as f:
        linhas = [dict(l) for l in csv.DictReader(f, delimiter=";")]
    linhas = [l for l in linhas if not normalizar(l.get("id")).startswith("exemplo")]

    validas = []
    for i, l in enumerate(linhas, 2):
        ident = (l.get("id") or ("linha %d" % i)).strip()
        historia = normalizar(l.get("historia"))
        if vazio(l.get("historia")):
            problemas.append("%s: historia vazia." % ident)
        else:
            if "como " not in historia:
                problemas.append("%s: a historia nao comeca por 'Como [cargo]'." % ident)
            if "quero " not in historia:
                problemas.append("%s: a historia nao tem a parte 'quero [acao]'." % ident)
            if "para " not in historia:
                problemas.append("%s: a historia nao tem a parte 'para [resultado]'. "
                                 "E a parte que justifica construir." % ident)
            if "quero " in historia:
                acao = historia.split("quero ", 1)[1].strip()
                solucao = [x for x in SOLUCOES if acao == x or acao.startswith(x + " ")]
                if solucao:
                    problemas.append("%s: depois de 'quero' vem a solucao ('%s'), e nao a acao. "
                                     "Escreva o que a pessoa quer fazer, com verbo, como "
                                     "'quero exportar o mapa em PDF'." % (ident, solucao[0]))

        criterio = (l.get("criterio_de_aceite") or "").strip()
        cn = normalizar(criterio)
        if vazio(criterio):
            problemas.append("%s: criterio de aceite vazio." % ident)
        elif any(cn == v or cn.startswith(v) for v in CRITERIOS_VAGOS):
            problemas.append("%s: o criterio '%s' nao permite dizer que ficou pronto. "
                             "Escreva o que outra pessoa verificaria sem voce por perto."
                             % (ident, criterio))
        elif len(criterio.split()) < 6:
            problemas.append("%s: o criterio de aceite tem %d palavras. Escreva a condicao "
                             "observavel inteira." % (ident, len(criterio.split())))

        valor = num(l.get("valor"))
        esforco = num(l.get("esforco"))
        if valor is None or not (1 <= valor <= 8):
            problemas.append("%s: valor precisa ser um numero de 1 a 8." % ident)
        if esforco is None or not (1 <= esforco <= 8):
            problemas.append("%s: esforco precisa ser um numero de 1 a 8." % ident)
        if valor is not None and esforco is not None and 1 <= valor <= 8 and 1 <= esforco <= 8:
            validas.append((ident, l, valor, esforco))

    if len(linhas) < MIN_HISTORIAS:
        problemas.append("ha %d historias. O minimo e %d." % (len(linhas), MIN_HISTORIAS))
    if len(linhas) > MAX_HISTORIAS:
        problemas.append("ha %d historias. O maximo e %d: backlog longo demais nesta altura "
                         "detalha o que ainda vai mudar." % (len(linhas), MAX_HISTORIAS))
    return linhas, validas


def cmd_priorizar():
    problemas = []
    linhas, validas = ler_backlog(problemas)

    if problemas:
        print("=" * 62)
        print("O BACKLOG AINDA NAO PODE SER PRIORIZADO")
        print("=" * 62)
        for i, p in enumerate(problemas, 1):
            print(" %d. %s" % (i, p))
        sys.exit(1)

    ordenado = sorted(validas, key=lambda x: (-(x[2] / x[3]), x[3]))

    acumulado = 0.0
    cabem = []
    for ident, l, valor, esforco in ordenado:
        if acumulado + esforco <= ESFORCO_DA_VERSAO_1:
            acumulado += esforco
            cabem.append(ident)

    marcadas = [l.get("id", "").strip() for _, l, _, _ in validas
                if normalizar(l.get("na_versao_1")).startswith("s")]

    print("=" * 62)
    print("BACKLOG PRIORIZADO")
    print("=" * 62)
    print("historias:", len(validas))
    print()
    print("  %-22s %6s %8s %8s" % ("id", "valor", "esforco", "razao"))
    for ident, l, valor, esforco in ordenado:
        print("  %-22s %6s %8s %8s" % (ident[:22], int(valor), int(esforco),
                                       ("%.2f" % (valor / esforco)).replace(".", ",")))
    print()
    print("Cabe na versao 1 (esforco somado ate %d): %s" % (ESFORCO_DA_VERSAO_1, ", ".join(cabem) or "nenhuma"))
    print("Esforco acumulado:", int(acumulado))
    print()

    if marcadas:
        fora = [m for m in marcadas if m not in cabem]
        if fora:
            print("Voce marcou como versao 1: %s" % ", ".join(marcadas))
            if len(fora) == 1:
                lista_fora, verbo = fora[0], "fica"
            else:
                lista_fora, verbo = ", ".join(fora[:-1]) + " e " + fora[-1], "ficam"
            print("Destas, %s %s fora do que cabe pela ordem de valor sobre esforco."
                  % (lista_fora, verbo))
            print("Isso pode estar certo, se houver dependencia entre historias. Se for o caso,")
            print("escreva a dependencia no backlog. Se nao for, refaca o corte.")
        else:
            print("A sua marcacao de versao 1 coincide com a ordem calculada.")
    else:
        print("Nenhuma historia marcada na coluna na_versao_1. Marque as que voce vai construir.")

    print()
    print("A ordem por valor sobre esforco e sugestao, e nao decisao. Dependencia entre")
    print("historias e obrigacao legal mudam a ordem, e isso se escreve.")

    os.makedirs(PASTA_SAIDAS, exist_ok=True)
    with open(PRIORIZADO, "w", encoding="utf-8") as f:
        f.write("# Backlog priorizado\n\n")
        f.write("| id | historia | criterio de aceite | valor | esforco | razao |\n")
        f.write("|---|---|---|---|---|---|\n")
        for ident, l, valor, esforco in ordenado:
            f.write("| %s | %s | %s | %d | %d | %s |\n" % (
                ident, (l.get("historia") or "").replace("|", "/"),
                (l.get("criterio_de_aceite") or "").replace("|", "/"),
                int(valor), int(esforco), ("%.2f" % (valor / esforco)).replace(".", ",")))
        f.write("\ncabe_na_versao_1: %s\n" % ", ".join(cabem))
        f.write("esforco_acumulado: %d\n" % int(acumulado))
        f.write("limite_de_esforco: %d\n" % ESFORCO_DA_VERSAO_1)
    print()
    print("Resultado gravado em", PRIORIZADO)


# ------------------------------------------------------------- conferencia

def conferir_ficha(problemas):
    if not os.path.exists(FICHA):
        problemas.append("ficha-produto.md nao existe. Rode: python atividade_modulo14.py produto")
        return
    campos = ler_campos(FICHA)
    obrigatorios = [
        ("usuario_cargo", "o cargo do usuario"),
        ("quem_mais_ocuparia_esse_lugar", "quem mais ocuparia esse lugar"),
        ("passos_hoje", "os passos do caminho atual"),
        ("tempo_por_execucao_minutos", "o tempo por execucao"),
        ("frequencia", "a frequencia"),
        ("o_que_a_pessoa_deixa_de_fazer", "o que a pessoa deixa de fazer"),
        ("sinal_de_que_funcionou", "o sinal de que funcionou"),
        ("o_que_entra", "o escopo da versao 1"),
        ("o_que_fica_de_fora", "o que ficou de fora"),
    ]
    for chave, nome in obrigatorios:
        if vazio(campos.get(chave)):
            problemas.append("ficha-produto.md: falta %s (campo %s)." % (nome, chave))

    usuario = normalizar(campos.get("usuario_cargo"))
    if usuario and usuario in USUARIOS_VAGOS:
        problemas.append("ficha-produto.md: '%s' e um grupo, nao um cargo. Escolha uma pessoa "
                         "concreta pelo cargo, porque o produto e escrito para ela."
                         % campos.get("usuario_cargo"))

    tempo = num(campos.get("tempo_por_execucao_minutos"))
    if not vazio(campos.get("tempo_por_execucao_minutos")) and tempo is None:
        problemas.append("ficha-produto.md: o tempo por execucao precisa ser um numero de "
                         "minutos. Sem ele nao ha como dizer depois se o produto ajudou.")

    passos = campos.get("passos_hoje") or ""
    if not vazio(passos) and passos.count(";") < 2:
        problemas.append("ficha-produto.md: o caminho atual tem menos de tres passos. "
                         "Descreva o que a pessoa faz hoje com grao fino, separando por ponto e virgula.")


def conferir_produto(problemas):
    if not os.path.exists(PRODUTO):
        problemas.append("produto.html nao existe. Construa a versao 1 ou rode o comando partida.")
        return
    with open(PRODUTO, "r", encoding="utf-8", errors="replace") as f:
        conteudo = f.read().replace("\r\n", "\n")
    if conteudo.strip() == TEXTO_PARTIDA.strip():
        problemas.append("produto.html ainda e o produto de partida, sem alteracao. Construa "
                         "sobre ele pelo menos uma historia do seu backlog.")


def conferir_teste(problemas):
    if not os.path.exists(TESTE):
        problemas.append("registro-teste.md nao existe. Rode: python atividade_modulo14.py teste")
        return
    campos = ler_campos(TESTE)
    obrigatorios = [
        ("quem_testou", "quem testou"),
        ("tarefa_dada", "a tarefa dada"),
        ("tempo_ate_concluir_minutos", "o tempo ate concluir, ou NAO CONCLUIU"),
        ("expectativa_frustrada", "o que a pessoa esperava e nao aconteceu"),
        ("historias_criadas", "as historias criadas a partir do teste"),
        ("o_que_entra_na_versao_2", "o que entra na versao 2"),
        ("o_que_atrapalhou_a_construcao", "a retrospectiva"),
    ]
    for chave, nome in obrigatorios:
        if vazio(campos.get(chave)):
            problemas.append("registro-teste.md: falta %s (campo %s)." % (nome, chave))

    achados = [(k, v) for k, v in campos.items() if k.startswith("achado_") and not vazio(v)]
    if not achados:
        problemas.append("registro-teste.md: nenhum achado registrado. Teste em que nada travou "
                         "quase sempre teve tarefa facil demais ou ajuda sua. Refaca com uma "
                         "tarefa mais dificil, ou escreva por que nada apareceu.")
    for chave, valor in achados:
        if "|" not in valor:
            problemas.append("registro-teste.md, %s: falta a classificacao depois da barra "
                             "(bloqueio ou incomodo)." % chave)
            continue
        _, _, classe = valor.partition("|")
        classe = normalizar(classe)
        if "bloqueio" not in classe and "incomodo" not in classe:
            problemas.append("registro-teste.md, %s: a classificacao precisa ser bloqueio ou "
                             "incomodo. Bloqueio vem antes na fila." % chave)


def cmd_conferir():
    problemas = []
    print("=" * 62)
    print("CONFERENCIA DO MODULO 14")
    print("=" * 62)
    conferir_ficha(problemas)
    if not os.path.exists(PRIORIZADO):
        problemas.append("backlog-priorizado.md nao existe. Rode: python atividade_modulo14.py priorizar")
    else:
        ler_backlog(problemas)
    conferir_produto(problemas)
    conferir_teste(problemas)

    if problemas:
        if len(problemas) == 1:
            print("A entrega ainda nao esta completa. Falta 1 item:\n")
        else:
            print("A entrega ainda nao esta completa. Faltam", len(problemas), "itens:\n")
        for i, p in enumerate(problemas, 1):
            print(" %d. %s" % (i, p))
        print()
        print("Corrija e rode a conferencia de novo.")
        sys.exit(1)

    print("Entrega completa.")
    print()
    print("  ficha-produto.md          usuario pelo cargo, caminho atual medido, escopo cortado")
    print("  backlog.csv               historias no formato, com criterio de aceite verificavel")
    print("  backlog-priorizado.md     ordem por valor sobre esforco e o que cabe na versao 1")
    print("  produto.html              a pagina do produto, alterada sobre a de partida")
    print("  registro-teste.md         achados classificados e proxima versao definida")
    print()
    print("Faca o commit pelo GitHub Desktop. No modulo 15 voce apresenta o produto,")
    print("inclusive o que ainda nao funciona.")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    comando = sys.argv[1].lower()
    if comando == "produto":
        cmd_produto()
    elif comando == "backlog":
        cmd_backlog()
    elif comando == "priorizar":
        cmd_priorizar()
    elif comando == "partida":
        cmd_partida()
    elif comando == "teste":
        cmd_teste()
    elif comando == "conferir":
        cmd_conferir()
    else:
        print("Comando desconhecido:", comando)
        print("Use: produto, backlog, priorizar, partida, teste, conferir")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        print("\nInterrompido.")
