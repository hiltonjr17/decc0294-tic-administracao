# Roteiro do módulo 8

Visualização de dados e painéis. Encontro 9, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este encontro fecha a entrega B1, que vale 60% da nota 2.

## Antes da aula

Material do professor: `slides/modulo8-visualizacao-e-paineis.html`, este roteiro e `scripts/atividade_modulo8.py`.

Publicado na turma virtual: a versão nova do script (revisão de 15 nov. 2026) e o lembrete de trazer um gráfico ruim e os resultados das consultas do encontro 8.

Gere um painel de teste antes da aula, com a base de reserva, uma vez com série por categoria e outra com série mensal, e projete-o no ciclo 8.3. Assim a turma vê o resultado esperado antes de preencher o formulário.

Separe dois ou três gráficos ruins de fontes públicas, caso a turma traga poucos. Relatório de gestão de órgão público e apresentação de resultado de empresa listada rendem exemplos, e o fato de serem públicos evita constrangimento com material de estágio.

Confira quem ficou pendente nos encontros 7 e 8. A B1 reúne os três encontros, e o script aponta item por item no último ciclo.

Quem usou a versão anterior do script tem formulário com nove colunas. O comando `atualizar` acrescenta `formula`, `polaridade`, `destinatario` e `decisao` sem apagar o que foi preenchido e guarda uma cópia em `entregas/modulo8-indicadores-anterior.csv`.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura, visão geral e termos | 10 min | 1 a 3 |
| Ciclo 8.1 | 45 min | 4 a 10 |
| Ciclo 8.2 | 50 min | 11 a 19 |
| Intervalo | 15 min | |
| Ciclo 8.3 | 55 min | 20 a 26 |
| Intervalo | 10 min | |
| Ciclo 8.4 | 50 min | 27 a 31 |
| Fechamento | 15 min | 32 a 35 |

O slide 3 retoma em uma linha os termos de módulos anteriores que o deck usa (agente, script, CSV, consulta SQL, série, eixo, commit e Push origin, B1) e antecipa painel (dashboard), definido por completo no slide 21, e HTML, formato do arquivo entregas/painel.html.

## Ciclo 8.1. Gráfico com pergunta e conclusão

Teoria, 18 min. O gráfico responde a uma pergunta de gestão, com o mesmo conjunto de números antes e depois do título-conclusão (slide 5). Os cinco defeitos que distorcem a leitura e a proporção dados-tinta de Tufte (slide 6). A pizza com no máximo três fatias aparece como regra prática da disciplina, e não como resultado de pesquisa. Exemplo numérico do eixo cortado, com o fator de distorção (slide 7).

Demonstração, 10 min. A turma escolhe o pior gráfico trazido e ele é refeito na projeção, começando pela pergunta e pelo título-conclusão (slide 8).

Prática, 12 min. Cada aluno reconstrói o próprio (slide 9). O slide traz o pedido ao agente, o resultado esperado e o que fazer quando o agente não lê a imagem: digitar os valores em `dados/grafico-original.csv`.

Entrega, 5 min. `entregas/modulo8-ciclo1-reconstrucao.md` (slide 10).

O teste do título escrito antes do gráfico é o conteúdo central do ciclo. Aplique na demonstração em voz alta: se ninguém consegue escrever a frase afirmativa, o diagnóstico é que falta análise, e não desenho.

O corte do eixo em gráfico de barras é o defeito que mais distorce. O slide 7 mostra a mesma série com e sem base no zero.

## Ciclo 8.2. Forma, escala e cor

Teoria, 30 min. Definição de indicador (MP, 2012) e os atributos fórmula de cálculo, referência, meta e polaridade (MP, 2018), com o exemplo do custo por atendimento (slide 12). As cinco comparações e a forma de cada uma, com o aviso de que o comando `painel` desenha barras e linha (slide 13). Critério de tabela contra gráfico (Few, 2012) e o risco de reidentificação em célula pequena, com o exemplo de dado de saúde (slide 14). A ordem de Cleveland e McGill, 1984, com a distinção entre o que os dois experimentos mediram (posição, comprimento e ângulo) e o que é proposta teórica (área, volume e cor) (slide 15). As três decisões de escala, com a definição de série sazonal (slide 16). Os três usos da cor, a definição de razão de contraste (de 1:1 a 21:1), o contraste mínimo de 3:1 para elemento gráfico e de 4,5:1 para texto da WCAG 2.2 e a cor de texto do painel (slide 17).

Prática, 15 min. Cada aluno classifica os resultados das consultas do encontro 8, escolhe a forma e declara fórmula, referência, polaridade, escala e título-conclusão de cada indicador (slide 18).

Entrega, 5 min. `entregas/modulo8-ciclo2-formas.md` (slide 19).

O par valor absoluto contra taxa é o que mais muda conclusão em gestão pública. A unidade maior tem mais atendimentos, e por atendimento pode ser a mais barata. Peça um exemplo da turma.

A polaridade é o ponto novo do ciclo. Pergunte à turma, para cada indicador projetado, se aumentar é bom. Tempo de espera e custo por atendimento costumam aparecer como "quanto menor, melhor", e a cor do painel depende dessa resposta.

Indicador sem título-conclusão, fórmula ou polaridade não entra no painel. As regras são do script.

## Ciclo 8.3. Do dado ao painel que abre no navegador

Teoria, 18 min. Os elementos de um painel, apontados sobre a imagem do painel que o script gera, com a definição de Few, 2006 (slide 21). Comparação entre o HTML do script, o Power BI e o Data Studio em três linhas (custo, local do dado e controle de acesso), com a segurança em nível de linha definida no slide e fontes consultadas em 15 nov. 2026 (slide 22).

Demonstração, 7 min. As treze colunas do formulário e as regras de recusa (slide 23). O painel de teste que você gerou antes da aula, aberto na projeção, com a regra da forma do gráfico, a opção `destaque=` e a cor da variação pela polaridade (slide 24).

Prática, 25 min. Cada aluno preenche os indicadores, exporta a série e gera o painel (slide 25). O slide traz os dois modelos de consulta, por categoria e por mês, com `strftime('%Y-%m', data)`.

Entrega, 5 min. `entregas/painel.html` e `entregas/modulo8-indicadores.csv` (slide 26).

A fonte de cada número no próprio painel é o elemento que mais falta nos painéis de mercado. A tabela "De onde vem cada número" traz fórmula, período, fonte e consulta, e o script recusa indicador sem fonte.

Quem gerar o painel e vir número diferente da consulta quase sempre tem filtro de período diferente entre o SQL e o que escreveu no formulário. Essa é a primeira coisa a checar.

Série mensal que sai em barras indica que a primeira coluna não está no formato `2026-01`. O script do módulo 7 converte datas para AAAA-MM-DD ao montar o banco, e o `strftime` resolve.

## Ciclo 8.4. O painel do projeto e a entrega B1

Teoria, 10 min. De quem é o painel: três destinatários de uma secretaria fictícia, a decisão de cada um e a regra de corte (slide 28).

Demonstração, 5 min. Os dois comandos de conferência, com saída ilustrativa do `b1` (slide 29).

Prática, 30 min. Destinatário e decisão na primeira linha do formulário, painel gerado de novo, `conferir`, `b1`, nome e matrícula no relatório, commit "entrega B1", Push origin e `b1` de novo (slide 30).

Entrega, 5 min. Repositório publicado com a mensagem "entrega B1" (slide 31).

O destinatário e a decisão passaram para o formulário. O painel é regravado a cada geração, e nada se edita no `painel.html`.

O `b1` confere treze itens: onze arquivos dos encontros 7, 8 e 9, o destinatário e a decisão no formulário, e a publicação. Publicado quer dizer que o último commit da pasta está no GitHub (referência `origin` igual à local) e que nenhum arquivo da entrega mudou depois desse commit. O relatório `entregas/B1-relatorio.md` entra nessa lista: o `b1` grava o relatório antes de conferir a publicação, e o relatório gravado ou assinado depois do último commit deixa a publicação pendente até o novo commit e Push. O relatório não traz a publicação e preserva a linha de nome e matrícula, por isso não muda quando o `b1` roda de novo depois do Push. A falha de publicação tem quatro mensagens, todas no slide 30: sem repositório, "Publique o repositorio" (Publish repository), "nenhum envio foi registrado" ou "nao esta no GitHub" (Push origin) e "Arquivo alterado depois do ultimo commit" (commit e Push origin).

A regra de que o indicador sobre o que o destinatário não pode mudar sai do painel é a que mais reduz painel inchado. Aplique a dois painéis da turma em voz alta.

Reserve os últimos vinte minutos para o comando `b1`. Quem rodar cedo tem tempo de corrigir.

## O que sai deste encontro

Um gráfico reconstruído, a forma justificada de cada indicador, com fórmula e polaridade, e o painel do projeto com destinatário e decisão declarados no formulário. Somados aos encontros 7 e 8, fecham a B1.

## Avisos no fechamento

Retomar o mapa de tarefas do módulo 1: a tarefa em primeiro lugar na ordem de prioridade é o objeto do encontro 10 (slide 33).

Trazer um documento que se refaz todo mês, com dois exemplares de meses diferentes se possível, e a anotação de quanto tempo ele leva hoje.

Deixar o painel funcionando: regerar o painel com dado novo é um exemplo de fluxo repetível para o encontro 10 (slide 33).

## Fontes conferidas em 15 nov. 2026

- Microsoft, página de preços do Power BI: Pro a US$ 14 por usuário por mês no plano anual, Desktop gratuito.
- Microsoft Learn, "Power BI service features by license type" (atualizada em 24 ago. 2026): publicar e consumir conteúdo de outro usuário exige Pro, salvo conteúdo em capacidade Premium ou Fabric F64 ou maior. O slide simplifica para a licença Pro.
- Microsoft Learn, "Row-level security (RLS) with Power BI".
- Google Cloud, documentação do Data Studio ("Welcome" e "Upload CSV files"): ferramenta sem custo, versão Pro paga, nome Data Studio desde abril de 2026, CSV enviado guardado no Cloud Storage.
- W3C, WCAG 2.2, Understanding 1.4.3 e 1.4.11.
- Ministério do Planejamento, Orçamento e Gestão. Indicadores: orientações básicas aplicadas à gestão pública. Brasília, 2012 (definição de indicador).
- Ministério do Planejamento, Desenvolvimento e Gestão. Guia metodológico para indicadores, PPA 2016-2019. Brasília, 2018, p. 29 (polaridade e fórmula de cálculo).

## Não conferido

- Few (2012), "Show me the numbers", 2. ed.: a edição e a editora foram confirmadas, e o critério de tabela contra gráfico do slide 14 foi conferido só por resumos secundários do livro.
- A definição de meta do slide 12 é da disciplina e não tem fonte citada.
- O limite de cinco casos para célula pequena é regra do script, sem norma de referência.
