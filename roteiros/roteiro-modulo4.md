# Roteiro do módulo 4

Do prompt ao artefato: arquivos, agentes e configuração. Encontro 5, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

## Antes da aula

Material do professor: `slides/modulo4-do-prompt-ao-artefato.html`, este roteiro e `scripts/atividade_modulo4.py`.

Publicado na turma virtual: o script e o lembrete de trazer um documento da própria área, em PDF ou Word, sem dado pessoal de terceiro. Esse documento é usado na cadeia do ciclo 4.4. A tarefa de análise do ciclo 4.2 não depende dele: o comando `iniciar` grava `dados/modulo4-planilha-teste.csv`, com dados ilustrativos de pedidos atendidos no prazo, e quem tiver planilha própria em `dados/` pode usá-la no lugar.

Prepare um documento de reserva, com dez a quinze páginas, para quem esquecer. Um edital de pregão publicado no Portal de Compras serve bem: é público, tem obrigações claras e rende os três estágios da cadeia do ciclo 4.4. Use a versão com texto selecionável, porque PDF digitalizado não traz texto para o agente ler.

Teste obrigatório numa máquina do laboratório, na semana da aula. O ciclo 4.3 depende de rede, e a rede é o que mais varia:

1. Confira se o Node.js está instalado (versão 18 ou mais recente, exigida pelo `brasil-data-mcp` 0.4.0). Sem ele, o MCP não instala, e a turma segue pelo script.
2. Peça ao agente o `opencode.json` do slide 26, feche e abra o opencode e confirme que as quinze ferramentas aparecem (no terminal, `opencode mcp list` mostra o servidor e o estado da conexão). O formato do slide é o da documentação consultada em 15 nov. 2026: o servidor fica em `mcp.servers.<nome>`, e o campo para desligar é `disabled`. O formato atual ignora `enabled`. A versão do opencode instalada no laboratório pode ser anterior a esse formato. Se o servidor não aparecer, teste a forma antiga (`"mcp": {"brasil-data": {..., "enabled": true}}`) e avise a turma qual vale no laboratório.
3. Rode `python atividade_modulo4.py apis testar` e anote quais das oito fontes a rede do CCET alcança. Rode também `apis cnpj 06279103000119`, a consulta usada nos slides 27 e 30.

Se o laboratório bloquear a instalação do MCP ou os domínios das APIs, o ciclo continua funcionando: a atividade foi desenhada para que o diagnóstico de bloqueio seja parte da entrega. Você precisa saber disso antes da aula.

Confira antes da aula quais alunos ainda não têm o AGENTS.md preenchido do encontro 3. Sem ele, o ciclo 4.2 não funciona, e a correção é rápida se feita antes.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 4.1 | 48 min | 3 a 10 |
| Ciclo 4.2 | 45 min | 11 a 19 |
| Intervalo | 15 min | |
| Ciclo 4.3 | 75 min | 20 a 35 |
| Intervalo | 10 min | |
| Ciclo 4.4 | 40 min | 36 a 41 |
| Fechamento e vocabulário | 15 min | 42 a 47 |

O deck foi refeito para uma turma sem contato anterior com o tema. Os slides de conceito, com a tarja CONCEITO, definem cada termo antes do primeiro uso: artefato, HTML, API, JSON e MCP. Dois slides de vocabulário fecham o encontro.

Na revisão de 2 nov. 2026 o deck passou de 40 para 42 slides, com o exemplo numérico da segunda rodada (Gloaguen et al., arXiv:2602.11988) e o slide do registro e do comando `conferir`.

Na revisão de 15 nov. 2026, pela regra de slide autossuficiente, o deck passou de 42 para 47 slides. Mudanças:

- Toda prática traz o passo a passo, o texto do pedido ao agente, o resultado esperado e o que fazer quando o resultado for outro (slides 9, 17, 18, 33, 34 e 40). As práticas dos ciclos 4.2 e 4.3 foram divididas em dois slides cada.
- Termos definidos no slide da primeira ocorrência: agente de IA, modelo de linguagem e repositório (slide 4), markdown e CSV (6), confabulação (8), sessão (12), custo de inferência (14), script (15), URL (21), contexto, provedor e ferramenta (23), Node.js, npm, registro npm e npx (26), Selic, CDI, IPCA, ISPB, SGS e PNCP (28), proxy (29), edital e subagente (37), critério de aceitação (38), pregão e habilitação (39), dado pessoal (40).
- Slide 12: o opencode lê o AGENTS.md quando inicia (opencode.ai/docs/rules). A prática da rodada 2 (slide 18) manda fechar e abrir o opencode antes de rodar de novo.
- Slide 14: o texto passou a dizer que a bateria indica se a regra mudou o resultado. Uma execução por versão, com nota do próprio aluno, não mede o efeito. Gloaguen et al. com a diferença entre a versão 1 (os arquivos tendem a reduzir a taxa de sucesso) e a versão 3 (não melhoram em geral).
- Slide 21: a definição de API cobre consulta, gravação e acionamento de operação. Saiu a analogia do balcão dos fundos, e o espaço passou para a definição de URL.
- O conceito de MCP (slide 23) vem antes das três formas de estender o agente (slide 24), que já usam o termo. Skill e subagente ficaram reduzidos a uma definição curta, porque não entram em prática. A menção a `@general` saiu: a documentação de agentes do opencode, consultada em 15 nov. 2026, não a descreve.
- Slides 26 e 27: o `opencode.json` no formato `mcp.servers`, com a versão do pacote fixada (`brasil-data-mcp@0.4.0`) e o pedido para o agente escrever o arquivo, em vez de digitar o JSON.
- Slides 29 e 30: saídas reais de 15 nov. 2026, com as oito fontes alcançadas, ao lado da saída de 2 nov. 2026, em que o proxy recusou os oito domínios.
- Slide 32, novo: as quatro perguntas aplicadas à instalação do próprio `brasil-data-mcp`, um pacote de terceiro que acrescentou na versão 0.4.0 um provedor pago com consulta de CPF.
- Slide 28: a nota sobre taxas sem data de referência citava brapi.dev, serviço distinto da BrasilAPI. A fonte passou a ser a própria resposta da BrasilAPI.
- Slide 7: a caixa da gráfica saiu e deu lugar à definição de marca (tag). A comparação com a gráfica pode ficar na fala, depois da definição.
- Slide 24: a linha da configuração diz que o AGENTS.md é lido quando o opencode inicia, como nos slides 12 e 18. Slide 42: a versão 2 é comparada à versão 1 nas mesmas três tarefas, rodadas uma vez cada, sem falar em medida.
- Slide 30: a saída abreviada marca os cortes com reticências e mostra a linha da UF, que é um dos campos de comparação com o MCP.

O ciclo 4.3 concentra quatro conceitos e é o mais pesado do encontro em vocabulário novo. A ordem é deliberada: primeiro a API, que é o que existe de fato, depois o JSON, que é o formato em que o dado chega, e só então o MCP, que é o embrulho por cima. Quem inverte essa ordem ensina a sigla e não o conceito, e a turma sai achando que MCP é uma fonte de dados.

A definição técnica está no slide e é o que se cobra. Analogia pode entrar na fala como apoio depois da definição, nunca no lugar dela. O funcionário novo que ganha acesso a mais um sistema, por exemplo, ajuda a separar "dar ferramenta" de "ficar mais inteligente".

## Ciclo 4.1: gerar documentos na pasta do projeto

Conceito, 6 min. O que é um artefato, slide 4, com as definições de agente de IA, modelo de linguagem e repositório. A ideia que resume o ciclo: uma tarde de conversa com o modelo pode terminar sem nenhum artefato, e é assim que o trabalho se perde.

Teoria, 12 min. Resposta na tela e arquivo na pasta, slide 5, em dois caminhos. A tabela dos quatro formatos, slide 6, com a coluna sobre o que o histórico mostra. O que é HTML, slide 7, com o arquivo por dentro e a página no navegador, antes da demonstração que gera um arquivo desses.

Demonstração, 7 min. O glossário em HTML, slide 8, aberto no navegador ali mesmo. Peça para ordenar a tabela por subárea, para mostrar que o arquivo é editado e não recriado.

Prática, 18 min. Slide 9. Cada aluno gera o glossário da própria área, revisa as doze definições e guarda a instrução e as correções em `prompts/modulo4-glossario.md`.

Entrega, 5 min. `entregas/glossario.html` e `prompts/modulo4-glossario.md`.

A instrução da demonstração proíbe o autor de referência de propósito, porque é exatamente onde a confabulação apareceria. O aluno acrescenta depois, conferindo. Três conceitos com autor conferido bastam.

## Ciclo 4.2: configurar o comportamento com o AGENTS.md

Teoria, 15 min. A instrução que vale em toda sessão da pasta, slide 12, com o que segue para o modelo a cada pedido, a leitura do AGENTS.md quando o opencode inicia e a situação do formato em nov. 2026 (Agentic AI Foundation, Linux Foundation). A regra testável, slide 13. O que a segunda rodada mostra, slide 14.

Demonstração, 6 min. O script `iniciar`, slide 15, que guarda a cópia da versão 1, prepara as três tarefas e grava a planilha de teste. O registro e o comando `conferir`, slide 16, que recusa a linha sem o que saiu fora e sem o ajuste.

Prática, 19 min. Slides 17 e 18. Rodada 1 numa sessão nova, correção do arquivo, fechar e abrir o opencode, rodada 2 e `conferir`.

Entrega, 5 min. Slide 19. `AGENTS.md`, `entregas/modulo4-registro.csv` e o relatório gerado.

O critério de que uma regra precisa poder ser violada é o conteúdo central do ciclo. Peça em voz alta que alguém leia uma regra sua e pergunte à turma como ela seria violada. Regra que ninguém consegue violar não permite verificar se foi cumprida.

O passo de fechar e abrir o opencode antes da rodada 2 é o que mais se esquece. Sem ele, a rodada 2 roda com a versão 1 do arquivo e o aluno conclui que a correção não teve efeito.

O script compara o AGENTS.md com a cópia da versão 1 e aponta se o arquivo não mudou. Quem defender que a versão 1 já estava perfeita precisa escrever isso no relatório, com as notas da rodada 1 sustentando o argumento. Uma rodada de cada versão, com nota do próprio aluno, indica a direção da mudança e não prova o efeito. O slide 14 diz isso.

Na tarefa de análise com a planilha de teste, a conta de janeiro é 96 ÷ 120 = 80,0%. Número diferente ou mês que não está na planilha conta como número inventado no registro.

Se a cota acabar: a rodada 1 é a prioridade. Quem não conseguir rodar a segunda completa em casa e registra a indisponibilidade.

## Ciclo 4.3: estender o agente, um MCP e as APIs públicas

Conceito, 12 min. O que é uma API, slide 21, com a anatomia da URL do IBGE e a definição de URL. Depois o JSON, slide 22, lendo em voz alta o par nome e valor do exemplo de São Luís e a mesma linha no CSV do script. Em seguida o que é um MCP, slide 23, com as definições de ferramenta, contexto e provedor, e só então as três formas de estender, slide 24, com os arquivos que o opencode lê (AGENTS.md, SKILL.md e o bloco `mcp` do opencode.json). Skill fica como definição: não há prática.

Teoria, 5 min. O diagrama do slide 25, com os dois caminhos até a BrasilAPI na consulta de CNPJ. Pelo MCP, o modelo escolhe a ferramenta e o argumento, e pelo script a URL fica impressa. O servidor MCP só empacota APIs que já existem, e é isso que o aluno leva para a reunião com fornecedor.

Demonstração da instalação, 12 min. Slide 26: peça ao agente o `opencode.json` e confira cada linha com o modelo do slide, explicando Node.js, npm, registro npm, npx e a versão fixada. Slide 27: feche e abra o opencode, confirme as quinze ferramentas e faça a primeira consulta com o número na instrução, CNPJ 06.279.103/0001-19, da UFMA. Peça ao agente o argumento que ele passou à ferramenta. Sem o número, o modelo pode completar um CNPJ por conta própria.

Teoria, 8 min. A tabela das oito fontes do comando apis, slide 28. Todas abrem sem cadastro. Portal da Transparência e DataJud ficam fora da aula porque cada aluno precisaria da própria chave.

Demonstração do que está por baixo, 8 min. Rode `apis testar`, slide 29, e compare com as duas saídas reais do slide: todas as fontes alcançadas em 15 nov. 2026 e todas recusadas pelo proxy em 2 nov. 2026. Rode `apis cnpj 06279103000119`, slide 30, e escreva a URL no quadro. A ferramenta `consultar_cnpj` do brasil-data-mcp consulta a mesma BrasilAPI, e o script diz isso na saída. Em `apis municipios MA` o script chama o IBGE direto, enquanto o MCP usa a BrasilAPI, segundo o README do servidor. O dado tem a mesma origem e a URL é outra, e o script também diz isso na saída.

Teoria, 5 min. As quatro perguntas de decisão, em árvore, slide 31. A pergunta sobre exportar o dado periodicamente vem antes da conexão. O slide 32 aplica as quatro perguntas ao próprio pacote instalado na aula: quem o publica, quantas versões teve em quatro meses, por que a versão fica fixada.

Prática, 20 min. Slides 33 e 34. Instalação, diagnóstico e consulta pelas duas vias, depois a ficha de decisão em `entregas/modulo4-ciclo3-decisao.md`. O agente cria os títulos da ficha, e o aluno escreve as respostas.

Entrega, 5 min. Slide 35. `entregas/modulo4-ciclo3-decisao.md`, `dados/api-diagnostico.md` e `dados/api-cnpj.json`.

Três coisas para conduzir bem.

A ordem dos conceitos segue a dos slides: API, JSON e só então MCP. Na demonstração, o MCP vem primeiro (slides 26 e 27) e a mesma consulta pelo script vem depois (slides 29 e 30). O aluno vê a resposta do agente e então descobre que embaixo dela havia um endereço que ele mesmo poderia ter chamado.

A instalação vai falhar em algumas máquinas. Isso está previsto: a entrega aceita o registro da falha, e o script funciona sem o MCP. Não pare a turma para resolver caso individual, e não deixe ninguém parado esperando: quem travou segue pelo script.

A pergunta sobre quem responde pelo acesso costuma ser ignorada. Insista: conectar um agente ao sistema da organização é decisão de segurança da informação, e o aluno vai ser o gestor que assina ou não assina essa decisão.

Ressalva sobre o material. Em 2 nov. 2026, `apis testar` foi rodado no contêiner da revisão e no computador do professor, e as duas redes recusaram os oito domínios no proxy (HTTP 403 no túnel, registrado pelo script como URLError). Em 15 nov. 2026, numa rede com acesso direto, as oito fontes responderam. Nesse teste apareceu um defeito do script, corrigido na mesma data: o serviço de dados do IBGE devolve a resposta compactada (gzip), e o script marcava `municipios` como inalcançável. A documentação e os testes indicam três pontos. O Banco Central recusa consulta ao SGS com mais de dez anos (HTTP 406 em 15 nov. 2026), e o script começa em 01/01/2026. No PNCP, a modalidade é obrigatória em contratacoes/publicacao e a página vai até 50 registros, como o script envia. Esses parâmetros do PNCP vieram de fontes secundárias e funcionaram no teste de 15 nov. 2026. O endpoint taxas da BrasilAPI devolve nome e valor sem data de referência.

Mudanças no script em 15 nov. 2026: o CNPJ de exemplo passou a ser o da UFMA, o mesmo do deck. O comando `cnpj` aceita o número com pontuação e o CNPJ alfanumérico, emitido desde 31 jul. 2026 (IN RFB 2.229/2024), e recusa formato inválido antes de chamar a API. Não foi possível confirmar se a BrasilAPI já reconhece CNPJ alfanumérico real: o README do brasil-data-mcp 0.4.0 afirma que sim, e o teste com um número fictício devolveu 404, como esperado para CNPJ inexistente. A mensagem "Esta URL e o que uma ferramenta de MCP executaria" foi trocada por uma frase por fonte, que diz se o MCP consulta a mesma API, outra URL ou nenhuma. A consulta de CNPJ mostra primeiro razão social, situação e município, os campos comparados com o MCP.

## Ciclo 4.4: tarefas encadeadas em etapas

Teoria, 15 min. Por que quebrar em etapas, slide 37, com as definições de edital e de subagente. Subagente fica como definição: não há prática. As quatro regras de uma cadeia e o critério de aceitação, slide 38.

Demonstração, 5 min. As três instruções em sequência sobre o documento do professor, slide 39, com as definições de pregão e habilitação na nota.

Prática, 15 min. Slide 40. Cada aluno roda a cadeia no próprio documento, com os critérios escritos antes em `prompts/modulo4-cadeia.md`.

Entrega, 5 min. Slide 41. Os três arquivos da cadeia e `prompts/modulo4-cadeia.md`.

Exija que os três critérios de aceitação sejam escritos antes de rodar. Quem escrever depois produz critérios que a resposta já cumpre, e o exercício perde o sentido.

Três etapas custam três pedidos. Avise antes: a cadeia se roda uma vez, com o documento certo, e não como teste.

## O que sai deste encontro

Um glossário em HTML, um AGENTS.md testado em duas rodadas, um MCP instalado ou o erro de instalação registrado, a mesma consulta feita também pela API, um diagnóstico do que a rede do laboratório bloqueia, uma ficha de decisão sobre estender ou não a ferramenta e uma cadeia de três etapas documentada.

## Avisos no fechamento

O encontro 6 (módulo 5) fecha a nota 1 com a entrega A2. Liste em voz alta o que ela reúne: mapa de tarefas do módulo 1, diário e par de prompts do módulo 3, AGENTS.md do módulo 4 e o mapa de dados que será feito no próprio encontro 6.

A organização do projeto precisa estar definida. Depois do encontro 6, mudar custa refazer o mapa de dados.

Trazer uma planilha ou base da organização escolhida, com pelo menos vinte linhas e sem dado pessoal identificável. Quem não tiver traz o endereço de uma base pública.
