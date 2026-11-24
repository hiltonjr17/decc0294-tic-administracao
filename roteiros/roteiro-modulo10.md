# Roteiro do módulo 10

Pesquisa, documentos longos e análise qualitativa. Encontro 11, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este encontro fecha a entrega B2, que vale 40% da nota 2, e com ela a nota 2 inteira.

Revisão de 15 nov. 2026: práticas reduzidas (duas camadas no 10.1, duas organizações no 10.2, livro de quatro ou cinco categorias sobre as 20 respostas da amostra no 10.3, três obrigações no 10.4), kappa de Cohen calculado pelo script e deck com 35 slides. Cada prática traz no slide o pedido ao agente, o resultado esperado e o que fazer quando o resultado for outro.

## Antes da aula

Material do professor: `slides/modulo10-pesquisa-e-analise-qualitativa.html`, este roteiro e `scripts/atividade_modulo10.py`.

Publicado na turma virtual, com pelo menos uma semana de antecedência: o pedido de que cada aluno traga um documento longo do próprio setor, com dez páginas ou mais, em PDF com texto selecionável, e um arquivo de respostas abertas em CSV, se tiver acesso a um. Relatório de gestão, plano diretor, edital, contrato e ata de reunião longa servem. PDF feito por escâner não tem camada de texto, e o agente não consegue ler as palavras.

Material de reserva, obrigatório: um relatório de gestão público em PDF com texto selecionável e um CSV de respostas abertas de pesquisa de satisfação, com pelo menos 40 linhas. Todo semestre parte da turma chega sem documento, e sem reserva esses alunos ficam parados.

Teste no laboratório, dois dias antes: o modelo gratuito do opencode lê o PDF de reserva e devolve a página de cada trecho? Se não ler, deixe na turma virtual uma versão em texto do mesmo documento, com a marca de página, e avise a turma.

Rode `python atividade_modulo10.py codificar <csv>` antes da aula sobre o CSV de reserva, para conhecer a amostra de 20 que o script sorteia. A semente é fixa, então a amostra da sua aula é a mesma da sua preparação.

Selecione uma lei ou norma que a turma conheça, para o ciclo 10.4. A Lei 8.666/1993 e a Lei 14.133/2021 servem porque muito aluno já ouviu falar das duas e quase ninguém leu, e porque o modelo costuma trocar uma pela outra.

Confira quem está pendente na B1 e nos encontros 9 e 10. A nota 2 fecha aqui.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura, visão geral e vocabulário | 10 min | 1 a 3 |
| Ciclo 10.1 | 50 min | 4 a 10 |
| Ciclo 10.2 | 45 min | 11 a 17 |
| Intervalo | 15 min | |
| Ciclo 10.3 | 55 min | 18 a 25 |
| Intervalo | 10 min | |
| Ciclo 10.4 | 50 min | 26 a 30 |
| Fechamento e B2 | 15 min | 31 a 35 |

Slide 3, novo: as palavras usadas em todos os ciclos (modelo de linguagem, agente, script e comando, provedor, token, confabulação, CSV e pastas, dado pessoal). Os termos de cada ciclo são definidos no slide em que aparecem.

## Ciclo 10.1. Leitura em camadas de documento longo

Teoria, 15 min. Slide 5: por que o resumo sem pergunta falha, com a janela de contexto e a queda de acerto quando a informação está no meio de um texto longo (Liu et al., 2024. Hong, Troynikov e Huber, 2025). Slide 6: as quatro camadas (mapa, extração com trecho de origem, análise sobre a lista, síntese), cada uma com o seu arquivo. A prática usa as camadas 2 e 4. O mapa entra quando o documento passa da janela. O slide avisa sobre PDF digitalizado sem camada de texto.

Demonstração, 10 min. Slide 7: extração com trecho literal e página sobre o relatório de reserva, na projeção. Procure três trechos no documento com Ctrl+F, na frente da turma. O slide traz um exemplo ilustrativo com um trecho que não existe no contrato. Explique que a página é a do arquivo, mostrada pelo leitor de PDF.

Prática, 20 min. Slides 8 e 9. Cada aluno testa se o PDF tem texto, pede a extração (camada 2), confere três trechos e pede a síntese de até 250 palavras para um destinatário nomeado (camada 4), com a seção Conferência no fim do arquivo. A regra é a mesma nos slides 7, 8 e 9: trecho não encontrado é marcado NÃO EXISTE, o item sai da lista e da síntese, e o aluno confere os demais itens da lista com Ctrl+F antes de entregar.

Entrega, 5 min. Slide 10. `entregas/modulo10-ciclo1-sintese.md` e `saidas/camada2-obrigacoes.csv`.

O trecho de origem é o item central do encontro inteiro. Afirmação sem trecho localizável no documento é descartada. Se uma verificação ao vivo falhar, mostre a falha à turma.

Documento longo consome contexto. Com modelo gratuito, oriente a trabalhar por seção. Duas requisições longas por aluno bastam neste ciclo.

## Ciclo 10.2. Comparação setorial com fontes verificadas

Teoria, 20 min. Slide 12: os três defeitos (período, medida e fonte secundária). Slide 13: exemplo numérico com três municípios fictícios em que a ordem da despesa com saúde por habitante se inverte entre despesa empenhada e despesa paga (Lei 4.320/1964, arts. 58, 63 e 64). Slide 14: o procedimento em quatro passos, com as definições de indicador e de fonte primária. Slide 15: demonstração dos comandos `fontes` e `conferir fontes`, dentro do tempo de teoria. O `conferir fontes` confere só a ficha, e o `conferir` completo fica para o fim do ciclo 10.3.

Prática, 20 min. Slide 16. Cada aluno compara a própria organização com uma comparável do mesmo setor e porte: pede ao agente a lista de fontes sem valores, cria a ficha com `fontes`, abre cada fonte, preenche uma linha por organização, roda `conferir fontes` e pede ao agente o arquivo da comparação com a ressalva que ele mesmo escreve.

Entrega, 5 min. Slide 17. `entregas/modulo10-fontes.csv` e `entregas/modulo10-ciclo2-comparacao.md`.

A ficha tem uma linha por organização comparada, com o mínimo de duas. Quem quiser acrescentar uma terceira organização pode, e o script aceita.

Número sem ano e sem fonte sai da tabela. Avise antes, para o aluno não preencher a ficha com números copiados da resposta do modelo.

## Ciclo 10.3. Análise de conteúdo de respostas abertas

Teoria, 20 min. Slide 19: o livro de códigos (Bardin, 1977), com um exemplo de categoria e as regras de exaustividade e exclusão mútua. Slide 20: a dupla codificação em fluxo, com o limite de 70% do script e dois estudos sobre modelo de linguagem como codificador (Gilardi, Alizadeh e Kubli, 2023. Reiss, 2023). Slide 21: concordância ao acaso e kappa de Cohen, com o cálculo sobre os 20 casos fictícios da demonstração (75% de concordância, Pe de 0,285, kappa de 0,65).

Demonstração, 10 min. Slide 22. `codificar` sobre o CSV de reserva na projeção e, depois de uma coluna preenchida, a saída de `concordancia`. O script detecta a coluna de texto mais longa, sorteia 20 respostas com semente fixa, cria o livro de códigos em branco e, no `concordancia`, imprime a taxa percentual, a concordância observada (Po), a esperada ao acaso (Pe) e o kappa.

Prática, 20 min. Slides 23 e 24. Trabalho individual. Cada aluno lê as 20 respostas da amostra, escreve um livro de quatro ou cinco categorias, preenche a coluna `categoria_aluno` no Excel, faz um commit e só então pede ao agente que preencha `categoria_agente` sem ler a coluna do aluno. Depois roda `concordancia` e `conferir`. Quem preferir pode trocar o agente por um colega na segunda coluna.

Entrega, 5 min. Slide 25. `entregas/modulo10-livro-de-codigos.md`, `entregas/modulo10-codificacao.csv` e `entregas/modulo10-relatorio.md`.

O limite de 70% funciona como gatilho de exame. Abaixo dele o `conferir` exige o campo `divergencia_examinada` em cada divergência. Em geral a causa é uma definição ambígua no livro. O kappa sai no relatório para leitura e não muda a regra de recusa.

Concordância de 100% na primeira rodada costuma indicar categorias amplas demais ("positivo", "negativo"). Vale conferir um desses livros em voz alta.

O script compara as categorias sem diferença de maiúsculas, acentos e espaços extras. Palavras diferentes ("canal" e "canal digital") contam como categorias diferentes.

## Ciclo 10.4. Legislação e conferência na fonte oficial

Teoria, 15 min. Slide 27: numeração, vigência e aplicação, com exemplos da Lei 14.133/2021 (definição de pregão no art. 6º, XLI, revogação da Lei 8.666/1993 em 30/12/2023, valor do art. 75, II, atualizado para R$ 65.492,11 pelo Decreto 12.807/2025) e os termos da tabela definidos. Slide 28, novo: Dahl et al. (2024), na versão publicada no Journal of Legal Analysis, com 58% (GPT-4) a 88% (Llama 2) de respostas confabuladas sobre decisões de tribunais federais dos EUA, em modelos lançados em 2023. A versão preliminar (arXiv, jan. 2024) trazia 69% a 88%. O slide traz também a multa do TSE noticiada pela Migalhas e a contagem da base de Charlotin. Slide 29: demonstração do teste em três passos (instrução com texto literal e NÃO SEI, conferência no Planalto, classificação em confirmado, dispositivo errado, redação desatualizada ou inexistente), dentro do tempo de teoria.

Prática, 25 min. Slide 30. Cada aluno pede no máximo três obrigações da norma escolhida, com dispositivo e texto literal, em tabela, confere cada uma no texto compilado e preenche a classe.

Entrega, 10 min. `entregas/modulo10-ciclo4-legislacao.md` e depois os comandos `conferir` e `b2`.

O aluno que não encontrar nenhum erro registra as três obrigações como confirmadas. Esse é o resultado do teste.

Reserve os últimos dez minutos para a rodada `b2` de cada aluno. O script confere doze itens: os quatro do módulo 9, a síntese, a ficha de fontes, a comparação, o livro de códigos, a codificação, o resumo legislativo, o `conferir` aprovado com o relatório gravado e o repositório publicado.

Não conferido na revisão de 15 nov. 2026: o número do processo do TSE (0600352-15.2024.6.05.0067), que aparece só na Migalhas. O slide passou a atribuir o caso à notícia e não cita o número. Para conferir, consultar o PJe do TSE ou a consulta processual do TRE-BA (o sufixo 6.05.0067 indica zona eleitoral da Bahia).

## O que sai deste encontro

Uma extração com trecho e página e uma síntese para destinatário nomeado. Uma comparação de duas organizações com ficha de fontes. Um livro de códigos com dupla codificação, concordância e kappa medidos. Um resumo legislativo com as citações conferidas e classificadas.

Com a B2 fechada, a nota 2 está completa. O bloco seguinte, encontros 12 a 16, é o da nota 3.

## Avisos no fechamento

O encontro 12 trata de aprendizado de máquina. Cada aluno precisa trazer uma base própria em CSV com pelo menos 30 linhas e três colunas de número, uma delas sendo algo que faça sentido prever. A base do encontro 7 serve, se tiver colunas numéricas suficientes.

Quem não tiver base usa a de reserva e perde o vínculo com o próprio trabalho, que dá sentido ao ciclo 11.4.
