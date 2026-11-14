# Roteiro do módulo 14

Produto digital e gestão ágil. Encontro 15, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Encontro sem entrega avaliada isolada. Tudo que sai daqui entra na C2 do encontro 16, que vale 60% da nota 3. É também a última janela para regularizar pendências da C1.

Forma do produto, decidida em 14 nov. 2026: uma página HTML única, que abre com duplo clique, sem servidor e sem biblioteca externa, gravada em `entregas/produto.html` e escrita pelo agente a partir das histórias de usuário. A forma é dita no slide 3 e repetida em cada prática de construção (slides 24, 25 e 30).

## Antes da aula

Material do professor: `slides/modulo14-produto-digital-e-agil.html`, este roteiro e `scripts/atividade_modulo14.py`.

Publicado na turma virtual, com uma semana de antecedência: o script e o pedido de que cada aluno escolha o processo que vai virar produto e anote quem é o usuário, pelo cargo, o que ele faz hoje, quantas vezes por semana e quanto tempo leva. Quem chega sem isso passa o primeiro ciclo escolhendo tema. Quem não trabalha nem estagia pode adotar o exemplo da Divisão de Compras do deck como caso de reserva (slide 8).

Monte um backlog de exemplo antes da aula e rode `priorizar`. As seis histórias do slide 16 servem: H1 8/3, H2 6/1, H3 5/2, H4 4/1, H5 3/5 e H6 4/6, com H1, H2, H3 e H5 marcadas para a versão 1. A saída mostra "Destas, H5 fica fora", que abre a conversa sobre dependência entre histórias. Uma cópia com a H5 escrita como "quero um botão de exportar para PDF" mostra a recusa de história que descreve solução (slide 14).

Rode `partida` numa pasta de teste e abra `entregas/produto.html` com duplo clique na máquina do laboratório. Confira que a página abre sem servidor e que as seis linhas da tabela do slide 20 dão as mensagens previstas. Faça também a demonstração do slide 22 com o modelo gratuito do dia e guarde a página resultante, para o caso de o modelo falhar em sala.

Prepare a lista de pendências da C1, aluno por aluno, tirada da rodada `c1` do encontro anterior. Entregue no início do encontro, por escrito.

O ciclo 14.3 é o mais longo de construção do semestre e depende da cota do modelo. Avise na semana anterior que a versão 2 é feita em aula, no ciclo 14.4, e que não há construção em casa.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura, visão geral e forma do produto | 10 min | 1 a 3 |
| Ciclo 14.1 | 40 min | 4 a 9 |
| Ciclo 14.2 | 50 min | 10 a 18 |
| Intervalo | 15 min | |
| Ciclo 14.3 | 55 min | 19 a 26 |
| Intervalo | 10 min | |
| Ciclo 14.4 | 60 min | 27 a 31 |
| Fechamento | 10 min | 32 a 35 |

## Abertura

Visão geral com os termos de base (slide 2): gestão ágil, backlog, história de usuário, critério de aceite, commit e versão 1. A forma do produto (slide 3): página HTML única em `entregas/produto.html`, escrita pelo agente, aberta com duplo clique, sem servidor. O que a página não faz (não guarda dados depois que a aba é fechada) e o comando `partida` para quem travar.

## Ciclo 14.1 — De processo a produto

Teoria, 12 min. Processo automatizado e produto digital, com a definição de MVP de Ries (2011) e a tabela que compara os dois (slide 5). As quatro perguntas da ficha ligadas aos campos do script, com o exemplo ilustrativo da Divisão de Compras: 45 minutos por processo, 12 processos por mês, 540 minutos ou 9 horas mensais (slide 6).

Demonstração, 10 min. A ficha na projeção, com o corte de escopo feito ao vivo sobre um caso da turma, e a saída do comando conferir sobre uma ficha com erros (slide 7). A saída tem 12 itens: os nove da ficha e os três arquivos dos ciclos seguintes (backlog priorizado, `produto.html` e registro do teste). A recusa vem do comando conferir. O comando produto só cria a ficha em branco.

Prática, 13 min (slide 8). Cada aluno preenche a ficha e roda o conferir. Resultado esperado no slide: nenhum item começa por `ficha-produto.md`.

Entrega, 5 min (slide 9). `entregas/ficha-produto.md`.

O usuário descrito como "os gestores" é o erro previsível e o script recusa. A comparação é com a lista exata de grupos do script, de modo que "os gestores da secretaria" passa pelo conferir e precisa ser apontado à mão. Insista no cargo: é ele que define o que precisa estar escrito no produto e qual papel o colega vai fazer no teste do ciclo 14.4.

A medida do caminho atual é o que permite dizer depois se o produto ajudou. Quem não mediu no encontro 10 mede por estimativa agora, e registra que é estimativa.

O corte de escopo é a decisão de produto do encontro. Uma tarefa completa vale mais que três pela metade, e o que sai não é apagado, vai para o backlog.

## Ciclo 14.2 — Backlog e critério de aceite

Teoria, 22 min. Gestão ágil e Scrum (slide 11): o Manifesto Ágil de 2001, a definição de Scrum do Guia do Scrum de novembro de 2020, que continua a edição publicada em scrumguides.org, e o caso Sentinel do FBI relatado por Sutherland (2014, cap. 1), com os números do relatório do Inspetor-Geral de out. 2010. O ciclo do Scrum (slide 12), com sprint, incremento, definição de pronto, impedimento e Daily Scrum definidos no slide. O Scrum neste módulo (slide 13): cada evento ligado a uma etapa do encontro e a um arquivo, os três papéis acumulados pelo aluno e a caixa sobre agentes de IA no desenvolvimento (DORA 2025 e METR 2025 e 2026). Depois, a história de usuário e o critério de aceite (slide 14), com a origem do formato na Connextra e a difusão por Cohn (2004), e exemplos que o comando priorizar recusa: falta de "para", solução no lugar da ação ("quero um botão de exportar para PDF"), critério vago e critério curto. As âncoras de valor e esforço de 1 a 8 (slide 15). Por fim, o exemplo numérico de valor sobre esforço com a saída real do script sobre o backlog de seis histórias, com a dependência H2 e H1 e a H5 marcada fora do limite (slide 16).

Prática, 23 min (slide 17). Cada aluno escreve de cinco a dez histórias com critério de aceite, dá as notas pelas âncoras e roda `priorizar`. O critério inclui a recusa esperada para o dado errado.

Entrega, 5 min (slide 18). `entregas/backlog.csv` e `saidas/backlog-priorizado.md`.

A parte "para [resultado]" é a que a turma esquece e a única que justifica construir. O script recusa a história sem ela e a que traz um elemento de tela logo depois de "quero" (botão, tela, menu, aba, página, sistema, painel, campo, formulário, link). A lista é exata: "quero que a página tenha um botão" passa e precisa ser apontado à mão.

"Funcionar bem" como critério de aceite aparece em quase todo backlog na primeira rodada. Pergunte quem verificaria isso, e como, sem o aluno por perto.

A ordem por valor sobre esforço é sugestão, e não decisão. Quando a marcação do aluno discorda da ordem calculada, a resposta certa costuma ser dependência entre histórias, e isso se escreve no backlog em vez de se mudar o número. Esforço 8 indica história a dividir.

## Ciclo 14.3 — A primeira versão, construída

Teoria, 10 min. Validação de entrada (slide 20), com a definição sintática e semântica da OWASP trazida do módulo 15 e o exemplo do pedido de papel com saldo de 40 resmas, o mesmo do comando `partida` e do slide 11 do módulo 15. Como conduzir o agente numa construção (slide 21): uma história por vez, pedido com a história, o critério e o arquivo, aba Changes do GitHub Desktop para ver o que mudou, teste com dado errado, critério conferido na página aberta, commit ao fim de cada história, instrução de uso no topo da página, dado pessoal fora do que o agente lê e cálculo conferido à mão.

Demonstração, 12 min. Uma história completa (slides 22 e 23): o pedido ao agente para a H1 do backlog de exemplo, a página aberta pelo GitHub Desktop (Repository, Show in Explorer) com duplo clique, os quatro casos digitados, o caso de valor zero que falhou, o pedido de correção só desse caso e o commit. Faça ao vivo com o modelo do dia. Se o agente acertar o valor zero na primeira tentativa, mostre a correção com outro caso que falhe ou use a página guardada antes da aula.

Prática, 30 min. Primeira história na página (slide 24) e, em seguida, dado errado, commit e próxima história (slide 25). Os dois slides trazem o texto do pedido, o resultado esperado e o que fazer quando o resultado for outro.

Entrega, 3 min (slide 26). `entregas/produto.html` com pelo menos uma história que atende ao critério e os commits.

Circule pela sala olhando os pedidos que os alunos escrevem ao agente. O que produz resultado ruim quase sempre omitiu o critério de aceite ou pediu várias histórias de uma vez.

O teste com dado errado é o que separa exercício de produto. Peça a cada aluno que faça na página os quatro casos (campo vazio, texto no lugar de número, número com vírgula, valor fora da regra) antes de dizer que a história está pronta.

O commit por história é a regra. Quem faz um commit só no fim perde a capacidade de voltar, e é o que mais atrapalha no encontro 16. O slide 25 mostra o Discard changes para desfazer um pedido que estragou o que funcionava.

Quem travar roda `partida` e constrói a primeira história sobre a página de pedido de material. O conferir recusa a página de partida sem alteração. Aluno sem cota escolhe outro modelo gratuito na lista do opencode. Sem nenhum modelo, segue com o teste da página e registra no backlog o que faltou (slide 34, dúvida 4).

## Ciclo 14.4 — Teste com usuário e iteração

Teoria, 10 min. O teste de uso com poucos usuários (slide 28). Nielsen (2000) estima que cada usuário de teste encontra em média 31% dos problemas e que cinco usuários encontram cerca de 85%. Tarefa concreta, pensar em voz alta e observação em silêncio. O colega como substituto do usuário: ele encontra problemas de uso da página e não testa a adequação à rotina, aos termos do setor nem aos casos reais. Bloqueio antes de incômodo.

Prática de teste, 22 min (slide 29). Em duplas, cada um usa o produto do outro, no papel do cargo da ficha. Depois, individual, o registro com `quem_testou` no formato "colega da turma, no papel de [cargo]" e a atualização do backlog.

Prática da versão 2, 25 min (slide 30). Os bloqueios do teste primeiro, uma correção por vez, teste com dado errado de novo, commit com resumo iniciado por "Versão 2", retrospectiva e `conferir`.

Entrega, 3 min (slide 31). `entregas/registro-teste.md`, `entregas/backlog.csv` atualizado e `entregas/produto.html` na versão 2.

A instrução mais difícil de cumprir é ficar calado. Circule e interrompa quem estiver explicando o próprio produto ao colega. Cada ajuda apaga um problema que vai reaparecer com o próximo usuário.

Teste em que nada travou significa quase sempre tarefa fácil demais ou ajuda dada. O script recusa registro sem achado, e a saída certa é refazer com tarefa mais difícil, não escrever um achado inventado.

A retrospectiva fecha o ciclo. A pergunta é o que atrapalhou a construção, e a resposta mais comum, começar pela formatação antes de a validação estar pronta, é útil para a turma inteira ouvir.

## O que sai deste encontro

A ficha do produto com usuário pelo cargo e caminho atual medido. O backlog com histórias no formato e critérios de aceite verificáveis, priorizado. A página `entregas/produto.html` na versão 2, com commits por história. O registro do teste com achados classificados.

## Avisos no fechamento

O encontro 16 é o projeto integrador e fecha a C2, 60% da nota 3. A versão 2 foi feita em aula, e o aluno não precisa usar cota do modelo em casa. O que não ficou pronto fica declarado no backlog e no bloco 4. A apresentação segue os quatro blocos do roteiro gerado pelo comando `apresentacao` do `atividade_modulo15.py`: o problema e quem o tem, o que você construiu, a demonstração ao vivo e o que ainda não funciona (slides 32 e 33). A demonstração inclui o caso com dado errado.

Diga que a demonstração do produto recusando entrada inválida vale mais na avaliação que a tela bonita, porque é isso que se avalia.

Quem ainda tem pendência da C1 entrega até o encontro 16. Depois disso a nota 3 fecha com o que estiver na pasta.

O comando `c2` do módulo 15 procura `produto.html`, `ficha-produto.md`, `backlog.csv`, `saidas/backlog-priorizado.md` e `registro-teste.md` (lista ENTREGAS de `atividade_modulo15.py`, alteração ainda sem commit). O funcionamento da página é avaliado na demonstração ao vivo. Se a inclusão de `produto.html` no `c2` for descartada, o slide 32 e este parágrafo voltam a dizer que o `c2` procura só os quatro arquivos .md e .csv.

## Informações não conferidas

- Ano exato de 2001 para o formato da história de usuário na Connextra: a fonte consultada (blog de Mike Cohn) diz "início dos anos 2000". O deck usa essa forma.
- Caso Sentinel (slide 11): US$ 405 milhões gastos de US$ 451 milhões em agosto de 2010, com duas de quatro fases entregues, conferido no resumo do DOJ OIG Report 11-01 em oig.justice.gov. Orçamento inicial de US$ 425 milhões e conclusão prevista para dezembro de 2009 conferidos em relatórios anteriores do OIG sobre o Sentinel (oig.justice.gov), consulta em 14/11/2026. O texto integral do PDF do Report 11-01 não foi lido. O relato de Sutherland (2014, cap. 1) não foi conferido no livro.
- Caminho para trocar de modelo no opencode desktop (slides 24 e 30 e dúvida 4 do slide 34): "clique no nome do modelo, abaixo da caixa de pedido" repete o caminho do slide de conexão do módulo 2. A documentação em opencode.ai/docs/models (consulta em 14/11/2026) descreve só o comando /models e não descreve o aplicativo desktop. Conferir na versão instalada no laboratório antes da aula e anotar a data.
- Nomes de menu do GitHub Desktop (Repository, Show in Explorer, Changes, Discard changes, Commit to main) conferidos de memória, a testar na versão instalada no laboratório.
