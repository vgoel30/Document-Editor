import fb
import json
from facepy import GraphAPI

token = 'EAAaReYTNsbQBAFPzZAolsUFGbkKDpUZBH5iWszmrvnkcGx236RMKy4yrLk2ZBlef1HN634N96EciaKZBIC48VuUaYFuBJj6KJF2ENDsgoaZCd9VocZBZCWuq23T7Kg1tS5iAfRhlfDlLFDULfFMivU2nVaZCipHuPDkZD'
facebook_access = fb.graph.api(token)
my_graph = GraphAPI(token)
query = "/me/feed"

feed = my_graph.get(query)
#idlist = [x['message'] for x in feed['data']]

#the list of all the messages (potential brithday wishes)
message_list = []
#filered posts will be identified by their id
id_list = []

for post in feed['data']:
	try:
		message = post['message']
		message_list.append(json.dumps(message))
		print(post['id'])
	except:
		pass

facebook_access.publish(cat = "likes", id = '1168324629855875_1168367846518220')
