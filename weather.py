import requests

class Forecast:
  def __init__(self, forecast_date, min_temp):
    self.forecast_date = forecast_date
    self.min_temp = min_temp


def get_forecast(url):
  resp = requests.get(url)

  data = resp.json()

  forecast = data.get('forecast')
  forecast_days = forecast.get('forecastday')

  forecast_data = []
  for fd in forecast_days:
    forecast_data.append(Forecast(fd['date'], fd['day']['mintemp_c']))

  return forecast_data

# f_data = get_forecast()
# for d in f_data:
#     print('On ' + d.date + ' min temperature is ' + str(d.min_temp))
#     print('-'*100)
  

