from geopy.geocoders import Nominatim

def obter_geolocalizacao(rua, numero, cidade, estado):
    """
    Função para obter a geolocalização (latitude e longitude) a partir de um endereço fornecido.
    
    Parâmetros:
    rua (str): Nome da rua
    numero (str): Número do local
    cidade (str): Cidade do local
    estado (str): Estado do local
    
    Retorna:
    tuple: Retorna a latitude e longitude do endereço ou (None, None) se não encontrar.
    """
    #criar um objeto geolocator com um user_agent personalizado
    geolocator = Nominatim(user_agent="seu_app_exemplo")
    
    #juntar o endereço completo
    endereco_completo = f"{rua}, {numero}, {cidade}, {estado}"
    
    #geocodificar o endereço
    location = geolocator.geocode(endereco_completo)
    
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

