# Roteiro do módulo 6

Análise exploratória de dados. Encontro 7, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Começa a nota 2.

## Antes da aula

Material do professor: `slides/modulo6-analise-exploratoria.html`, este roteiro e `scripts/atividade_modulo6.py`.

Publicado na turma virtual: o script e o lembrete de que a base tratada precisa estar em `dados/` e as três perguntas de gestão escritas.

Rode o script sobre a base de reserva antes da aula, para conhecer a saída que a turma vai ver. O script é determinístico e não usa modelo, então o resultado do seu teste é exatamente o que aparecerá na tela dos alunos com o mesmo arquivo.

Prepare uma base de reserva com defeitos plantados: uma coluna com valores em branco, uma coluna de valor com ponto de milhar (12.480), dois valores mil vezes maiores por unidade trocada, um valor negativo impossível e uma linha duplicada. É o material que faz o ciclo 6.3 funcionar mesmo para quem trouxe uma base limpa demais.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 6.1 | 45 min | 3 a 9 |
| Ciclo 6.2 | 60 min | 10 a 17 |
| Intervalo | 15 min | |
| Ciclo 6.3 | 50 min | 18 a 24 |
| Intervalo | 10 min | |
| Ciclo 6.4 | 45 min | 25 a 30 |
| Fechamento | 15 min | 31 a 34 |

Revisão de 15 nov. 2026: o deck passou de 31 para 34 slides. Entraram o slide 5 (comparações múltiplas, com nível de significância, falso positivo e comparações independentes definidos), o 13 (quartis e amplitude interquartil sobre dez valores, pelo método do QUARTIL.INC do Excel) e o 14 (histograma e diagrama de caixa dos mesmos dez valores). O log do ciclo 6.4 passou de cinco para três números.

## Ciclo 6.1. Da pergunta de gestão à pergunta de dados

Teoria, 18 min. Análise exploratória e análise confirmatória (Tukey, 1977), com a definição de hipótese (slide 4). O problema das comparações múltiplas no slide 5: o slide define nível de significância, falso positivo e comparações independentes antes da conta. Em 20 comparações independentes sem efeito real, a 5%, a chance de ao menos um falso positivo é 1 − 0,95²⁰ = 64%. A pergunta de gestão e a pergunta de dados, com a definição da medida em numerador, denominador, período e recorte (slide 6).

Demonstração, 7 min. A tradução de uma pergunta, com a instrução que proíbe calcular antes de listar o que falta.

Prática, 15 min. Três perguntas de gestão, traduzidas pelo agente uma a uma em saidas/traducao-pergunta-1.md a -3.md (slide 8, com resultado esperado e o que fazer quando o agente entrega um número).

Entrega, 5 min. `entregas/modulo6-ciclo1-perguntas.md`.

O critério que separa pergunta boa de pergunta ruim é se alguém decide algo com a resposta. Aplique em voz alta a duas ou três perguntas da turma: a maioria vira pedido de estatística descritiva sem destinatário, e a correção em público ensina mais que o slide.

O "não calcule nada ainda" da instrução é deliberado. Sem ele o modelo entrega um número e o aluno aceita a definição implícita que ele usou, que é justamente a decisão que deveria ser do administrador.

## Ciclo 6.2. Perfil da base

Teoria, 25 min. Os quatro passos antes de qualquer gráfico (slide 11). Média, mediana e a distância entre elas (slide 12): a mediana é resistente porque trocar o maior valor por outro maior não a altera. Quartis e amplitude interquartil com a conta sobre dez prazos (slide 13): Q1 = 18,5, mediana 22, Q3 = 27,25, AIQ = 8,75 e cercas 5,4 e 40,4. O mesmo conjunto em histograma e diagrama de caixa, com a leitura (slide 14). Se alguém conferir no Excel, =QUARTIL.INC dá os mesmos valores. Outros programas usam outra regra de posição e podem divergir na segunda casa.

Demonstração, 8 min. O script perfilando a base de reserva na projeção.

Prática, 22 min. Cada aluno perfila a própria base, lê o perfil inteiro, inclusive os histogramas em texto, e pede a interpretação ao agente (slide 16).

Entrega, 5 min. `entregas/modulo6-ciclo2-perfil.md`.

Vale mostrar na projeção a linha da coluna de custo da base de reserva, em que a média fica muito acima da mediana por causa dos dois valores de unidade trocada, e o histograma dessa coluna no perfil, com os dois valores contados fora das cercas. Antecipa o ciclo seguinte.

O script não usa o modelo. Diga isso: cálculo determinístico dá sempre o mesmo resultado, e por isso o perfil é auditável de um jeito que a resposta de um modelo não é. O modelo entra depois, para interpretar.

Quando o script não abre o arquivo, o defeito costuma estar no arquivo. A mensagem informa o que foi tentado. Corrigir separador ou codificação é parte da atividade.

Leitura de números pelo script (corrigida em 15 nov. 2026): vírgula decimal, ponto de milhar e o prefixo R$ são aceitos. O ponto de milhar é decidido por coluna, como no script do módulo 11: só em CSV separado por ponto e vírgula, e só se a coluna tiver vírgula decimal em algum valor ou se todo valor com ponto tiver o formato de milhar. O script imprime as colunas lidas assim. Uma coluna de valor vira texto quando mais de 10% dos valores têm letras ou anotações.

## Ciclo 6.3. Valores ausentes e atípicos

Teoria, 22 min. Os três mecanismos de ausência do formulário e a terminologia de Rubin (1976) e Little e Rubin (1987), slide 19: ausente ao acaso corresponde a MCAR (missing completely at random), por regra a ausência estrutural, e com viés reúne MAR (missing at random, a falta depende de outra coluna observada) e MNAR (missing not at random, depende do próprio valor). Vale dizer em voz alta que MAR, apesar do nome, não é ausência ao acaso no sentido comum. O exemplo numérico do slide 20, um caso de MNAR, em que a ausência com viés inverte a conclusão e o preenchimento pela média não corrige. A árvore de classificação do valor atípico e as cercas de Tukey, que são o critério do script (slide 21, com remissão à conta do slide 13).

Demonstração, 6 min. O script apontando os casos e criando o formulário de decisão.

Prática, 17 min. Cada aluno decide sobre cada caso, com a razão escrita (slide 23). Desde 15 nov. 2026 o script lista por coluna só os três atípicos mais distantes das cercas e reúne os demais numa linha "demais atipicos", decidida em conjunto. Os rótulos são aceitos com ou sem acento.

Entrega, 5 min. `entregas/modulo6-tratamento.csv`.

O ausente com viés é o conteúdo mais importante do ciclo e o menos intuitivo. Use o exemplo do slide 20: a unidade Norte parece custar 100 e o Sul 150, mas os meses caros do Norte não foram lançados e o custo real do Norte é 200. Preencher os vazios pela média leva o Norte a 116,7 e mantém a conclusão invertida.

O script recusa duas coisas: decisão sem razão escrita, e exclusão de um valor classificado como realidade. A segunda regra existe porque excluir o que atrapalha a média é o atalho mais comum e o mais grave. A alternativa legítima é separar em análise própria e dizer que se fez isso.

## Ciclo 6.4. Conferência dos números calculados pelo agente

Teoria, 20 min. Os dois caminhos do número calculado pelo agente (escrito na resposta ou produzido por script) e o tipo de erro de cada um, com filtro, junção e conversão de tipo definidos e o procedimento do módulo 5 descrito no próprio slide (slide 26). As quatro conferências e o campo correspondente no log (slide 27). A quarta conferência passou a ser a medida refeita à mão numa amostra (um mês ou dez registros), campo recalculo_amostra, porque uma medida agregada não se confere numa linha só. O script aceita o nome antigo, linha_recalculada, nos logs já entregues.

Demonstração, 6 min. A instrução que pede o script junto do número, com as linhas descartadas e o total antes do filtro.

Prática, 14 min. Três números calculados e conferidos, registrados no log (slide 29).

Entrega, 5 min. `entregas/modulo6-log-verificacao.csv`.

O ponto que precisa ficar: quando o agente escreve e executa um script, o risco muda de lugar. Sai do cálculo, que passa a ser confiável, e vai para o filtro aplicado. Por isso a instrução pede as linhas descartadas e o total antes do filtro.

O script marca com aviso, e não com erro, o número cuja medida não foi refeita numa amostra.

Três números que passam nas quatro conferências na primeira tentativa é improvável. Se acontecer na turma inteira, o mais provável é que as conferências não tenham sido feitas.

## O que sai deste encontro

Três perguntas de gestão traduzidas em perguntas de dados, o perfil completo da base, o tratamento de ausentes e atípicos com razão registrada, e três números com log de verificação. É o começo da nota 2.

## Avisos no fechamento

Deixar a base tratada em `dados/`, com o arquivo original preservado ao lado. No encontro 8 as duas bases viram tabelas ligadas por uma chave.

Escrever cinco perguntas que só podem ser respondidas cruzando as duas bases. São elas que viram consultas.

A entrega B1, no encontro 9, reúne o trabalho dos encontros 7, 8 e 9. Quem atrasar aqui chega sem base para consultar.
