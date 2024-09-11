# Install the necessary packages (uncomment the lines bellow if you haven't installed them yet)
# install.packages("httr")
# install.packages("jsonlite")
# install.packages("dotenv")

library(httr)
library(jsonlite)
library(dotenv)

# weather_api: Main function to make requests to the OpenWeatherMap API
weather_api <- function(params) {
  # get function from namespace instead of possibly getting
  # implementation shipped with recent R versions:
  bp_URLencode = getFromNamespace("URLencode", "backports")

  # Set OpenWeatherMap API key from environment variable
  load_dot_env(file = ".env")
  api_key <- Sys.getenv("API_KEY")

  # Check if API key is defined
  if (api_key == "") {
    stop("Error: API key not found. Make sure it is defined in the .env file.")
  }

  # Set OpenWeatherMap API URL
  api_url <- "https://api.openweathermap.org/data/2.5/weather"

  # Encode URL parameters
  url <- bp_URLencode(paste0(api_url, "?", params, "&appid=", api_key, "&units=metric&lang=pt_br")) # nolint

  # Make API request
  data <- try(RETRY("GET", url, times = 3))

  # Check if request failed
  if (is(data, "try-error")) data <- list(status_code = 404)

  # Check if request was successful
  if (data$status_code != 200) {
    stop(paste0("Error: API request failed with status code ", data$status_code), call. = FALSE) # nolint
  }

  # Parse JSON to object
  result_obj <- fromJSON(content(data, "text", type = "application/json", encoding = "UTF-8"), simplifyVector = FALSE)

  # Parse JSON response to data frame
  result <- as.data.frame(result_obj)

  # Return result
  return(result)
}

# weather_geo: Function to make requests to the OpenWeatherMap API using geographic coordinates
weather_geo <- function(lat, lon) {
  # Set parameters to call weather_api
  params <- paste0("lat=", lat, "&lon=", lon)

  # Call weather_api
  result <- weather_api(params)

  # Return result
  return(result)
}

# weather_city: Function to make requests to the OpenWeatherMap API using city name
weather_city <- function(city) {
  # Set parameters to call weather_api
  params <- paste0("q=", city)

  # Call weather_api
  result <- weather_api(params)

  # Return result
  return(result)
}
