import configparser

from send_message import send_message
from weather import get_forecast

# Create a configuration object
config = configparser.ConfigParser()

def get_configuration(key):
    # Load the configuration file
    config.read('app_config.ini')

    # Get the value associated with the key from the configuration file
    return config['APP_CONFIG'].get(key)


def main():
  RECIPIENTS = get_configuration('recipients').split(',')
  WEATHER_API_KEY = get_configuration('weatherapi_key')
  FORECAST_REGION = get_configuration('forecast_region')
  FORECAST_DAYS = get_configuration('forecast_day_num')

  url = f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={FORECAST_REGION}&days={FORECAST_DAYS}'
  forecast = get_forecast(url)

  message_to_send = ''
  for f in forecast:
     message_to_send += 'On ' + f.forecast_date + ' min temperature is ' + str(f.min_temp) + '\n'
     
  
  if(len(message_to_send) > 0):
    print(message_to_send)
    for r in RECIPIENTS:
      send_message(r, message_to_send)

if __name__ == "__main__":
    main()