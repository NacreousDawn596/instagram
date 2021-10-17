import requests
	
r = requests.get('https://api.quotable.io/random', auth=('user', 'pass'))
	
quotes = r.json()
	
n = f"{quotes['content']} \n      -NacreousDawn596"

print(n)
