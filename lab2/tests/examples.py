# all primitives
number = 5
float_temp = 6.23
str_temp = "Mercedes"
bool_temp = True
bytes_temp = bytes(b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b')
bytes_arr_temp = bytearray(bytes_temp)
buitin_func_temp = dir

# lists(set, tuple, frozenset)
list_temp = ['one', 2, 'three']
set_temp = set(list_temp)
frozenset_temp = frozenset(list_temp)
tuple_temp = tuple(list_temp)

# dict
dict_temp = {'first': 1, 'second': 2}

class TempClass:
    def __init__(self):
        self.el1 = 't'
        self.el2 = 2


class ClassB:
    pass


# class that checked on inheritance
class ClassA(TempClass, ClassB):
    pass


# temp object
obj_temp = TempClass()


# global variable
age = 'NinetyFour'


# function with globals variable
def my_age_question():
    global age
    return 'How old is your Porsche? My Porsche is ' + age


test_age_answer = 'i love mercedes'


# temp function
def question_temp_func():
    return 'How old are you?'


test_question = 'Babadji or fortnait?'


# lambda function
multiple = lambda x, y: x * y
test_multiple = 10  # x = 2, y = 5


# function with parameters
def mul_params(first, second):
    return first * second
