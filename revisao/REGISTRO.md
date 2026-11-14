# Registro de revisões do material 2026.2

Estado de cada deck e histórico das revisões. O padrão e o procedimento estão em `revisao/GUIA-DE-REVISAO.md`. Atualize este arquivo ao fim de cada sessão de revisão.

## Estado por módulo

Os sinais vêm de `python revisao/auditar_texto.py`, rodado em 2 nov. 2026. Elementos visuais conta os slides com diagrama, fluxo ou tabela anotada.

| Mód. | Enc. | Deck | Slides | Sinais | Elementos visuais | Situação |
|---|---|---|---|---|---|---|
| 1 | 2 | Transformação digital | 36 | 1 | 17 | revisado em 2 nov. 2026, deck inteiro. O sinal restante é "Ensino fundamental", falso positivo |
| 2 | 3 | Ambiente de trabalho digital | 46 | 0 | 21 | revisado em 2 nov. 2026, deck inteiro, mantida a adaptação de set. 2026 |
| 3 | 4 | IA e engenharia de prompt | 44 | 0 | 20 | revisado em 2 nov. 2026, deck inteiro, mantida a adaptação de set. 2026 |
| 4 | 5 | Do prompt ao artefato | 42 | 0 | 20 | revisado em 2 nov. 2026, deck inteiro, mantida a adaptação de set. 2026 |
| 5 | 6 | Dados na Administração | 32 | 0 | 11 | revisado em 2 nov. 2026, slides 6 a 32 (ver abaixo) |
| 6 | 7 | Análise exploratória | 31 | 2 | 15 | revisado em 2 nov. 2026, deck inteiro (ver abaixo). Os dois sinais restantes são falsos positivos: "significativa" como termo estatístico e o separador ';' na saída do script |
| 7 | 8 | Dados estruturados e consulta | 31 | 0 | 14 | revisado em 2 nov. 2026, deck inteiro |
| 8 | 9 | Visualização e painéis | 31 | 0 | 13 | revisado em 2 nov. 2026, deck inteiro |
| 9 | 10 | Automação | 31 | 0 | 13 | revisado em 2 nov. 2026, deck inteiro |
| 10 | 11 | Pesquisa e análise qualitativa | 31 | 0 | 13 | revisado em 2 nov. 2026, deck inteiro |
| 11 | 12 | Aprendizado de máquina | 29 | 0 | 11 | revisado em 2 nov. 2026, deck inteiro |
| 12 | 13 | Governança, LGPD e cibersegurança | 29 | 0 | 11 | revisado em 2 nov. 2026, deck inteiro |
| 13 | 14 | Decisão apoiada por IA | 28 | 0 | 10 | revisado em 2 nov. 2026, deck inteiro |
| 14 | 15 | Produto digital e ágil | 27 | 0 | 10 | revisado em 2 nov. 2026, deck inteiro |
| 15 | 16 | Projeto integrador | 26 | 0 | 12 | revisado em 2 nov. 2026, deck inteiro |

Todos os 15 decks foram revisados pelo padrão do guia em 2 nov. 2026. Próximas ações: resolver as pendências dos scripts listadas abaixo, reconferir antes de cada encontro as informações datadas (modelos gratuitos do OpenCode Zen, PL 2338/2023, regulamentação da ANPD) e abrir os decks no laboratório com a Segoe UI.

Em 2 nov. 2026 os marcadores de tempo foram retirados de todos os decks (ver histórico). A contagem de slides acima já reflete o estado posterior.

## Histórico

### 14 nov. 2026, módulos 12 a 15 e errata da turma, por workflow

Executado por um workflow de agentes: um agente por módulo aplicou o pacote do plano, um revisor independente conferiu cada módulo (os quatro reprovaram a primeira versão, com falhas de gravidade média e baixa), um agente corrigiu as falhas apontadas, e um agente final conferiu a coerência entre os módulos 11 a 15. Todos seguiram a regra de slide autossuficiente.

Módulo 12, de 29 para 33 slides. Novos: 11 (bases do art. 11 ao lado do art. 7º, com execução de contrato sem equivalente e a alínea g), 18 (pseudonimização e anonimização, com o k-anonimato reduzido a uma caixa), 20 (o que o AGENTS.md e o .gitignore fazem e não fazem), 24 (engenharia social, phishing, falsa central, voz ou vídeo sintético) e 25 (ransomware e injeção de instrução em agentes, OWASP LLM01:2025). Linha do tempo do slide 19 só com fontes primárias (Res. CD/ANPD 30/2025, Decreto 12.880/2026, ficha do PL 2338/2023 na Câmara). Incidente alinhado ao script (primeiras duas horas) e à Res. CD/ANPD 15/2024. A base com dado pessoal e a tabela de correspondência ficam fora da pasta do projeto, e dados/restrito/ serve para demonstrar o .gitignore. Script: recusa de responsável vago por conteúdo e não por texto exato, regras de base para linha com dado sensível (prevenção à fraude e exercício de direito em contrato aceitos, legítimo interesse, proteção ao crédito e execução de contrato recusados) e campo obrigatório "vetor:" no plano de resposta.

Módulo 13, de 28 para 36 slides. Novos: vocabulário da licitação (4 e 5) e do contrato (15), caso de reserva com edital e três propostas fictícias (10 e 11), que passa a ser o padrão da matriz, documento a enviar ao modelo e sigilo comercial (18), empate técnico do script e empate ficto da LC 123/2006, art. 44 e 45 (29), rubrica da C1 em 10 pontos (32). "Régua" virou "escala de pontuação". Frases de efeito saíram do script e dos slides que reproduzem a saída. Script: limite de 3 a 4 critérios e 2 a 3 alternativas, docstring com cinco seções. Portaria MGI 3.485/2026: o texto no DOU não foi localizado, e o slide usa a ata do MGI sem afirmar exigência de sinalizar o uso de IA.

Módulo 14, de 27 para 35 slides. O produto passou a ser uma página HTML única em entregas/produto.html (slide 3). Novos: gestão ágil e Scrum definidos (11 e 13), âncoras de valor e esforço (15), validação de entrada (20), demonstração completa de uma história do pedido à página aberta (22 e 23), duas práticas de construção (24 e 25) e a versão 2 em aula (30). O slide sobre agentes no desenvolvimento virou caixa. Script: comando novo de produto de partida e entregas/produto.html no conferir. Nomes de menu do GitHub Desktop e o seletor de modelos do opencode foram escritos sem teste na versão do laboratório.

Módulo 15, de 26 para 30 slides. Novos: vocabulário do módulo (2), rubrica da C2 em 10 pontos com 5,5 para caminho, conferência e caderno de prompts e 2,0 para o produto (6), ordem, formato por tamanho de turma e escala de avaliadores (12), rodar os scripts sem o agente (23). Formulário de avaliação com código da ordem de apresentação no lugar do nome. Script: entregas/produto.html e prompts/ no c2, formulário com código.

Errata da turma em revisao/errata-turma-2026-2.md: oito itens, só com o que afeta entrega futura, conferidos no código dos scripts. O agente da errata encontrou um defeito na correção do script 11 feita mais cedo no mesmo dia: em CSV com ponto e vírgula, "45.678" (decimal) era lido como milhar, o que afeta as tabelas gravadas pelo módulo 7. Corrigido com decisão por coluna (ponto de milhar só quando algum valor da coluna tem vírgula decimal ou todos os valores com ponto têm formato de milhar). Testado com quatro formatos de CSV. Resta ambígua a coluna em que todos os valores com ponto têm exatamente três casas, descrita no item 8 da errata.

Conferência final, refeita fora do workflow: auditoria sem sinais nos decks 11 a 15, conferir_slides.js sem estouro nos decks 12 a 15, py_compile nos scripts 11 a 15, teste da pasta de aluno fictícia com 11 de 11 verificações (o teste passou a incluir entregas/produto.html). Imagens abertas: módulo 12, slide 25, módulo 13, slide 32, módulo 14, slide 22, módulo 15, slide 6. A fonte DejaVu Sans não está instalada na máquina, e o segundo teste de largura usou fonte substituta.

Decisões que ficaram com o professor:
- Rubricas da C1 (módulo 13, slide 32) e da C2 (módulo 15, slide 6), apresentadas como proposta.
- Limites do script 13 (3 a 4 critérios, 2 a 3 alternativas) e caso de reserva contado como problema específico na C1 e na C2.
- Formato das apresentações: até 12 alunos individual, 13 ou mais em dupla. Falta informar o tamanho da turma e publicar a ordem com códigos (A01, A02...).
- Campo "vetor:" obrigatório no plano do módulo 12 e as novas regras de base para dado sensível: valem se nenhum aluno gerou o plano com o script antigo.
- Caso C&M Software (módulo 12, slide 26) apoiado só em fonte jornalística. Relato do projeto Sentinel (módulo 14, slide 11) não conferido no livro de Sutherland.
- Tempos dos roteiros 12 a 15 redistribuídos para decks maiores (33, 36, 35 e 30 slides). Conferir em aula se cabem.
- Testar no laboratório: menus do GitHub Desktop e seletor de modelos do opencode citados no módulo 14, comando de terminal do slide 23 do módulo 15.

### 14 nov. 2026, módulo 11, pacote do plano de atualização

Primeiro módulo revisado pela regra de slide autossuficiente. O deck passou de 29 para 30 slides.

- Slide novo 22, "Regressão linear: a reta que o script ajusta": gráfico de dispersão com a reta, definição de regressão linear, intercepto, coeficiente e mínimos quadrados, e a conta de uma previsão com os números da demonstração (9.734,51 + 43,9863 × 200 = 18.531,77).
- Termos definidos na primeira ocorrência: regressão, classificação, otimização e simulação (slide 4), palpite simples como modelo de referência (baseline), acurácia, treino e teste, titular (slide 5), alvo, preditora e sobreajuste (overfitting) no lugar de "memória do modelo" (slide 11), parâmetro, modelo de árvore e o critério das cinco opções do ImageNet (slide 15), RLHF e modelo de raciocínio (slide 16), semente (slide 23).
- Slide 17: a lei de conversão passou a ser nomeada (MP 869/2018, Lei 13.853/2019) e a Nota Técnica 12/2025 da ANPD descrita como consolidação da tomada de subsídios, sem posição final.
- Contradição resolvida entre a demonstração e a prática: as duas preditoras são declaradas na ficha antes do treino, a versão entregue é a das duas, e a Leitura registra o erro das duas execuções. O slide 24 não diz mais "troque de coluna", e o script também não.
- Slide 23: limites do teste (12 casos, embaralhamento inadequado para série mensal).
- As quatro práticas (slides 7, 12, 18 e 25) ganharam o pedido ao agente, quando há, o resultado esperado e o que fazer quando o resultado for outro.
- "Régua" saiu do título dos slides 1 e 21.

Script `atividade_modulo11.py`: a mensagem de modelo que perde deixou de mandar trocar as preditoras. A ficha pede duas preditoras na ordem de teste. Percentual com vírgula decimal ("70,6%"). Aviso quando o teste tem menos de 20 casos. Em CSV separado por ponto e vírgula, "12.480" passou a ser lido como 12.480 e não como 12,48. Teste com base de 40 linhas no formato brasileiro: coeficiente de 45,6 para um valor gerado de 43,99.

Roteiro 11: o encontro deixa de ser descrito como sem entrega avaliada, porque a ficha e o resultado entram na C1. Tabela de tempo renumerada (ciclo 11.4 nos slides 20 a 26, fechamento 27 a 30) e ciclo 11.4 com 17 min de teoria e 25 de prática.

Conferência: auditoria de linguagem sem sinais. Medição de estouro da área útil nos 30 slides, sem estouro. Captura dos slides 22 e 25.

### 14 nov. 2026, avaliação geral, regra de slide autossuficiente e tempos do módulo 15

Avaliação dos 15 módulos e plano de atualização em `revisao/PLANO-DE-ATUALIZACAO.md`, aplicado ao restante de 2026.2 a partir do módulo 11.

Pedido do professor: toda a explicação deve estar no próprio slide, sem depender de outro material nem do professor, e os slides não devem trazer marcação de tempo. A regra entrou no guia.

Módulo 15: retirados os tempos da apresentação do aluno, que haviam ficado em 2 nov. Slide 5 ("dez minutos" virou "quatro blocos"), slide 10 (título "A apresentação em quatro blocos", faixa sem minutos, sem aviso e corte), slide 14 (passo 3 sem cronômetro) e slide 16. Conferência visual do slide 10 no navegador. O modelo `entregas/roteiro-apresentacao.md` gravado pelo `atividade_modulo15.py` perdeu os tempos no mesmo dia (ver abaixo). O roteiro do professor mantém os tempos.

Número do encontro retirado dos 15 decks, por decisão do professor. Foram 117 trocas de "encontro N" por "módulo N − 1" (por exemplo, "o painel do encontro 9" virou "o painel do módulo 8"), e as 15 capas perderam o prefixo "Encontro N ·" do subtítulo. Ficaram 12 ocorrências dentro de blocos de saída de script (módulo 8, slide 25, e módulo 15, slides 6 e 20), porque os scripts dos módulos 8 e 15 imprimem "encontro N". Esses três slides receberam uma nota de correspondência, retirada no mesmo dia quando os scripts passaram a imprimir módulo. Auditoria de linguagem sem sinais novos. Conferência visual no navegador dos slides que ganharam texto (módulo 8, slide 25, e módulo 15, slides 6 e 10). Os roteiros do professor continuam numerados por encontro.

Scripts, com autorização do professor para alterá-los durante o semestre:

- `atividade_modulo15.py`: a lista `ENTREGAS` do comando `c2` passou a usar os nomes que os scripts gravam (`modulo3-diario-de-alucinacao`, `modulo5-mapa-de-dados`, `modulo9-fluxo.csv` e `modulo9-relatorio.md`, `modulo10-codificacao.csv` e `modulo10-relatorio.md`). Antes, um aluno com tudo entregue via os módulos 3, 5, 9 e 10 como ausentes. Rótulos por módulo (2 a 15) no `c2` e no `portfolio`. O modelo do roteiro de apresentação perdeu "Dez minutos, cronometrados" e os minutos por bloco. O `portfolio` passou a ler `prompts/`. As mensagens deixaram de mandar o aluno digitar `python ...` e passaram a indicar o pedido ao agente.
- `atividade_modulo11.py`: o `conferir` aceita "não" com acento (função `normalizar`).
- `atividade_modulo12.py`: o `conferir` aceita "nao - revisado" quando nenhuma linha é eliminável, como a própria mensagem do script pedia.
- `atividade_modulo13.py`: o `conferir` aceita "todas as categorias constam" no mapa do documento, além de NAO CONSTA.
- Scripts 2, 4, 5, 7, 8, 9, 10, 13 e 14: "encontro N" trocado por "modulo N − 1" em rótulos, docstrings e mensagens.

Teste: pasta de aluno fictícia com os arquivos de todos os módulos, 11 verificações (c2 completo e incompleto, roteiro sem tempos, portfólio, acento no 11, "revisado" no 12, frase de cobertura e NÃO CONSTA no 13). As versões novas passam nas 11. As versões anteriores falham nas 8 que testam os defeitos corrigidos. O script de teste ficou fora do repositório.

Slides alinhados aos scripts: módulo 8, slide 25 (saída do `b1`), módulo 11, slide 28 (dúvida sobre acento), módulo 12, slide 12 (linha "revisado" e acento), módulo 13, slide 13 (frase de cobertura), módulo 14, slide 24 ("apresentação de dez minutos", marcação de tempo que escapou da primeira varredura), módulo 15, slides 4 (números dos módulos e nomes de arquivo do `c2`), 6, 20, 21 e 22. Conferência no navegador dos slides 4 e 6 do módulo 15 e 13 do módulo 13. Medição de estouro da área útil nos slides 28 do módulo 11 e 12 do módulo 12, sem estouro.

Atenção: os alunos recebem cópia dos scripts na turma virtual. As versões novas dos scripts 11 a 15 precisam ser publicadas lá antes do módulo correspondente. Quem já tem a cópia antiga do `atividade_modulo15.py` verá os módulos 3, 5, 9 e 10 como ausentes.

Os demais 14 decks foram varridos por minutos, horas e cronômetro. As ocorrências restantes são dado de exemplo (tempo de espera, tempo de tarefa, prazo de chamado) e não marcação de aula.

### 2 nov. 2026, módulos 1, 2, 3 e 4, decks inteiros

Os módulos 2 a 4 mantiveram a adaptação de setembro para turma sem contato prévio (componentes `.conceito` e `.duas`). O módulo 1 recebeu o componente `.conceito`, que não tinha. Auditoria com zero sinais nos módulos 2 a 4 e um falso positivo no módulo 1. Conferência visual com Liberation Sans e DejaVu Sans.

Módulo 1 (encontro 2), de 34 para 36 slides. Novos: 6, velocidade de adoção da IA generativa, e 20, quanto do trabalho a IA generativa alcança. Correções: Schwab usa velocidade, amplitude e profundidade, e impacto sistêmico. Saíram uma afirmação sem fonte sobre o emprego no Maranhão e uma comparação de "ordem de grandeza" que era de cerca de cinco vezes. Dados: TIC Empresas 2025 (17% das empresas usam IA), TIC Domicílios 2025 (32% dos usuários de internet usam IA generativa), PNAD TIC 2025, Pintec Semestral 2024, Eurostat, Bick, Blandin e Deming, OIT e NASK (2025), Eloundou et al. Conferir antes da aula se o STF concluiu o Tema 1291.

Módulo 2 (encontro 3), 46 slides. Saiu o antigo 35 (repetia 15 e 34) e entrou o 27, esquema anotado da tela do opencode desktop. Correções: o comando `criar` cria quatro pastas, e o deck dizia cinco. O GitHub Desktop grava sozinho o Initial commit, e o README não pode ser marcado na criação. Cada `conferir` reescreve o relatório A1. Tabela dos modelos gratuitos do OpenCode Zen com a política de dados de cada um. Verificação em duas etapas obrigatória no GitHub.

Módulo 3 (encontro 4), de 42 para 44 slides. Novos: 7, tokens e previsão do próximo token, 10, o que ocupa a janela de contexto, e 11, o ciclo do agente com ferramentas. Correções: a janela cheia é compactada pelo opencode (resumo da conversa antiga), e o deck dizia que o começo era descartado. Janelas atuais de cerca de 1 milhão de tokens. Passo a passo dispensável em modelos de raciocínio, com o esforço de raciocínio como parâmetro. Repetição de um número entre execuções não prova que ele está certo. Alucinação com os dados do SimpleQA (acerto, erro e abstenção) e Kalai et al. (2025). MCP e AGENTS.md na Agentic AI Foundation desde 9 dez. 2025.

Módulo 4 (encontro 5), de 40 para 42 slides. Novos: 14, o que a segunda rodada mostra (Gloaguen et al., 2026, sobre o efeito de arquivos AGENTS.md, conferido), e 16, o registro das rodadas e o comando conferir. Correções: o bloco de MCP estava no formato `mcpServers`, que o opencode não lê. O correto é o bloco `mcp` em `opencode.json`. Skills e subagentes do opencode. Limite de 10 anos por consulta no SGS do Banco Central desde mar. 2025. CNPJ da UFMA (06.279.103/0001-19, conferido) na demonstração do MCP. As oito APIs públicas não puderam ser testadas: o proxy recusou os oito domínios no contêiner e no computador do professor. O slide 27 mostra essas saídas reais. O teste com `python scripts/atividade_modulo4.py apis testar` precisa ser feito na rede do laboratório.

Roteiros 1 a 4 renumerados, com descrições de teoria e demonstração atualizadas e travessões retirados dos títulos.

### 2 nov. 2026, módulos 13, 14 e 15, decks inteiros

Auditoria com zero sinais nos três. Conferência visual com Liberation Sans e DejaVu Sans.

Módulo 13 (encontro 14), de 26 para 28 slides. Novos: 6, do critério vago ao critério verificável, e 18, o comando conferir diante de uma devolutiva incompleta. Correções: o script aponta a norma não conferida e não a retira. A devolutiva tem cinco seções no modelo do script, e o deck falava em quatro. Art. 50 da Lei 9.784 com incisos e § 1º. A Lei 14.133 usa "extinção" no lugar de "rescisão". Fontes: guia de licitações e contratos do TCU (arts. 36, 92, 117 e 140 da Lei 14.133), LINDB arts. 20 e 28, Keeney (1992), Jakesch et al. (2023). O empate técnico de 5% é a regra do script para a matriz de decisão, e não o critério legal de empate em licitação.

Módulo 14 (encontro 15), de 25 para 27 slides. Novos: 12, valor sobre esforço num backlog de exemplo, com saída real do comando `priorizar`, e 17, agentes de IA no desenvolvimento em 2025 e 2026 (DORA 2025, METR jul. 2025 e atualização de fev. 2026, Spec Kit). O Guia do Scrum de nov. 2020 continua a versão oficial. O "AI and Scrum" v2026.1 (Jocham e Sutherland, jan. 2026) é complemento do Scrum Guide Expansion Pack (conferido). Correções: a recusa da ficha vem do `conferir`, e não do `produto`. Teste com usuários pela curva de Nielsen (2000): cerca de 31% dos problemas por usuário e 85% com cinco. Os números do projeto Sentinel do FBI vieram de resenha do livro de Sutherland e devem ser conferidos na edição da Leya.

Módulo 15 (encontro 16), de 20 para 26 slides. Novos: 4, o semestre na pasta do projeto, 6, a conferência da C2 na projeção, 11, o produto diante do dado errado, 13, o formulário conferido pelo script, 20, o índice do semestre, 24, depois da disciplina. Correções: o comando `c2` confere os encontros 3 a 16 e só verifica se os arquivos existem. O comando `apresentacao` passou a constar no deck. O `portfolio` grava um índice e três campos, sem espaço por bloco. Os tempos do roteiro de apresentação do aluno (2, 2, 4 e 2 min) ficaram, por serem parte da tarefa. Fontes: OWASP sobre validação de entrada, Topping (1998) e Hattie e Timperley (2007) sobre avaliação por pares e devolutiva.

Roteiros 13, 14 e 15 renumerados, com descrições de teoria e demonstração atualizadas.

### 2 nov. 2026, módulos 10, 11 e 12, decks inteiros

Auditoria com zero sinais nos três (o auditor passou a contar palavras proibidas só no início de palavra, para não acusar "coeficiente"). Conferência visual com Liberation Sans e DejaVu Sans.

Módulo 10 (encontro 11), de 29 para 31 slides. Novos: 11, a mesma comparação com despesa empenhada e paga (Lei 4.320/1964), e 19, concordância observada e ao acaso (kappa de Cohen, 1960, e Krippendorff, 2018). Fontes: Liu et al. (2024) sobre informação no meio de textos longos, Dahl et al. (2024) sobre alucinação em perguntas jurídicas, Gilardi, Alizadeh e Kubli (2023) sobre modelo como codificador, revogação da Lei 8.666 pela LC 198/2023, valor do art. 75, II, da Lei 14.133 em R$ 65.492,11 pelo Decreto 12.807/2025 (conferido). Corrigido: as classes do diário do módulo 3 não eram as mesmas do ciclo 10.3.

Módulo 11 (encontro 12), de 27 para 29 slides. Novos: 16, como se treina um modelo de linguagem (pré-treino, ajuste supervisionado, reforço), e 22, treino e teste dentro do script. Saiu a afirmação sem fonte de que a regressão "custa 2 a 3 pontos percentuais". Entraram Rudin (2019), Mitchell (1997), Grinsztajn et al. (2022), Ouyang et al. (2022). Leitura para o módulo 12 corrigida para os arts. 5, 6, 7 e 48 da LGPD. Prática e entrega do 11.4 alinhadas ao script.

Módulo 12 (encontro 13), de 27 para 29 slides. Novos: 12, linhas que o script aceita e recusa, e 18, proteção de dados e IA em novembro de 2026. Correções: comunicação de incidente em 3 dias úteis, complemento em 20 dias úteis e registro por 5 anos (Res. CD/ANPD 15/2024). ANPD agência reguladora pela Lei 15.352/2026 (conferido). ECA Digital em vigor desde 17 mar. 2026. PL 2338/2023 aguardando parecer na comissão especial da Câmara. NIST SP 800-63B-4: SMS como autenticador restrito (conferido). k-anonimato (Sweeney, 2002). O deck antigo dizia que o script aponta consentimento usado entre servidor e chefia, o que é falso.

Roteiros 10, 11 e 12 renumerados, com descrições de teoria atualizadas.

### 2 nov. 2026, módulos 7, 8 e 9, decks inteiros

Os três decks foram reescritos pelo padrão do guia e passaram de 29 para 31 slides cada. Auditoria de linguagem com zero sinais nos três. Conferência visual com Liberation Sans e DejaVu Sans.

Módulo 7 (encontro 8). Slides novos: 6, "Tipo declarado e valor gravado", e 19, "Acerto dos modelos ao escrever SQL" (teste BIRD, Li et al., 2023, e resultado de 80,04% do Gemini-SQL2 no ranking de modelos únicos, jun. 2026, por fontes secundárias, porque o ranking oficial não abriu). Correções: a coluna tipada do SQLite só barra valor errado no modo STRICT, que o script não usa. O script não informa linhas antes e depois do filtro, e o slide passou a pedir duas consultas COUNT(*). CNPJ alfanumérico a partir de jul. 2026 (IN RFB 2.229/2024). Acrescentados o comando `conferir` e suas regras. Treze `\n` literais removidos. Citações: Codd (1970), Chen (1976), Kimball e Ross (2013).

Módulo 8 (encontro 9). Slides novos: 6, eixo cortado e fator de distorção (Tufte, 1983), e 12, barra e pizza pela ordem de precisão de Cleveland e McGill (1984). Correções: as colunas do formulário e o comando `painel saidas/consulta-N.csv` agora coincidem com o script. O painel gera só barras ordenadas por valor, e o deck avisa que série mensal perde a ordem do calendário. Ferramentas: Power BI Desktop gratuito, compartilhamento com licença Pro, Copilot com capacidade F2 ou P1. Looker Studio voltou a se chamar Data Studio em abril de 2026 (docs.cloud.google.com/data-studio, conferido). Acessibilidade pela WCAG 2.2 (critérios 1.4.1 e 1.4.11).

Módulo 9 (encontro 10). Slides novos: 5, "Quatro sinais de tarefa automatizável", previsto no roteiro e ausente no deck, e 12, "Substituição por script e redação pelo agente". Correções: o comando `conferir` exige quatro números, e o deck falava em três. Marcadores do modelo precisam estar em maiúsculas e sem acento. Fontes: IEEE 2755-2017 (RPA), Taulli (2020), OSWorld (Xie et al., 2024), Acórdão TCU 1.498/2026 sobre concessão automática no INSS (por fontes secundárias), LGPD art. 20. O roteiro dizia que o encontro abria a nota 3. Corrigido: ele integra a B2.

Roteiros 7, 8 e 9 renumerados, com descrições de teoria e demonstração atualizadas.

### 2 nov. 2026, marcadores de tempo retirados de todos os decks

Pedido do professor: os slides não devem mostrar tempo. Em todos os 15 decks foram retirados o "~N min" dos cartões da visão geral, o "~N minutos" dos divisores e os minutos da linha de etapas dos divisores, que passou a mostrar só "Teoria · Demonstração · Prática · Entrega". O subtítulo das práticas passou de "N minutos, individual" para "Individual" (e variantes como "Turma inteira"). No módulo 15, "a ordem dos seus 35 minutos" virou "a ordem das correções". Ficaram, por serem conteúdo e não marcação de aula, os tempos do roteiro de apresentação do projeto integrador (2, 2, 4 e 2 min no módulo 15). Os tempos continuam nos roteiros do professor.

### 2 nov. 2026, módulo 6 (encontro 7), deck inteiro

Pedido do professor: revisar o módulo 6 pelo mesmo padrão do módulo 5. Todos os slides depois da capa foram reescritos. O deck passou de 30 para 31 slides.

Mudanças de conteúdo:

- slide 4: exploratória e confirmatória com referência a Tukey (1977) e o problema das comparações múltiplas quantificado (1 − 0,95²⁰ = 64%), com figura de 20 cruzamentos
- slide 5: fluxo decisão, pergunta de gestão, pergunta de dados e verificação na base, com a ficha da medida (numerador, denominador, período, recorte)
- slide 11: média e mediana com o exemplo de 101 contratos desenhado e a conta explícita (R$ 108.910), mediana apresentada como medida resistente
- slide 16: as três classificações do formulário do script ligadas à terminologia de Rubin (1976): MCAR, ausência estrutural, MAR ou MNAR
- slide 17 (novo): exemplo numérico em que a ausência com viés inverte a conclusão (Norte 100 observado, 200 real, Sul 150) e o preenchimento pela média (116,7) não corrige
- slide 18: árvore de decisão do valor atípico, com a definição das cercas de Tukey (Q1 − 1,5 × AIQ, Q3 + 1,5 × AIQ), que é o critério do script
- slide 23: os dois caminhos do número calculado pelo agente (escrito na resposta ou produzido por script) e onde o erro aparece em cada um
- slide 24: as quatro conferências ligadas aos campos do log. A afirmação anterior de que estavam "em ordem de custo" era inconsistente e saiu
- slides 12, 19 e 25: saídas ilustrativas no formato real do script, em bloco de terminal
- slide 30: pergunta nova sobre preencher vazios com a média
- `\n` literais, ponto e vírgula e paralelismos removidos

Os rótulos do formulário (ausente ao acaso, por regra, com viés, erro de registro, unidade trocada, realidade) e as decisões aceitas (manter, corrigir, separar, excluir, não preencher) foram mantidos exatamente como o script os valida.

Roteiro: tabela de distribuição renumerada (6.1 slides 3 a 8, 6.2 9 a 14, 6.3 15 a 21, 6.4 22 a 27, fechamento 28 a 31), títulos dos ciclos e textos de teoria atualizados.

Conferência: renderização com Liberation Sans e DejaVu Sans, sem estouro relevante.

### 2 nov. 2026, módulo 5 (encontro 6), slides 6 a 32

Pedido do professor: linguagem com cara de modelo de linguagem, inadequada para material acadêmico, poucos elementos visuais e conteúdo sobre IA a atualizar. Revisão a partir do slide 6. O deck passou de 29 para 32 slides.

Slides novos:

- 6, "Onde o agente de IA acerta e onde erra com dados": matriz de quatro tarefas com desempenho, falha característica e controle, mais a definição de saída estruturada
- 18, "As dimensões aplicadas a uma base de fornecedores": base fictícia anotada, com o cálculo da completude (338 ÷ 400 = 84,5%)
- 21, "O que o agente envia ao provedor do modelo": fluxo pasta, agente e provedor, retenção e uso de dados pelos modelos gratuitos, transferência internacional (LGPD, art. 33)

Correções de conteúdo:

- qualidade de dados passou de cinco para seis dimensões (validade incluída), com fonte DAMA UK (2013)
- LGPD: troca de nome por código reclassificada como pseudonimização (arts. 12 e 13), minimização apresentada como princípio da necessidade (art. 6º, III)
- API: menção aos conectores padronizados (MCP)
- cruzamento e diagnóstico de qualidade pedidos como script gravado em `saidas/`
- `\n` literais removidos dos slides de cruzamento

Elementos visuais acrescentados: matriz de tarefas (6), tabela de inventário com lacunas (7), fluxo da linhagem com barra de rastreabilidade (11), eixo de dependência (12), diagrama de cruzamento com códigos IBGE (13), grade das seis dimensões (17), base anotada (18), diagrama de governança (19), fluxo até o provedor (21), ficha do mapa de dados (25), sequência dos comandos do script (26).

Roteiro: tabela de distribuição do tempo renumerada (ciclo 5.1 slides 3 a 9, 5.2 10 a 15, 5.3 16 a 23, 5.4 24 a 28, fechamento 29 a 32) e menções aos slides 6, 20 e 21.

Fontes consultadas: OpenCode Zen, seção Privacy (opencode.ai/docs/zen), 2 nov. 2026. Ficha do PL 2338/2023 no Senado. IBGE Cidades para os códigos 2111201 e 2107506.

Conferência: renderização com Liberation Sans e DejaVu Sans. Falta conferir no laboratório com a Segoe UI, em especial os slides 6 e 13, que são os mais cheios.

### Set. 2026, histórico anterior (git)

- 31 ago.: material completo dos 15 módulos (4b9c99f)
- 1º set.: módulo 2 revisado para turma sem contato prévio (a374d7f). Módulos 3 e 4 no mesmo sentido (4083a3c)
- 14 set.: ajustes no módulo 3 e no roteiro 3 (7a074f5, 5efb7a9). README e modelo de AGENTS.md para os alunos (7709dbd)
- 15 set.: ajustes pequenos em quase todos os decks (e882102). Links do README para o GitHub Pages (600fbc3)

## Pendências fora dos decks

Defeitos nos scripts encontrados na revisão de 2 nov. 2026. Os scripts não foram alterados, e os decks avisam o aluno onde o defeito afeta a atividade.

- `atividade_modulo7.py`, comando `juntar`: conta os registros sem par com NOT IN. Com chave vazia em qualquer das tabelas, a contagem sai menor que a real (teste: 0 em vez de 1). Trocar por NOT EXISTS resolve.
- `atividade_modulo7.py`, função `numero()`: lê "1.234" como 1,234. Valor não numérico em coluna numérica vira vazio sem ser contado como rejeitado. CNPJ só com dígitos perde os zeros à esquerda.
- `atividade_modulo7.py`: pede "as cinco contagens" e imprime seis. A numeração `consulta-N` usa a contagem de arquivos e pode sobrescrever um arquivo se algum for apagado.
- `atividade_modulo8.py`, comando `painel`: pinta todo aumento em vinho, mesmo quando aumentar é bom, e destaca sempre a maior barra. A variação negativa em verde-azulado tem contraste de 2,7:1 para texto, abaixo do mínimo de 4,5:1 da WCAG. O critério "sem data de atualização perde metade do item" ficou no deck, embora o script já grave a data.
- `atividade_modulo9.py`: o cabeçalho do modelo (Responsável, Última revisão, Regra para dado ausente) sai em todo documento gerado, porque o corte é feito só em "COMO ADAPTAR ESTE MODELO". Marcador em minúscula ou com acento sai sem substituição e sem aviso.
- Módulo 8: o deck dizia que o painel "volta no encontro 11", mas os módulos 9 e 10 não tratam de painel. Ficou "exemplo de fluxo repetível para o encontro 10". Confirmar.
- Roteiro 7: notas fora do escopo ainda têm ponto e vírgula e "valiosa".
- `atividade_modulo10.py`: o comando `b2` confere 10 itens, mas não verifica `entregas/modulo10-fontes.csv` nem se o `conferir` foi aprovado. O `conferir` acusa a falta da codificação enquanto o ciclo 10.3 não termina (o deck avisa).
- Roteiro 10, ciclo 10.3: fala em duplas e diz que o ciclo não usa modelo de linguagem, mas o script prevê a coluna `categoria_agente`. O deck segue o script. Decidir qual desenho vale.
- `atividade_modulo11.py`: o `conferir` recusa "não" com acento, porque compara com "nao" (o deck avisa). Resolvido em 14 nov. 2026.
- Roteiro 11: diz que o encontro não tem entrega avaliada, mas o deck tem slide de entrega com critério de correção. Decidir.
- `atividade_modulo1.py`: a linha de exemplo diz "quatro vezes por mes", mas a conta de 6 h só fecha com quatro unidades. Tarefa com texto igual ao do exemplo é ignorada. No encontro 2 não há opencode: confirmar quem executa o `conferir`.
- `atividade_modulo2.py`: a prática 2.2 pede o comando `criar` antes da instalação do opencode, que só ocorre no 2.3 (o deck manda rodar logo após a instalação). Em repositório clonado em outra máquina, o `conferir` conta zero versões. Confirmar se a conexão ao OpenCode Zen pede cartão.
- `atividade_modulo3.py`: só aceita rótulos e vereditos sem acento ("nao verificavel"). O deck orienta escrever sem acento. "sem erro" conta como um dos três tipos mínimos.
- `atividade_modulo4.py`: a mensagem "Esta URL e o que uma ferramenta de MCP executaria" não vale para `municipios` (o script chama o IBGE direto, e o MCP passa pela BrasilAPI). O CNPJ é pedido "so numeros", e há CNPJ alfanumérico desde jul. 2026. Parâmetros do PNCP vieram de fontes secundárias.
- Acentos: os scripts dos módulos 3, 11 e outros recusam "não" e rótulos acentuados. Uma normalização de acentos na leitura dos formulários resolveria o problema em todos de uma vez.
- Resolvido em 14 nov. 2026. `atividade_modulo15.py`, lista `ENTREGAS` usada pelo comando `c2`: para os encontros 10 e 11 espera arquivos que começam por `entregas/modulo9-ciclo4` e `entregas/modulo10-ciclo3`, que nenhum deck nem script manda criar (as entregas reais são `modulo9-relatorio.md`, `modulo9-fluxo.csv` e `modulo10-codificacao.csv`). No encontro 4, o prefixo `modulo3-ciclo` não encontra o diário de alucinação. Um aluno que fez tudo verá esses encontros como ausentes na conferência da C2. Correção recomendada antes do encontro 16. O deck orienta o aluno a mostrar o arquivo e o commit.
- Resolvido em 14 nov. 2026 o primeiro item. `atividade_modulo13.py`: o `conferir` exige "nao consta" mesmo quando o documento trata das cinco categorias (o deck orienta a escrever "categorias que nao constam: nenhuma"). A docstring fala em quatro seções, e o modelo tem cinco. O `c1` só confere se os arquivos dos encontros 12 e 13 existem. A comparação com o critério escrito em casa foi para a seção 3 da devolutiva, porque o script não prevê arquivo próprio. Confirmar.
- `atividade_modulo14.py`: aceita público genérico ("os gestores da secretaria") e história que descreve solução em vez de necessidade ("quero um botão de exportar para PDF"). O deck mostra o segundo caso como aceito e inadequado. O deck pede dois pedidos longos ao modelo por história, e o planejamento fala em dois por ciclo prático. Decidir.
- Roteiros 13, 14 e 15: trechos antigos, fora das descrições atualizadas, ainda têm travessão em títulos, ponto e vírgula e "vale mais que".
- Resolvido em 14 nov. 2026 o primeiro item. `atividade_modulo12.py`: quando nenhuma linha é eliminável, o script manda escrever "nao - revisado", e a conferência recusa (só aceita linha que começa com "s"). A recusa de responsável vago compara o texto exato ("a equipe de TI" passa). Falta a base do art. 11, II, g (prevenção à fraude). Não confere `entregas/modulo12-ciclo3-exemplo.md`.

- Em 2 nov. 2026 os decks (e os dois .pptx antigos) foram movidos para `slides/` e os scripts das atividades para `scripts/`. Na mesma data, os roteiros foram para `roteiros/`. Foram atualizados `index.html`, `README.md`, `indice-material-2026-2.md`, os roteiros e as ferramentas de `revisao/`. Os scripts receberam um ajuste de poucas linhas que muda o diretório de trabalho para a raiz quando estão em `scripts/`. O texto dos decks continua dizendo "execute atividade_moduloN.py", porque na turma o script é copiado para a raiz do projeto do aluno. Os endereços antigos do GitHub Pages (sem `slides/`) deixam de funcionar depois do próximo push.

- Alterações sem commit em 2 nov. 2026: ajustes de exemplos numéricos nos decks 4, 6, 7, 8, 10, 11 e 13, a revisão do módulo 5 e a pasta `revisao/`. A pasta `estilo-vale/` e o arquivo `justificativa-diarias-passagens-fora-prazo.docx` também estão fora do controle de versão. Decidir o que entra no repositório público antes do próximo commit.
- `build_moduloN.js` e `tema_ufma.js` não estão na pasta. Se forem recuperados, portar a revisão do módulo 5 antes de gerar os decks de novo.
- Antes de cada semestre, reconferir a política dos modelos gratuitos do OpenCode Zen e a situação do PL 2338/2023.
