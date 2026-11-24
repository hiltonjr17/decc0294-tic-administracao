# Roteiro do módulo 3

Inteligência artificial, modelos de linguagem e engenharia de prompt. Encontro 4, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

## Antes da aula

Material do professor: `slides/modulo3-ia-e-engenharia-de-prompt.html`, este roteiro e `scripts/atividade_modulo3.py`.

Publicado na turma virtual com uma semana de antecedência: o capítulo 1 de Taulli, o script e o aviso de que cada aluno precisa trazer uma referência bibliográfica que use em algum trabalho seu.

Antes do encontro, confira quem ficou pendente na entrega A1 do encontro 3. Aluno sem repositório não consegue gravar nada hoje, e o problema se agrava a cada semana.

Teste o roteiro na semana da aula. O provedor gratuito muda de modelo e de limite sem aviso.

Desde a revisão de novembro de 2026 os slides não trazem marcadores de tempo. Os tempos por etapa ficam neste roteiro.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 3.1 | 50 min | 3 a 13 |
| Ciclo 3.2 | 55 min | 14 a 22 |
| Intervalo | 15 min | |
| Ciclo 3.3 | 55 min | 23 a 30 |
| Intervalo | 10 min | |
| Ciclo 3.4 | 45 min | 31 a 38 |
| Fechamento e vocabulário | 15 min | 39 a 44 |

Revisão de 15 nov. 2026 (o deck continua com 44 slides):

- Taxonomia corrigida no slide 5. A divisão passou a ser regras e aprendizado de máquina, este com uso preditivo e uso generativo. O modelo de linguagem aparece como aprendizado de máquina generativo. O slide 4 acompanha a mudança.
- Saiu o slide sobre o que ocupa a janela de contexto (janelas por modelo, compactação a 85%, servidores MCP). O slide do ciclo do agente (10) ficou com o diagrama redesenhado, a definição de servidor MCP e uma caixa sobre injeção de instrução, que o módulo 12 trata em detalhe.
- O slide 35 perdeu os níveis de esforço do GPT-5.5 e do Claude 5.5 e ganhou uma definição de esforço de raciocínio.
- O diário de alucinação passou a ter três casos, sem mínimo de tipos diferentes, e aceita o caso sem erro conferido. A prática ocupa dois slides: os passos (20) e a leitura da saída real do comando conferir (21).
- Termos definidos no slide da primeira ocorrência: aprendizado de máquina, viés, agente, opencode, script (5), parâmetro (6), tokenizador (7), DOI (8), AGENTS.md e compactação (9), ferramenta e servidor MCP (10), SimpleQA (17), SPELL e SciELO (18), few-shot, chain of thought e prompt chaining com tradução (32), esforço de raciocínio (35).
- As práticas (12, 20, 29 e 37) trazem o pedido ao agente, o resultado esperado e o que fazer quando o resultado for outro.
- Conferido em 15/11/2026: data de corte do GPT-5.5 (1º/12/2025, página do modelo na OpenAI) e do Claude Opus 5.5 (jun. 2026, Models overview da Anthropic), tabela do SimpleQA (OpenAI, 05/09/2025, números confirmados nos trechos da própria página exibidos pela busca, porque a página recusou o acesso automatizado, nova tentativa em 15/11/2026 com o mesmo resultado), PersonQA no system card do o3 e do o4-mini (16/04/2025), página de tokens do Gemini, lançamento do MCP (25/11/2024) e OWASP LLM01:2025.
- Não conferido e retirado do deck: "Gemini 4" com 1.048.576 tokens e a tabela de janelas por modelo.
- A página de tokens do Google (aistudio.google.com/docs/tokens, que substituiu o endereço em ai.google.dev) diz que, nos modelos Gemini, um token equivale a cerca de 4 caracteres. A estimativa em palavras (60 a 80 por 100 tokens) é atribuída ao inglês. A proporção depende do tokenizador e não vale para qualquer modelo, e não há valor publicado para o português. O slide 7 e o vocabulário (slide 40) dizem isso nesses termos.

Nos slides de conceito, a definição vem na caixa do topo e os quatro pontos abaixo a desenvolvem. A caixa dourada no pé traz uma analogia de apoio. Apresente a definição primeiro e use a analogia depois, como reforço, pedindo à turma um exemplo próprio.

## Ciclo 3.1. O que é IA e o que é um modelo de linguagem

Teoria, 25 min. Regras e aprendizado de máquina, este com uso preditivo e generativo, em tabela (slide 5). Tokens e previsão do próximo token (slide 7). O que o mecanismo explica no uso diário (slide 8). O ciclo do agente com ferramentas, o MCP e a injeção de instrução (slide 10). No diagrama, o modelo devolve o pedido de ferramenta ao agente, e é o agente quem executa a ferramenta. Os módulos 4, 10 e 12 retomam agente, janela de contexto e injeção de instrução.

Demonstração, 8 min. A mesma instrução rodada duas vezes, em sessões separadas, com as duas respostas gravadas em arquivo (slide 11).

Prática, 12 min. Cada aluno repete com um conceito da própria área (slide 12). O slide traz o pedido, com os arquivos `saidas/variacao-1.md` e `saidas/variacao-2.md`, o resultado esperado e o que fazer se as respostas saírem idênticas.

Entrega, 5 min. `entregas/modulo3-ciclo1-variacao.md`.

Os três slides de conceito do ciclo, 4, 6 e 9, sustentam o que vem depois. O de treinamento explica por que o modelo não consegue abrir a fonte e traz a data de corte e os modelos de raciocínio. O de sessão e janela de contexto explica por que a demonstração exige sessões separadas e por que o agente esquece uma regra dada no início da conversa. Vale dar a eles o tempo previsto, porque a dúvida volta nos ciclos seguintes.

Ponto de atenção: alguém vai concluir que a variação torna a ferramenta inútil. A variação de redação é esperada. A variação de fato indica que uma das respostas precisa de conferência, e o exercício serve para separar as duas.

## Ciclo 3.2. Alucinação e verificação

Conceito, 8 min. O que é alucinação, também chamada confabulação, slide 15. Os quatro pontos seguem esta ordem: sem intenção de enganar, sem aviso no texto, concentrada no que sustenta decisão e presente também nos modelos novos. O último traz o resultado do PersonQA publicado pela OpenAI, em que o o3 e o o4-mini alucinaram mais que o o1. Ele mostra que a conferência não depende da versão do modelo.

Teoria, 15 min. Os tipos de erro com o rótulo aceito pelo script, slide 16. Por que acontece e o que reduz, slide 17, com a tabela do teste SimpleQA publicada pela OpenAI em 05/09/2025. A tabela compara dois modelos diferentes com acerto parecido. O que mais deixou de responder errou menos, e a comparação não isola o efeito da abstenção. Depois, onde se confere cada tipo de afirmação, slide 18, o slide mais operacional do encontro: título entre aspas no Google Acadêmico, segunda base antes de concluir que a obra não existe, DOI em doi.org, artigo no texto compilado do Planalto, número no órgão que o produz, procedimento no próprio sistema.

Demonstração, 7 min. A instrução com e sem a autorização do NÃO SEI, sobre o tema da referência que o aluno trouxe (slide 19). Vale rodar as duas versões na projeção. A diferença costuma ser visível, e quando não for, registre o empate com a turma.

Prática, 20 min. Três casos no diário, com o script (slides 20 e 21).

Entrega, 5 min. `entregas/modulo3-diario-de-alucinacao.csv` e o `.md` gerado.

O script exige três casos e recusa a coluna de conferência preenchida com "pesquisei". Ele aceita rótulos e vereditos com ou sem acento e não exige tipos diferentes. O caso sem erro, conferido e com a fonte, vale como caso. A mudança evita que o aluno force ou invente um erro para cumprir uma cota de tipos. O script avisa, sem recusar, quando o rótulo e o veredito se contradizem (sem erro com incorreto, ou um tipo de erro com confirmado). O slide 21 mostra a saída real do comando conferir sobre um diário ilustrativo. A recusa gera reclamação e faz parte do exercício, porque a nota recai sobre a conferência.

Caso a cota acabe: o aluno registra os casos que conseguiu, anota a indisponibilidade e completa os demais em casa.

## Ciclo 3.3. Os quatro elementos de um prompt

Teoria, 22 min. Papel, contexto, instrução e formato num prompt anotado (slide 25). O prompt fraco e o forte lado a lado (slide 26). Os quatro erros que estragam um prompt bom, com a base na documentação da Anthropic e do Google (slide 27). O slide de conceito (24) apresenta também a engenharia de contexto. A definição de engenharia de prompt e o subtítulo do slide 25 deixaram de prometer resultado utilizável na primeira tentativa, o que contradizia o erro "aceitar a primeira resposta" do slide 27.

Demonstração, 13 min. O slide 28 já traz um prompt fraco e sua versão forte, prontos, sobre um edital de compras. Projete os dois, rode as duas versões ao vivo e compare o que muda na resposta com a turma.

Prática, 15 min. A tarefa é fixa para toda a turma, um parecer sobre terceirizar a limpeza de um prédio público, para o professor poder comparar os pares entre si. Cada aluno inventa o órgão e o papel que dão contexto e escreve o próprio par de prompts. O slide 29 traz os arquivos `saidas/parecer-fraco.md` e `saidas/parecer-forte.md` e o pedido que monta a entrega com a seção Diferença observada em branco, para o aluno escrevê-la.

Entrega, 5 min. `prompts/modulo3-par-de-prompts.md`.

Este é o ciclo que mais rende em qualidade de trabalho no resto do semestre. Se algum ciclo precisar ceder tempo, que seja outro.

## Ciclo 3.4. Técnicas e quando cada uma vale

Teoria, 18 min. Exemplos, passo a passo e do simples ao complexo, com a coluna sobre modelos de raciocínio (slide 32): a OpenAI recomenda não pedir passo a passo a esses modelos, e a Anthropic prefere instrução geral a roteiro escrito à mão. Verificação em cadeia e consistência (slide 33), com a ressalva de que número repetido nas execuções também precisa de fonte. Depois, dois slides de fecho: escolher a técnica pelo erro que ela evita (34) e a pergunta entre trocar de técnica ou trocar de modelo, com a definição de esforço de raciocínio (35).

Demonstração, 6 min. O slide 36 traz as duas instruções prontas, sem exemplos e com exemplos, cada uma gravando num arquivo de nome diferente (`classificacao-sem-exemplos.csv` e `classificacao-com-exemplos.csv`). As quatro demandas ficam numa caixa à parte e são coladas no fim dos dois pedidos. Três delas estão na fronteira entre categorias. O exemplo do entulho fixa que infração e risco à saúde contam como denúncia (demandas 2 e 3), e o exemplo do carnê marca a fronteira entre reclamação e solicitação (demanda 4). Mesmo assim, os dois arquivos podem coincidir. O slide avisa e pede que o empate seja registrado.

Prática, 16 min. Três técnicas, um arquivo por técnica em `prompts/`, cada uma rodada sem e com a técnica (slide 37). O pedido cria seis seções: Instrução sem a técnica, Resposta sem a técnica, Instrução com a técnica, Resposta com a técnica, Erro evitado e Quando compensa. As duas últimas ficam em branco para o aluno escrever. Quem tiver acesso a outro modelo repete uma técnica nele e registra numa seção opcional Outro modelo. A comparação final fica no fim do último arquivo, como pede o slide 38.

Entrega, 5 min. Três arquivos `prompts/modulo3-tecnica-*.md`.

O critério de escolha é o tipo de erro. O aluno pode trocar de provedor durante o semestre, e um critério ancorado em cota deixaria de valer no dia da troca. O tipo de erro que cada técnica evita continua valendo em qualquer modelo.

O slide sobre trocar de modelo fixa a ordem instrução, técnica, modelo. Aluno que troca de modelo antes de corrigir a instrução não descobre onde estava o problema.

Se parte da turma estiver em provedores diferentes, peça que dois alunos com modelos distintos leiam em voz alta o resultado da mesma instrução e compare com a turma.

## O que sai deste encontro

Uma comparação de variação, um diário de alucinação com três casos, um par de prompts e o início do caderno de prompts. O diário e o par de prompts compõem a entrega A2, conferida pelo comando `a2` do script do módulo 5 e avaliada no encontro 6.

## Avisos no fechamento

Gravar e publicar antes de sair da sala, com a mensagem "entregas do modulo 3".

Trazer um documento da própria área para o encontro 5: edital, contrato, relatório ou regulamento, em PDF ou Word, sem dado pessoal de terceiro.

A escolha da organização do projeto precisa estar fechada até o encontro 6.
