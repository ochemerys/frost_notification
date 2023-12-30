import sys
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


def main(api_url, api_key, region, forecast_days):
  url = f'{api_url}?key={api_key}&q={region}&days={forecast_days}'
  fd = get_forecast(url)
  for dw in fd:
    print(dw)


if __name__ == '__main__':
  # for idx, arg in enumerate(sys.argv):
  #   print("Argument #{} is {}".format(idx, arg))
  # print ("No. of arguments passed is ", len(sys.argv))
  url = sys.argv[1]
  key = sys.argv[2]
  reg = sys.argv[3]
  days = sys.argv[4]
  main(url, key, reg, days)