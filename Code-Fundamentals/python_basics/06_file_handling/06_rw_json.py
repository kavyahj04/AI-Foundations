import json

data = {'name': 'Kavya', 'role': 'AI Engineer', 'years_exp': 3, 'active': True}
json_string = json.dumps(data)
print(json_string)
print(type(json_string))

# json.dumps() (dump-string) takes a Python dict and turns it into a JSON-formatted string. Notice True became lowercase true — JSON has its own spelling for booleans, and json.dumps() handles that conversion for you.

# json.loads() (load-string) does the reverse — JSON string back to a real Python dict, and true becomes Python's True again. This round-trip (dumps → loads) is exactly what happens when your code sends a request to an API (dict → JSON string, over the network) and gets a response back (JSON string → dict, so you can actually use it in Python).

# json.dump() — no s, writes directly to a file object
with open('config.json', 'w') as f:
    json.dump(data, f)
# Notice: json.dump(data, f) — you pass it the dict and the open file object, and it writes the JSON straight in. You don't call .write() yourself at all; json.dump() does that internally. with still handles opening and closing, exactly like before — JSON just replaces the manual .write() step.

# json.load() — no s, reads directly from a file object
with open('config.json', 'r') as f:
    data = json.load(f)

print(data)
print(data['name'])

