import json

f = open('ingredients.json')
data = json.load(f)
f.close()
for i in range(len(data)):
    data[i] = {"model": "api.ingredient", "fields": data[i]}
print(data)
f = open('ingredients.json', "w")
json.dump(data, f, ensure_ascii=False)

f.close()
