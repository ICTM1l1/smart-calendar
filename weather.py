import json
import urllib
import urllib3
import ipinfo
import datetime
import read_keys

endpoint = "api.weatherapi.com/v1/forecast.json?"
history = "api.weatherapi.com/v1/history.json?"

http = urllib3.PoolManager()
keys = read_keys.keys()

def get_ip_city():
	handler = ipinfo.getHandler()
	details = handler.getDetails()
	return details.city

def historic_p(d):
	now = datetime.date.today()
	if type(d) == datetime.datetime:
		return d.date() < now
	else:
		past = datetime.datetime.strptime(d, "%Y-%m-%d")
		return past.date() < now

def handle_forecast(f):
	if "error" in f.keys():
		if "30 days only" in f["error"]["message"]:
			return None
		else:
			return f["error"]["message"]
	else:
		return f['forecast']['forecastday'][0]['day']

# date is either a datetime object or a date string formatted as
# YYYY-mm-dd. it automatically detects if it historic data or not
# and returns it as such. some fields are missing when it is
# historic data, such as `condition` or `daily_chance_of_rain`
def request_forecast(key, location, date):
	params = urllib.parse.urlencode({'key': key, 'q': location, 'dt': date})
	url = None
	if historic_p(date):
		url = history + params
	else:
		url = endpoint + params
	print(url)
	data = http.request("GET", url)
	return handle_forecast(json.loads(data.data.decode("UTF-8")))

#forecast = request_forecast(keys.weatherapi, get_ip_city(), '2020-09-12')