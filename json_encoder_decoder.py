"""
json_encoder_decoder.py

"""
import json
from json import JSONEncoder

person = {
    'name': 'Baragu',
    'age': 19,
    'country': 'Kenya',
    'Email': 'baraguantony@gmail.com',
    'occupation': 'student'
}

# serializing person dict to json object and placing it to a file 
with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)

# deserializing json object to python dict
with open('person.json', 'r') as f:
    person = json.load(f)
#    print(person)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

baragu = User('Baragu', 19)
print(baragu.__dict__)

# custom function to encode User object
def encode_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    raise TypeError('Object of type User is not JSON serializable')

# baragu_json = json.dumps(baragu, default=encode_user,indent=4)
#  print(baragu_json)

# overiding default function of json encoder class
class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)

# baragu_json = json.dumps(baragu, cls=UserEncoder, indent=4)
baragu_json = UserEncoder().encode(baragu)
print(baragu_json)

# function to decode json object
def decode(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

baragu_json_loads = json.loads(baragu_json, object_hook=decode)
print(type(baragu_json_loads))
