def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers) #对numbers数组中每个元素作用square函数，返回一个新的数组

print(list(numbers))   # [1, 2, 3, 4, 5]
print(list(squared))   # [1, 4, 9, 16, 25]

####################
mp = {"a": 1, "b":2}
def my_print(**mp):
    print(mp) # {'a': 1, 'b': 2}
        
my_print(**mp)

####################
def my_function(x, y):
    print("x:", x)
    print("y:", y)

params = {'x': 1, 'y': 2, 'z': 3}
my_function(**params)  #看到‘#’初现在函数的入参中，说明params是dict类型，实现my_function的时候可以用**params入参接收，也可以用params里面的key名作为入参名接收。

#################### 创建dict
# Using the `dict()` constructor
student_dict = dict([
    ("name", "John Doe"),
    ("age", 21),
    ("courses", ["Math", "Physics"])
])

# Using the shorthand syntax
student_dict_short = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Physics"]
}

keys = ["a", "b", "c"]
values = [1, 2, 3]

zipped = zip(keys, values)
dict_from_zip = dict(zipped) # Result: {"a": 1, "b": 2, "c": 3}

# Sequence of key-value pairs
student_dict2 = dict(name="Jane Doe", age=22, courses=["Biology", "Chemistry"])
# Dictionary literal definition
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Physics"]
}
# From another dictionary
student_dict_combined = dict(student, **student_dict2)
