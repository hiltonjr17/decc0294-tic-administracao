# Errata da turma 2026.2

DECC0294, Tecnologia da Informação e Comunicação Aplicada à Administração, UFMA. Versão de 14 nov. 2026.

Errata é a lista de erros encontrados no material depois de entregue, com a correção de cada um. Esta página traz só o que muda alguma entrega que ainda vai acontecer (C1, C2 e módulos 11 a 15) ou algum arquivo que você ainda vai reaproveitar. Erros dos módulos 1 a 10 que não afetam mais nada ficam para a próxima turma e não aparecem aqui.

Três termos usados em toda a página:

- **Script**: o arquivo `atividade_moduloN.py`, um programa curto em Python que o agente do opencode executa a seu pedido. Você não precisa ler nem editar o código.
- **CSV**: arquivo de tabela em texto puro, uma linha por registro. As colunas são divididas por um caractere chamado **separador**. No Excel em português o separador é o ponto e vírgula, e a vírgula fica para as casas decimais.
- **Commit**: o registro de uma versão da pasta do projeto, feito no GitHub Desktop.

## Como trocar um script pela versão nova

Os itens 1 a 5 pedem a versão de 14 nov. 2026 de um script. O procedimento é o mesmo para todos.

1. Baixe o script na turma virtual.
2. Coloque o arquivo na pasta do projeto, no mesmo lugar da cópia antiga e com o mesmo nome, substituindo a antiga.
3. Confira se a troca deu certo. Peça ao agente: "procure no arquivo atividade_moduloN.py o texto X e me diga se ele aparece", com o texto indicado no item. Se o texto não aparecer, a cópia ainda é a antiga.
4. Faça o commit no GitHub Desktop, com uma mensagem como "Atualiza script do módulo N".

## Resumo

| Item | Onde aparece | O que você faz |
|---|---|---|
| 1. Conferência da C2 (`atividade_modulo15.py`) | Módulo 15, C2 | Baixar a versão nova antes do módulo 15. Gerar os relatórios dos módulos 9 e 10 se ainda não existem |
| 2. Modelo preditivo (`atividade_modulo11.py`) | Módulo 11, C1 | Baixar a versão nova antes do módulo 11 |
| 3. Inventário de dados (`atividade_modulo12.py`) | Módulo 12, C1 | Baixar a versão nova antes do módulo 12 |
| 4. Mapa do documento (`atividade_modulo13.py`) | Módulo 13, C1 | Baixar a versão nova antes do módulo 13 |
| 5. Produto digital (`atividade_modulo14.py`) | Módulo 14 | Baixar a versão nova. Só o texto de uma mensagem mudou |
| 6. Números com ponto de milhar nos scripts 6, 7 e 8 | Reuso da base no módulo 11 e na C2 | Não reaproveitar números afetados sem conferir |
| 7. Contagem de registros sem par no módulo 7 | Reuso da junção no módulo 13, 14 ou na C2 | Refazer a contagem antes de citar o número |
| 8. Coluna com todos os decimais de três casas no módulo 11 | Módulo 11, com CSV separado por ponto e vírgula | Conferir a média do treino |

## 1. Conferência da C2: `atividade_modulo15.py`

**Onde aparece.** Módulo 15. O comando `c2` lista, módulo a módulo, os arquivos do semestre que estão na pasta e os que faltam. O que ele apontar como pendente conta como não entregue na C2.

**O que estava errado.** A versão antiga procurava nomes de arquivo que nenhum módulo manda criar. Um aluno com tudo entregue via os módulos 3, 5, 9 e 10 como ausentes. A versão antiga também numerava as linhas por encontro e não por módulo, e o roteiro de apresentação que ela grava trazia minutos por bloco.

**O que mudou.** O `c2` procura os nomes que os scripts de fato gravam e numera por módulo (2 a 15). O roteiro de apresentação (`entregas/roteiro-apresentacao.md`) saiu sem tempos, com a frase "A duracao da apresentacao e informada em sala". O comando `portfolio` passou a incluir a pasta `prompts/`. As mensagens indicam o pedido ao agente, e não um comando digitado.

**O que você faz.**

1. Troque o script pela versão nova antes do módulo 15. Texto para conferir a versão: `modulos 2 a 15`.
2. Se você já rodou o `c2` com a cópia antiga, desconsidere o resultado e rode de novo: "execute atividade_modulo15.py com o comando c2".
3. Se você já criou o roteiro de apresentação com a cópia antiga, ele continua com os minutos, porque o script não regrava um roteiro que já existe. Apague os minutos à mão ou peça ao agente que os retire.
4. Confira se estes arquivos existem na sua pasta. O `c2` aceita o nome exato ou, onde está escrito "começa com", qualquer arquivo cujo nome comece com aquele trecho (prefixo).

| Módulo | Arquivos que o `c2` procura |
|---|---|
| 2 | `AGENTS.md` e `README.md` |
| 3 | começa com `entregas/modulo3-diario-de-alucinacao` |
| 4 | `dados/api-diagnostico.md` |
| 5 | começa com `entregas/modulo5-mapa-de-dados` |
| 6 | começa com `entregas/modulo6-` |
| 7 | começa com `entregas/modulo7-` |
| 8 | `entregas/painel.html` |
| 9 | `entregas/modulo9-fluxo.csv` e `entregas/modulo9-relatorio.md` |
| 10 | `entregas/modulo10-codificacao.csv` e `entregas/modulo10-relatorio.md` |
| 11 | `modelo/ficha-modelo.md` e `modelo/resultado.md` |
| 12 | `saidas/varredura-dados-pessoais.md`, `entregas/inventario-dados.csv`, `entregas/plano-resposta-incidente.md` e `.gitignore` |
| 13 | `entregas/matriz-decisao.csv`, `saidas/resultado-decisao.md`, `entregas/mapa-documento.md` e `entregas/devolutiva.md` |
| 14 | `entregas/ficha-produto.md`, `entregas/backlog.csv`, `saidas/backlog-priorizado.md` e `entregas/registro-teste.md` |
| 15 | `entregas/roteiro-apresentacao.md` e `entregas/avaliacao-pares.md` |

5. Atenção aos módulos 9 e 10. Os arquivos `modulo9-relatorio.md` e `modulo10-relatorio.md` só são gravados quando o comando `conferir` do módulo correspondente termina sem problema. Se o seu `conferir` acusou erro e você não corrigiu, o relatório não existe e o `c2` marca o módulo como incompleto. Corrija o que o `conferir` apontou e peça de novo: "execute atividade_modulo9.py com o comando conferir" (e o mesmo com `atividade_modulo10.py`).

O `c2` confere só se o arquivo existe, e não o conteúdo. A conferência do conteúdo continua sendo a de cada módulo.

## 2. Modelo preditivo: `atividade_modulo11.py`

**Onde aparece.** Módulo 11. A ficha do modelo e o resultado entram na C1.

**O que estava errado.**

- Quando o modelo perdia para o palpite simples (prever sempre a média), a mensagem mandava trocar de coluna. Testar colunas até uma ganhar e relatar só essa compromete o teste.
- O comando `conferir` recusava "não" com acento.
- Em CSV separado por ponto e vírgula, o valor "12.480" (doze mil quatrocentos e oitenta) era lido como 12,48.

**O que mudou.**

- A ficha pede duas preditoras (as colunas usadas para prever o alvo), escritas antes do treino e na ordem em que você vai testá-las. A mensagem do modelo que perde diz que o resultado é válido e deve ser registrado sem troca de coluna.
- O `conferir` aceita "não" e "nao".
- O percentual sai com vírgula decimal ("70,6%").
- Quando o teste tem menos de 20 casos, o script avisa que a diferença entre modelo e palpite não sustenta decisão.
- Em CSV separado por ponto e vírgula, "12.480" e "R$ 12.480" passam a ser lidos como 12.480 quando a coluna segue o padrão do Excel em português. A decisão é tomada por coluna, e as tabelas do módulo 7, que usam ponto decimal, continuam lidas certo.

**O que você faz.** Troque o script antes do módulo 11. Texto para conferir a versão: `na ordem em que vai testa-las`. Siga o slide da prática do ciclo 11.4: uma execução com a primeira preditora, outra com as duas, e os erros das duas na seção Leitura. Veja também o item 8.

## 3. Inventário de dados: `atividade_modulo12.py`

**Onde aparece.** Módulo 12. O inventário entra na C1.

**O que estava errado.** Quando nenhum campo do inventário podia ser eliminado, o script mandava escrever "nao - revisado" na coluna `poderia_ser_eliminado`, e o próprio `conferir` recusava essa resposta.

**O que mudou.** O `conferir` aceita "nao - revisado" e "não - revisado".

**O que você faz.** Troque o script antes do módulo 12. Texto para conferir a versão: `revisadas`.

## 4. Mapa do documento: `atividade_modulo13.py`

**Onde aparece.** Módulo 13. O mapa do documento e a devolutiva entram na C1.

**O que estava errado.** O `conferir` exigia ao menos uma categoria marcada como NAO CONSTA, mesmo quando o documento tratava das cinco categorias.

**O que mudou.** O `conferir` aceita a frase "todas as categorias constam" no mapa, com ou sem acento. O comando `c1`, que confere a C1 inteira, passou a identificar cada item pelo módulo (11, 12 e 13).

**O que você faz.** Troque o script antes do módulo 13. Texto para conferir a versão: `todas as categorias constam`. Se o seu documento trata das cinco categorias, escreva essa frase no mapa.

## 5. Produto digital: `atividade_modulo14.py`

**Onde aparece.** Módulo 14.

**O que mudou.** Só a mensagem final do `conferir`, que dizia "encontro 16" e passou a dizer "modulo 15". O funcionamento não mudou.

**O que você faz.** Troque o script quando baixar os demais, para manter a pasta igual à da turma. Texto para conferir a versão: `No modulo 15 voce apresenta`.

## 6. Números com ponto de milhar nos scripts dos módulos 6, 7 e 8

**Onde aparece.** Em qualquer reuso da base ou dos números produzidos nos módulos 6, 7 e 8: no módulo 11, se você treinar o modelo com a mesma base, e na C2, se citar esses números no roteiro de apresentação ou no portfólio.

**O que está errado.** Os scripts dos módulos 6 (perfil e atípicos), 7 (banco de dados) e 8 (painel) leem um número com ponto de milhar e sem casa decimal como número decimal. "12.480" e "R$ 12.480" viram 12,48. Um número com dois pontos de milhar, como "1.234.567", não é reconhecido como número. O mesmo número escrito com centavos ("12.480,00") ou sem ponto ("12480") é lido certo. A base original em `dados/` não é alterada. O erro fica nos números que o script calculou: mínimo, máximo, média, mediana e atípicos do perfil do módulo 6, os valores gravados no banco do módulo 7 e nas tabelas `saidas/consulta-N.csv`, e as barras do painel do módulo 8. O script do módulo 7 também grava como número um CNPJ escrito só com dígitos, e com isso perde os zeros à esquerda.

**O que mudou.** Esses scripts não foram alterados neste semestre. Só o script do módulo 11 foi corrigido (item 2).

**O que você faz.**

1. Peça ao agente: "abra o arquivo dados/SUA-BASE.csv e diga se alguma coluna numérica tem valores com ponto de milhar e sem vírgula decimal, como 12.480". Se não tiver, este item não afeta você.
2. Se tiver, não reaproveite os números do perfil do módulo 6, das consultas do módulo 7 nem do painel do módulo 8 para essa coluna. Para usar a base de novo, peça ao agente uma cópia em `dados/` com essa coluna escrita sem ponto de milhar (12480), mantenha o arquivo original e registre a troca no seu caderno de prompts.
3. No módulo 11, use o arquivo original ou a cópia, e não um `saidas/consulta-N.csv` feito com essa coluna, porque nele o valor já foi gravado errado.
4. Se você usa CNPJ como chave em tabela que veio do módulo 7, confira se os zeros à esquerda continuam lá antes de juntar com outra tabela.

## 7. Contagem de registros sem par no módulo 7

**Onde aparece.** Em qualquer reuso da junção do módulo 7 (comando `juntar`), por exemplo para citar no módulo 13, no módulo 14 ou na C2 quantos registros de uma tabela não têm correspondente na outra.

**O que está errado.** Quando a coluna usada como chave (o código que liga as duas tabelas) tem alguma célula vazia, o `juntar` informa zero registros sem par, ou um número menor que o real. Num teste com três registros e um sem par, o resultado foi 0 em vez de 1.

**O que mudou.** O script não foi alterado neste semestre.

**O que você faz.** Antes de citar esse número, peça ao agente: "conte, no banco do módulo 7, quantos registros de TABELA_A não têm correspondente em TABELA_B pela coluna CHAVE, usando NOT EXISTS, e quantas linhas de cada tabela têm a chave vazia". Use o número dessa contagem.

## 8. Coluna com todos os decimais de três casas no módulo 11

**Onde aparece.** Módulo 11, quando a base do modelo é um CSV separado por ponto e vírgula que usa ponto como separador decimal, como as tabelas `saidas/consulta-N.csv` gravadas pelo módulo 7.

**O que está errado.** O script decide, coluna por coluna, se o ponto separa milhar ou casas decimais. Ele trata o ponto como milhar quando algum valor da coluna tem vírgula decimal ou quando todo valor com ponto tem o formato de milhar: um a três algarismos seguidos de grupos de exatamente três (12.480, 1.234.567). Uma coluna em que todos os valores com ponto têm exatamente três casas, como 2.125, 45.678 e 1.000, é ambígua e é lida como milhar. Em coluna com valores como 45.678912 ou 12.5, o ponto é lido como decimal.

**O que mudou.** A primeira versão da correção de 14 nov. 2026 decidia valor por valor e lia "45.678" como milhar mesmo numa coluna de decimais. A versão final decide por coluna e deixa só o caso ambíguo descrito acima.

**O que você faz.** Depois do comando `prever`, confira se a "media do treino" que o script imprime tem a ordem de grandeza que você espera para a coluna alvo. Se estiver mil vezes maior, peça ao agente uma cópia do arquivo em `dados/` com essa coluna escrita com vírgula decimal (45,678) e treine com a cópia.
