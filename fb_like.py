import fb
import datetime
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

#the function checks if today is actually the user's birthday by checking today's date and the facebook provide birthday
def birthday_is_today():
	#this query gets the user's birthday
	birthday_query = "/me/?fields=birthday"
	#get the birthday JSON object from the graph API
	birthday_object = my_graph.get(birthday_query)
	#get the whole birthday string (mm/dd/yyyy) format
	birthday_string = birthday_object['birthday']
	#get the birthday month in integer format
	birthday_month = int(birthday_string.split('/')[0])
	#get the birthday year in integer format
	birthday_date = int(birthday_string.split('/')[1])
	#get today's date
	today_date = datetime.date.today()
	#return true iff today is birthday
	return birthday_month == int(today_date.month) and birthday_date == int(today_date.day)


if __name__ == '__main__':
	print(birthday_is_today())
    #automated_likes()
