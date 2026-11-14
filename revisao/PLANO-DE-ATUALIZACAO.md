# Avaliação e plano de atualização da DECC0294

Data: 14 nov. 2026. Escopo: os 15 decks (494 slides), os 15 roteiros, os 15 scripts de atividade e o planejamento da disciplina. Critério de leitura: turma em primeiro contato com o tema, sem conhecimento de programação.

Método: leitura integral dos decks, roteiros e mensagens dos scripts, com conferência na web de até quatro pontos datados por módulo. Cada item abaixo indica se foi conferido (em arquivo, por teste ou em fonte) ou se é avaliação. Nenhum arquivo do material foi alterado.

## 1. Avaliação geral

O desenho da disciplina é adequado e atual. A unidade de trabalho é a pasta do projeto, o aluno pede, confere e decide, e o cálculo é sempre feito por script. A revisão de 2 nov. 2026 resolveu o problema de redação: restam poucas frases de efeito. As fontes datadas conferidas estão, em sua maioria, corretas.

Os problemas que restam são de outra natureza e se concentram em cinco pontos.

1. Carga por encontro. Vários ciclos pedem em 15 a 20 minutos tarefas que um iniciante não conclui. A dificuldade cresce ao longo do semestre, e os módulos 4, 7, 10 e 14 são os mais carregados.
2. Termo usado antes da definição. O módulo 2 promete definir todo termo antes do uso (slide 3), e os demais módulos não seguem a regra. Há cerca de 80 termos sem definição prévia nos 15 decks.
3. Conferência que exige leitura de código. "Ler o script antes de usar" aparece nos módulos 5, 6 e 14 sem um procedimento que um aluno sem programação consiga seguir.
4. Divergência entre deck, roteiro e script. Em pelo menos dez pontos o deck descreve o que o script não faz, ou o script cobra o que o deck não ensina. Três desses pontos afetam nota.
5. Informação sobre ferramentas com validade de semanas. A lista de modelos gratuitos, o formato de configuração do opencode e a localização dos servidores mudaram ou podem ter mudado desde 2 nov.

Sobre a linguagem: o pedido de texto mais técnico e objetivo é compatível com a turma iniciante, desde que a definição formal venha no slide em que o termo aparece pela primeira vez. Hoje os roteiros 2 e 3 orientam o contrário ("não substitua a analogia por explicação técnica"). O plano inverte essa orientação: definição técnica com fonte no corpo do slide, analogia como apoio opcional na fala do professor.

## 2. Achados por prioridade

### 2.1 Defeitos que afetam nota ou travam a aula

| Onde | Problema | Situação |
|---|---|---|
| `atividade_modulo15.py`, lista `ENTREGAS` | O comando `c2` procura `modulo3-ciclo`, `modulo9-ciclo4` e `modulo10-ciclo3`, nomes que nenhum script grava. O slide 8 do módulo 15 diz que pendência do script conta como não entregue | Conferido no código (linhas 109, 115 e 116) |
| `atividade_modulo6.py`, função `numero()` | "12.480" é lido como 12,48 e "R$ 1.500" como 1,5, sem aviso. Os slides 10, 12 e 30 descrevem outro defeito (vírgula decimal lida como texto), que o script não tem | Conferido por teste |
| `atividade_modulo5.py`, comando `conferir` | Exige completude numérica e data de extração para as quatro fontes do mapa, e o aluno só mediu uma. O script induz número inventado, contra a regra do NÃO INFORMADO | Conferido no código pelo leitor |
| Módulo 7, slides 6, 7, 17 e 20 | A coluna de data está como texto em DD/MM/AAAA, e a consulta de exemplo filtra por AAAA-MM-DD. Com os dados da demonstração o filtro devolveria zero linhas | Lido nos slides, a testar |
| Módulo 4, slide 25 | A documentação atual do opencode mostra os servidores MCP em `mcp.servers.<nome>` com `disabled`. O slide usa o nome direto sob `mcp` com `enabled` | Conferido na documentação, a testar na versão do laboratório |
| Módulo 2, slide 26 | Os nomes dos modelos gratuitos do slide não coincidem com os encontrados na página do OpenCode Zen em 14 nov. A página lista hoje modelo gratuito hospedado na China, o que contradiz "EUA ou União Europeia" (módulos 2 e 5) | Conferido em parte |
| Todos os scripts | Dependem de Python instalado. Nenhum roteiro manda verificar Python no laboratório, e não foi possível confirmar que o opencode desktop para Windows o traga | Conferido nos roteiros |
| Módulos 2 a 4 | A palavra "clonar" não aparece em nenhum deck. Se o laboratório restaura as máquinas, o aluno não recupera a pasta no encontro seguinte | Conferido por busca |
| Módulo 1, slides 29 e 30 | A prática 1.4 pede que o aluno rode o `conferir`, e o opencode só é instalado no encontro 3 | Lido nos slides |
| Módulo 8, slide 26 | O aluno edita à mão o HTML do painel para preencher destinatário e decisão, e o conteúdo se perde quando o painel é gerado de novo | Lido no slide e no script |
| Módulo 9, slides 13 e 30 | Marcador em minúscula ou com acento sai sem substituição e sem aviso. O deck documenta o defeito em vez de corrigi-lo | Já registrado em `REGISTRO.md` |

### 2.2 Adequação ao iniciante

Ordem de ensino invertida:

- Módulo 7: `SELECT COUNT(*)` é pedido nos slides 7, 8 e 14, e a leitura de consulta começa no slide 17. O ciclo 7.3 pede perguntas que cruzam bases, e a junção só é ensinada no 7.4.
- Módulo 2: a conferência do que não pode ir ao repositório (slide 38) vem depois do primeiro commit (slide 37).
- Módulo 9: "Quando não automatizar" (slide 20) vem depois de o aluno ter escolhido a tarefa.
- Módulo 15: validação de entrada só é definida no slide 11, depois de o produto estar construído no módulo 14.

Conceitos usados sem definição, por gravidade:

- Módulo 11: regressão linear, coeficiente e intercepto nunca são definidos, e são a técnica que o aluno executa. Faltam os termos modelo de referência (baseline) e sobreajuste (overfitting), substituídos por "palpite simples", "régua" e "memória do modelo".
- Módulo 6: quartil, Q1, Q3, nível de significância e falso positivo.
- Módulo 13: cerca de quinze termos de licitação e contrato (edital, habilitação, atesto, liquidação, termo aditivo, termo de referência, LINDB).
- Módulo 14: Scrum, ágil, sprint, incremento e definição de pronto.
- Módulo 4: Node.js, npx, registro npm e proxy.
- Módulo 1: transformação digital, que dá título ao módulo, e IA generativa.

Práticas que não cabem no tempo do roteiro (avaliação):

| Módulo | Prática | Tempo no roteiro |
|---|---|---|
| 3 | Cinco casos de alucinação provocados, conferidos e rotulados, com três tipos diferentes | 20 min |
| 6 | Cinco números com quatro conferências cada | 19 min |
| 7 | Cinco consultas SQL pedidas, lidas, executadas e conferidas | 20 min |
| 10 | Livro de códigos, 30 respostas, dupla codificação e divergências | 20 min |
| 13 | Até 21 notas com razão e fonte, conclusão e fechamento da C1 | 40 min |
| 14 | Construção da versão 1 do produto, sem demonstração | 40 min |

O módulo 14 é o menos adequado: não diz que forma o produto tem (página HTML, script ou planilha), não tem demonstração no ciclo de construção e pede a versão 2 em casa, onde o aluno depende de cota de modelo gratuito.

Pré-requisito oculto: os módulos 9, 13 e 14 supõem que o aluno tem tarefa de trabalho, documento real ou usuário real. Não há caso de reserva completo para quem não trabalha nem estagia.

### 2.3 Precisão técnica

- Módulo 3, slides 4 e 5: modelo de linguagem aparece como terceira técnica ao lado de aprendizado de máquina. Modelo de linguagem é aprendizado de máquina.
- Módulo 3, slide 18: o subtítulo extrapola a tabela, que compara dois modelos diferentes. Slide 16: "cada geração alucina menos" tem contraexemplo publicado.
- Módulos 2 e 3: definições divergentes de modelo de linguagem ("continuação mais provável" no módulo 2, sorteio segundo a probabilidade no módulo 3).
- Módulo 2, slide 15: reprodutibilidade definida como "chega ao mesmo resultado", e a resposta do modelo varia. O que se reproduz é o script.
- Módulo 6, slide 16: o rótulo "ausente ao acaso" corresponde a MCAR, e MAR significa missing at random. Slide 11: a afirmação sobre a mediana está incorreta como escrita.
- Módulo 8, slide 12: parte da ordem de Cleveland e McGill é teórica e não medida.
- Módulo 10, slide 24: Dahl et al. na versão publicada informa 58% a 88%. O intervalo de 69% a 88% é do preprint (conferido).
- Módulo 12, slide 10: execução de contrato também não tem equivalente no art. 11 da LGPD, e falta a prevenção à fraude (art. 11, II, g). Slide 19: regra no AGENTS.md é instrução ao agente e não controle de acesso.
- Módulo 5, slide 20: o texto trata consentimento como única base legal.
- Módulo 13: "empate técnico" de 5% é regra do script e tem outro sentido em licitação.

### 2.4 Atualidade

Confirmado em 14 nov. 2026: TIC Domicílios 2025 e TIC Empresas 2025 (módulo 1), janela e data de corte do GPT-5.5 e tabela do SimpleQA (módulo 3), caminhos de skills e AGENTS.md no opencode (módulo 4), Gemini-SQL2 no BIRD e CNPJ alfanumérico (módulo 7), Data Studio e preço do Power BI Pro (módulo 8), Acórdão TCU 1.498/2026 (módulo 9), Decreto 12.807/2025 (módulo 10), Lei 15.352/2026 e ECA Digital (módulo 12), Portaria MGI 3.485/2026, Guia do Scrum 2020 e atualização do METR (módulos 13 e 14).

A atualizar:

- Lista, política de dados e local de hospedagem dos modelos gratuitos (módulos 2, 5, 12 e 15).
- Formato do `opencode.json` e a menção `@general` (módulo 4).
- PNAD sobre trabalho por aplicativo, que pode ter edição de 2025, e situação do Tema 1291 no STF (módulo 1, slide 13).
- Módulo 12, slide 18: faltam o Decreto 12.880/2026 (ECA Digital) e a Resolução CD/ANPD 30/2025. A situação do PL 2338/2023 só foi confirmada em fonte secundária.
- Módulo 5, slide 21: falta a Resolução CD/ANPD 19/2024 sobre transferência internacional.
- Fontes secundárias (blogs e sites de escritórios) nos módulos 7, 9, 12 e 13, onde existe fonte primária.

Não confirmado, a conferir antes de usar: "Gemini 4" com 1.048.576 tokens e data de corte do Claude Opus 5.5 (módulo 3), número do processo do TSE (módulo 10), números do DORA 2025 e do projeto Sentinel (módulo 14), requisito de capacidade do Copilot no Power BI (módulo 8).

### 2.5 Lacunas e excessos de conteúdo

Lacunas:

- Injeção de instrução (prompt injection), phishing e engenharia social não aparecem em nenhum dos 15 decks (conferido por busca). Os alunos usam um agente que lê arquivos e páginas a partir do módulo 4. A cibersegurança ocupa dois slides no módulo 12.
- Módulo 6: análise exploratória sem histograma nem diagrama de caixa.
- Módulo 8: definição de indicador com fórmula, meta e polaridade. O script desenha só barras, e o ciclo 8.2 ensina cinco formas.
- Módulo 9: ferramentas de fluxo que o administrador encontra (Power Automate, n8n), gatilho e agendamento.
- Módulo 2: modelos de serviço em nuvem (IaaS, PaaS, SaaS), acordo de nível de serviço e cópia de segurança.
- Módulo 1: distinção entre digitalizar um processo e mudar o modelo de negócio.
- Planejamento: os ciclos "Editais e compra pública", "Skill da área" e "Scrum e XP" e o caderno de prompts consolidado da C2 estão previstos e não constam nos decks.

Excessos, candidatos a corte ou a nota de rodapé:

- Módulo 3: slides 10, 11 e 35 (janelas por modelo, MCP, níveis de esforço de raciocínio).
- Módulo 4: skills e subagentes, que não entram em nenhuma prática.
- Módulo 7: modo STRICT, CROSS JOIN, UNION ALL e relação 1:1.
- Módulo 8: slide 19, com detalhe de licenças.
- Módulo 10: cálculo do kappa de Cohen, que o script não executa.
- Módulo 12: k-anonimato sem prática.
- Módulo 14: slide 17, com quatro fontes voltadas a desenvolvedores.

### 2.6 Avaliação e bibliografia

- Não há rubrica com pontos. O critério comum tem cinco itens sem pontuação, e os scripts conferem presença e formato.
- A C2 vale 60% da nota 3 e exige produto funcionando com demonstração ao vivo. É a entrega menos guiada do semestre.
- Roteiro e deck divergem sobre haver entrega avaliada no módulo 11.
- Taulli (2020) é anterior aos modelos de linguagem atuais e é a leitura indicada nos módulos 2, 3 e 11.
- Sharda, Delen e Turban tem 5ª edição em inglês (Pearson, 2024), que reúne o livro básico e o complementar. Tradução brasileira não conferida.
- Sutherland tem edição da Sextante de 2019, vista em catálogos e não na ficha da editora.
- Normas e guias citados nos decks estão fora da lista: Lei 14.133/2021, LINDB, Lei 9.784/1999, manual de licitações e contratos do TCU e Guia do Scrum.
- Não foi indicada obra nova em português porque nenhuma foi conferida. A escolha fica para a fase 5.

## 3. Plano de atualização

### Aplicação ao restante de 2026.2

Decisão do professor em 14 nov. 2026: o plano vale para os encontros que restam em 2026.2. As fases abaixo passam a ser executadas pelo calendário, e não pela ordem dos blocos.

Regra de sequência:

1. A fase 0 vem primeiro, limitada aos scripts e decks dos encontros que ainda vão ocorrer e aos comandos de fechamento de nota (`b1`, `b2`, `c1`, `c2`).
2. Cada módulo ainda não ministrado recebe seu pacote da fase 2, 3 ou 4 até sete dias antes do encontro. O pacote tem, nesta ordem: defeito de script, erro técnico e informação desatualizada no deck, definição dos termos na primeira ocorrência, redução das práticas ao tempo do roteiro, roteiro alinhado ao deck.
3. Dois dias antes de cada encontro: teste do roteiro numa máquina do laboratório e reconferência das informações datadas do deck.
4. Das regras transversais da fase 1, entram agora a definição na primeira ocorrência, o procedimento de conferência de script e o caso de reserva. O glossário único e a verificação automática no `auditar_texto.py` ficam para depois do semestre.
5. Módulos já ministrados não são refeitos agora. Recebem apenas errata quando o erro afeta nota ou uma entrega futura (por exemplo, o nome de arquivo que o `c2` procura). As demais correções desses módulos ficam para a próxima oferta.
6. A fase 5 se limita, neste semestre, à rubrica da C2 e das entregas ainda abertas. Bibliografia e programa ficam para a próxima oferta.

Correções de conteúdo novo (slides sobre injeção de instrução, vetores de ataque, regressão linear, forma do produto) entram no módulo em que cabem se ele ainda não foi ministrado. Se já foi, o tema é levado ao módulo seguinte mais próximo: injeção de instrução vai para o módulo 12, e validação de entrada para o módulo 14.

Situação informada pelo professor em 14 nov. 2026: o próximo encontro está entre os módulos 11 e 13. A sequência abaixo parte do módulo 11. Se ele já foi ministrado, o pacote correspondente vira errata e a fila avança.

| Ordem | Trabalho | Itens |
|---|---|---|
| 1 | Scripts que fecham nota (feito em 14 nov. 2026, ver `REGISTRO.md`) | Corrigir a lista `ENTREGAS` do `atividade_modulo15.py` (comando `c2`) e o slide 4 do módulo 15. Normalizar acentos na leitura dos formulários dos scripts 11 a 15. Corrigir no `atividade_modulo13.py` a exigência de "nao consta" e no `atividade_modulo12.py` a recusa de "nao - revisado" |
| 2 | Módulo 11 | Slide de regressão linear. Termos modelo de referência (baseline) e sobreajuste (overfitting). Contradição entre os slides 23 e 24. Ressalva sobre teste pequeno e série temporal. Decisão sobre entrega avaliada. Roteiro alinhado |
| 3 | Módulo 12 | Vetores de ataque no ciclo 12.4, com injeção de instrução em agentes. Slides 10 e 19 corrigidos. Pseudonimização e anonimização retomadas. Slide 18 atualizado com fontes primárias. Reconferência dos modelos gratuitos do OpenCode Zen (slide 16) |
| 4 | Módulo 13 | Glossário de licitação e contrato. Caso de reserva para a matriz. Limite de quatro critérios e três alternativas. "Escala de pontuação" no lugar de "régua". Rubrica da C1 |
| 5 | Módulo 14 | Forma fixa do produto e produto de partida. Demonstração completa no ciclo 14.3. Definição de Scrum e ágil. Validação de entrada. Versão 2 dentro da aula |
| 6 | Módulo 15 | Rubrica da C2 com pontos. Escala de avaliadores. Caderno de prompts no portfólio. Formato das apresentações pelo tamanho da turma. Caixa datada do slide 19 |
| 7 | Errata dos módulos 1 a 10 | Uma página para a turma, só com o que afeta entrega futura: nomes de arquivo que o `c2` aceita e leitura de "12.480" pelo script do módulo 6 para quem reutilizar a base no módulo 11 |

Ficam para a próxima oferta: as fases 2 e 3 inteiras (módulos 1 a 10), o glossário único, a verificação automática de termos, a bibliografia e o programa.

### Fase 0. Antes dos próximos encontros (correção de defeito, sem mudança de desenho)

1. Corrigir a lista `ENTREGAS` do `atividade_modulo15.py` e o slide 4 do módulo 15.
2. Corrigir `numero()` no script do módulo 6 (e a função equivalente do módulo 7) para o ponto de milhar e o prefixo R$, e alinhar os slides 10, 12 e 30.
3. Aceitar NÃO MEDIDO em completude e data no mapa de dados do módulo 5.
4. Normalizar acentos e caixa na leitura dos formulários de todos os scripts, e fazer o `gerar` do módulo 9 avisar sobre marcador não reconhecido.
5. Testar no laboratório: Python disponível, formato do `opencode.json`, instalação do MCP, as oito APIs e a leitura de PDF pelo modelo gratuito.
6. Reconferir em opencode.ai/docs/zen a lista de modelos, a política de dados e o local de hospedagem, e corrigir os módulos 2, 5, 12 e 15.

Critério de conclusão: cada script roda de ponta a ponta com uma pasta de aluno fictícia e nenhum comando de fechamento (`a2`, `b1`, `b2`, `c1`, `c2`) acusa falta de arquivo que os decks mandam criar com outro nome.

### Fase 1. Regras transversais

Regra principal, definida pelo professor em 14 nov. 2026: slide autossuficiente. Toda a explicação fica no próprio slide, e o aluno não precisa de outro material nem do professor para entender o conceito e executar a prática. A regra está detalhada no `GUIA-DE-REVISAO.md` e muda quatro pontos deste plano:

- A definição de cada termo se repete, em uma linha, em todo deck que o usa. Não basta ter sido definido em módulo anterior.
- Resultado esperado, caso de reserva e providência para erro ficam no slide da prática, e não no roteiro. A dúvida 4 do slide 26 do módulo 14, que remete ao roteiro, é reescrita.
- As leituras indicadas (Taulli, Sharda) passam a ser complemento. Nenhum slide depende delas.
- O texto por slide aumenta. A solução é dividir o slide, o que eleva o número de slides por módulo, e por isso os cortes da seção 2.5 passam a ser necessários para manter o deck no tamanho atual.

Os slides não trazem marcação de tempo. Os tempos da apresentação do módulo 15 foram retirados em 14 nov. 2026.

1. Regra de primeira ocorrência: todo termo técnico recebe definição formal, equivalente em inglês e fonte no slide em que aparece pela primeira vez. Acrescentar a regra ao `GUIA-DE-REVISAO.md` e trocar a orientação dos roteiros 2 e 3 sobre analogias.
2. Glossário único da disciplina, gerado a partir dos slides de vocabulário, com o módulo de primeira ocorrência de cada termo. Estender os slides "As palavras deste encontro" (hoje nos módulos 2 a 4) aos módulos 5 a 15.
3. Acrescentar ao `auditar_texto.py` a verificação de termo usado antes do módulo em que é definido.
4. Procedimento padrão "como conferir um script sem saber programar": pedir ao agente a explicação do script em linguagem natural, exigir que o script imprima as contagens de entrada e de saída e refazer dois números à mão. Um slide no módulo 5, referido nos módulos 6, 7, 8, 11 e 14.
5. Limite de carga por ciclo: no máximo cinco termos novos e uma prática com um produto. Rever os tempos dos roteiros a partir dessa regra.
6. Caso de reserva completo (organização fictícia com bases, documento, tarefa recorrente e usuário) para quem não tem material próprio, usado dos módulos 5 a 15.
7. Trocar fontes secundárias por primárias e manter a data de consulta.

### Fase 2. Bloco 1, módulos 1 a 5

- Módulo 1: slide de conceito inicial (transformação digital, digitalização, IA generativa, modelo e assistente). Preencher o CSV no encontro 2 e rodar o `conferir` no encontro 3. Reconferir o slide 13.
- Módulo 2: conta do GitHub criada antes da aula. Ensinar Clone. Inverter os slides 37 e 38. Alinhar a definição de modelo de linguagem com a do módulo 3. Corrigir "arquivo fechado" e a definição de reprodutibilidade. Acrescentar modelos de serviço em nuvem no lugar do detalhe de custo.
- Módulo 3: corrigir a taxonomia dos slides 4 e 5 e os subtítulos dos slides 16 e 18. Reduzir o diário a três casos e aceitar "sem erro" documentado. Retirar os slides 10, 11 e 35 e incluir um slide sobre injeção de instrução.
- Módulo 4: corrigir o slide 25 depois do teste. Mostrar uma saída bem-sucedida no slide 27. Reduzir skill e subagente a uma menção. Definir Node.js e npx ou pedir a configuração ao agente. Usar a instalação de pacote de terceiro como exemplo das quatro perguntas do slide 28.
- Módulo 5: slide do procedimento de conferência de script. Conversão de .xlsx para .csv. Atualizar o slide 21. Corrigir o slide 20.

### Fase 3. Bloco 2, módulos 6 a 10

- Módulo 6: slide de conceito com quartil e amplitude interquartil sobre dez valores. Definir significância e falso positivo ou retirar o cálculo do slide 4. Acrescentar histograma ou diagrama de caixa. Reduzir a prática 6.4 a três números. Corrigir os slides 11 e 16.
- Módulo 7: reordenar para 7.1, 7.2, 7.4 e 7.3, ou restringir o 7.3 a uma tabela. Reduzir a três consultas. Corrigir a cadeia de datas. Slide de leitura de `SELECT COUNT` antes do slide 7. Cortar STRICT, CROSS JOIN, UNION ALL e 1:1.
- Módulo 8: destinatário e decisão no formulário CSV. O comando `painel` passa a desenhar linha com a ordem do calendário, ou o ciclo 8.2 se limita a duas formas. Definição de indicador com polaridade. Reduzir o slide 19.
- Módulo 9: mover o slide 20 para o ciclo 9.1. Trocar "medido" por "estimado" no tempo manual. Slide sobre ferramentas de fluxo, gatilho e agendamento.
- Módulo 10: retirar um ciclo ou reduzir as práticas. Reescrever o ciclo 10.3 do roteiro conforme deck e script. Kappa calculado pelo script ou reduzido a uma caixa. Corrigir o slide 24.

### Fase 4. Bloco 3, módulos 11 a 15

- Módulo 11: slide de regressão linear com equação, coeficiente, intercepto e gráfico de dispersão. Introduzir modelo de referência (baseline) e sobreajuste (overfitting). Resolver a contradição entre os slides 23 e 24. Ressalva sobre teste pequeno e série temporal. Decidir se há entrega avaliada.
- Módulo 12: ampliar o ciclo 12.4 com vetores de ataque definidos (phishing, engenharia social, ransomware, injeção de instrução em agentes, fraude com voz ou vídeo sintético). Corrigir os slides 10 e 19. Retomar pseudonimização e anonimização. Atualizar o slide 18.
- Módulo 13: glossário de licitação e contrato antes do slide 4. Caso de reserva padrão para a matriz e documento do aluno só para o mapa. Limite de quatro critérios e três alternativas. Trocar "régua" por escala de pontuação e sinalizar o empate de 5% como regra do script.
- Módulo 14: fixar a forma do produto (página HTML única). Demonstração completa de uma história no ciclo 14.3. Produto de partida para quem travar. Definir Scrum e ágil. Âncoras para valor e esforço. Validação de entrada trazida do módulo 15. Versão 2 dentro da aula.
- Módulo 15: rubrica da C2 com pontos. Escala de avaliadores. Caderno de prompts no portfólio. Formato das apresentações conforme o tamanho da turma.

### Fase 5. Programa, avaliação e bibliografia

1. Rubrica com níveis e pontos para as seis entregas, publicada no encontro 1.
2. Reequilibrar a C2: peso maior para o caminho documentado e a conferência, menor para o produto funcionando.
3. Bibliografia: conferir a tradução da 5ª edição de Sharda, a edição de 2019 de Sutherland e uma obra introdutória em português posterior a 2023 para substituir Taulli. Incluir as normas e os guias gratuitos citados nos decks.
4. Alinhar `planejamento-disciplina-v2.md` e `programa-decc0294-2026-2.docx` aos decks (ciclos previstos e ausentes).
5. Fechar as pendências do planejamento: tamanho da turma, restauração das máquinas e prova final.

## 4. Decisões que dependem do professor

1. Decidido em 14 nov. 2026: o plano vale para o restante de 2026.2. Falta informar qual é o próximo encontro e a data, para fixar os prazos de cada pacote.
2. As analogias saem dos slides ou ficam como apoio abaixo da definição formal?
3. A redução de carga é feita por corte de conteúdo (lista da seção 2.5) ou por redução das práticas com o conteúdo mantido?
4. O produto do módulo 14 passa a ter forma fixa e ponto de partida comum?
5. Os scripts podem ser alterados durante o semestre em curso?
