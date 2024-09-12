## Pré Requisitos

- Python 3.x
- Biblioteca geopy
- R
- Pacote dplyr
- OpenWeatherMap API key

## Introdução
A **FarmTech Solutions** firmou um contrato com uma fazenda que investe em inovação e tecnologia para otimizar sua produtividade, com o objetivo de migrar para a Agricultura Digital. Para atender esse cliente estratégico, a FarmTech iniciará o desenvolvimento de uma aplicação em **Python** focada em análises agrícolas.

Selecionamos as culturas de **milho** e **soja** por diversas razões: são culturas altamente rentáveis, apresentam uma alta produção por metro quadrado, permitem múltiplas colheitas ao ano e não dependem tanto de variações climáticas extremas, como seca ou excesso de chuva.

A forma geométrica escolhida para representar as áreas de cultivo foi o **retângulo**, já que as plantações são organizadas em fileiras retas, facilitando o manejo, a irrigação e o uso de maquinário agrícola, como colheitadeiras e pulverizadores. O formato retangular maximiza o uso eficiente do espaço e facilita o tráfego de máquinas entre as fileiras.

Os insumos selecionados para as culturas foram:
- **Milho**: Fosfato, Potássio e Nitrogênio
- **Soja**: Fosfato e Potássio

Como ainda não estava claro quais cálculos seriam feitos no programa em **R**, decidimos, antes de começar o desenvolvimento em Python, estruturar os cálculos estatísticos a serem realizados. Assim, optamos por calcular os seguintes indicadores:

### Estatísticas calculadas:

1. **Gastos com Insumos (R$)**:
   - **Mínimo e Máximo**: Permitem identificar o intervalo de variação nos custos dos insumos, auxiliando na comparação entre cenários e otimização de recursos.
   - **Média**: Oferece uma visão geral dos gastos médios, útil para planejamento financeiro.
   - **Desvio Padrão**: Mede a variabilidade dos gastos, sendo importante para identificar consistência ou variações significativas de safra para safra.

2. **Lucro (R$)**:
   - **Mínimo e Máximo**: Essenciais para entender o retorno financeiro nas melhores e piores condições.
   - **Média**: Indica o lucro médio ao longo do tempo, ajudando na projeção de retornos sobre investimentos.
   - **Desvio Padrão**: Avalia a estabilidade dos lucros; um desvio padrão alto pode sinalizar riscos ou grandes variações nas condições de mercado.

3. **Produção Total (Milho + Soja) (kg)**:
   - **Mínimo e Máximo**: Mostram os extremos da produção, revelando os limites de capacidade das operações.
   - **Média**: Indica a produção média, útil para definir metas e prever volumes de vendas.
   - **Desvio Padrão**: Mede a variação da produção ao longo dos anos ou entre áreas, indicando consistência ou a influência de fatores externos como clima e pragas.

Essas estatísticas são fundamentais para uma análise detalhada dos custos, lucros e produção, permitindo decisões estratégicas mais acertadas, otimização de recursos e previsão de resultados futuros. Portanto, a aplicação dessas métricas é essencial para uma análise agrícola ou econômica robusta.

## Funcionalidades da aplicação em Python:
- Inclusão de dados como largura, comprimento e endereço do local, que serão usados para verificar as condições climáticas.
- Cálculo de área, número de fileiras, quantidade de insumos necessários, custos, valor líquido e bruto, além do gasto com insumos.
- Uso de dados fixos no código, como tipos de cultura, forma geométrica, quantidade de milho e soja produzida por metro quadrado, preços de saca (60 kg), e custo de insumos por saca. Esses valores podem ser posteriormente alterados no programa.
- Saída de dados detalhada com todas as informações (obrigatoriedade de gerar um arquivo **CSV**, que será usado pelos programas em R).
- Execução de programas R para verificar as condições climáticas do local e realizar os cálculos estatísticos.

### Passo a passo para executar os programas

1. Baixar todos os programas num diretório.
2. Certifique que todos os arquivos estão dentro do mesmo diretório: 
   `calculo_geo.py`, `app.py`, `requirements.txt`, `weather_csv.R`, `weather.R`, `statistics.R`e `.env`
3. Criar uma api key do OpenWeatherMap no site: https://openweathermap.org/api    
4. Editar o arquivo `.env`
    ```sh
    R_HOME=<caminho-de-instalação-do-R>
    API_KEY=<seu-openweathermap-api-key>
    ```
5. Ir no prompt de comando ou em editor de código
6. Navegue até o diretório onde estão os programas 
7. Instalar a biblioteca geopy:
    ```sh
    pip install -r requirements.txt
    ```
8. Ou pode instalar direto a biblioteca:
   ```sh
    pip install pip install geopy
    ```
9. Ir no R ou no RStudio
10. Instalar o pacote `dplyr`
```r
install.packages("dplyr")
```
10. O programa `calculo_geo.py` utiliza a biblioteca geopy, especificamente a classe Nominatim, para realizar a geocodificação, ou seja, a conversão de um endereço (composto por rua, número, cidade e estado) em coordenadas geográficas (latitude e longitude)

## Executar o programa Python
1. No cmd ou no editor de código
2. Executar:
   ```sh
    python app.py
    ```
3. Vai aparecer a seguinte tela
      ```sh
         --- Menu de Opções ---
         1. Entrada de Dados
         2. Saída de Dados
         3. Atualizar Dados
         4. Deletar Dados
         5. Executar Programa R para exibir informações meteorológicas
         6. Executar Programa R para cálculos estatísticos
         7. Sair do Programa
         Escolha uma opção (1-7):
    ```
4. Tem que fazer necessariamente todos os passos do menu 1 e 2, depois disso poderá alterar, deletar dados e eecutar o programa
5. No menu: 1. Entrada de dados:
   Vai aparecer esses inputs:
      ```sh
         Digite a largura do terreno em metros:
         Digite o comprimento do terreno em metros:
         Digite o nome da rua:
         Digite o número:
         Digite a cidade:
         Digite o estado (abreviado):
    ```
6. No menu: 2. Saída de Dados:
    Fazer todas as opções:
      ```sh      
         1. Exibir dados
         2. Exibir insumos para cada proporção de culturas (para cálculos estatísticos)
         3. Gerar CSV com preço e valor líquido (é necessário para executar os programas R)
         4. Voltar ao menu anterior
    ```
7. No menu: 3. Atualizar Dados:
      ```sh      
         1.  Culturas
         2.  Figura geométrica
         3.  Largura do terreno
         4.  Comprimento do terreno
         5.  Atualizar endereço e geolocalização
         6.  Atualizar a quantidade produzida de milho por m² (kg/m²)
         7.  Atualizar a quantidade produzida de soja por m² (kg/m²)
         8.  Atualizar o preço da saca de milho (60 kg)
         9.  Atualizar o preço da saca de soja (60 kg)
         10. Atualizar o preço de insumo gasto para cada saca de milho
         11. Atualizar o preço de insumo gasto para cada saca de soja
         12. Voltar ao menu anterior
    ```
8. No menu: 4. Deletar Dados:
      ```sh  
         1.  Culturas
         2.  Figura geométrica
         3.  Largura do terreno
         4.  Comprimento do terreno
         5.  Espaçamento
         6.  Quantidade produzida de milho por m² (kg/m²)
         7.  Quantidade produzida de soja por m² (kg/m²)
         8.  Preço da saca de milho (60 kg)
         9.  Preço da saca de soja (60 kg)
         10. Preço de insumo gasto para cada saca de milho
         11. Preço de insumo gasto para cada saca de soja
         12. Voltar ao menu anterior
   ```
9. No menu: 5. Executar Programa R para exibir informações meteorológicas:
    Vai aparecer esse print com as informações de clima da localização:
      ```sh 
         Previsão do tempo para :
         Descrição: 
         Temperatura:
         Sensação térmica:
         Umidade:
         Velocidade do vento:
         Dados de clima exibido com sucesso!
   ```
10. No menu: 6. Executar Programa R para cálculos estatísticos:
    ```sh
         Estatísticas de Gastos de Insumo (R$):
         Mínimo: 
         Máximo: 
         Média: 
         Desvio Padrão: 
         
         Estatísticas de Lucro (R$):
         Mínimo: 
         Máximo:
         Média:
         Desvio Padrão: 
         
         Estatísticas de Produção Total (Milho + Soja) (kg):
         Mínimo:
         Máximo: 
         Média:
         Desvio Padrão: 
         Dados estatísticos exibidos com sucesso!
    ```
