# Roteiro do módulo 2

Ambiente de trabalho digital. Encontro 3, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este é o encontro de que dependem todos os seguintes. Ao final dele todo aluno precisa sair com opencode desktop instalado, conta criada, pasta do projeto montada e repositório publicado. Quem não sair assim não acompanha os encontros seguintes.

## Antes da aula, obrigatoriamente

Teste de sanidade numa máquina do laboratório, com o técnico presente, cronometrando:

1. Verificar se o Python está instalado e se o opencode consegue executá-lo. Todos os scripts da disciplina dependem dele.
2. Baixar e instalar o opencode desktop (opencode.ai/download, Windows x64). Anote se o antivírus bloqueia e o que foi preciso fazer.
3. Conectar a conta do OpenCode Console e escolher um modelo gratuito. Anote o tempo, o nome com que o provedor aparece na tela de conexão (OpenCode Console, OpenCode pay-as-you-go ou OpenCode Zen) e se foi pedido cartão de crédito ou crédito pago. Em 15/11/2026, o endereço opencode.ai/docs/zen redireciona para opencode.ai/docs/console/models, e a página não usa mais o nome Zen. Ela manda adicionar dados de cobrança e créditos no site do Console, escolher no /connect o provedor OpenCode pay-as-you-go e não diz se os modelos gratuitos dispensam esse passo. O nome que aparece no opencode desktop não foi conferido na própria aplicação. O slide 29 orienta o aluno a parar e chamar o professor se aparecer pedido de cartão.
4. Baixar e instalar o GitHub Desktop. Criar conta, adicionar uma pasta, gravar, publicar e clonar o repositório numa segunda pasta (File, Clone repository).
5. Verificar se as máquinas são restauradas a cada uso. Se forem, providenciar imagem com os dois aplicativos ou combinar reinstalação no início da aula. O slide 45 ensina a clonar o repositório para recuperar a pasta.
6. Conferir em opencode.ai/docs/console/models a lista de modelos gratuitos, a política de dados e o local de hospedagem de cada um. O slide 27 reproduz a consulta de 15/11/2026: GLM-5.3-Flash Free, DeepSeek V4.1 Flash Free e MiniMax M3.1 Flash Free declaram retenção zero e sem treino. O LongCat 2.5 Free também declara retenção zero, mas é hospedado na China, e por isso o slide o classifica como "evitar". Os demais modelos ficam nos EUA e na União Europeia. Na linha dos modelos que podem usar os dados, o slide resume a página: Big Pickle, Iceman Free e MiMo-V2.6-Flash Free podem usar os dados para aprimorar o modelo, o Inkling 2 Small Free retém os dados para monitorar o desempenho e para treino, o Flint 40B Free guarda os dados por 30 dias e o Jev 1.13 Free não tem política própria. O LongCat 2.5 Free tem limite de 100 pedidos por dia, e a página não publica o limite dos demais. Se a lista mudou, ajuste os slides 11, 27 e 29.
7. Fazer dez pedidos seguidos de máquinas diferentes do laboratório e anotar se algum modelo bloqueia por excesso de pedidos da mesma rede. A documentação não publica o limite dos modelos gratuitos.
8. No GitHub Desktop, criar o repositório a partir de uma pasta já montada pelo script (File, Add local repository, link create a repository) e confirmar que o Initial commit inclui os arquivos existentes e não sobrescreve o README.

O tempo medido nesse teste decide se o ciclo 2.4 cabe nos 70 minutos previstos. Se passar de 25 minutos por máquina, reduza o ciclo 2.1 e transfira o tempo.

Providencie também: os endereços de download escritos na turma virtual, um monitor circulando pela sala e o usuário do professor para ser adicionado como colaborador no repositório. Se possível, peça à turma que crie a conta no GitHub antes da aula.

Os slides não trazem marcadores de tempo nem número de encontro. Os tempos por etapa ficam neste roteiro, que é material de preparação e não de consulta durante a aula.

## Material

Deck `slides/modulo2-ambiente-de-trabalho-digital.html` (51 slides), este roteiro e o arquivo `scripts/atividade_modulo2.py`, publicado na turma virtual antes da aula.

O deck foi refeito em setembro para uma turma sem contato anterior com o tema, revisado em 2 nov. 2026 (linguagem, esquemas e atualização das ferramentas) e revisado de novo em 15 nov. 2026 pela regra do slide autossuficiente: todo termo técnico é definido no slide em que aparece pela primeira vez, e cada prática traz o passo a passo, o texto do pedido ao agente, o resultado esperado e o que fazer quando o resultado for outro. O slide 2 define script, README, agente, AGENTS.md, repositório e A1, que aparecem na visão geral antes dos slides de conceito. Dois slides de vocabulário fecham o encontro, com vinte termos.

Nos slides de conceito, a definição está no topo, os quatro pontos abaixo a sustentam e a caixa dourada no pé traz uma analogia. Leia a definição primeiro. A analogia é apoio para quem não entendeu, e não substitui a definição. Peça à turma um exemplo próprio do conceito antes de avançar.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura, visão geral e combinado | 10 min | 1 a 3 |
| Ciclo 2.1 | 47 min | 4 a 13 |
| Ciclo 2.2 | 40 min | 14 a 22 |
| Intervalo | 15 min | |
| Ciclo 2.3 | 82 min | 23 a 36 |
| Intervalo | 10 min | |
| Ciclo 2.4 | 70 min | 37 a 45 |
| Fechamento e vocabulário | 15 min | 46 a 51 |

O slide 3 é o combinado de abertura: toda palavra técnica é definida no slide em que aparece pela primeira vez, ninguém precisa saber programar e a pergunta que parece óbvia deve ser feita. Leia os quatro pontos em voz alta. Numa turma que nunca viu o tema, esse minuto reduz a quantidade de gente que fica calada com dúvida.

Em relação à versão de 2 nov. 2026, o ciclo 2.2 perdeu 10 minutos e o ciclo 2.3 ganhou 10, porque o comando `criar` e o preenchimento do README passaram para o ciclo 2.3, depois da instalação do opencode. Na revisão seguinte de 15 nov. 2026, o ciclo 2.3 ganhou mais 5 minutos e um slide (o 30), para o conferir do módulo 1, e o ciclo 2.1 perdeu 5 minutos na teoria.

## Ciclo 2.1: Infraestrutura de TI, o que roda onde

Conceito, 12 min. O que é infraestrutura de TI, slide 5, com equipamento, programa, rede e dado. O slide define servidor, sistema operacional e cópia de segurança (backup). Depois a separação entre programa, arquivo e sistema, slide 6, em tabela com exemplos (SIGAA, SIAFI, SEI) e a definição de banco de dados.

Teoria, 13 min. Os três lugares onde um programa roda, slide 7, com diagrama da rede da organização e do data center do fornecedor, definido na tabela. O slide 8 define computação em nuvem com base em Mell e Grance (NIST SP 800-145, 2011) e define disponibilidade. O slide 9, novo, traz os modelos de serviço da mesma norma (IaaS, PaaS e SaaS), com o que o fornecedor entrega e o que a organização mantém, o acordo de nível de serviço (SLA) com a conta de 99,5% ao mês (3 horas e 36 minutos fora do ar) e a cópia de segurança no contrato. O slide 10 traz o custo total de propriedade com exemplo numérico ilustrativo (protocolo eletrônico de uma prefeitura, R$ 500 mil em cinco anos, dos quais R$ 150 mil, 30%, aparecem na proposta comercial). A frase que atribuía ao Gartner a difusão do conceito saiu em 15 nov. 2026: o glossário do Gartner não pôde ser aberto para conferência, e o slide ficou só com a definição.

Demonstração, 5 min. A própria ferramenta da disciplina submetida à pergunta, slide 11. O slide define modelo de linguagem, provedor e agente, porque a demonstração os usa antes do ciclo 2.3. O programa roda na máquina, o conteúdo lido pelo agente vai ao servidor do provedor, fora do Brasil (EUA e União Europeia, e China no caso do LongCat 2.5 Free, consulta em 15/11/2026), e o envio de dado pessoal ao exterior é transferência internacional (LGPD, art. 33, e Resolução CD/ANPD nº 19/2024).

Prática, 12 min. Cada aluno escolhe um sistema que usa e responde às perguntas do slide 12, sem o agente. O slide traz o resultado esperado e o que fazer quando a página do serviço não informa onde ele roda (escrever NÃO INFORMADO com a fonte consultada).

Entrega, 5 min. Ficha de infraestrutura, anotada no caderno e gravada em `entregas/` no ciclo 2.3, depois do comando `criar` (slide 13).

Este ciclo é o mais compressível do encontro. Se o teste de sanidade indicou instalação demorada, corte o slide 10, o do custo total, que não é pré-requisito de nada adiante. Os slides de conceito e o slide 9 não se cortam: sem eles, os ciclos seguintes usam termos sem definição.

## Ciclo 2.2: A pasta do projeto

Conceito, 8 min. Arquivo, pasta e caminho, slide 15, com a definição de raiz. O slide explica com precisão o problema do espaço e do acento: o Windows e o GitHub aceitam, mas num comando o espaço separa um item do outro e o nome precisa ir entre aspas, e o acento pode ser gravado de forma diferente em outro sistema. Escreva um caminho no quadro, dados/vendas-2025.csv, e peça que alguém leia em voz alta o que ele significa.

Teoria, 14 min. Conversa, pasta e repositório, slide 16, em tabela. A definição de reprodutibilidade foi corrigida: a resposta do modelo pode variar a cada pedido, e o que se reproduz é o que fica gravado (dado de entrada, pedido, script e arquivo de saída). A estrutura padrão, slide 17, em árvore: quatro pastas (dados, prompts, saidas, entregas), README.md, AGENTS.md e .gitignore, mais os arquivos LEIA-ME.md e .manter que o comando `criar` grava dentro das pastas. Texto puro e formato empacotado, slide 18: o .docx é um pacote ZIP de formato aberto (Office Open XML, ISO/IEC 29500), que não é texto legível. O termo "arquivo fechado" saiu. Os formatos, slide 19, em tabela, com o separador do CSV no Excel em português e a codificação UTF-8 (no Excel, Salvar como, CSV UTF-8).

Demonstração, 8 min. O professor executa `atividade_modulo2.py criar` na projeção. O slide 20 mostra a saída real do comando numa pasta vazia. Desde 15 nov. 2026 o script imprime os caminhos com barra normal (entregas/LEIA-ME.md) também no Windows, e o primeiro dos próximos passos que ele lista é mover os arquivos do módulo 1 e rodar o conferir do módulo 1.

Prática, 7 min. Cada aluno prepara a pasta, slide 21: cria a pasta com nome sem espaço e sem acento, salva o script na raiz, copia do módulo 1 as três fichas .md, o formulário `modulo1-mapa-de-tarefas.csv` e o script `atividade_modulo1.py` e anota o texto do README. O resultado esperado são seis arquivos na raiz. O mapa .md do módulo 1 ainda não existe: ele é gravado no ciclo 2.3. O comando `criar` não é pedido aqui, porque o opencode só é instalado no ciclo 2.3.

Entrega, 3 min. Pasta preparada, slide 22.

## Ciclo 2.3: opencode desktop, instalação e primeiro uso

Conceito, 12 min. O que é um modelo de linguagem, slide 24. A definição foi alinhada com o módulo 3: o modelo calcula a probabilidade de cada continuação e sorteia uma delas entre as mais prováveis, e por isso o mesmo pedido pode ter respostas diferentes. O slide usa o termo confabulação, com alucinação entre parênteses, como os módulos 5 e 6. Depois, o que é um agente, slide 25, com a diferença entre ser o carregador de informação e ser o revisor. As analogias do estagiário e do consultor ficam como apoio, depois da definição.

Teoria, 8 min. O que o opencode faz, slide 26, em fluxo (lê, grava, executa, você confere) com os modos build e plan. Os modelos gratuitos do OpenCode Console e a política de dados de cada um, slide 27, com a definição de cota e o que fazer quando o modelo parar (consulta de 15/11/2026).

Demonstração e instalação assistida, 22 min. O esquema da tela do opencode desktop, slide 28, e os seis passos do slide 29, com toda a turma acompanhando na própria máquina. O passo 4 manda escolher o OpenCode Console, definido no slide 11, e avisa que o nome na tela pode ser OpenCode pay-as-you-go ou OpenCode Zen, conforme a versão. O slide define x64 e registra que a documentação do Console pede dados de cobrança e não diz se os modelos gratuitos dispensam esse passo. Monitor circulando. Ninguém avança sozinho.

Prática de montagem, 15 min, em dois slides. Slide 30: o aluno pede ao agente o comando `criar`, pede que os arquivos `modulo1-*` da raiz (as três fichas e o formulário `modulo1-mapa-de-tarefas.csv`) sejam movidos para `entregas/`, pede "execute atividade_modulo1.py com o comando conferir" e escreve as seções 6 e 7 do mapa `entregas/modulo1-mapa-de-tarefas.md` que o script grava. É a etapa que o slide 34 do módulo 1 deixou para este encontro. O resultado esperado é CRIADO (11) e "Tarefas validas: 10 de 10 esperadas". Com lista de PROBLEMAS, o aluno corrige o .csv e roda de novo, porque o mapa só é gravado sem problema. As seções 6 e 7 são escritas depois do último conferir, porque cada execução regrava o mapa. Slide 31: o aluno preenche o README no Bloco de Notas (os quatro PREENCHER, incluindo ferramenta e modelo) e pede a gravação da ficha do ciclo 2.1. Sem o mapa, o pedido do slide 32, o teste de análise do slide 35 e o item 4 do conferir da A1 falham.

Primeira instrução, 5 min. O pedido do slide 32, que lê um arquivo da pasta e grava outro. Cada aluno faz na própria máquina, porque `saidas/resumo-mapa.md` entra na entrega do ciclo.

Conceito do AGENTS.md, slide 33, com as quatro seções na mesma ordem e com os mesmos títulos que o script procura.

Prática, 15 min, em dois slides. Slide 34: preencher o AGENTS.md, com exemplo ilustrativo preenchido. O script considera curta demais a seção com menos de 25 caracteres fora do comentário entre parênteses e só reconhece os títulos numerados originais. Slide 35: testar com três pedidos, cujos textos estão no slide (conceito, análise e redação), e registrar em `prompts/modulo2-testes-agents.md`.

Entrega, 5 min. AGENTS.md preenchido, três testes registrados, `saidas/resumo-mapa.md` e a pasta montada pelo `criar` com README preenchido, slide 36.

Se a cota do modelo falhar em parte da turma, os alunos afetados escrevem o AGENTS.md mesmo assim e fazem os três testes na aula seguinte. Registram na entrega o horário e a mensagem de erro, como orientam os slides 27 e 35. A instalação, a autenticação e o comando `criar` são o que não pode ficar pendente.

## Ciclo 2.4: GitHub Desktop e a entrega A1

Conceito, 10 min. O que é versionar, slide 38, começando pela pilha de relatorio-final-v3 que todo mundo tem. Depois o slide 39, em tabela, com git, GitHub Desktop, GitHub e repositório, que a turma costuma confundir na primeira semana: um é o programa, outro é a tela com botões, outro é o site e o último é a pasta com histórico.

Teoria, 10 min. Os quatro gestos, slide 40, em diagrama (pasta de trabalho, histórico local, GitHub) com os nomes em inglês porque é assim que estão nos botões. O slide define main e origin. O que nunca vai para o repositório, slide 41, em tabela com os padrões do .gitignore que o script grava, a definição de chave de API e de .env e o limite de 100 MB por arquivo do GitHub. Este slide passou para antes da criação do repositório: o Initial commit grava tudo o que estiver na pasta, e arquivo apagado depois continua no histórico.

Demonstração e execução assistida, 25 min. Os seis passos do slide 42, com a turma acompanhando. Este é o trecho em que o encontro trava ou não trava. Ao criar o repositório a partir da pasta, o GitHub Desktop grava sozinho a versão Initial commit. Insista em deixar desmarcado Initialize this repository with a README e Git ignore em None, porque o script já criou esses arquivos.

Conferência, 15 min. Cada aluno roda `atividade_modulo2.py conferir` e corrige o que o script apontar, slide 43. O script verifica nove itens e escreve `entregas/A1-relatorio.md`. Logo após o Initial commit e a publicação, a saída mostra 8 de 9, porque o item de duas versões gravadas exige um segundo commit. Cada execução reescreve o relatório, e por isso nome e matrícula são preenchidos depois da última execução, antes do commit com a mensagem entrega A1.

Entrega, 5 min. Endereço do repositório enviado na turma virtual, ainda em sala, slide 44.

Clone, 5 min. Slide 45, novo: como recuperar a pasta numa máquina restaurada ou em outro computador (File, Clone repository, aba GitHub.com, Local path, Clone). Mostre na projeção clonando o repositório de exemplo numa segunda pasta. Reforce que só volta o que foi enviado com Push origin.

Ordem de resolução quando alguém trava: primeiro o que impede publicar, depois o preenchimento de arquivos. Um aluno com AGENTS.md incompleto resolve em casa. Um aluno sem conta no GitHub não resolve.

## Os nove itens que o script confere

Estrutura de pastas, README preenchido, AGENTS.md com as quatro seções, os cinco arquivos do módulo 1 em `entregas/` (três fichas, o formulário .csv e o mapa .md), ficha do ciclo 2.1, .gitignore presente, pasta sob controle de versão, ao menos duas versões gravadas e repositório publicado.

O script lê o estado do repositório direto dos arquivos internos do git, sem depender do programa git. Desde 15 nov. 2026, a contagem de versões segue os commits a partir do HEAD, nos objetos soltos e nos pacotes da pasta .git. Por isso ela funciona também num repositório clonado, em que o registro local (.git/logs/HEAD) começa sem commits. Num clone raso (shallow), conta só as versões baixadas. O registro local continua como reserva, caso a leitura dos objetos falhe. Testado em 15 nov. 2026 com repositório fictício: 31 versões em objetos soltos, em pacote com deltas, em clone completo e sem o registro local, e 5 num clone raso de profundidade 5.

## O vocabulário do fim

Os slides 47 e 48 trazem os vinte termos do encontro com uma linha de definição em cada. Servem para o aluno fotografar e consultar durante o semestre. Reserve dois minutos, diga isso e siga.

Se algum termo gerar dúvida ali, o slide de conceito correspondente passou rápido demais. Anote qual foi e ajuste o ritmo no próximo semestre.

## Problemas conhecidos

Antivírus bloqueia o instalador. Não autorizar por conta própria: chamar o professor, que resolve com o técnico.

E-mail de confirmação não chega. Verificar spam, esperar cinco minutos, trocar de endereço e seguir.

Agente diz que não encontra o arquivo. Quase sempre a pasta aberta não é a do projeto.

GitHub Desktop não deixa publicar. Faltou autenticar, ou não há nenhuma versão gravada ainda.

Cota do modelo esgotada. Trocar para outro modelo da primeira linha do slide 27. Se persistir, registrar na entrega o horário e a mensagem e seguir com os passos que não dependem do modelo.

GitHub pede verificação em duas etapas. A exigência vale para contas selecionadas por atividade de contribuição, com 45 dias para ativar (docs.github.com, consulta em 02/11/2026). Orientar o uso de aplicativo autenticador e a guarda dos códigos de recuperação fora do repositório.

Máquina restaurada e pasta perdida. Clonar o repositório pelo slide 45. O que não foi publicado com Push origin não volta.

O slide 49 reúne estes problemas em tabela, com causa provável e providência.

## Depois da aula

Confira os repositórios recebidos antes do encontro 4 e identifique quem ficou pendente. Quem não publicou precisa resolver na semana, com atendimento fora de aula. Não deixe passar para o encontro 5: o módulo 3 já grava trabalho na pasta.
