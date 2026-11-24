# Roteiro do módulo 9

Automação de documentos e processos. Encontro 10, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este encontro não tem entrega avaliada própria. O que se produz aqui entra na entrega B2, conferida no encontro 11 pelo comando `b2` do script do módulo 10, que percorre os encontros 10 e 11. É o encontro em que a turma passa do relatório pontual ao fluxo repetível.

Revisão de 15 nov. 2026: o deck passou de 31 para 35 slides. Novos: caso de reserva (slides 9 e 17), taxa de acerto dos agentes de uso do computador (22) e ferramentas de fluxo de baixo código (23). "Quando não automatizar" foi para o ciclo 9.1 (slide 6), antes da escolha da tarefa. Toda prática traz pedido ao agente, resultado esperado e o que fazer quando o resultado for outro.

## Antes da aula

Material do professor: `slides/modulo9-automacao.html`, este roteiro e `scripts/atividade_modulo9.py`.

Publicado na turma virtual: o script e o pedido de que cada aluno traga uma tarefa que ele mesmo repete, com periodicidade e tempo gasto, e um exemplar do documento que ela produz. Quem não trabalha nem estagia usa o caso de reserva do comunicado do almoxarifado (slides 9 e 17), que traz a tarefa, os passos com minutos estimados, dois exemplares e a terceira linha da tabela.

Rode `python atividade_modulo9.py iniciar` e depois `gerar` uma vez antes da aula, com o caso de reserva. Os três documentos saem sem o cabeçalho do modelo, e o terceiro traz o aviso de NAO INFORMADO na situação. A turma vê o mesmo texto fixo repetido com valores diferentes.

Prepare uma tabela de exemplo com uma coluna faltando de propósito, para a demonstração do ciclo 9.2. O script interrompe a geração quando um marcador não tem coluna. Mostre também um marcador escrito como `[mes]`: o `gerar` avisa e sugere `[MES]`.

Separe um caso local de automação que deu errado, como ofício com nome trocado, boleto duplicado ou e-mail em massa com campo não preenchido. O ciclo 9.3 usa um exemplo concreto de erro repetido em muitos documentos.

## Mudanças no script em 15 nov. 2026

- O `gerar` grava só o texto entre a linha `## Documento` e a linha `---` do modelo. Responsável, data de revisão e regra para dado ausente ficam no modelo. Modelo antigo, sem a linha `## Documento`, continua funcionando, com aviso.
- O `gerar` avisa colchete que não segue a regra de nome (maiúsculas de A a Z, algarismos e sublinhado) e sugere o nome corrigido. Link de Markdown e caixa de seleção (`[ ]`, `[x]`) não geram aviso.
- O formulário `entregas/modulo9-fluxo.csv` ganhou a linha `manutencao_minutos_por_ano`. O ponto de equilíbrio passou a usar a economia líquida: tempo manual menos tempo automatizado menos manutenção por execução. Arquivo criado antes, sem essa linha, é aceito com aviso, e a manutenção conta como zero.
- O `gerar` ignora linha vazia mesmo quando ela tem mais campos que o cabeçalho, caso das três linhas vazias criadas pelo `iniciar` depois que o cabeçalho é trocado. Linha com valor além da última coluna gera aviso com o número da linha. A prática do slide 18 pede ao agente que apague as linhas vazias junto com a troca do cabeçalho.
- O `conferir` recusa `execucoes_por_ano` igual a zero. O relatório identifica o tempo manual como estimado e os tempos automatizado e de construção como medidos.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 9.1 | 50 min | 3 a 11 |
| Ciclo 9.2 | 55 min | 12 a 19 |
| Intervalo | 15 min | |
| Ciclo 9.3 | 45 min | 20 a 26 |
| Intervalo | 10 min | |
| Ciclo 9.4 | 45 min | 27 a 31 |
| Fechamento | 10 min | 32 a 35 |

## Ciclo 9.1. O que é automatizável

Teoria, 20 min. Slides 4 a 7. Coleta, produção e decisão (slide 4), com dois casos brasileiros. O ALICE, da CGU, lê editais e emite alertas, e gestores e auditores decidem o que corrigir. Na análise automática do INSS, o TCU encontrou desconformidade em 10,94% dos indeferimentos automáticos de janeiro a maio de 2024 (Acórdão 634/2025-Plenário) e, em 2026, determinou que o segurado seja avisado de pendência que possa aumentar o benefício (Acórdão 1.498/2026-Plenário). O slide define CNIS. Os quatro sinais de tarefa automatizável, com a definição de agente de IA e dos destinos do mapa do módulo 1 (slide 5). Quando não automatizar, em quatro situações (slide 6): baixa frequência, regra instável, processo em mudança e decisão sobre direito de pessoa (LGPD, art. 20). A turma aplica as quatro situações antes de escolher a tarefa. O método de decomposição em quatro etapas (slide 7). O tempo manual é estimado, lembrado da última execução. Só o tempo do fluxo automatizado é cronometrado, no ciclo 9.4.

Demonstração, 10 min. Slide 8. O relatório mensal da ouvidoria (exemplo ilustrativo) decomposto em oito passos, 120 minutos estimados por execução: 54 min de coleta, 42 de produção e 24 de decisão. Coleta e produção somam 96 min e são os passos candidatos, a confirmar pelos quatro sinais. A instrução pede a soma por classe em script gravado em `saidas/`, conferida à mão. O slide define script e arquivo .csv.

Caso de reserva, 3 min. Slide 9. O comunicado mensal de consumo de papel da Divisão de Almoxarifado: oito passos, 92 minutos estimados por execução, 12 execuções por ano, estimativa de 1 h por mês no mapa do módulo 1. Os passos vêm sem classe, porque classificar é a prática.

Prática, 12 min. Slide 10. Cada aluno decompõe a tarefa que trouxe, ou a do caso de reserva, e pede ao agente a classificação e a soma por script.

Entrega, 5 min. Slide 11. `entregas/modulo9-ciclo1-decomposicao.md`, com uma frase sobre as quatro situações de não automatizar.

O erro comum é decompor em três passos genéricos ("coletar, analisar, escrever"). Peça grão fino: de onde vem cada número, quem abre qual arquivo, em que ordem. Oito passos permitem separar coleta e produção da decisão, e três passos genéricos não permitem.

A decisão continua na lista, marcada como decisão, e fica com uma pessoa. Essa marcação separa a automação da transferência de responsabilidade para o sistema.

## Ciclo 9.2. Modelos de documento com variáveis

Teoria, 20 min. Slides 13 a 15. O modelo de documento com variáveis em diagrama (modelo, tabela, script, três documentos) e a definição, ligada à mala direta (slide 13). Substituição por script e redação pelo agente comparadas (slide 14): repetibilidade, com a definição de determinística, falha característica, para onde vão os dados e conferência necessária. O slide define provedor e saída estruturada. As quatro regras sobre um trecho anotado do modelo (slide 15): nome descritivo em maiúsculas e sem acento, nenhum número no texto fixo, regra para dado ausente, responsável e data de revisão no topo. Só o trecho entre `## Documento` e `---` entra nos documentos gerados.

Demonstração, 12 min. Slide 16. Um modelo executado com três linhas de dados, incluindo a execução com a coluna faltando, para que a turma veja o script interromper a geração e depois preencher com `NAO INFORMADO` e o aviso no topo.

Caso de reserva, 3 min. Slide 17. Dois exemplares fictícios do comunicado (Compras e Protocolo, outubro/2026), a terceira linha da tabela com a situação vazia e a lista de marcadores esperados para conferência. A coluna SITUACAO é escrita pela pessoa, porque decidir se o setor recebe alerta é passo de decisão.

Prática, 15 min. Slide 18. Cada aluno roda `iniciar`, escreve o modelo, pede ao agente o cabeçalho da tabela, preenche três linhas e roda `gerar`.

Entrega, 5 min. Slide 19. `prompts/modulo9-modelo.md`, `dados/modulo9-variaveis.csv`, `saidas/documento-*.md` e `entregas/modulo9-ciclo2-modelo.md`.

Documento gerado com campo vazio e sem aviso circula como se estivesse completo. Mostre o aviso de NAO INFORMADO enquanto explica a regra para dado ausente.

Este é o ciclo que mais consome cota do modelo gratuito. Duas requisições longas por aluno bastam. O restante é feito pelo script, que não usa modelo de linguagem.

## Ciclo 9.3. Automação de processos e seus limites

Teoria, 25 min. Slides 21 a 24. API, RPA e agentes de uso do computador comparados (slide 21), com as definições de API e de RPA (IEEE 2755-2017, Taulli, 2020, cap. 5). A linha "Mesma tarefa, mesmos passos" substituiu a antiga linha de previsibilidade. Taxa de acerto dos agentes de uso do computador (slide 22): no OSWorld (Xie et al., 2024), pessoas concluíram 72,36% das 369 tarefas e o melhor agente de 2024, 12,24%. No ranking oficial OSWorld-Verified, a maior taxa é 90,19% em 361 tarefas (Intelligence-Indeed Agent, registro de 25/07/2026, consulta em 15/11/2026). A taxa conta tarefas concluídas no teste e não indica qual execução vai falhar. O slide traz também a previsão do Gartner sobre projetos com agentes. Ferramentas de fluxo de baixo código (slide 23): gatilho, agendamento e ação, com Power Automate, n8n e Zapier, onde os dados passam e o custo de manutenção. O ponto de conferência humana em diagrama, antes do passo irreversível, com onde, o quê, quem e o que fazer se falhar (slide 24).

Prática, 15 min. Slide 25. Cada aluno declara o ponto de conferência do fluxo que está montando, em frase verificável, e pede ao agente que copie os quatro itens para `entregas/modulo9-fluxo.csv`.

Entrega, 5 min. Slide 26. `entregas/modulo9-ciclo3-conferencia.md` e as quatro linhas correspondentes de `entregas/modulo9-fluxo.csv`.

"O gestor revisa" não diz o que se confere. "O coordenador confere se o total do relatório bate com o extrato do mês" diz. Exija o segundo formato.

O caso local de erro em muitos documentos entra aqui. A pergunta para a turma é onde estaria o ponto de conferência que teria detectado aquele erro, e por que ele não existia.

## Ciclo 9.4. Um fluxo repetível e medido

Teoria, 12 min. Slide 28. Os cinco itens da documentação e quem preenche cada um no relatório gerado pelo script, com a definição de ponto de equilíbrio e de manutenção. Exemplo: 360 min de construção, 120 − 40 = 80 min de economia e 120 min de manutenção por ano em 12 execuções, o que dá 360 ÷ (80 − 10) = 5,1 execuções.

Demonstração, 8 min. Slide 29. O comando `conferir`, com a saída do script, o gráfico de minutos acumulados e a comparação com a estimativa do módulo 1.

Prática, 20 min. Slide 30. Cada aluno cronometra o fluxo, preenche a medição e roda `conferir`. O script calcula em quantas execuções a automação se paga e recusa a entrega se o responsável for "a equipe".

Entrega, 5 min. Slide 31. `entregas/modulo9-fluxo.csv` e `entregas/modulo9-relatorio.md`, gerado pelo comando `conferir`.

O ponto de equilíbrio é o argumento do aluno diante da chefia. Exemplo: quatro horas de construção, vinte minutos economizados por semana e 52 min de manutenção por ano em 52 execuções, isto é, 1 min por execução. O cálculo dá 240 ÷ (20 − 1) = 12,6 execuções, cerca de três meses. O cálculo cabe em um e-mail.

O responsável é registrado pelo cargo, e não pelo nome da pessoa, porque o cargo permanece quando a pessoa sai. Fluxo sem responsável deixa de ser executado no primeiro mês em que ninguém o roda. O script recusa "a equipe".

## O que sai deste encontro

Uma tarefa decomposta em passos, com tempo estimado e marcação de decisão. Um modelo de documento com variáveis, testado em três casos. Um ponto de conferência humana declarado. Um fluxo documentado, com tempo automatizado medido e ponto de equilíbrio calculado com a manutenção.

Esses arquivos são a matéria-prima do módulo 14 e do projeto integrador. Quem sai daqui sem eles chega ao encontro 15 sem processo para transformar em produto.

## Avisos no fechamento

O encontro 11 fecha a entrega B2, que vale 40% da nota 2. Cada aluno precisa trazer um documento longo do próprio setor, com no mínimo dez páginas, e um arquivo com respostas abertas, se tiver. Sem os dois, o encontro 11 roda com material de reserva.

Quem ficou pendente na B1 tem até o encontro 11 para regularizar. Leve a lista de pendências para a sala.

## Fontes conferidas em 15 nov. 2026

- TCU, notícia de 26/03/2025, Acórdão 634/2025-Plenário (10,94% de desconformidade nos indeferimentos automáticos de jan. a maio de 2024), portal.tcu.gov.br.
- TCU, notícia de 11/06/2026, Acórdão 1.498/2026-Plenário, TC 007.094/2025-6, relator ministro Bruno Dantas, portal.tcu.gov.br.
- CGU, página Alice (gov.br/cgu/pt-br/assuntos/auditoria-e-fiscalizacao/alice): ferramenta da CGU que lê editais do Compras.gov.br, do Licitações-e do Banco do Brasil, do Licitações Caixa e do Diário Oficial da União e emite alertas à gestão.
- Agência Gov, notícia de 30/12/2024 sobre o ALICE da CGU (agenciagov.ebc.com.br).
- OSWorld, página oficial e planilha do ranking OSWorld-Verified (os-world.github.io, redirecionada para osworld-v1.xlang.ai). A taxa das pessoas (72,36%) foi medida no OSWorld original, de 369 tarefas, e não há linha de base humana no Verified. O primeiro lugar do ranking muda com frequência: reconfira antes de cada oferta.
- Gartner, comunicado de 25/06/2025, conferido pelo título e endereço no resultado de busca (a página devolveu erro 403 à leitura direta).
- Lei nº 13.709/2018, art. 20, no portal do Planalto.
- Microsoft Learn (Overview of cloud flows, atualizado em 24/07/2026), n8n Docs (Schedule Trigger), Zapier Help Center (Learn key concepts in Zaps).

Não conferido: o número de 2,2 milhões de análises automáticas e a meta de 50% de concessão automática do INSS, que não entraram no deck. A data de 2014 para a origem do ALICE aparece só em fontes secundárias e também ficou fora.
