## Documentação da minha resolução do desafio de código da Intuitive Care

<br>

O diretório raíz deste repositório está dividido nesta estrutura de pastas:

- **Códigos Python:** Contém 2 códigos Python que usei no desafio;

- **Codigos-Java:** Contém 1 código Java que usei no desafio;
  
- **Códigos SQL:** Contém 3 códigos SQL que usei no desafio;

- **Vue-Interface:** Contém uma estrutura feita com Vue.Js

- **Outros_Arquivos:** Contém arquivos adicionais de extensão csv

### Como resolvi o desafio:

1. PRIMEIRA ETAPA: Criar um código Java ou Python que acesse esse site: [Atualização do Rol de Procedimentos - ANS](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos),faça download dos arquivos Anexo_I.pdf e Anexo_II.pdf e compacte-os em um ZIP ou WINRAR.Nessa etapa decidi usar Java com auxílio do gerenciador de dependências Gradle.O código que usei aqui está em **Codigos-Java** e se chama **WebScraper**.Essa classe acessa o site,faz download dos arquivos e os compacta em um ZIP.
   
<br>

2. SEGUNDA ETAPA: Criar um código Java ou Python que extraia dados de uma tabela presente no Anexo_I.pdf e use esses dados para criar uma planilha em formato csv com essas informações,substituindo as abreviações "OD" por "Seg. Odontológica" e "AMB" por "Seg. Ambulatorial".Após isso,o CSV é compactado em um ZIP denominado **Teste_Lucas_Gomes_Santana.zip** na pasta **Outros_Arquivos**.Decidi fazer o código para esta etapa em Python,pois é uma linguagem mais adequada para manipulação de dados.O nome do código que faz esse processo é **extract_dates.py** disponível no diretório **Códigos-Python**.

<br>

3. TERCIERA ETAPA: Baixar os arquivos dos últimos dois anos deste site: [https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/) | Baixar os Dados Cadastrais das Operadoras Ativas na ANS em formato CSV nesta página na web: [https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/) | Criar scripts SQL que criem queries para estruturar tabelas para as planilhas csv para estas planilhas CSV.Todos os códigos desse trecho do desafio estão na pasta **Codigos_SQL**.

<br>

4. Criar um servidor(API) com Python que interaja com uma interface Vue.O servidor Python irá interagir com os dados de uma planilha CSV que é extraída do ZIP **Teste_Lucas_Gomes_Santana.zip** e quando o usuário interage com o front-end(interface Vue) buscando por informações de procedimentos,o Vue interage com a API Python que pega as informações do CSV de acordo com que o usuário inseriu na barra de pesquisa.O código da API Python se chama **server.py** e da página Vue: **Interface.vue**.Também foi pedido para criar uma collecion para testes do servidor Python no Postman,o nome da collection é **Python Server Collection** e está no diretório raíz do repositório.

