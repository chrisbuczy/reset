import json

with open("data.json", "r") as f:
    data = json.load(f)

with open("data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=False)

#indent is just how you format it with a certain amount of indents
#sort keys puts the key sin alphabetical order
#sort keys and indent is not needed



