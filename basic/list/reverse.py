# 反转列表
def reverse_list_example():
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    reversed_list = list(reversed(my_list))
    print("Reversed list:", reversed_list)

# 反转字符串
def reverse_string_example():
    my_string = "Hello"
    print("Original string:", my_string)
    reversed_string = ''.join(reversed(my_string))
    print("Reversed string:", reversed_string)

# 反转元组
def reverse_tuple_example():
    my_tuple = (1, 2, 3, 4, 5)
    print("Original tuple:", my_tuple)
    reversed_tuple = tuple(reversed(my_tuple))
    print("Reversed tuple:", reversed_tuple)

# 运行示例
reverse_list_example()
reverse_string_example()
reverse_tuple_example()
