import config
from send_message import send_message
from weather import get_forecast

def execute():
  # print('_'*50)
  RECIPIENTS = config.get_configuration('recipients').split(',')
  WEATHER_API_KEY = config.get_configuration('weatherapi_key')
  FORECAST_REGION = config.get_configuration('forecast_region')
  FORECAST_DAYS = int(config.get_configuration('forecast_day_num'))
  NOTIFICATION_TEMP = float(config.get_configuration('notification_temp'))

  url = f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={FORECAST_REGION}&days={FORECAST_DAYS}'
  forecast = get_forecast(url)

  message_to_send = ''

  if len(forecast) > 0:
    for d in forecast:
      print(f"Forecast on {d['forecast_date']}: min temperature is {d['min_temp']}")
      if d['min_temp'] <= NOTIFICATION_TEMP:
        message_to_send += f"On {d['forecast_date']} min temperature is {d['min_temp']}\n"
  else:
    err_message = 'ERROR: Weather API failed to return forecast data'
    print(err_message)
    message_to_send = err_message
  
  print('-'*50)   

  if(len(message_to_send) > 0):
    for r in RECIPIENTS:
      send_message(r, message_to_send)

