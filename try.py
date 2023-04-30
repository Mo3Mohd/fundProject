import json
with open('data.json', 'r') as f:
    data = json.loads(f.read())

# Remove the object with title 'title_to_delete'
for obj in data:
    if obj['title'] == 'FirstProject':
        data.remove(obj)

# Write the updated Python object back to the JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)
