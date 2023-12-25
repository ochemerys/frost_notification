import requests

def get_forecast(url):
  resp = requests.get(url)

  data = resp.json()

  forecast = data.get('forecast')
  forecast_days = forecast.get('forecastday')

  forecast_data = []
  for fd in forecast_days:
    forecast_data.append({'forecast_date': fd['date'], 'min_temp': fd['day']['mintemp_c']})

  return forecast_data

