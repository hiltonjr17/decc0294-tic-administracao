# Roteiro do módulo 15

Projeto integrador. Encontro 16, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Último encontro. Fecha a entrega C2, que vale 60% da nota 3, e encerra a disciplina.

## Antes da aula

Material do professor: `slides/modulo15-projeto-integrador.html`, este roteiro e `scripts/atividade_modulo15.py`.

Publicado na turma virtual: o script, a estrutura dos quatro blocos da apresentação, a rubrica da C2 (slide 6) e o lembrete de que a demonstração ao vivo é obrigatória, incluindo o caso com dado errado em `entregas/produto.html`.

Ordem das apresentações, com código. Monte a ordem antes da aula e publique-a com um código por apresentação (A01, A02...). O deck (slide 12) usa a ordem para três regras que não dependem de decisão na hora: a ordem vale para as duas rodadas, cada aluno avalia as três apresentações seguintes à sua em ciclo (depois da última vem a primeira) e colega ausente é substituído pela apresentação seguinte da ordem. O formulário de pares identifica a apresentação pelo código, e o comando `pares` recusa nome no campo `quem_apresentou_N`.

Formato pelo tamanho da turma. O slide 12 traz a regra: até 12 alunos, apresentação individual; com 13 ou mais, apresentação em dupla, publicada junto da ordem, com o tempo dividido e cada aluno demonstrando o próprio produto. O limite de 12 e a forma da dupla são proposta a validar pelo professor antes de publicar a ordem. Se a regra mudar, altere a caixa "Formato pelo tamanho da turma" do slide 12.

Confira a sala: projeção, tomada, e um plano para quem for apresentar de máquina própria. O produto é a página `entregas/produto.html`, que abre com duplo clique, sem servidor, e por isso roda em qualquer máquina com navegador. Perder cinco minutos por apresentação em troca de cabo derruba o encontro inteiro.

Prepare a lista de pendências por aluno, da última rodada de `c1` e `conferir`. O ciclo 15.1 depende dela.

Comando `c2`. A lista `ENTREGAS` foi corrigida em 14 nov. 2026 e revista no mesmo dia: o módulo 14 passou a incluir `entregas/produto.html` (decisão do professor sobre a forma do produto), e o módulo 15 passou a incluir o caderno de prompts, aceito como qualquer arquivo de `prompts/` cujo nome comece por `modulo` (os módulos 2, 3 e 9 gravam `prompts/modulo2-...`, `prompts/modulo3-...` e `prompts/modulo9-modelo.md`, e o slide 9 pede `prompts/modulo14-produto.md`). Se o deck do módulo 14 adotar outro nome para o produto, a lista precisa acompanhar.

O tempo das apresentações depende do tamanho da turma. O roteiro abaixo prevê duas rodadas somando 130 minutos, o que comporta cerca de doze apresentações de dez minutos com transição. Com duplas, o número de apresentações cai à metade e cabe no mesmo tempo.

## Rubrica da C2: proposta a validar

A rubrica do slide 6 é proposta, a validar pelo professor antes de ser publicada. Ela segue o plano de atualização (seção 3, fase 5, item 2): peso maior para o caminho documentado e a conferência do que para o produto funcionando.

| Parte | Pontos | Divisão |
|---|---|---|
| Caminho documentado | 2,5 | ficha e backlog com a fila revista depois do teste (1,0), registro do teste com achados classificados (1,0), commits ao longo do trabalho (0,5) |
| Conferência | 1,5 | `c2` sem pendência ou pendência declarada (0,5), `c1` e `conferir` sem recusa (0,5), portfólio com as três frases (0,5) |
| Caderno de prompts | 1,5 | um arquivo por técnica ou etapa com pedido, resultado e correção (1,0), pedidos que construíram o produto (0,5) |
| Produto | 2,0 | história completa segundo o critério de aceite (1,0), dado inválido recusado com mensagem (1,0) |
| Apresentação | 1,5 | quatro blocos (0,5), demonstração ao vivo do caso completo e do dado errado (0,5), bloco 4 dito (0,5) |
| Avaliação dos colegas (o formulário do aluno) | 1,0 | três apresentações com `pares` sem pendência (0,5), justificativas que citam o que se viu (0,5) |

Caminho, conferência e caderno somam 5,5 pontos, contra 2,0 do produto. Papel dos formulários de pares (slide 7): o formulário que o aluno preenche vale 1,0 ponto. Os formulários que os colegas escrevem sobre ele não viram ponto e servem ao professor como registro do que a turma viu na demonstração. Isso substitui a frase anterior do deck sobre "devolutiva sem nota numérica", que deixava o papel do formulário ambíguo.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura | 5 min | 1 a 3 |
| Ciclo 15.1 | 40 min | 4 a 10 |
| Ciclo 15.2 | 70 min | 11 a 17 |
| Intervalo | 15 min | |
| Ciclo 15.3 | 60 min | 18 a 20 |
| Ciclo 15.4 | 40 min | 21 a 26 |
| Encerramento | 10 min | 27 a 30 |

O deck foi revisado em novembro de 2026 e passou de 20 para 26 slides. Em 14 nov. 2026 passou a 29 slides: vocabulário do módulo (2), rubrica da C2 com pontos (6), como a correção lê a C2, com o papel dos formulários de pares (7), e ordem, formato e quem avalia quem (12). As práticas (9, 17, 19 e 24) ganharam as caixas de resultado esperado e do que fazer quando o resultado for outro.

## Abertura

O vocabulário do módulo (slide 2) define os termos que o deck usa: entrega C2, agente de IA, script e comando, os comandos de conferência `c1`, `conferir` e `c2`, README.md, AGENTS.md e `dados/restrito/`, commit e push, produto digital, backlog e história de usuário, critério de aceite, teste com usuário, caderno de prompts, rubrica, avaliação por pares e portfólio. Não precisa ser lido em voz alta. Serve de consulta para quem perdeu o módulo 14.

## Ciclo 15.1 — Conferência da C2 e últimas correções

Teoria e demonstração, 5 min. O semestre na pasta (slide 5): os quinze módulos por nota, as seis entregas e o arquivo que o `c2` procura em cada módulo, agora com `entregas/produto.html` no módulo 14 e o caderno de prompts no 15. A rubrica de dez pontos (slide 6). O peso das partes, o papel dos formulários de pares, o que fica fora da avaliação, a regra de pendência e o critério comum às seis entregas (slide 7). A saída do `c2` sobre uma pasta de teste, com os módulos 14 e 15 parciais (slide 8). A saída do slide 8 foi gerada pelo script revisto, sobre pasta fictícia.

Prática, 35 min. Cada aluno roda `c2`, confere o conteúdo com `c1` do módulo 13 e `conferir` do módulo 14, completa o caderno de prompts com `prompts/modulo14-produto.md`, corrige com um commit por correção e cria o roteiro com o comando `apresentacao` (slides 9 e 10). O slide 9 traz o resultado esperado e o que fazer com arquivo de nome diferente, pendência sem solução, recusa do `c1` ou do `conferir` e pedidos do módulo 14 não guardados (reescritos de memória e marcados como reconstituídos). O passo 2 traz o texto do pedido que cria `prompts/modulo14-produto.md`.

Entrega, incluída na prática.

Entregue a lista de pendências impressa no início. O aluno que descobre a pendência pelo papel corrige em dez minutos; o que descobre pelo script no meio da apresentação, não corrige.

Deixe claro, uma vez, que esta é a última janela do semestre. Depois disso a nota fecha com o que estiver na pasta.

Quem estiver com tudo em ordem usa o tempo para ensaiar a demonstração. Peça que rode o caso com dado errado ao menos uma vez antes de apresentar.

## Ciclo 15.2 — Apresentações, primeira rodada

Teoria e demonstração, 5 min. A ordem publicada, o formato pelo tamanho da turma e a escala de avaliadores, com o exemplo de oito apresentações (slide 12). Os quatro blocos e os campos de `entregas/roteiro-apresentacao.md`, com a demonstração aberta em `entregas/produto.html` (slide 13). Validação de entrada, sintática e semântica, retomada do módulo 14 com a definição completa no slide, ilustrada pelo produto de pedidos ao almoxarifado (slide 14, conceito da OWASP, reconferido em 14/11/2026). A avaliação por pares com respostas aceitas e recusadas pelo script e o valor do formulário na C2 (slide 15, Topping, 1998, e Hattie e Timperley, 2007). A saída do comando `pares` sobre um formulário incompleto, já com o código A05 no lugar do nome (slide 16). Os slides 14 e 16 podem ser mostrados em ritmo rápido.

Prática, 65 min. Apresentações (slide 17). Antes da primeira, cada aluno cria o formulário e escreve os três códigos que vai avaliar.

Cronômetro visível, com aviso aos oito minutos. Corte aos dez, com gentileza e sem exceção, porque a exceção da primeira apresentação vira o padrão de todas.

Duas perguntas por apresentação, no máximo. As demais ficam para o intervalo.

O bloco 4, o que ainda não funciona, é o que a turma tende a pular. Se alguém pular, pergunte. É a parte que mais diferencia as apresentações.

Quando uma demonstração falhar ao vivo, deixe a pessoa ler a mensagem de erro e dizer o que faria. O slide 17 traz essa orientação e a regra para colega ausente.

Circule olhando os formulários de pares. Justificativa em branco ou "ficou bom" precisa ser cobrada no momento, porque depois ninguém lembra do detalhe. Confira também que o campo `quem_apresentou_N` tem código, e não nome.

## Ciclo 15.3 — Apresentações, segunda rodada

Prática, 55 min. Mesmo formato (slide 19). Pela escala circular, as apresentações que cada aluno avalia podem estar nas duas rodadas. A frase anterior do deck, "quem apresentou na primeira rodada avalia nesta", foi retirada por contradizer a escala.

Entrega, 5 min. `entregas/roteiro-apresentacao.md` e `entregas/avaliacao-pares.md`, com a rodada de `pares` para conferência, commit e push (slide 20).

Quem já apresentou costuma dar a melhor devolutiva, porque reconhece o problema do outro.

A ideia que cada aluno leva de cada produto assistido é um campo do formulário e serve ao fechamento do ciclo 15.4. Colete duas ou três em voz alta antes do intervalo.

## Ciclo 15.4 — O portfólio e o que continua

Teoria, 15 min. O que continua depois da disciplina (slide 22): o que funciona sem modelo, o que depende de prática e o que muda com as ferramentas. O slide 23, Rodar os scripts sem o agente, mostra o uso fora da disciplina em quatro passos: terminal aberto na pasta do projeto pelo GitHub Desktop (Repository, Open in Command Prompt), `cd scripts` se o script estiver nessa pasta, `python atividade_modulo15.py c2` e leitura da saída. A caixa de resultado diferente cobre "python não é reconhecido" (Python não instalado, o uso volta a ser pelo agente) e "No such file or directory" (terminal em outra pasta). O slide 23 foi criado nesta revisão porque o texto não cabia no slide 22. A caixa datada foi reconferida em 14/11/2026: a página do OpenCode Zen lista 14 modelos gratuitos, quase todos por tempo limitado, com uso dos dados para aprimorar ou treinar o modelo em Big Pickle, Iceman Free, Inkling 2 Small Free, Flint 40B Free e MiMo-V2.6-Flash Free, retenção de 30 dias em Beam Free e Flint 40B Free, registro de uso nos três Nemotron para segurança e para aprimorar produtos da NVIDIA, com o pedido de não enviar dado pessoal ou confidencial (frase "do not submit personal or confidential data" confirmada na página), e hospedagem na China do LongCat 2.5 Free. A ficha da Câmara (camara.leg.br/propostas-legislativas/2487262) mostra o PL 2338/2023 apresentado em 17/03/2025, vindo do Senado, aguardando parecer do relator na Comissão Especial sobre Inteligência Artificial. A previsão de votação atribuída ao relator na versão anterior do slide (fonte secundária, Mobile Time) foi retirada. Reconfira as duas informações dois dias antes da aula.

Demonstração e prática, 25 min. A saída do comando `portfolio` e a estrutura de `saidas/portfolio.md` (slide 24). Cada aluno roda `portfolio`, confere a lista e escreve as três frases nos campos `o_que_ficou_pronto`, `o_que_eu_usaria_de_novo` e `o_que_eu_abandonaria` (slide 25, com resultado esperado e a saída para push recusado). A entrega C2 está no slide 26 e remete à rubrica do slide 6.

O índice gerado costuma surpreender a turma pelo tamanho. Vale projetar o de um voluntário: quinze encontros produzem cerca de trinta arquivos, e quase ninguém percebeu isso acontecendo.

A frase sobre o que abandonaria é a mais difícil e a mais honesta. Aceite respostas que critiquem a disciplina, e anote as recorrentes para o semestre seguinte.

O aviso final é prático: a máquina do laboratório pode ser restaurada, o repositório no GitHub não. Peça que cada aluno confira, ali mesmo, que o repositório remoto está atualizado.

O encerramento (slides 27 a 30) tem o balanço do semestre por nota, os próximos passos depois da disciplina, as dúvidas frequentes e o slide final. Nos próximos passos (slide 28), antes de tornar o repositório público, o aluno troca por código o nome de colega ou de usuário do teste e roda a varredura do módulo 12. O comando `portfolio` imprime o mesmo aviso.

## O que sai deste encontro

A C2 conferida. A apresentação feita, com demonstração ao vivo e o que não funciona dito. O formulário de avaliação por pares com justificativas escritas e apresentações identificadas por código. O caderno de prompts com os pedidos do produto. O portfólio do semestre com as três frases do aluno.

## Não conferido

- A presença do Python na máquina do aluno, para o uso dos scripts sem o agente pelo terminal, não foi testada, nem o menu Repository, Open in Command Prompt do GitHub Desktop nas máquinas do laboratório. O slide 23 e a dúvida 4 do slide 29 indicam a saída para "python não é reconhecido".

Conferido: o módulo 14 ensina validação de entrada (slide "Validação de entrada", OWASP, consulta em 14/11/2026), e a menção "retomada do módulo 14" no slide 14 deste deck está correta.
- A data de aprovação do PL 2338/2023 no Senado não foi conferida em fonte primária nesta revisão e saiu do slide.

## Depois do semestre

Guarde os formulários de avaliação por pares. Eles são a melhor fonte sobre o que a turma entendeu, melhor que a nota das entregas, porque mostram o que um aluno consegue reconhecer no trabalho do outro.

Anote as respostas recorrentes de "o que eu abandonaria". São o insumo direto para o ajuste dos módulos no semestre seguinte.

Registre também quantos alunos ficaram sem cota do modelo em cada encontro. Se o número crescer, os ciclos de prática precisam de mais atividade sem modelo, e os scripts já foram escritos para isso.
