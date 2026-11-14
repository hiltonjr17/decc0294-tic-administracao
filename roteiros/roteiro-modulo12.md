# Roteiro do módulo 12

Governança de dados, LGPD e cibersegurança. Encontro 13, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Encontro do bloco da nota 3, sem entrega avaliada isolada. As quatro entregas daqui (varredura, inventário, seção de uso seguro com a pasta restrita no `.gitignore` e plano de resposta) entram na C1 do encontro 14. O exemplo `entregas/modulo12-ciclo3-exemplo.md` e o commit são conferidos na correção, porque o script não os verifica.

## Antes da aula

Material do professor: `slides/modulo12-governanca-lgpd-ciberseguranca.html`, este roteiro e `scripts/atividade_modulo12.py`.

Publicado na turma virtual, com uma semana de antecedência: o script, o texto vigente da Lei 13.709 (artigos 5, 6, 7, 11 e 48) e o pedido de que cada aluno levante quais dados pessoais passam pelas mãos dele no trabalho ou no estágio. Deixe explícito, por escrito, que ninguém deve trazer arquivo com dado pessoal de terceiro. A lista é de tipos e caminhos.

Rode `python atividade_modulo12.py varrer .` numa pasta de teste antes da aula. Monte a pasta com um arquivo que tenha CPF gerado por gerador de teste, e-mail e telefone, para a demonstração do ciclo 12.1. Não use dado real de ninguém, nem seu.

Confira que o script recusa o CPF com dígito inválido. Isso é o que evita a varredura acusar toda sequência de onze números, e vale mostrar na projeção.

Reconfira, dois dias antes, as informações datadas do deck: a página do OpenCode Zen (opencode.ai/docs/zen, seção Privacy) para o slide 17, a ficha do PL 2338/2023 na Câmara e os atos da ANPD para o slide 19. A consulta registrada no deck é de 14/11/2026.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 12.1 | 45 min | 3 a 8 |
| Ciclo 12.2 | 50 min | 9 a 15 |
| Intervalo | 15 min | |
| Ciclo 12.3 | 45 min | 16 a 22 |
| Intervalo | 10 min | |
| Ciclo 12.4 | 65 min | 23 a 29 |
| Fechamento | 10 min | 30 a 33 |

## Ciclo 12.1 · Que dado pessoal passa por você

Teoria, 15 min. Os seis termos do artigo 5º em tabela (dado pessoal, dado sensível, titular, controlador, operador e encarregado), com a definição de tratamento e da ANPD, ligados aos papéis de governança do módulo 5 (slide 4). Depois, a tabela das cópias que se formam fora do sistema oficial, com a definição de tabela de temporalidade (slide 5).

Demonstração, 10 min. A varredura na projeção, sobre a pasta de teste (slide 6).

Prática, 15 min. Cada aluno roda a varredura na própria pasta do projeto e começa o inventário (slide 7, com resultado esperado e o que fazer quando o resultado for outro).

Entrega, 5 min. `entregas/inventario-dados.csv` e `saidas/varredura-dados-pessoais.md` (slide 8).

O ponto do ciclo é que dado pessoal vai além do CPF. Peça à turma exemplos de combinação que identifica sem nome: cargo mais unidade mais ano de admissão costuma bastar em setor pequeno, e alguém sempre reconhece a situação.

A varredura encontrar zero é comum e precisa ser dito como resultado válido, junto com o limite: o script não lê PDF, imagem nem planilha binária, e não reconhece nome de pessoa. Quem interpretar zero como "está limpo" entendeu errado.

Vigie o inventário enquanto a turma escreve. Todo semestre alguém copia um CPF real "para ilustrar". O script recusa, mas é melhor interromper antes.

## Ciclo 12.2 · Base legal, finalidade e retenção

Teoria, 20 min. As dez bases do artigo 7º com os rótulos que o script aceita, o consentimento e o teste do legítimo interesse (slide 10). As bases do artigo 11 para dado sensível (slide 11): legítimo interesse e proteção ao crédito não têm correspondente, execução de contrato também não tem equivalente direto (a alínea d cobre o exercício regular de direitos, inclusive em contrato), e a alínea g acrescenta a prevenção à fraude na identificação e autenticação em cadastro eletrônico. O prazo de retenção no ciclo de vida do dado, com os artigos 15, 16, 18 e 19 (slide 12). As linhas que o script aceita e as que ele recusa (slide 13).

Prática, 25 min. Cada aluno completa o inventário com base legal, finalidade e prazo em cada linha (slide 14).

Entrega, 5 min. `entregas/inventario-dados.csv` (slide 15).

O erro previsível é marcar consentimento em tudo. Consentimento pressupõe que o titular pode dizer não sem prejuízo, e isso quase nunca é verdade entre servidor e chefia, ou entre cidadão e serviço do qual ele depende. Faça essa correção com um caso da própria turma.

A finalidade escrita como substantivo é o segundo erro. "Cadastro" não serve como finalidade, e "conceder o auxílio transporte" serve. O script recusa finalidade com menos de três palavras por isso.

O script agora confere a base da linha com `sensivel = sim`: recusa legítimo interesse, proteção ao crédito e execução de contrato, e aceita dois rótulos que só valem nessa linha, `prevencao a fraude` (art. 11, II, g) e `exercicio de direito em contrato` (art. 11, II, d). Os dois rótulos são recusados em linha de dado comum. Avise a turma antes da prática, porque o comando `inventario` lista os rótulos.

A coluna de eliminação por desnecessidade é a que gera a discussão mais útil. Peça que cada aluno diga em voz alta um campo que a organização coleta e não usa. Sempre aparece um.

## Ciclo 12.3 · IA e dado pessoal: o que não vai no prompt

Teoria, 25 min. Conta pessoal, contrato da organização e modelo local, comparados em treinamento, retenção, papel do provedor e transferência internacional, com a política dos modelos gratuitos do OpenCode Zen (slide 17). Pseudonimização e anonimização pelos artigos 5º, 12 e 13, com a base pseudonimizada, a tabela de correspondência e o k-anonimato reduzido a uma caixa (slide 18). A situação regulatória em novembro de 2026, com a Res. CD/ANPD nº 30/2025, a ANPD como agência, o ECA Digital e o Decreto nº 12.880/2026 e o PL 2338/2023 na Câmara (slide 19). O que o AGENTS.md e o `.gitignore` fazem e o que não fazem (slide 20).

Prática, 15 min. Cada aluno escreve a seção de uso seguro no AGENTS.md, cria a pasta restrita com um `teste.txt`, põe a pasta no `.gitignore` e monta um exemplo de tarefa com identificadores trocados (slide 21).

Entrega, 5 min. `AGENTS.md`, `.gitignore` e `entregas/modulo12-ciclo3-exemplo.md` (slide 22).

O slide 20 separa três proteções. A seção do AGENTS.md é instrução ao agente, e o modelo pode descumpri-la. O `.gitignore` impede que a pasta entre no commit e suba ao GitHub, mas não impede a leitura pelo agente e não retira arquivo que já entrou em commit anterior. Contra a leitura, a base com dado pessoal e a tabela de correspondência ficam fora da pasta do projeto (slides 18 e 20). A pasta `dados/restrito/` guarda só arquivo sem dado real, como o `teste.txt` da prática, e serve para a turma ver o `.gitignore` funcionar.

A conferência de que a pasta restrita não subiu é feita olhando a lista de arquivos do commit no GitHub Desktop, e não confiando na configuração. Pasta vazia não aparece no Git, por isso a prática manda gravar `dados/restrito/teste.txt`. Faça essa verificação na projeção uma vez, devagar.

O caso da tabela de correspondência guardada ao lado da base pseudonimizada (slide 18) merece dez segundos de silêncio depois de dito. É o erro mais comum e o que anula todo o resto.

Retome aqui a regra que a turma escreveu no encontro 4, no AGENTS.md. Este ciclo acrescenta uma seção ao arquivo existente.

## Ciclo 12.4 · Cibersegurança e resposta a incidente

Teoria, 30 min. Ataques que exploram pessoas (slide 24): engenharia social, phishing com o alerta da Receita Federal de abril de 2025, falsa central com o diagnóstico da ENCCLA 2025 e fraude com voz ou vídeo sintético com a operação da Polícia Civil de Goiás de novembro de 2026. Ataques a arquivos e a agentes (slide 25): ransomware com o caso do STJ de novembro de 2020 e injeção de instrução em agentes, com exemplo ilustrativo de edital com texto escondido. As quatro medidas com critério verificável, com a definição de gerenciador de senhas, aplicativo autenticador e chave de segurança física, e o caso C&M Software (slide 26). Depois, as primeiras duas horas, a apuração e os prazos da Resolução CD/ANPD nº 15/2024, com três dias úteis para comunicar a ANPD e os titulares, e o caso INSS (slide 27).

A injeção de instrução é o vetor mais próximo da turma, que usa um agente que lê arquivos desde o módulo 4. Não há caso brasileiro documentado em fonte primária até a consulta de 14/11/2026, por isso o slide usa exemplo ilustrativo e a definição do OWASP.

Prática, 30 min. Cada aluno escreve o plano de resposta, com o vetor de ataque no campo `vetor`, e roda a conferência final (slide 28).

Entrega, 5 min. `entregas/plano-resposta-incidente.md` (slide 29).

"Não apague nada antes de registrar" é a instrução que salva o caso. O primeiro impulso de quem envia a planilha errada é apagar a mensagem, e com ela vai o registro de para quem foi e o que continha.

A recusa do script a "a equipe de TI" como responsável é conteúdo. O script recusa responsável formado só por nome de unidade ou de grupo ("a equipe de TI", "o setor de tecnologia", "todos os servidores", "o servidor de plantão"), além de sigla de unidade em maiúsculas com até cinco letras ("o NTI", "a STI"), e aceita quando há um cargo ("coordenador de TI", "chefe do setor de TI", "diretor do NTI"). As siglas de cargo DPO, CISO, CIO, CTO, CEO, CFO e COO passam. Pergunte quem, nominalmente pelo cargo, faria a primeira ligação às duas da manhã de um sábado. Se ninguém souber responder, esse é o achado do plano.

Muitos alunos vão descobrir que a organização não tem encarregado designado. Registre isso no plano em vez de inventar um cargo.

## O que sai deste encontro

Um relatório de varredura com decisão escrita. Um inventário com base legal, finalidade e prazo por linha, com base do artigo 11 nas linhas de dado sensível. Uma seção de uso seguro no AGENTS.md, com pasta restrita fora do controle de versão. Um plano de resposta a incidente em uma página, com vetor de ataque e cargos responsáveis.

## Avisos no fechamento

O encontro 14 fecha a C1, que vale 40% da nota 3. Cada aluno precisa trazer um documento de decisão do próprio setor, com dez páginas ou mais e sem dado pessoal: edital, termo de referência, contrato, parecer ou devolutiva. Se o documento tiver dado pessoal, leva a versão publicada ou substitui os identificadores, aplicando o que foi feito hoje.

Peça também o critério de decisão escrito antes da aula, em três linhas. Ele vai ser comparado com o que o modelo propõe, e quem escrever durante a aula perde a comparação.

## Fontes do deck e situação da conferência

Conferido em fonte primária em 14/11/2026: Lei 13.709/2018 (arts. 5º, 7º, 11, 12, 13 e 48, planalto.gov.br), Lei 15.211/2025 e vigência em 17/03/2026 (planalto.gov.br), Lei 15.352/2026 (planalto.gov.br e camara.leg.br), Decreto 12.880, de 18/03/2026 (camara.leg.br), Res. CD/ANPD nº 15/2024 (bibliotecadigital.mj.gov.br), Res. CD/ANPD nº 30, de 23/12/2025 (gov.br/anpd e dspace.mj.gov.br), ficha do PL 2338/2023 na Câmara, caso INSS (gov.br/anpd, 01/02/2024), alerta da Receita Federal (23/04/2025), ENCCLA 2025, Ação 01 (gov.br/mj), operação Máquina de Fraudes (agencia.go.gov.br, 09/11/2026), comunicados do STJ de 04 e 06/11/2020, CERT.br (fascículo Golpes e página Ransomware), OWASP LLM01:2025, opencode.ai/docs/zen, Decreto 12.880/2026, art. 1º, parágrafo único (camara.leg.br, publicação original), NIST SP 800-63B-4, seção 3.2.9, autenticador restrito (pages.nist.gov/800-63-4), Res. CD/ANPD nº 2/2022, art. 2º, I, agente de pequeno porte (gov.br/anpd).

Não conferido em 14/11/2026, mantido da revisão de 2 nov.: termos da Anthropic para contas individuais (slide 17), no NIST SP 800-63B-4, o critério de 15 caracteres (slide 26), US-CERT (slide 26), caso C&M Software, que segue apoiado só em fontes jornalísticas (CNN Brasil e Baguete), e Sweeney (2002) no k-anonimato.

O Decreto 12.880/2026 atribui à ANPD a regulamentação e a fiscalização da Lei 15.211 (art. 1º, parágrafo único), conferido em 14/11/2026 e incluído na linha do tempo do slide 19.
