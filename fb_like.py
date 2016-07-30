import fb
#import facebook
import json
from facepy import GraphAPI

token = 'EAAaReYTNsbQBAFPzZAolsUFGbkKDpUZBH5iWszmrvnkcGx236RMKy4yrLk2ZBlef1HN634N96EciaKZBIC48VuUaYFuBJj6KJF2ENDsgoaZCd9VocZBZCWuq23T7Kg1tS5iAfRhlfDlLFDULfFMivU2nVaZCipHuPDkZD'
facebook = fb.graph.api(token)
my_graph = GraphAPI(token)
query = "/me/feed"

feed = my_graph.get(query)
#idlist = [x['message'] for x in feed['data']]
message_list = []

for post in feed['data']:
	try:
		message = post['message']
		message_list.append(json.dumps(message))
	except:
		pass

print(message_list[0])

# post = graph.get_object(id='908875805800760')
# print(post['name'])
#100000350486230
