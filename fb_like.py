import fb
import datetime
import json
from facepy import GraphAPI

#some constants that will be of use in the script

#the access token
token = #get access token from https://developers.facebook.com/tools/explorer
#connect to the facebook graph api 
facebook_access = fb.graph.api(token)
#get the graph 'object'
my_graph = GraphAPI(token)
#get today's date
today_date = datetime.date.today()
#a list of birthday keywords that will help filter birthday messages
birthday_keywords = ["happy","birthday", "bday", "b\'day", "wish","birth day",
 "bless", "blessings", "returns"]

#function that does a trivial check on a message to see if it is a birthday wish
def message_is_birthday_wish(message):
 	#get the lower case version of the message for easier checking for keywords
 	message = message.lower()
 	#go through all the keywords in the birthday keywords list
 	for keyword in birthday_keywords:
 		#if a keyword exists in the message, exit the function by returning true
 		if keyword in message:
 			return True
 	return False

#function to check if a post on facebook was made today
def post_was_posted_today(post):
	#From the API, get the date of posting of the post
    post_date_stamp = post['created_time'].split('T')[0]
    #get the numerical value of the date
    post_date = int(post_date_stamp.split('-')[2])
    #get the numerical value of the month
    post_month = int(post_date_stamp.split('-')[1])
    #return true iff the post date was today
    return post_date == int(today_date.day) and post_month == int(today_date.month)


#the function that will go through the posts and filter the birthday ones and like/comment on them
def automated_likes():    
    #this query will get you your feed from the  graph
    query = "/me/feed?limit=20"
    #this will get you your feed
    feed = my_graph.get(query)

    #the list of all the messages (potential brithday wishes)
    message_list = []
    #filered posts will be identified by their id 
    id_list = []
    #access the feed's data index to get all the posts
    for post in feed['data']:
    	#if the post wasn't posted today, we can be sure that the posts before it are obviously older. Exit the loop
    	if not post_was_posted_today(post):
    		break
    	#all posts might not have a message. This ensures that only posts with messages are taken
    	try:
    		#get the textual content of the post
    		message = post['message']
    		#check if it is a birthday wish
    		if(message_is_birthday_wish(message)):
    			message_list.append(json.dumps(message))
    			#append the post id to the list of post id's that are to be liked
    			id_list.append(post['id'])
    	except:
    		pass
    #see all the wishes 
    print(message_list) 
    #go through all the birthday posts and like them
    for birthday_message_id in id_list:
   		facebook_access.publish(cat="likes", id=birthday_message_id)

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
	#return true iff today is birthday
	#return True
	return birthday_month == int(today_date.month) and birthday_date == int(today_date.day)


if __name__ == '__main__':
	if birthday_is_today:
		print('Happy Birthday! Hope you are having a great day today!')
		try:
			automated_likes()
		except:
			print("Check your internet connection")
			pass
	else:
		print("No need to run the script if it isn't your birthday today")
