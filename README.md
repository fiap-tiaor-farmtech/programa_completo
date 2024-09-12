## Pré Requisitos

- Python 3.x
- Biblioteca geopy
- R
- rpy2 library
- OpenWeatherMap API key

## Passo a passo

1. Baixar todos os programas num diretório.
2. Certifique que todos os arquivos estão dentro do mesmo diretório: 
   `calculo_geo.py`, `app.py`, `requirements.txt`, `weather_csv.R`, `weather.R`, `statistics.R`e `.env`
3. Editar o arquivo `.env`
    ```sh
    R_HOME=<caminho-de-instalação-do-R>
    API_KEY=<seu-openweathermap-api-key>
    ```
4. Ir no prompt de comando ou em editor de código
5. Navegue até o diretório onde estão os programas 
6. Instalar a biblioteca geopy:
    ```sh
    pip install -r requirements.txt
    ```
7. Ou pode instalar direto a biblioteca:
   ```sh
    pip install pip install geopy
    ```
8. Ir no R ou no RStudio
9. Instalar o pacote `dplyr`
```r
install.packages("dplyr")
```

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
