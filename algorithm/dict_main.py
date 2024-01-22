def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers) #对numbers数组中每个元素作用square函数，返回一个新的数组

print(list(numbers))
print(list(squared))

####################
mp = {"a": 1, "b":2}
def my_print(**mp):
    print(mp) # {'a': 1, 'b': 2}
        
my_print(**mp)

####################
def my_function(x, y):
    print("x:", x)
    print("y:", y)

params = {'x': 1, 'y': 2}
my_function(**params)

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
