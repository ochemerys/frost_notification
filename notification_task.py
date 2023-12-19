import config
from send_message import send_message
from weather import get_forecast

def execute():
  print('_'*50)
  RECIPIENTS = config.get_configuration('recipients').split(',')
  WEATHER_API_KEY = config.get_configuration('weatherapi_key')
  FORECAST_REGION = config.get_configuration('forecast_region')
  FORECAST_DAYS = config.get_configuration('forecast_day_num')

  url = f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={FORECAST_REGION}&days={FORECAST_DAYS}'
  forecast = get_forecast(url)

  message_to_send = ''
  for f in forecast:
    print('Message on ' + f.forecast_date)
    # if f.min_temp < 0:
    #   message_to_send += 'On ' + f.forecast_date + ' min temperature is ' + str(f.min_temp) + '\n'
     
  
  if(len(message_to_send) > 0):
    for r in RECIPIENTS:
      #print(message_to_send)
      send_message(r, message_to_send)

