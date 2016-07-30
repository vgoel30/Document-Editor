import fb
import json
from facepy import GraphAPI

#some constants that will be of use in the script
#the access token
token = 'EAACEdEose0cBAGOyshsApPUtONVwRU7CoYQADE9qZB0d6XkdVw7aCg98glpxuWWyxZBSYg88BIbMORJ1p6u3UJw1qCxRih6Fxxco13jFQxNovk7lfYK2Vb9d0kSPOcyAPLIhlA3IySGRGhCe983pPkO600ZBEM2k6xAGMZAqmgZDZD'
#connect to the facebook graph api 
facebook_access = fb.graph.api(token)
#get the graph 'object'
my_graph = GraphAPI(token)

#the function that will go through the posts and filter the birthday ones and like/comment on them
def automated_likes():    
    #this query will get you your feed from the  graph
    query = "/me/feed"
    #this will get you your feed
    feed = my_graph.get(query)

    #the list of all the messages (potential brithday wishes)
    message_list = []
    #filered posts will be identified by their id
    id_list = []
    #access the feed's data index to get all the posts
    for post in feed['data']:
    	#all posts might not have a message. This ensures that only posts with messages are taken
    	try:
    		#get the textual content of the post
    		message = post['message']
    		message_list.append(json.dumps(message))
    		id_list.append(post['id'])
    		print(post['id'])
    	except:
    		pass

    print(message_list)
    #testing the like functionality
    facebook_access.publish(cat="likes", id=id_list[0])

if __name__ == '__main__':
    automated_likes()
