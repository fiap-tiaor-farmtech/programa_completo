## Pré Requisitos

- Python 3.x
- Biblioteca geopy
- R
- Pacote dplyr
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

## Motivos de cada cálculo:
1. Gastos de Insumo (R$):
Mínimo e Máximo: Ajuda a entender o intervalo de variação dos custos de insumo, permitindo identificar o custo mais baixo e mais alto registrado. Isso é crucial para comparar cenários e otimizar a alocação de recursos.
Média: Fornece uma visão geral do valor médio dos gastos ao longo do tempo ou de várias fazendas/produções, o que ajuda no planejamento financeiro.
Desvio Padrão: Indica a variabilidade dos gastos. Um desvio padrão alto sugere que os gastos variam muito de uma safra para outra ou de uma operação para outra, enquanto um desvio padrão baixo indica que os custos são relativamente consistentes.
2. Lucro (R$):
Mínimo e Máximo: Essencial para ver qual foi o menor e o maior retorno financeiro, o que ajuda a entender a lucratividade nas melhores e piores condições.
Média: Dá uma ideia do lucro típico, que pode ser usada para estimar o retorno esperado sobre o investimento ao longo de várias safras.
Desvio Padrão: Um desvio padrão alto no lucro sugere que os resultados financeiros são imprevisíveis, o que pode ser um sinal de risco elevado ou de uma variabilidade significativa nas condições de mercado, clima, etc.
3. Produção Total (Milho + Soja) (kg):
Mínimo e Máximo: Mostra os extremos de produção, revelando a capacidade mínima e máxima das operações.
Média: Dá uma ideia da produção média total, que pode ser útil para definir metas e prever o volume de vendas.
Desvio Padrão: Informa o quão variada é a produção entre os anos ou entre diferentes áreas, ajudando a identificar se a produção é consistente ou se há fatores externos que afetam muito os resultados (como clima, pragas, práticas de cultivo).
4. Conclusão:
Calcular essas estatísticas permite que você tenha uma visão abrangente da variação dos custos, lucros e produção, o que é fundamental para decisões estratégicas, otimização de recursos e previsão de resultados futuros. Portanto, esses cálculos fazem sentido para uma análise detalhada de seu processo agrícola ou econômico.
