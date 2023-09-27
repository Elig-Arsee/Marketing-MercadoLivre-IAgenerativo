
# Explorando IA Generativa em um Pipeline de ETL com Python

Este repositório contém o projeto desenvolvido para o desafio *Explorando IA Generativa em um Pipeline de ETL com Python* do bootcamp Ciência de Dados com Python promovido pelo Santander Bootcamp 2023. O objetivo principal deste projeto é construir um processo de ETL utilizando todos os conceitos estudados durante o primeiro e o segundo módulo do bootcamp.

Este projeto demonstra um processo de ETL (Extração, Transformação e Load) para extrair dados de produtos em promoção no Mercado Livre, transformá-los e gerar mensagens personalizadas com a ajuda de IA generativa. As etapas do projeto incluem a extração de dados da web, a transformação desses dados para cálculos relevantes e a criação de mensagens de marketing personalizadas para os produtos com desconto.


## Descrição do Projeto
*1. Extração de Dados*: Nesta fase, os dados são extraídos da página de ofertas do Mercado Livre por meio de raspagem de dados. São coletadas informações sobre os produtos, como título, preço original, desconto e preço final.

*2. Transformação dos Dados*:
Após a extração, os dados são transformados para torná-los mais úteis. Isso inclui a seleção das colunas relevantes, o cálculo do desconto em reais e a preparação dos dados para a geração de mensagens personalizadas.

*3. Geração de Mensagens Personalizadas com IA Generativa*:
Nesta etapa, é aplicada uma IA generativa para criar mensagens de marketing personalizadas com base nos atributos dos produtos, desconto e preço final. A IA generativa gera mensagens persuasivas que incentivam os usuários a aproveitar as ofertas.

*4. Conversão para CSV*: 
Os dados transformados, incluindo as mensagens personalizadas, são convertidos em um arquivo CSV para facilitar o uso posterior e a distribuição.

## Objetivos Principais
- Demonstrar um processo de ETL completo, desde a extração até a transformação e o carregamento dos dados.
- Utilizar raspagem de dados para extrair informações de uma página da web.
- Aplicar IA generativa para criar mensagens de marketing personalizadas.
- Disponibilizar os dados transformados em um formato acessível para análises ou uso posterior.

## Estrutura do Repositório
- `script.py`: Este é o notebook Jupyter que contém o código Python completo do projeto. Você pode seguir as etapas e executar o código para entender o processo de ETL.

- `projeto_ETL_IA_generativa.csv`: Este arquivo CSV contém os dados transformados, incluindo as mensagens personalizadas geradas pela IA generativa.

-  `requirements.txt`: Este arquivo contém uma lista das bibliotecas Python utilizadas neste projeto, juntamente com suas versões correspondentes.

- `README` (este arquivo): Fornece uma visão geral do projeto, seus objetivos e como navegar pelo repositório.
## Como Instalar e Executar o Projeto

1. Clone este repositório:

`git clone https://github.com/seu-usuario/nome-do-repositorio.git`

2. Abra o arquivo Jupyter Notebook Script.ipynb para explorar o código e os resultados.

3. Certifique-se de ter as bibliotecas Python instaladas, o que pode ser feito com o seguinte comando:
`pip install -r requirements.txt`

4. Execute cada célula do notebook para seguir o processo ETL e gerar as mensagens personalizadas.

5. Os dados transformados serão armazenados em `projeto_ETL_IA_generativa.csv.`

##   _____________________________________________________________________________________________________
Este projeto é apenas um exemplo e pode ser adaptado para suas necessidades específicas. Sinta-se à vontade para substituir a função de IA generativa por uma implementação personalizada.

Para mais informações sobre a utilização e licenciamento da API OpenAI, consulte https://openai.com.


Lembre-se de substituir `"seu-usuario/nome-do-repositorio"` pela URL do seu repositório no GitHub e ajustar os detalhes conforme necessário. Este README fornece uma estrutura básica para documentar seu projeto e torná-lo acessível para outros desenvolvedores e usuários.
