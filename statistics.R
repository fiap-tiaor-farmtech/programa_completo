#install.packages("tidyr")

#ler o arquivo CSV ignorando as primeiras 14 linhas
file_data <- readLines("saida_dados.csv")[-(1:14)]

#função para limpar e extrair os valores das linhas do CSV
extract_values <- function(line) {
  #remover espaços e dividir a linha nos pares chave-valor
  parts <- unlist(strsplit(line, ";"))
  
  #função para converter valores para numérico, removendo quaisquer espaços extras
  clean_value <- function(value) {
    as.numeric(gsub("[^0-9.-]", "", value)) #remove tudo que não é número, ponto ou hífen
  }

  #extrair e limpar os valores desejados
  insumo_milho <- clean_value(sub(".*insumo milho \\(kg/ha\\):\\s*", "", parts[1]))
  insumo_soja <- clean_value(sub(".*insumo soja \\(kg/ha\\):\\s*", "", parts[2]))
  valor_gastos <- clean_value(sub(".*valor total gastos\\(R\\$\\):\\s*", "", parts[11]))
  valor_lucro <- clean_value(sub(".*valor lucro\\(R\\$\\):\\s*", "", parts[13]))
  producao_milho <- clean_value(sub(".*producao total milho \\(kg\\):\\s*", "", parts[14]))
  producao_soja <- clean_value(sub(".*producao total soja \\(kg\\):\\s*", "", parts[15]))
  
  #retornar um vetor com os valores
  return(c(insumo_milho, insumo_soja, valor_gastos, valor_lucro, producao_milho, producao_soja))
}

#aplicar a função para extrair os valores de cada linha do CSV
data_matrix <- do.call(rbind, lapply(file_data, extract_values))

#converter para um data frame com nomes de colunas
data <- as.data.frame(data_matrix)
names(data) <- c("insumo_milho", "insumo_soja", "valor_gastos", "valor_lucro", "producao_milho", "producao_soja")

#calcular a produção total somando milho e soja
data$producao_total <- data$producao_milho + data$producao_soja

#função para calcular estatísticas (mínimo, máximo, média e desvio padrão)
calc_stats <- function(values) {
  return(list(
    minimo = min(values, na.rm = TRUE),
    maximo = max(values, na.rm = TRUE),
    media = mean(values, na.rm = TRUE),
    desvio_padrao = sd(values, na.rm = TRUE)
  ))
}

#cálculos para insumo (gastos), lucro e produção total
gastos_stats <- calc_stats(data$valor_gastos)
lucro_stats <- calc_stats(data$valor_lucro)
producao_total_stats <- calc_stats(data$producao_total)

#exibir os resultados com cada item
cat("\n")
cat("Estatísticas de Gastos de Insumo (R$):\n")
cat("Mínimo:", gastos_stats$minimo, "\n")
cat("Máximo:", gastos_stats$maximo, "\n")
cat("Média:", gastos_stats$media, "\n")
cat("Desvio Padrão:", gastos_stats$desvio_padrao, "\n\n")

cat("Estatísticas de Lucro (R$):\n")
cat("Mínimo:", lucro_stats$minimo, "\n")
cat("Máximo:", lucro_stats$maximo, "\n")
cat("Média:", lucro_stats$media, "\n")
cat("Desvio Padrão:", lucro_stats$desvio_padrao, "\n\n")

cat("Estatísticas de Produção Total (Milho + Soja) (kg):\n")
cat("Mínimo:", producao_total_stats$minimo, "\n")
cat("Máximo:", producao_total_stats$maximo, "\n")
cat("Média:", producao_total_stats$media, "\n")
cat("Desvio Padrão:", producao_total_stats$desvio_padrao, "\n")
