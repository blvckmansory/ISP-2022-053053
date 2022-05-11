from Serializer.json_serializer import serializer_json
import math

c = 42


def f(x):
    a = 123
    return math.sin(x * a * c)


js = serializer_json.JsonSerializer('json')

obj = serializer_json.JsonSerializer.dumps(js, f(10))
print(obj)

obj_ = serializer_json.JsonSerializer.loads(js, obj)
print(obj_)