import requests

def get_forecast(url):
  forecast_data = []

  try:
    resp = requests.get(url)

    data = resp.json()

    forecast = data.get('forecast')
    forecast_days = forecast.get('forecastday')

    for fd in forecast_days:
      forecast_data.append({'forecast_date': fd['date'], 'min_temp': fd['day']['mintemp_c']})

  except Exception as e:
    print('ERROR:', e)

  return forecast_data

