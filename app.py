from calculo_geo import obter_geolocalizacao
import subprocess
import csv

#vetores iniciais com os dados padrão
culturas = ["milho", "soja"]  #culturas
figura_geometrica = "retangulo"  #forma geométrica
espacamento = 0.75  #espaçamento fixo entre fileiras (metros)
produto_milho = {
    "nome": "fosfato, potássio e nitrogênio",
    "quantidade_por_hectare": 100  # quantidade por hectare(kg)
}
produto_soja = {
    "nome": "fosfato, potássio",
    "quantidade_por_hectare": 60  # quantidade por hectare(kg)
}

producao_milho_m2 = 1.05  # Produção de milho por metro quadrado (kg/m²)
producao_soja_m2 = 0.30   # Produção de soja por metro quadrado (kg/m²)
preco_venda_milho_saca = 62.33  # Preço da saca de milho (60 kg)
preco_venda_soja_saca = 140.82  # Preço da saca de soja (60 kg)
preco_insumo_milho_saca = 14.25  # Preço de insumo gasto para cada saca de milho (60 kg)
preco_insumo_soja_saca = 10.25  # Preço de insumo gasto para cada saca de soja (60 kg)
preco_venda_milho_total = 0
preco_insumo_milho_total = 0
valor_liquido_milho = 0



#função para verificar se os dados foram inseridos antes de exibir
def dados_inseridos():
    global largura_terreno, comprimento_terreno
    #verifica se os dados essenciais foram inseridos (largura e comprimento)
    return largura_terreno is not None and comprimento_terreno is not None
    
# Função para chamar o script R que exibe informações meteorológicas
def chamar_script_r():
    # Chama o script R
    try:
        subprocess.run(['Rscript', 'weather_csv.R'], check=True)
        print("Dados de clima exibido com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script R: {e}")
        
# Função para chamar o script R para calculos estatísticos
def chamar_script_r1():
    # Chama o script R
    try:
        subprocess.run(['Rscript', 'statistics.R'], check=True)
        print("Dados estatísticos exibidos com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script R: {e}")        

def calcular_gasto_producao(area_total, proporcao_milho):
    proporcao_soja = 1 - proporcao_milho  # Complemento da proporção de soja
    preco_venda_milho_total = 0
    preco_insumo_milho_total = 0
    valor_liquido_milho = 0
    preco_venda_soja_total = 0
    preco_insumo_soja_total = 0
    valor_liquido_soja = 0

    # Área de plantio para cada cultura
    area_milho = area_total * proporcao_milho  # m2
    area_soja = area_total * proporcao_soja    # m2

    # Cálculo da produção
    producao_total_milho = area_milho * producao_milho_m2  #Kg
    producao_total_soja = area_soja * producao_soja_m2     #Kg

    # Cálculo do uso de insumos em quantidade
    insumo_milho = (area_milho / 10000) * produto_milho['quantidade_por_hectare']  # hectares Kg
    insumo_soja = (area_soja / 10000) * produto_soja['quantidade_por_hectare']     # hectares Kg
    #print(f"Debug-: quantidade de insumo_milho: {insumo_milho}, quantidade de insumo_soja: {insumo_soja}")
    #print(f"Debug-: Produção total de milho: {producao_total_milho}, Produção total de soja: {producao_total_soja}")

    # Verificar se a área de milho ou soja é válida (maior que 0)
    if producao_total_milho > 0:
        # Cálculo do preço de venda
        preco_venda_milho_total = (producao_total_milho / 60) * (preco_venda_milho_saca) # R$
        # Cálculo do preço de insumos
        preco_insumo_milho_total = (producao_total_milho / 60) * (preco_insumo_milho_saca) #R$
        #print 
        # Valor líquido (lucro) = preço de venda - preço de insumos
        valor_liquido_milho = preco_venda_milho_total - preco_insumo_milho_total #R$
    #else:
        #print(f"Produção de milho é zero ou inválida: {producao_total_milho}")

    if producao_total_soja > 0:
        # Cálculo do preço de venda
        preco_venda_soja_total = (producao_total_soja / 60) * preco_venda_soja_saca #R$
        # Cálculo do preço de insumos
        preco_insumo_soja_total = (producao_total_soja / 60) * preco_insumo_soja_saca # R$
        # Valor líquido (lucro) = preço de venda - preço de insumos
        valor_liquido_soja = preco_venda_soja_total - preco_insumo_soja_total #R$
    #else:
        #print(f"Produção de soja é zero ou inválida: {producao_total_soja}")

    #print(f"Debug: Preço de venda milho: {preco_venda_milho_total}, Preço de venda soja: {preco_venda_soja_total}")
    #print(f"Debug: Valor líquido milho: {valor_liquido_milho}, Valor líquido soja: {valor_liquido_soja}")

    # Retorna todos os valores calculados, incluindo os preços de venda e insumos
    valor_total_gastos = preco_insumo_milho_total +preco_insumo_soja_total
    valor_total_venda = preco_venda_milho_total + preco_venda_soja_total
    valor_lucro = valor_total_venda - valor_total_gastos
    return {
        'proporcao_milho': proporcao_milho * 100,
        'proporcao_soja': proporcao_soja * 100,
        'area_milho': area_milho,
        'area_soja': area_soja,
        'producao_total_milho': producao_total_milho,
        'producao_total_soja': producao_total_soja,
        'insumo_milho': insumo_milho,
        'insumo_soja': insumo_soja,
        'preco_venda_milho_total': preco_venda_milho_total,
        'preco_venda_soja_total': preco_venda_soja_total,
        'preco_insumo_milho_total': preco_insumo_milho_total,
        'preco_insumo_soja_total': preco_insumo_soja_total,
        'valor_liquido_milho': valor_liquido_milho,
        'valor_liquido_soja': valor_liquido_soja,
        'valor_total_gastos': valor_total_gastos,
        'valor_total_venda': valor_total_venda,
        'valor_lucro': valor_lucro
    }

def saida_dados():
    global culturas, figura_geometrica, largura_terreno, comprimento_terreno, latitude, longitude, espacamento, area_total, numero_de_fileiras, volume_por_fileira, volume_total

    # Verifica se os dados foram inseridos
    if not dados_inseridos():
        print("Erro: Nenhum dado foi inserido ainda. Por favor, insira os dados primeiro.")
        return
    
    # Calcula a área total do terreno
    area_total = largura_terreno * comprimento_terreno

    if espacamento > 0:
        numero_de_fileiras = largura_terreno / espacamento # quantidade de fileiras
        
        # Usar as proporções de milho e soja para calcular o volume por fileira baseado nos insumos
        area_milho = area_total * 0.5  # 50% da área para milho
        area_soja = area_total * 0.5   # 50% da área para soja
        
        # Cálculo de insumos por fileira para milho e soja
        area_por_fileira_milho = (area_milho / numero_de_fileiras)  # area por fileira para milho m2
        area_por_fileira_soja = (area_soja / numero_de_fileiras)    # area  por fileira para soja m2
        
        # Area total calculado com base nas proporções
        #area_total_milho = area_por_fileira_milho * numero_de_fileiras
        #area_total_soja = area_por_fileira_soja * numero_de_fileiras  
        
    else:
        numero_de_fileiras = None
        area_por_fileira_milho = None
        area_por_fileira_soja = None
        #area_total_milho = None
        #area_total_soja = None

    # Nome do arquivo CSV
    csv_filename = 'saida_dados.csv'

    while True:
        print("\nSaída de Dados:")
        print("1. Exibir dados")
        print("2. Exibir insumos para cada proporção de culturas (para cálculos estatísticos)")
        print("3. Gerar CSV com preço e valor líquido (é necessário para executar os programas R)")
        print("4. Voltar ao menu anterior")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Exibe os dados
            print(f"{'Culturas:':<60}{culturas}")
            print(f"{'Figura geométrica:':<60}{figura_geometrica}")
            print(f"{'Largura do terreno:':<60}{largura_terreno:.2f} m")
            print(f"{'Comprimento do terreno:':<60}{comprimento_terreno:.2f} m")
            print(f"{'Espaçamento entre fileiras:':<60}{espacamento:.2f} m")
            print(f"{'Área total:':<60}{area_total:.2f} m²")
            print(f"{'Produção de milho por metro quadrado:':<60}{producao_milho_m2} kg/m²")
            print(f"{'Produção de soja por metro quadrado:':<60}{producao_soja_m2} kg/m²")
            print(f"{'Preço da saca de milho (60 kg):':<60}R$ {preco_venda_milho_saca:.2f}")
            print(f"{'Preço da saca de soja (60 kg):':<60}R$ {preco_venda_soja_saca:.2f}")
            print(f"{'Preço de insumo gasto para cada saca de milho:':<60}R$ {preco_insumo_milho_saca:.2f}")
            print(f"{'Preço de insumo gasto para cada saca de soja:':<60}R$ {preco_insumo_soja_saca:.2f}")

            if espacamento > 0:
                print(f"{'Número de fileiras:':<60}{int(numero_de_fileiras)}")
                print(f"{'Área por fileira de milho:':<60}{area_por_fileira_milho:.2f} m²") #<<<
                print(f"{'Área por fileira de soja:':<60}{area_por_fileira_soja:.2f} m²")   #<<<<
                #print(f"{'Area total milho :':<60}{area_total_milho:.2f} m²")     #<<<
                #print(f"{'Area total soja :':<60}{area_total_soja:.2f} m²")       #<<<

            #exibe a geolocalização, se disponível
            if latitude and longitude:
                print(f"{'Latitude:':<60}{latitude}")
                print(f"{'Longitude:':<60}{longitude}")
            else:
                print(f"{'Geolocalização:':<60}Não disponível.")

        elif opcao == "2":
            for proporcao in range(0, 101, 10):
                #print('<<<calcular_gasto_producao>>>')
                resultado = calcular_gasto_producao(area_total,proporcao / 100)  # Chama a função calcular_gasto_producao
                print(f"Proporção milho: {proporcao:>6.2f}%, Proporção soja: {100 - proporcao:>6.2f}%\n"
      f"Quantidade de insumo_milho: {resultado['insumo_milho']:>6.2f} kg/ha, Quantidade de insumo_soja: {resultado['insumo_soja']:>6.2f} kg/ha")
                print(" ")
                
        elif opcao == "3":
            # Preenche a lista de dados para o CSV
            csv_data = []
            csv_data.append(['culturas', str(culturas)])
            csv_data.append(['figura geometrica', figura_geometrica])
            csv_data.append(['largura do terreno (m)', f"{largura_terreno:.2f}"])
            csv_data.append(['comprimento do terreno (m)', f"{comprimento_terreno:.2f}"])
            csv_data.append(['espacamento entre fileiras (m)', f"{espacamento:.2f}"])
            csv_data.append(['area total (m2)', f"{area_total:.2f}"])
            csv_data.append(['producao de milho por metro quadrado (kg/m2)', f"{producao_milho_m2:.2f}"])
            csv_data.append(['producao de soja por metro quadrado (kg/m2)', f"{producao_soja_m2:.2f}"])
            csv_data.append(['preco da saca de milho (60 kg)', f"R$ {preco_venda_milho_saca:.2f}"])
            csv_data.append(['preco da saca de soja (60 kg)', f"R$ {preco_venda_soja_saca:.2f}"])
            csv_data.append(['preco de insumo gasto para cada saca de milho', f"R$ {preco_insumo_milho_saca:.2f}"])
            csv_data.append(['preco de insumo gasto para cada saca de soja', f"R$ {preco_insumo_soja_saca:.2f}"])

            if latitude and longitude:
                csv_data.append(['latitude', latitude])
                csv_data.append(['longitude', longitude])
            else:
                csv_data.append(['geolocalizacao', 'nao disponivel'])        

            # Adicionar preços e valor líquido para cada proporção de milho e soja
            for proporcao in range(0, 101, 10):
                #print('<<<calcular_gasto_producao>>>')
                resultado = calcular_gasto_producao(area_total,proporcao / 100)  # Chama a função calcular_gasto_producao
                #print(f"quantidade de insumo_milho: resultado['insumo_milho'], quantidade de insumo_soja: resultado['insumo_soja']")
                #print(resultado)
                csv_data.append([
                    f'insumo milho (kg/ha): {resultado["insumo_milho"]:.2f}',
                    f'insumo soja (kg/ha): {resultado["insumo_soja"]:.2f}',
                    f'proporcao milho: {resultado["proporcao_milho"]:.2f}%',
                    f'proporcao soja: {resultado["proporcao_soja"]:.2f}%',
                    f'preco de venda milho (R$): {resultado["preco_venda_milho_total"]:.2f}',
                    f'preco de venda soja (R$): {resultado["preco_venda_soja_total"]:.2f}',
                    f'preco de insumos Milho (R$): {resultado["preco_insumo_milho_total"]:.2f}',
                    f'preco de insumos Soja (R$): {resultado["preco_insumo_soja_total"]:.2f}',
                    f'valor liquido milho (R$): {resultado["valor_liquido_milho"]:.2f}',
                    f'valor liquido soja (R$): {resultado["valor_liquido_soja"]:.2f}',
                    f'valor total gastos (R$): {resultado["valor_total_gastos"]:.2f}',
                    f'valor total venda (R$): {resultado["valor_total_venda"]:.2f}',
                    f'valor lucro (R$): {resultado["valor_lucro"]:.2f}',    
                    f'producao total milho (kg): {resultado["producao_total_milho"]:.2f}',
                    f'producao total soja (kg): {resultado["producao_total_soja"]:.2f}'
                ])
                #print(csv_data)
            # Gera o arquivo CSV com ";" como separador
            try:
                with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerows(csv_data)
                print(f"Arquivo CSV '{csv_filename}' gerado com sucesso!")
            except Exception as e:
                print(f"Erro ao gerar o arquivo CSV: {e}")

        elif opcao == "4":
            return  # Volta ao menu principal

        else:
            print("Opção inválida! Tente novamente.")


#função para entrada de dados sem permitir inputs vazios e com tratamento de erros
def entrada_dados():
    global culturas, figura_geometrica, largura_terreno, comprimento_terreno, latitude, longitude
    
    print("\nEntrada de Dados:")

    #verificação para largura do terreno: não pode ser 0 ou negativa
    while True:
        try:
            largura_terreno_input = input("Digite a largura do terreno em metros: ")
            largura_terreno = float(largura_terreno_input)  # Tenta converter para float
            if largura_terreno <= 0:
                print("A largura deve ser maior que 0. Digite novamente.")
                continue  #solicita nova entrada se a largura for inválida
            break  #sai do loop se a conversão for bem-sucedida e o valor for válido
        except ValueError:
            print("Dado inválido, digite novamente.")  #exibe a mensagem de erro e pede nova entrada

    #verificação para comprimento do terreno: não pode ser 0, negativa e deve ser maior que a largura
    while True:
        try:
            comprimento_terreno_input = input("Digite o comprimento do terreno em metros: ")
            comprimento_terreno = float(comprimento_terreno_input)  # Tenta converter para float
            if comprimento_terreno <= 0:
                print("O comprimento deve ser maior que 0. Digite novamente.")
                continue  #solicita uma nova entrada se o comprimento for inválido
            if comprimento_terreno <= largura_terreno:
                print("O comprimento deve ser maior que a largura (formato escolhido: retângulo). Digite novamente.")
                continue  #solicita uma nova entrada se o comprimento for menor ou igual à largura
            break  #sai do loop se a conversão for bem-sucedida e o valor for válido
        except ValueError:
            print("Dado inválido, digite novamente.")  #exibe a mensagem de erro e pede nova entrada

    #coleta os dados de endereço sem permitir inputs vazios
    while True:
        rua = input("Digite o nome da rua: ")
        if rua:
            break
        else:
            print("Dado inválido, digite novamente.")  #se o usuário deixar em branco, pede novamente

    while True:
        numero = input("Digite o número: ")
        if numero:
            break
        else:
            print("Dado inválido, digite novamente.")  #se o usuário deixar em branco, pede novamente

    while True:
        cidade = input("Digite a cidade: ")
        if cidade:
            break
        else:
            print("Dado inválido, digite novamente.")  #se o usuário deixar em branco, pede novamente

    while True:
        estado = input("Digite o estado (abreviado): ")
        if estado:
            break
        else:
            print("Dado inválido, digite novamente.")  #se o usuário deixar em branco, pede novamente

    #obtém as coordenadas geográficas com base no endereço
    latitude, longitude = obter_geolocalizacao(rua, numero, cidade, estado)

    #verifica se a geolocalização foi bem-sucedida
    if latitude is None or longitude is None:
        print("Não foi possível encontrar a geolocalização. Verifique o endereço.")
    else:
        print(f"Geolocalização obtida com sucesso! Latitude: {latitude}, Longitude: {longitude}")

    print("Dados inseridos com sucesso!")

#função para atualizar os dados
def atualizar_dados():
    global culturas, figura_geometrica, largura_terreno, comprimento_terreno, latitude, longitude, producao_milho_m2, producao_soja_m2, preco_venda_milho_saca, preco_venda_soja_saca, preco_insumo_milho_saca,preco_insumo_soja_saca 
    while True:  #laço para continuar exibindo o menu até que uma opção válida seja inserida
        print("\nAtualizar Dados:")
        
        #exibe as opções de dados que podem ser atualizados
        print("1.  Culturas")
        print("2.  Figura geométrica")
        print("3.  Largura do terreno")
        print("4.  Comprimento do terreno")
        print("5.  Atualizar endereço e geolocalização")
        print("6.  Atualizar a quantidade produzida de milho por m² (kg/m²)")
        print("7.  Atualizar a quantidade produzida de soja por m² (kg/m²)")
        print("8.  Atualizar o preço da saca de milho (60 kg)")
        print("9.  Atualizar o preço da saca de soja (60 kg)")
        print("10. Atualizar o preço de insumo gasto para cada saca de milho")
        print("11. Atualizar o preço de insumo gasto para cada saca de soja")
        print("12. Voltar ao menu anterior")        
        #o usuário escolhe qual dado deseja atualizar
        escolha = input("Escolha qual dado deseja atualizar (1-12): ")
        
        #verifica se o input foi inserido e chama a função correspondente
        if escolha == "1":
            novas_culturas = input("Digite as novas culturas (separadas por vírgula): ")
            if novas_culturas:
                culturas = novas_culturas.split(",")
        elif escolha == "2":
            nova_figura_geometrica = input("Digite a nova figura geométrica da área plantada: ")
            if nova_figura_geometrica:
                figura_geometrica = nova_figura_geometrica
        elif escolha == "3":
            nova_largura = input("Digite a nova largura do terreno em metros: ")
            if nova_largura:
                largura_terreno = float(nova_largura)
        elif escolha == "4":
            novo_comprimento = input("Digite o novo comprimento do terreno em metros: ")
            if novo_comprimento:
                comprimento_terreno = float(novo_comprimento)
        elif escolha == "5":
            #atualiza o endereço e obtém a nova geolocalização
            nova_rua = input("Digite o novo nome da rua: ")
            novo_numero = input("Digite o novo número: ")
            nova_cidade = input("Digite a nova cidade: ")
            novo_estado = input("Digite o novo estado: ")
            if nova_rua and novo_numero and nova_cidade and novo_estado:
                latitude, longitude = obter_geolocalizacao(nova_rua, novo_numero, nova_cidade, novo_estado)
                if latitude is None or longitude is None:
                    print("Não foi possível encontrar a geolocalização. Verifique o endereço.")
                else:
                    print(f"Nova geolocalização obtida! Latitude: {latitude}, Longitude: {longitude}")
        
        elif escolha == "6": 
            nova_producao_milho_m2 = input("Digite a nova produção de milho por metro quadrado (kg/m²): ")
            if nova_producao_milho_m2:
                producao_milho_m2 = nova_producao_milho_m2

        elif escolha == "7": 
            nova_producao_soja_m2 = input("Digite a nova produção de soja por metro quadrado (kg/m²): ")
            if nova_producao_soja_m2:
                producao_soja_m2 = nova_producao_soja_m2        

        elif escolha == "8": 
            nova_preco_venda_milho_saca = input("Digite o novo preço da saca de milho (60 kg): ")
            if nova_preco_venda_milho_saca:
                preco_venda_milho_saca = nova_preco_venda_milho_saca  
                
        elif escolha == "9": 
            nova_preco_venda_soja_saca = input("Digite o novo preço da saca de soja (60 kg): ")
            if nova_preco_venda_soja_saca:
                preco_venda_soja_saca = nova_preco_venda_soja_saca  

        elif escolha == "10": 
            nova_preco_insumo_milho_saca = input("Digite o novo preço de insumo gasto para cada saca de milho: ")
            if nova_preco_insumo_milho_saca:
                preco_insumo_milho_saca = nova_preco_insumo_milho_saca  

        elif escolha == "11": 
            nova_preco_insumo_soja_saca = input("Digite o novo preço de insumo gasto para cada saca de soja: ")
            if nova_preco_insumo_soja_saca:
                preco_insumo_soja_saca = nova_preco_insumo_soja_saca  
      
        elif escolha == "12":
            return  #volta ao menu principal
        else:
            print("Escolha inválida! Tente novamente.")
        
        print("Dados atualizados com sucesso!")


#função para deletar os dados
def deletar_dados():
    global culturas, figura_geometrica, largura_terreno, comprimento_terreno, espacamento, producao_milho_m2, producao_soja_m2, preco_venda_milho_saca, preco_venda_soja_saca, preco_insumo_milho_saca, preco_insumo_soja_saca
    print("\nDeletar Dados:")    
    #exibe as opções de dados que podem ser deletados
    print("1.  Culturas")
    print("2.  Figura geométrica")
    print("3.  Largura do terreno")
    print("4.  Comprimento do terreno")
    print("5.  Espaçamento")
    print("6.  Quantidade produzida de milho por m² (kg/m²)")
    print("7.  Quantidade produzida de soja por m² (kg/m²)")
    print("8.  Preço da saca de milho (60 kg)")
    print("9.  Preço da saca de soja (60 kg)")
    print("10. Preço de insumo gasto para cada saca de milho")
    print("11. Preço de insumo gasto para cada saca de soja")
    print("12. Voltar ao menu anterior")        
    #o usuário escolhe qual dado deseja atualizar
    escolha = input("Escolha qual dado deseja atualizar (1-12): ")
    
    #verifica e deleta o dado escolhido (zerando ou limpando a variável)
    if escolha == "1":
        if culturas:
            culturas = []
            print("Culturas deletadas com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em Culturas.")
    elif escolha == "2":
        if figura_geometrica:
            figura_geometrica = ""
            print("Figura geométrica deletada com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em Figura geométrica.")
    elif escolha == "3":
        if largura_terreno is not None and largura_terreno > 0:
            largura_terreno = 0
            print("Largura do terreno deletada com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em Largura do terreno.")
    elif escolha == "4":
        if comprimento_terreno is not None and comprimento_terreno > 0:
            comprimento_terreno = 0
            print("Comprimento do terreno deletado com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em Comprimento do terreno.")
    elif escolha == "5":
        if espacamento is not None and espacamento > 0:
            espacamento = 0.75  #ou redefinir para o valor padrão
            print("Espaçamento deletado com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em Espaçamento.")
    elif escolha == "6":
        if producao_milho_m2:
            producao_milho_m2 = "" 
            print("Produção de milho por metro quadrado deletada com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em produção de milho por metro quadrado.")
    elif escolha == "7":
        if producao_soja_m2:
            producao_soja_m2 = "" 
            print("Produção de soja por metro quadrado deletada com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em produção de soja por metro quadrado.")
    elif escolha == "8":
        if preco_venda_milho_saca:
            preco_venda_milho_saca = ""
            print("Preço da saca de milho (60 kg) deletada com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em preço da saca de milho (60 kg).")
    elif escolha == "9":
        if preco_venda_soja_saca:
            preco_venda_soja_saca = ""
            print("Preço da saca de soja (60 kg) deletada com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em preço da saca de soja (60 kg).")
    elif escolha == "10":
        if preco_insumo_milho_saca:
            preco_insumo_milho_saca = ""
            print("Preço de insumo gasto para cada saca de milho deletada com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em preço de insumo gasto para cada saca de milho.")
    elif escolha == "11":
        if preco_insumo_soja_saca:
            preco_insumo_soja_saca = ""
            print("Preço de insumo gasto para cada saca de soja deletada com sucesso!")
            print("Esse dado foi deletado. Vá para a opção 3 no menu principal para atualizar os dados.")
        else:
            print("Nenhum dado para deletar em preço de insumo gasto para cada saca de soja.")
            
    elif escolha == "12":
        return  #volta ao menu principal sem deletar nada
    else:
        print("Escolha inválida! Tente novamente.")

#função principal com o menu de opções
def menu():
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Entrada de Dados")
        print("2. Saída de Dados")
        print("3. Atualizar Dados")
        print("4. Deletar Dados")
        print("5. Executar Programa R para exibir informações meteorológicas")
        print("6. Executar Programa R para cálculos estatísticos")
        print("7. Sair do Programa")        
        #captura a escolha do usuário
        opcao = input("Escolha uma opção (1-7): ")
        
        #verifica se o usuário digitou uma opção válida e não deixou em branco
        if opcao == "1":
            entrada_dados()  #entrada de dados
        elif opcao == "2":
            saida_dados()  #exibe os dados e realiza cálculos
        elif opcao == "3":
            atualizar_dados()  #atualiza os dados existentes
        elif opcao == "4":
            deletar_dados()  #deleta os dados
        elif opcao == "5":
            if dados_inseridos():
                chamar_script_r()  # Chama o script R se os dados foram inseridos
            else:
                print("Erro: Realize todos os passos do menu 2 primeiro antes de executar o programa R.")
        elif opcao == "6":
            if dados_inseridos():
                chamar_script_r1()  # Chama o script R se os dados foram inseridos
            else:
                print("Erro: Realize todos os passos do menu 2 primeiro antes de executar o programa R.")

        elif opcao == "7":
            print("Saindo do programa...")
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida! Tente novamente.")
#variáveis globais para armazenar os dados
largura_terreno = None
comprimento_terreno = None
latitude = None
longitude = None

#executa o menu
menu()
