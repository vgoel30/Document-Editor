import fb
#import facebook
import json
from facepy import GraphAPI

token = 'EAACEdEose0cBAOTRwwHR2BajvknZBtfLdMsjJ8TCzhTWZAUlKPCzE0JaZAOt7UTiQu3fZAaVu1lxUkOWd8l1UKpJ8wzyHaOPWkZAwJKX5yv6j1R7saSrGJGsPZBC2th2JzsVzyhehPdhPumRRw3IqSWyAHN7C0cq6roljZCLp7eaQZDZD'
facebook = fb.graph.api(token)
my_graph = GraphAPI(token)
query = "/me/feed"

feed = my_graph.get(query)
#idlist = [x['message'] for x in feed['data']]

for post in feed['data']:
	print(post['message'])

#print(idlist)

# post = graph.get_object(id='908875805800760')
# print(post['name'])
#100000350486230
