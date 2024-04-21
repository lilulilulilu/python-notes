# 定义自定义异常
class CustomInputException(Exception):
    """
    属性:
        expression -- 发生错误的表达式
        message -- 解释错误的信息
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

# 使用自定义异常，用raise抛出异常
def test_input(test_data):
    if test_data < 0:
        raise CustomInputException(test_data, "输入必须是非负数")

try:
    test_input(-10)
except CustomInputException as e:
    print(f'Caught an error: {e.message} - Faulty expression: {e.expression}')
