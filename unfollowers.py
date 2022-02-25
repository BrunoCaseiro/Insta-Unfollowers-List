import json

ers = json.load(open('followers.json'))
ing = json.load(open('following.json'))

ersArr = []
unfs = []

for i in ers["relationships_followers"]:
	ersArr.append(i['string_list_data'][0]['value'])

for i in ing["relationships_following"]:
	if (i['string_list_data'][0]['value'] not in ersArr):
		unfs.append(i['string_list_data'][0]['value'])

unfsF = open("unfollowers.txt", "a")
for x in unfs:
	unfsF.write(x + "\n")

unfsF.close()
