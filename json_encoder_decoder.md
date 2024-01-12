# json_encoder_decoder.md

---

- javascript object notation is a lightweight data format used for data exchange 
#### Encoding `json` (serialization)

- use `json.dumps`

```python
import json
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], indent=4 ))
```

-  Write custom encoding function for classes 
#### Decoding __`json`__ 
- use `json.loads`
```python
import json
person = {
"name": "Baragu",
"age": 19,
"city": "Rongai",
"titles": ["student", "developer"]
}

personjson = json.dumps(person, indent=4)
print(personjson)
print(type(personjson))
print(json.loads(personjson))
print(type(json.loads(personjson)))
```

```python
import json
from json import JSONEncoder
class user:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
baragu = user("baragu", 19)
def encode_user(obj):
# implementing a custom encoder
	if isinstance(obj, user):
		return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
	else:
		raise TypeError("object is not json serializable")
baragujson = json.dumps(baragu, default=encode_user)
print(baragujson)

class user_encoder(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, user):
			return {
			'name': obj.name,
			'age': obj.age,
			obj.__class__.__name__: True
			}
		return JSONEncoder.default(self, obj)
baragucustom = json.dumps(baragu, cls=user_encoder)
# baragucustom = user_encoder().encode(baragu)
print(baragucustom)

def decode__user(dct):
	if user.__name__ in dct:
		return user(name=dct['name'], age=dct['age'])
	return dct
User = json.loads(baragucustom)
print(type(User))
print(User)
print(User.name)
```
[json_encoder_decoder](json_encoder_decoder.py)
