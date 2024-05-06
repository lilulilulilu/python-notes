
from collections import defaultdict

#################### 创建dict ####################
# 1.创建一个空dict，并往里面加入k-v对
mymap = {}
mymap['alice'] = 88
mymap['bob'] = 77

# 2.创建一个带有初始值的dict by Using the shorthand syntax
myMap2 = {"alice": 88, "bob": 77}

# 3.用dict comprehension创建dict
mymap3 = { i: 2*i for i in range(3)}

# 4.Using the `dict()` constructor
student_dict = dict([
    ("name", "John Doe"),
    ("age", 21),
    ("courses", ["Math", "Physics"])
])

# 5.Sequence of key-value pairs with dict() constructor
student_dict2 = dict(name="Jane Doe", age=22, courses=["Biology", "Chemistry"])

# 6.create a dict by combining two dicts
student_dict3 = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Physics"],
    "hobbies": ["Singing", "Dancing"]
}
student_dict_combined = dict(student_dict3, **student_dict2) # student_dict2 will overwrite student_dict3
# {'name': 'Jane Doe', 'age': 22, 'courses': ['Biology', 'Chemistry'], 'hobbies': ['Singing', 'Dancing']}

# 7.用zip构造dict
keys = ["a", "b", "c"]
values = [1, 2, 3]
zipped = zip(keys, values)
dict_from_zip = dict(zipped) # Result: {"a": 1, "b": 2, "c": 3}



################ dict作为入参 ################
params = {'x': 1, 'y': 2, 'z': 3}

#（1）用**params作为入参
def my_function(x, y):
    print("x:", x)
    print("y:", y)
    
#（2）用params里面的key名作为入参名
def my_function(**params):
    print(params)  # {'x': 1, 'y': 2, 'z': 3}   

# ‘**’初现在函数的入参中，说明params是dict类型；
# 实现my_function的时候(如上)：
# （1）可以用**params作为入参
# （2）也可以用params里面的key名作为入参名接收。    
my_function(**params)  




