import json

data = json.load(open('connections.json'))

fling = list(data['following'].keys())
flers = list(data['followers'].keys())

unfs = list(set(fling)-set(flers))

with open("unfs.txt", "w") as fp:
	for item in unfs:
		fp.write(item)
		fp.write('\n')
	
