import json
import urllib
import urllib3
import ipinfo
import read_keys

endpoint = "api.weatherapi.com/v1/forecast.json?"
http = urllib3.PoolManager()

keys = read_keys.keys()

def get_ip_city():
	handler = ipinfo.getHandler()
	details = handler.getDetails()
	return details.city

def request_forecast(key, location, days):
	params = urllib.parse.urlencode({'key': key, 'q': location, 'days': days})
	url = endpoint + params
	data = http.request("GET", url)
	return json.loads(data.data.decode("UTF-8"))

forecast = request_forecast(keys.weatherapi, get_ip_city(), 7)