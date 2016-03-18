import requests
import random
import json

class Simulator:
	base_url = None
	keys = None

	def __init__(self, base_url):
		self.base_url = base_url
		r = requests.get(self.base_url + '/sections')
		self.keys = []
		for item in json.loads(r.text):
			self.keys.append(item['section'])

	def random_request(self, keys, req_type):
		r = requests.get(self.base_url + '/sections/' + str(random.choice(keys)) + req_type + str(random.randint(1,10)))
		return r.text

	def random_free(self):
		return self.random_request(self.keys, '/free/')

	def random_reserve(self):
		return self.random_request(self.keys, '/reserve/')

	def simulate(self):
		functions = [self.random_free, self.random_reserve]
		while True:
			print random.choice(functions)()
			

if __name__ == '__main__':
	sim = Simulator('http://localhost:5000')
	sim.simulate()