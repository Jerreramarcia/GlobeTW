import tweepy
import csv
# assign the values accordingly
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
#AAAAAAAAAAAAAAAAAAAAAO6%2FWwEAAAAA%2BQFjRHFx3iue2PMNM%2FiCBmmqaEI%3D5Uu8b6uYfBKvdTuFmpExClu8eLvwWVpN3n237YVIMxBjc0qFpM

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

with open('data.csv','r', newline='', encoding="utf-8") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if row:
			doc = row[0]+".csv"
			with open(doc,'r', newline='', encoding="utf-8") as csvfile:
				spamreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')
				for row2 in spamreader2:
					a2.append(row2[0])

			
			with open(doc, 'a', newline='', encoding="utf-8") as csvfile:
				spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				subUser_ids = api.get_friend_ids(screen_name=row[0])
				for user in subUser_ids:
					try:
					
						userObject = api.get_user(user_id=user)
						userName = userObject.screen_name
						
						if userName in a2:
							pass
						else:
							spamwriter.writerow([userName]+[row[0]])
							print(row[0], userName)

					except Exception as e:
						pass