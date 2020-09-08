import json

class Keys:
	def __init__(self, weatherapi, weerlive):
		self.weatherapi = weatherapi
		self.weerlive = weerlive

def keys():
	with open("private.json") as f:
		data = json.load(f)
		return Keys(data["weatherapi"], data["weerlive"])