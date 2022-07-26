import tweepy
import csv
# assign the values accordingly
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth, wait_on_rate_limit=True)

# the ID of the user
#id = 57741058
# fetching the user
#user = api.get_user(screen_name='jerreramarcia')
# fetching the followers_count
#followers_count = user.followers_count
#print("The number of followers of the user are : " + str(followers_count))

users_ids = api.get_follower_ids(screen_name='jerreramarcia');
a2 = []
a3 = []
with open('data.csv', newline='', encoding="utf-8") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		a2.append(row[0])
		a3.append(row[1])



zip_iterator = zip(a3, a2)

a_dictionary = dict(zip_iterator)

with open('data.csv', 'a', newline='', encoding="utf-8") as csvfile:


	spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['User'] + ['Following'])
	awsd = 0
	stop = 0
	a =0 
	stop2 = 0
	for data in users_ids:
		username = api.get_user(user_id =data)
		subUser_ids = api.get_friend_ids(user_id=username.id)
		if username.screen_name in a2:
			awsd = 1
		else:
			print(username.screen_name)
			spamwriter.writerow(["jerreramarcia"]+[username.screen_name])
			
		for users in subUser_ids:
			try:
				SUBusername = api.get_user(user_id =users)
				if (SUBusername.screen_name,username.screen_name) in a_dictionary.items():
					awsd = 1
				else:
					print(username.screen_name, SUBusername.screen_name)
					spamwriter.writerow([username.screen_name]+[SUBusername.screen_name])
					a= a+1;
					print("Numero de amigos:", a)
			except Exception as e:
				raise e				