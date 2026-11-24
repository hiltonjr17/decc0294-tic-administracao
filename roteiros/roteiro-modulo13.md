# Roteiro do módulo 13

Decisão apoiada por IA: contratos, editais e devolutivas. Encontro 14, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este encontro fecha a entrega C1, que vale 40% da nota 3 e reúne os módulos 11, 12 e 13 (encontros 12, 13 e 14).

Revisão de 14 nov. 2026: o deck passou de 28 para 36 slides. Entraram três slides de vocabulário (licitação e contrato), dois slides com o caso de reserva, um slide sobre que documento enviar ao modelo, um slide que separa o empate técnico do script do empate da LC 123/2006 e um slide com a rubrica da C1. A matriz passou a usar o caso de reserva por padrão, com três a quatro critérios e duas a três alternativas, e o documento do aluno ficou só para o mapa.

## Antes da aula

Material do professor: `slides/modulo13-decisao-apoiada-por-ia.html`, este roteiro e `scripts/atividade_modulo13.py`.

Publicado na turma virtual, com uma semana de antecedência: o script e o aviso de que a matriz usa o caso de reserva do deck. O documento próprio (edital, contrato ou minuta) é opcional e serve só ao mapa do ciclo 13.2. Quem trouxer contrato de empresa precisa de autorização escrita para enviá-lo ao modelo (slide 18). Quem não trouxer usa a minuta fictícia gravada pelo comando `reserva`.

Caso de reserva: o comando `reserva` grava `dados/caso-reserva-modulo13.md` com o edital fictício nº 07/2026 da Prefeitura de Vila Serena (consultoria para redesenho do processo de compras, técnica e preço), as três propostas fictícias X, Y e Z (as mesmas dos slides 10 e 11) e uma minuta de contrato fictícia. Na minuta não constam reajuste, data-base, exclusões de escopo e recebimento definitivo, que são as ausências esperadas no mapa.

Teste feito em 14 nov. 2026, numa cópia do script fora do repositório, com uma matriz do caso de reserva: preço global 40, prazo 20, atestados 25 e formação do coordenador 15, com escala "menor preço = 10, até 10% acima = 8, até 20% acima = 6", "até 120 dias = 10, até 150 = 8, até 170 = 6", "4 atestados = 10, 2 = 7, 1 = 5" e "doutorado = 10, mestrado = 8, especialização = 6". Resultado: Y 8,40, Z 7,75, X 7,35, diferença de 7,74%, e a vencedora muda para X com o preço em 60. É uma matriz possível, e não a resposta: cada aluno define a própria escala. Rode `reserva`, `matriz` e `avaliar` antes da aula numa pasta de teste para ter essa saída à mão.

Confira quem tem pendência dos módulos 11 e 12. A C1 conferida pelo script aponta arquivo por arquivo, e é melhor que a lista apareça no início do encontro do que nos últimos dez minutos.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 13.1 | 45 min | 3 a 13 |
| Ciclo 13.2 | 50 min | 14 a 20 |
| Intervalo | 15 min | |
| Ciclo 13.3 | 45 min | 21 a 26 |
| Intervalo | 10 min | |
| Ciclo 13.4 | 60 min | 27 a 32 |
| Fechamento e C1 | 15 min | 33 a 36 |

Os slides de vocabulário (4, 5 e 15) acrescentam leitura ao ciclo. Se o tempo apertar, apresente só os termos que aparecem no slide seguinte e deixe a tabela para consulta: as definições estão no deck.

## Ciclo 13.1, O critério vem antes da alternativa

Teoria, 15 min. Slides 4 a 8. Vocabulário da licitação nos slides 4 e 5: licitação, edital, termo de referência, minuta de contrato, proposta, habilitação, atestado de capacidade técnica, critério de julgamento, técnica e preço, fatores de julgamento, TCU e LINDB, com os artigos da Lei 14.133/2021 conferidos no Planalto em 14 nov. 2026. A ordem dos cinco passos (critérios, pesos, alternativas, notas, sensibilidade) no slide 6, com a definição de teste de sensibilidade, o pensamento orientado a valores de Keeney (1992), a técnica e preço (art. 36, § 2º, proposta técnica com no máximo 70%) e o parágrafo único do art. 20 da LINDB. A matriz de decisão por soma ponderada no slide 7, com três propostas ilustrativas de manutenção predial e a conta da vencedora (B, 7,45, contra 6,95 de A). O critério vago convertido em verificável no slide 8, com a definição de escala de pontuação, termo que substitui "régua" em todo o deck, e o peso fixado sem olhar a amplitude entre a melhor e a pior alternativa (Keeney, 1992, p. 147).

Demonstração, 10 min. Slide 9. Saída real de `avaliar` com a matriz do slide 7 e as regras de recusa do script, agora com o limite de três a quatro critérios e duas a três alternativas. Lembre que o CSV deve ser editado pelo agente ou pelo Bloco de Notas, porque o Excel pode trocar o separador e a codificação. O script avisa nesses dois casos.

Prática, 15 min. Slides 10 a 12. O caso de reserva: o edital no slide 10 e as propostas no slide 11. Peça que a turma escreva critérios, pesos e escala antes de avançar para o slide 11. O slide 12 traz o passo a passo, os pedidos ao agente, o resultado esperado e o que fazer quando o resultado for outro. Quem tiver documento próprio de decisão pode usá-lo, no mesmo limite de critérios e alternativas. A escala de pontuação não tem coluna própria no CSV: o passo 3 do slide 12 manda gravá-la na coluna `justificativa_do_peso`, depois da justificativa ("maior parte do custo. Escala: menor preço = 10, até 10% acima = 8"). O script confere que a coluna está preenchida, mas não confere a escala. Ela é conferida na leitura, pela rubrica do slide 32.

Entrega, 5 min. Slide 13. `entregas/matriz-decisao.csv`, ainda sem notas, com a escala escrita em `justificativa_do_peso`.

Peça que ninguém dê nota antes de os pesos estarem escritos e justificados. Quem inverte a ordem produz uma planilha que confirma a escolha que já tinha feito.

O item "horas de capacitação" é igual nas três propostas. Quem o escolhe como critério descobre na prática o critério que não separa, do slide 8. Não antecipe.

A comparação entre a lista de critérios do aluno e a do agente substitui a antiga comparação com o critério escrito em casa. Pergunte quantos mudaram de critério e por quê.

## Ciclo 13.2, Leitura crítica de documento de decisão

Teoria, 15 min. Slides 15, 16 e 18. Vocabulário do contrato no slide 15: fiscal do contrato, recebimento provisório e definitivo, atesto, liquidação da despesa (Lei 4.320/1964, art. 63), reajuste e data-base, termo aditivo, extinção e multa de mora. O atesto da nota fiscal tem como base a prática administrativa e o comprovante do art. 63, § 2º, III, da Lei 4.320/1964. O slide avisa que, nos arts. 60, II, e 88, § 4º, da Lei 14.133/2021, atesto é o registro cadastral de cumprimento de obrigações, outro uso da palavra. O termo aditivo traz a exceção do art. 132: em necessidade justificada, os efeitos podem ser antecipados e o termo é formalizado em até um mês. Textos conferidos no Planalto em 14 nov. 2026. As cinco categorias do mapa (obrigações com prazo, pagamento e reajuste, penalidades e rescisão, escopo e exclusões, fiscalização e aceite) ligadas às cláusulas necessárias do art. 92 da Lei 14.133/2021 (incisos I, V, VI, VII, XIV, XVIII e XIX) e aos arts. 117 e 140, no slide 16. O risco da falta de prazo foi reescrito: sem prazo escrito, falta a data para caracterizar o atraso e aplicar a multa de mora do art. 162. O slide 18 trata de que documento enviar ao modelo: documento público com dado pessoal trocado por código, contrato de empresa só com autorização escrita (sigilo comercial e política de dados do modelo gratuito) e a minuta do caso de reserva. A caixa de dado pessoal escreve a regra de uso seguro do AGENTS.md do módulo 12 no próprio slide: trocar nome, CPF e assinatura por código e não enviar o que estiver em `dados/restrito/`.

Demonstração, 10 min. Slide 17. A instrução com a regra NAO CONSTA, um trecho ilustrativo do mapa e o que o comando `conferir` verifica no mapa (categorias, aspas, marca NAO CONSTA ou a frase "todas as categorias constam"). Ele não verifica se o trecho existe no documento.

Prática, 20 min. Slide 19. Cada aluno mapeia o documento próprio ou a minuta do caso de reserva, seção por seção. O slide traz o resultado esperado da minuta: reajuste, exclusões de escopo e recebimento definitivo não constam.

Entrega, 5 min. Slide 20. `entregas/mapa-documento.md`.

A frase "não preencha com o que costuma constar" precisa ser lida em voz alta. Sem ela, o modelo completa o documento com o texto de contratos parecidos, e o aluno acredita ter encontrado cláusulas que não existem.

Em quase todo contrato falta a lista de exclusões de escopo, e é dali que sai o pedido de termo aditivo. Peça exemplos da turma.

A conferência dos três trechos é obrigatória. Quando aparecer uma citação inventada, mostre para a turma inteira, sem identificar o aluno.

## Ciclo 13.3, A devolutiva escrita e assinada

Teoria, 15 min. Slides 22 e 23. A definição de devolutiva e as cinco seções do arquivo criado por `devolutiva`, com o art. 50 da Lei 9.784/1999 e o § 1º. Depois, o que se delega ao modelo e o que fica com quem assina, com Jakesch et al. (2023), o art. 28 da LINDB e a Portaria MGI nº 3.485/2026. Jakesch et al. foi conferido no artigo (arXiv 2302.00560, seções 4.1 e 4.4): 1.506 participantes, as frases escritas com o assistente enviesado tiveram cerca de 2 vezes mais chance (2,04 e 2,0) de defender a posição do modelo que as do grupo de controle, e a maioria não percebeu a influência. A portaria foi conferida na ata da 10ª reunião da CTTI/MGI, de 2 jun. 2026, publicada em gov.br/servicoscompartilhados: data de 24 abr. 2026, IA generativa limitada a informação pública salvo avaliação prévia de riscos, revisão crítica do conteúdo gerado. A afirmação anterior de que a portaria "pede sinalizar o uso de IA em documentos" não foi encontrada em fonte primária e saiu do deck.

Demonstração, 5 min. Slide 24. Saída real de `conferir` sobre uma devolutiva ilustrativa com três defeitos: norma sem registro de conferência, análise curta e sensibilidade declarada diferente da apurada. As mensagens do script foram reescritas em 14 nov. 2026 e o slide reproduz o texto novo.

Prática, 20 min. Slide 25. Cada aluno escreve a devolutiva do próprio caso, com o pedido ao agente, o resultado esperado e o que fazer quando o resultado for outro.

Entrega, 5 min. Slide 26. `entregas/devolutiva.md`.

"Escreva a recomendação antes de pedir redação" é a instrução do ciclo. O modelo redige em volta da conclusão do aluno.

O campo `norma_conferida_em` é obrigatório e o script cobra 15 caracteres ou mais.

A declaração de uso da ferramenta é regra da disciplina. Uma linha basta, e ela precisa dizer o que a ferramenta fez.

## Ciclo 13.4, Sensibilidade e entrega C1

Teoria, 10 min. Slides 28 e 29. O teste de sensibilidade em gráfico, com a matriz do slide 7. Com o peso do preço em 40 vence B. Acima de 48,6 vence A. Entre 42,2 e 55,0 a diferença fica abaixo de 5%. O script calcula só os pontos 20, 40 e 60, e o restante do gráfico foi calculado para o exemplo. O slide 29 separa o empate técnico do script (diferença menor que 5%, convenção da atividade) do empate de ME e EPP da LC 123/2006, arts. 44 e 45 (até 10% acima da mais bem classificada, 5% no pregão, com direito a nova proposta, e só quando a melhor oferta inicial não é de ME ou EPP, art. 45, § 2º, conferido no Planalto em 14 nov. 2026), aplicado às licitações pelo art. 4º da Lei 14.133/2021, e cita o art. 60 para propostas iguais.

Prática, 40 min. Slide 30. Notas com razão e fonte, `avaliar`, recomendação escrita na devolutiva, `conferir` e depois `c1`.

Entrega, 10 min. Slides 31 e 32. A pasta inteira, conferida pelo script, e a rubrica com pontos.

Quando a vencedora muda no teste, o aluno costuma querer mexer nos pesos até ela parar de mudar. Interrompa. A devolutiva registra que a recomendação depende do peso adotado.

O empate técnico abaixo de cinco por cento é resultado legítimo. A saída é um critério de desempate declarado.

Reserve os últimos dez minutos para a rodada `c1` de cada aluno. O script lista os onze arquivos dos três módulos e diz qual falta.

### Rubrica da C1 (slide 32): proposta a validar pelo professor

A rubrica do slide 32 é proposta desta revisão e ainda não foi aprovada. Distribui 10 pontos: módulo 11, 2,0. Módulo 12, 2,0. Matriz e resultado, 2,0. Mapa, 1,5. Devolutiva, 2,5. Para cada item, o slide separa o que o script confere (presença e formato) do que a leitura confere (conteúdo), e aplica o critério comum às seis entregas do planejamento. Duas regras precisam de decisão: item com pendência no `c1` recebe zero, e o caso de reserva conta como "problema real e específico" do critério comum.

## O que sai deste encontro

Uma matriz do caso de reserva (ou do documento próprio) com três a quatro critérios, escala de pontuação, pesos justificados e notas com fonte. O resultado com ranking e teste de sensibilidade. O mapa do documento nas cinco categorias, com trechos de origem e ausências marcadas. Uma devolutiva fundamentada, com norma conferida e uso de ferramenta declarado.

Com a C1 fechada, resta 60% da nota 3, na C2 do módulo 15 (encontro 16).

## Avisos no fechamento

O módulo 14 (encontro 15) trata de produto digital e gestão ágil. O produto é uma página HTML única, gravada em `entregas/produto.html`, que abre com duplo clique. Cada aluno precisa escolher, antes da aula, o processo que vai virar produto e anotar quem é o usuário: cargo, o que ele faz hoje, quantas vezes por semana, quanto tempo leva.

Quem ficou com pendência na C1 tem o módulo 14 como última janela antes do fechamento da nota. Diga isso com a lista do script na mão.

## Não conferido

- Keeney (1992, p. 147), citado por J. Baron, e os itens 3.4.4, 5.11.1 e 6.1.4 do manual do TCU: mantidos com a consulta de 02/11/2026, sem nova conferência.
- Texto integral da Portaria MGI nº 3.485/2026 no Diário Oficial da União: não localizado em 14 nov. 2026. O deck usa a ata oficial do MGI como fonte.
- Definição de pregão como modalidade para bens e serviços comuns (slide 29): conhecimento geral da Lei 14.133/2021, sem leitura do art. 6º, XLI nesta revisão.
