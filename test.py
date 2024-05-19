import json


with open('config.json','r',encoding='utf8') as f:
    data = json.load(f)


name = data['充当 Linux 终端']

print(name)

print(str(name).format('pwd'))


print(data.get('123'))