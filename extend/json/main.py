import json


json_str = '{"name": "John","age": 30,"city": "New York","children": [{"name": "Jane","age": 10}]}'

json_obj = json.loads(json_str)
print(json_obj)

print(type(json_obj))
print(json_obj['name'])

print(type(json.dumps(json_obj)))
print(json.dumps(json_obj))

print(json.dumps(json_obj, indent=1))

arr = '[1,2,3,4,5]'

print(json.loads(arr))

dict_arr = '[{"a": 1}, {"b": 2}]'

print(json.loads(dict_arr))


