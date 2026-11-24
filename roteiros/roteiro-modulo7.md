# Roteiro do módulo 7

Dados estruturados e consulta. Encontro 8, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

## Antes da aula

Material do professor: `slides/modulo7-dados-estruturados-e-consulta.html` (35 slides), este roteiro e `scripts/atividade_modulo7.py`.

Publicado na turma virtual: o script e o lembrete de que as duas bases precisam estar em `dados/` e as perguntas do módulo 6 escritas, marcando quais usam uma só base.

Rode o script sobre a base de reserva antes da aula: crie o banco, faça uma consulta e uma junção. Você vai precisar conhecer a saída, e a demonstração do ciclo 7.4 depende de uma junção que dê certo na projeção.

Prepare também uma segunda tabela de referência com uma chave repetida, para demonstrar a junção que multiplica linhas. Ela não acontece sozinha se as bases estiverem bem formadas.

Versão do script revisada em 15 nov. 2026. O que mudou em relação à versão usada pela turma de 2026.2:

- O comando `banco` grava como TEXT as colunas de identificador (nome com cnpj, cpf, codigo, cod_ ou id, ou valor com zero à esquerda), converte datas DD/MM/AAAA para AAAA-MM-DD, decide por coluna se o ponto é separador de milhar e informa, coluna por coluna, os valores descartados. Acentos saem do nome da coluna (Município vira municipio).
- O comando `sql` só aceita consulta que começa por SELECT ou WITH, abre o banco só para leitura e nega qualquer outra ação (CREATE, INSERT, REPLACE, ATTACH, PRAGMA).
- A numeração `consulta-N` usa o maior número já gravado mais um, e não sobrescreve arquivo.
- O comando `juntar` conta os registros sem par com NOT EXISTS, conta a chave vazia como sem par e imprime oito contagens. A mensagem final testa à parte a chave repetida e as linhas sem par, porque as duas podem se compensar e deixar a contagem igual com resultado errado. Só diz "juncao por chave unica" quando não há nenhuma das duas.
- O `registrar` cria três linhas e o `conferir` exige três consultas.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 7.1 | 50 min | 3 a 11 |
| Ciclo 7.2 | 45 min | 12 a 17 |
| Intervalo | 15 min | |
| Ciclo 7.3 | 60 min | 18 a 26 |
| Intervalo | 10 min | |
| Ciclo 7.4 | 45 min | 27 a 31 |
| Fechamento | 15 min | 32 a 35 |

## Ciclo 7.1. Da planilha à tabela

Teoria, 23 min. Planilha, tabela em arquivo CSV e banco relacional (slide 4, Codd, 1970), com CSV e chave estrangeira definidos no slide. Onde o administrador encontra um banco relacional (slide 5): ERP, sistemas estruturantes do governo federal, sistemas setoriais, as três formas de acesso e quem concede o acesso. Os quatro problemas que a planilha não resolve (slide 6), com transação definida. Tipo declarado e valor gravado (slide 7): as regras do script para identificador, data, número e valor descartado. Como ler uma consulta de contagem (slide 8): COUNT(*), COUNT(coluna) e COUNT(DISTINCT coluna) sobre uma tabela de cinco linhas, com o resultado de cada uma. Este slide vem antes da primeira consulta pedida ao aluno.

Demonstração, 7 min. O script criando o banco na projeção (slide 9), com as linhas de conversão e de valores descartados e a conferência de COUNT(custo) contra os vazios do perfil: 12.466 linhas menos 399 vazios menos 3 descartados dá 12.064.

Prática, 15 min. Cada aluno cria o banco com as próprias bases (slide 10). O slide traz o pedido ao agente, o resultado esperado e o que fazer quando o resultado for outro.

Entrega, 5 min. `entregas/modulo7-ciclo1-banco.md`.

A conferência de contagem contra o perfil do módulo 6 é obrigatória. Diferença sem explicação compromete o resto do encontro, e é melhor descobri-la agora.

Coluna de valor que o script tipou como TEXT indica valores fora do padrão numérico. Corrigir o CSV e recriar o banco leva poucos minutos. Valor descartado precisa de correção ou de explicação na entrega.

## Ciclo 7.2. Modelo relacional: entidades, chaves e relações

Teoria, 20 min. Entidade, atributo e relação, com o diagrama das tabelas usadas nas demonstrações (Chen, 1976) e cardinalidade definida. Chave primária e chave estrangeira, o agrupamento pelo nome que divide São Luís em quatro grupos e o CNPJ alfanumérico: a Receita Federal emite CNPJ com letras e números desde 31 jul. 2026 (IN RFB nº 2.229/2024), de forma gradual, e o CNPJ só numérico continua a ser emitido. Os dois tipos de relação usados nas práticas (1:N e N:N) e o efeito de cada um na contagem da junção. A relação 1:1 ficou só em uma linha de rodapé.

Prática, 20 min. Cada aluno modela as próprias tabelas e gera o diagrama em Mermaid, definido no slide 16.

Entrega, 5 min. `entregas/modulo7-ciclo2-modelo.md` e `saidas/modelo.md`.

Este ciclo não tem demonstração: a competência é escrever a relação nos dois sentidos, e isso se faz no papel antes de se fazer com ferramenta.

Retome o cruzamento que falhou no módulo 5. A causa era chave de texto, e o slide 14 explica por quê.

Aluno cujas bases não têm chave comum registra a ausência e segue. A tabela de correspondência montada à mão resolve a junção depois.

## Ciclo 7.3. Perguntas de negócio viram consultas a uma tabela

Teoria, 25 min. As palavras de uma consulta (slide 19): SUM, AVG, COUNT, AS, BETWEEN, IS NULL e DESC, cada uma com exemplo, e o motivo de a data ficar em AAAA-MM-DD. As cinco partes de uma consulta e a ordem em que o banco as executa (slide 20). Os três erros que produzem número errado plausível e o conceito de granularidade (Kimball e Ross, 2013). O acerto dos modelos ao escrever SQL no teste BIRD (slide 22): 80,04% para o melhor modelo único treinado (Gemini-SQL2, jun. 2026), contra 92,96% de especialistas humanos, conferido no ranking oficial em 15 nov. 2026. A taxa vale para os bancos do teste e não deve ser apresentada como taxa esperada em sala.

Demonstração, 10 min. A sequência completa: esquema, pedido ao agente com o significado das colunas, leitura da consulta, execução. O script mostra só as linhas do resultado, então a contagem antes e depois do filtro sai de duas consultas COUNT(*), sem e com o WHERE.

Prática, 20 min. Três perguntas respondidas com uma só tabela (slide 24) e o registro no formulário com o comando `conferir` (slide 25). A pergunta que cruza as duas bases fica para o ciclo 7.4, depois da junção.

Entrega, 5 min. `entregas/modulo7-consultas.csv`, `saidas/consulta-N.sql` e `entregas/modulo7-relatorio.md`.

Insista na leitura da consulta antes de executar. O aluno que não entende o filtro não pode aceitar o número.

O script recusa entrega sem a contagem antes e depois do filtro e com menos de três consultas.

## Ciclo 7.4. Junção de tabelas conferida pela contagem

Teoria, 12 min. Junção definida, com o exemplo de quatro linhas em que duas ficam sem par. A contagem esperada depois da junção e a causa quando ela é maior ou menor. A diferença entre a junção interna, que é a do comando `juntar`, e a junção à esquerda, que o aluno pode pedir pelo comando `sql`. UNION ALL e CROSS JOIN saíram do deck.

Demonstração, 8 min. A junção com a tabela de chave repetida que você preparou, com as oito contagens do script. A conta do slide 29: 12.466 menos 37 sem par dá 12.429, e 12.429 mais os 4.102 atendimentos de São Luís em dobro dá 16.531. As 6 linhas de chave vazia estão entre as 37 sem par.

Prática, 20 min. Cada aluno junta as próprias tabelas, explica as linhas sem par com uma consulta NOT EXISTS pedida ao agente e responde a pergunta que cruza as bases com a tabela juntada.

Entrega, 5 min. `entregas/modulo7-ciclo4-juncao.md`.

Se a junção aumentou a contagem, a chave não era única e qualquer soma sobre o resultado está inflada. O script informa quantas chaves se repetem, o que encurta a investigação. Contagem igual não basta: 2 linhas sem par e 1 chave repetida com 2 linhas se compensam. Por isso o slide 28 manda conferir sem par e chaves repetidas, e o script avisa a repetição mesmo com a contagem igual.

## O que sai deste encontro

Um banco com as duas bases tipadas, o modelo com chaves e relações, três consultas com SQL gravado e contagem conferida, e a junção validada com a resposta da pergunta que cruza as bases. Tudo compõe a entrega B1 do encontro 9.

## Avisos no fechamento

Escolher os três indicadores do painel entre as três consultas e a pergunta do ciclo 7.4, e anotar a razão da escolha.

Trazer um gráfico ruim de relatório, jornal ou apresentação, para ser reconstruído em sala.

A entrega B1 reúne os módulos 6, 7 e 8. Quem está atrasado precisa acertar esta semana, porque o painel se constrói sobre estas consultas.

## Não conferido

- A nota da Receita Federal sobre o CNPJ alfanumérico foi lida na reprodução da Agência Gov (jul. 2026). A página do programa no portal da Receita não foi aberta. O número da IN RFB nº 2.229/2024 foi conferido em fonte secundária.
- Os números do GPT-4 no BIRD (54,89 e 34,88) vêm de Li et al. (2023) e não foram reconferidos no ranking em 15 nov. 2026.
- Não foi testado se o opencode desktop mostra o desenho do bloco Mermaid. O slide 16 cita só o GitHub.
- Conferido em 15 nov. 2026: o módulo 8 já não cita cinco consultas, e o `b1` só confere a existência de `entregas/modulo7-consultas.csv`.
