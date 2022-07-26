import csv

with open('data.csv', newline='', encoding="utf-8") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

	for row in spamreader:
		print(row[0])
with open('data.csv', 'a', newline='', encoding="utf-8") as csvfile:


	spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['User'] + ['Following'])
	
	stop = 0
	a =0 
	stop2 = 0
	for data in users_ids:
		username = api.get_user(user_id =data)
		print(username.name)
		spamwriter.writerow([1]+[username.name])
		subUser_ids = api.get_friend_ids(user_id=username.id)
		stop = stop+1
		if stop == 20:
			stop =0
			break

		for users in subUser_ids:
			
			SUBusername = api.get_user(user_id =users)
			print(username.name, SUBusername.id)
			spamwriter.writerow([username.name]+[SUBusername.name])
			a= a+1;
			print("Numero de amigos:", a)

			stop2 = stop2+1
			if stop2 == 20:
				stop2 = 0
				break
				with open('data.csv', 'a', newline='', encoding="utf-8") as csvfile:


	spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['User'] + ['Following'])
	
	stop = 0
	a =0 
	stop2 = 0
	for data in users_ids:
		username = api.get_user(user_id =data)
		if a.contains(username.name):
			pass
		else:
			print(username.name)
			spamwriter.writerow([1]+[username.name])
			subUser_ids = api.get_friend_ids(user_id=username.id)
			stop = stop+1
			if stop == 20:
				stop =0
				break

			for users in subUser_ids:
				
				SUBusername = api.get_user(user_id =users)
				print(username.name, SUBusername.id)
				spamwriter.writerow([username.name]+[SUBusername.name])
				a= a+1;
				print("Numero de amigos:", a)

				stop2 = stop2+1
				if stop2 == 20:
					stop2 = 0
					break

