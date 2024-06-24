import json
 
# Opening JSON file
f = open('data.json')
 
# returns JSON object as
# a dictionary
info = json.loads(f)
 
print(info)

# Iterating through the json
# list
for i in info['pageid']:
    print(i)
 
# Closing file
f.close()