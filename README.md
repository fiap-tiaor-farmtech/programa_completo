## Pré Requisitos

- Python 3.x
- Biblioteca geopy

## Passo a passo

1. Baixar.
2. Certifique que todos os arquivos estão dentro do mesmo diretório: 
   `calculo_geo.py`, `app.py` e `requirements.txt`
3. Ir no prompt de comando ou em editor de código
4. Navegue até o diretório onde estão os programas 
5. Instalar a biblioteca geopy:
    ```sh
    pip install -r requirements.txt
    ```
6. Ou pode instalar direto a biblioteca:
   ```sh
    pip install pip install geopy
    ```
7. Executar o programa `app.py`
   ```sh
    python app.py
    ```
8. Vai aparecer a seguinte tela (aí é só explorar o programa!)
      ```sh
    --- Menu de Opções ---
    1. Entrada de Dados
    2. Saída de Dados
    3. Atualizar Dados
    4. Deletar Dados
    5. Sair do Programa
    Escolha uma opção (1-5): 
    ```
9. O programa `calculo_geo.py` utiliza a biblioteca geopy, especificamente a classe Nominatim, para realizar a geocodificação, ou seja, a conversão de um endereço (composto por rua, número, cidade e estado) em coordenadas geográficas (latitude e longitude)


