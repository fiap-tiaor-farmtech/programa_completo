##instale os pacotes necessários (descomente as linhas abaixo se você ainda não os tiver instalados)
#install.packages("tidyr")

library(tidyr)

#carregar o arquivo "weather.R", que contém a função weather_geo()
source("weather.R")

file_data <- readLines("saida_dados.csv")

#extrair a latitude e longitude das linhas 13 e 14
latitude <- as.numeric(strsplit(file_data[13], ";")[[1]][2])
longitude <- as.numeric(strsplit(file_data[14], ";")[[1]][2])

#chamar a função weather_geo() para obter a previsão do tempo
#com as coordenadas extraídas
result <- weather_geo(latitude, longitude)

#extrair as informações relevantes da previsão do tempo
if (result$cod == 200) {
  cidade <- result$name
  pais <- result$sys.country
  descricao <- result$weather.description
  temperatura <- result$main.temp
  sensacao_termica <- result$main.feels_like
  umidade <- result$main.humidity
  vento <- result$wind.speed

#exibir a previsão do tempo no terminal
  cat("\n")
  cat("Previsão do tempo para", cidade, "-", pais, ":\n")
  cat("Descrição:", descricao, "\n")
  cat("Temperatura:", temperatura, "°C\n")
  cat("Sensação térmica:", sensacao_termica, "°C\n")
  cat("Umidade:", umidade, "%\n")
  cat("Velocidade do vento:", vento, "m/s\n")
} else {
  cat("Cidade não encontrada ou ocorreu um erro na requisição.\n")
}

q()
