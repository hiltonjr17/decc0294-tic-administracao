# Roteiro do módulo 5

Dados na Administração. Encontro 6, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este encontro fecha a nota 1 com a entrega A2.

## Antes da aula

Material do professor: `slides/modulo5-dados-na-administracao.html`, este roteiro e `scripts/atividade_modulo5.py`.

Publicado na turma virtual: o script e o lembrete de trazer uma planilha ou base da organização escolhida, com pelo menos vinte linhas e sem dado pessoal identificável.

Prepare uma base de reserva para quem não trouxer, e um arquivo de reserva das bases públicas (`dados/api-municipios.csv`, `dados/api-serie.csv` e `dados/api-contratacoes.csv`) para o caso de a rede bloquear as APIs. O diagnóstico do encontro 5 já diz quais fontes o laboratório alcança: use aquele resultado.

Confira a situação de cada aluno nas entregas dos módulos 1, 3 e 4. Quem chegar hoje com pendência acumulada não fecha a A2, e o script vai apontar item por item. É melhor avisar antes do encontro do que descobrir no último ciclo.

Reconfira, dois dias antes, a seção Privacy de opencode.ai/docs/zen. Os slides 26 e 27 trazem a lista de modelos gratuitos consultada em 15/11/2026.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura, visão geral e palavras do módulo | 10 min | 1 a 3 |
| Ciclo 5.1 | 45 min | 4 a 10 |
| Ciclo 5.2 | 50 min | 11 a 20 |
| Intervalo | 15 min | |
| Ciclo 5.3 | 50 min | 21 a 29 |
| Intervalo | 10 min | |
| Ciclo 5.4 | 55 min | 30 a 34 |
| Fechamento | 15 min | 35 a 38 |

O ciclo 5.2 ganhou quatro slides em 15 nov. 2026 (14, 16, 17 e 18 são novos, e o 15 é a demonstração antiga). Se o tempo apertar, os slides 17 e 18 podem ser mostrados durante a prática, que é quando o aluno converte a própria planilha.

## Ciclo 5.1. De onde nasce o dado da organização

Teoria, 18 min. O slide 3 define os termos usados em todo o módulo (base, fonte, CSV, agente, script, API, pastas, repositório, commit e Push origin, e a regra do NÃO INFORMADO). Repositório, commit e Push origin ficam definidos aí porque aparecem no slide 28 e na publicação da A2 (slide 33). As três origens e o erro típico de cada uma. As três formas do dado, com JSON, XML, log e achatamento definidos no slide 6. O quadro do slide 7: em que tarefas o agente acerta e em que tarefas erra no trabalho com dados, o controle adotado para cada uma, e a definição de esquema e de saída estruturada.

Demonstração, 7 min. Montar uma linha de inventário na projeção, com a regra do NÃO INFORMADO.

Prática, 15 min. Três fontes da organização de cada aluno (slide 9). O aluno escreve primeiro um rascunho com o que sabe e depois pede o CSV ao agente, que grava `entregas/modulo5-ciclo1-inventario.csv` com nove colunas, incluindo `a_quem_perguntar`.

Entrega, 5 min. `entregas/modulo5-ciclo1-inventario.csv`.

O conteúdo do ciclo é a regra do NÃO INFORMADO. Metade da turma vai deixar o agente preencher o que não sabe, e o inventário resultante parece completo e descreve uma organização genérica. Insista que cada lacuna vira uma pergunta a levar à organização. O slide 9 mostra o que fazer quando o agente preenche campo deixado em branco.

## Ciclo 5.2. Onde os dados ficam e como são extraídos

Teoria, 18 min. As quatro etapas do caminho do dado até a decisão e a linhagem de dados. As três formas de extrair o dado do sistema, com layout, credencial e MCP definidos no slide 13. O procedimento de conferência de script do slide 14: explicação em linguagem comum, contagens de entrada e saída, dois números refeitos à mão. Os módulos 6, 7 e 8 remetem a esse slide.

Demonstração, 8 min. Baixar a lista de municípios e cruzar com uma base da turma (slide 15). Os não encontrados são o ponto da demonstração. Aplique os três passos do slide 14 ao script gerado, na projeção. O slide 16 mostra a chave e o ajuste de cada base pública (código IBGE ou nome normalizado, data reduzida ao mês, CNPJ só com caracteres, com a previsão de CNPJ com letras da IN RFB 2.229/2024). A nota sob a tabela avisa que o comando do PNCP traz só pregão eletrônico (modalidade 6) e até 50 registros por consulta: a taxa de correspondência baixa no cruzamento por CNPJ reflete em parte esse recorte. Os slides 17 e 18 mostram a conversão de .xlsx em CSV e o dicionário de dados mínimo.

Prática, 19 min. Cada aluno baixa a base pública que serve ao projeto, converte a própria planilha em CSV, monta o dicionário de dados e cruza as duas (slide 19).

Entrega, 5 min. `entregas/modulo5-ciclo2-cruzamento.md`, com a taxa de correspondência, os registros sem par e o dicionário de dados.

O slide das quatro etapas costuma provocar reconhecimento imediato na turma que trabalha. Peça que alguém conte um caso em que ninguém conseguiu explicar de onde veio um número. O caso prepara o mapa de dados do ciclo 5.4.

Se a rede bloquear as APIs, use os arquivos de reserva. O cruzamento continua funcionando, e a limitação de rede entra no mapa como restrição declarada.

## Ciclo 5.3. Qualidade e governança de dados

Teoria, 25 min. As seis dimensões de qualidade (DAMA UK, 2013) e a base de fornecedores anotada (slide 23). Na tabela, só a linha 4 tem CNPJ com dígitos verificadores inválidos. Os CNPJs das demais linhas são fictícios com dígitos válidos, corrigidos em 15 nov. 2026 (antes, quatro deles também eram inválidos). A nota do slide 22 registra que a ISO/IEC 25012 tem modelo próprio, com quinze características. Os três papéis da governança. As três verificações da LGPD (slide 25), com a correção de 15 nov. 2026: finalidade nova exige uma das dez bases legais do art. 7º, e o consentimento é uma delas. O inciso IV (estudo por órgão de pesquisa) vale só para entidade pública ou privada sem fins lucrativos (art. 5º, XVIII), e não serve à empresa do exemplo. O que o agente envia ao provedor do modelo (slide 26). Os modelos gratuitos do OpenCode Zen e a transferência internacional (slide 27): Resolução CD/ANPD nº 19/2024 (cláusulas-padrão) e Resolução CD/ANPD nº 32/2026 (União Europeia reconhecida como destino adequado).

Prática, 20 min. Cada aluno mede completude e unicidade na própria base, confere dois números à mão pelo procedimento do slide 14, verifica validade, consistência e atualidade e confere a exatidão em cinco registros ou a registra como NÃO MEDIDO (slide 28).

Entrega, 5 min. `entregas/modulo5-ciclo3-qualidade.md`.

A conferência manual de dois números é obrigatória. Sem ela, o aluno aceita o percentual que o agente calculou, e o hábito que a disciplina quer formar é o oposto.

A parte de LGPD aqui é operacional. O aprofundamento jurídico vem no módulo 12. No slide 25, a confusão comum a corrigir é a troca do nome por um código, que é pseudonimização: o dado continua pessoal. O slide 26 liga a LGPD ao uso do agente: o conteúdo que ele lê vai ao servidor do provedor, e parte dos modelos gratuitos usa esses dados para aprimoramento. O slide 27 mostra que um dos modelos gratuitos fica na China e que os modelos da NVIDIA pedem que não se envie dado pessoal. O que precisa acontecer hoje: quem tiver CPF, telefone ou endereço na base apaga a coluna agora, antes de gravar no repositório.

## Ciclo 5.4. Mapa de dados e fechamento da entrega A2

Teoria, 10 min. O que um mapa de dados resolve.

Demonstração, 8 min. Os três comandos do script, incluindo o `a2`.

Prática, 32 min. Preencher o mapa e rodar as duas conferências (slide 33).

Entrega, 5 min. Repositório publicado com a mensagem "entrega A2".

Reserve os últimos vinte minutos para o comando `a2`. Ele percorre doze itens dos módulos 1, 3, 4 e 5 e imprime o que falta. Quem rodar cedo tem tempo de corrigir.

O script recusa linha de mapa com data de extração, completude ou responsável em branco. A data e a completude são o que torna a análise refazível seis meses depois, e é essa a razão a dar quando alguém reclamar.

Desde 15 nov. 2026, o script aceita NÃO MEDIDO em `data_da_extracao` e em `completude_percentual` para fonte que o aluno não extraiu nem mediu, e exige pelo menos uma fonte com os dois campos medidos (a base diagnosticada no ciclo 5.3). Antes, o script exigia número para as quatro fontes, e o aluno que só mediu uma base era levado a inventar os outros três. O mapa gerado lista as fontes não medidas numa seção própria.

Aceite NÃO INFORMADO em dono e custodiante. O mapa registra a lacuna e pergunta a quem o aluno perguntaria. Descobrir quem responde pelo dado é trabalho de campo e não condição para a entrega.

## O que sai deste encontro

Inventário de três fontes, uma base pública baixada e cruzada, o dicionário de dados da base do aluno, um diagnóstico de qualidade com conferência manual, e o mapa de dados com quatro fontes. Somados às entregas dos módulos 1, 3 e 4, fecham a A2 e a nota 1.

## Avisos no fechamento

A organização do projeto está definida a partir de hoje. Trocar depois custa refazer o mapa de dados.

Deixar a base tratada em `dados/` para o encontro 7: é sobre ela que se trabalha, e não sobre outra.

Escrever três perguntas de gestão que o projeto deve responder. São o ponto de partida do próximo encontro.

O capítulo 3 de Sharda, Delen e Turban fica como leitura complementar. O módulo 6 não depende dele.

Quem ficar com item pendente da A2 tem a semana seguinte para corrigir.

## Informações não conferidas

- A ISO/IEC 25012:2008 não foi lida na íntegra (norma paga). O slide 22 cita apenas o que consta do resumo público: quinze características, dois pontos de vista e parte dos nomes. A lista completa das quinze não foi conferida.
- O nome da coluna `orgaoEntidade.cnpj` no arquivo do PNCP (slide 16) vem da estrutura conhecida da API e do achatamento feito por `atividade_modulo4.py`. Não foi testado com download real nesta revisão.
- CNPJ com letras (slide 16): a data de jul. 2026 e a IN RFB 2.229/2024 vêm do anúncio da Receita Federal publicado na Agência Gov em out. 2024 (consulta em 15/11/2026). Não foi conferido se a emissão começou na data prevista, por isso o slide diz "prevê".
