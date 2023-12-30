"""Retrieve weather forecast from API.
Usage:
  python3 weather.py <API URL> <"API KEY"> <FORECAST REGION> <FORECAST DAYS>
"""
import sys
import requests


def get_forecast(url):
  """ Fetch a list of weather forecast from json document returned by API URL.

    Arguments:
      url: The complete URL with query parameters of a UTF-8 json document.

    Returns:
      A list of dictionary items which contain the weather forecast per day
  """
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
  """Print each forecast per day from a json document from at API URL.

    Args:
      api_url: The URL of a UTF-8 weather forecast api
      api_key: The key of the weather api account 
      region: The forecast region (city name)
      forecast_days: number of days of the weather forecast (max 14 day)
  """
  url = f'{api_url}?key={api_key}&q={region}&days={forecast_days}'
  fd = get_forecast(url)
  for dw in fd:
    print(dw)


if __name__ == '__main__':
  url = sys.argv[1]
  key = sys.argv[2]
  reg = sys.argv[3]
  days = sys.argv[4]
  main(url, key, reg, days)