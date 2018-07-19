#1------##############################
class MyClass:
    __instance = None

    class local_class:

        def __init__(self, val):
            self.data = val

        def function1(self):
            pass


    def __init__(self, val):
        if MyClass.__instance is None:
            MyClass.__instance = self.local_class(val)

        self.__dict__['MyClassObj'] = MyClass.__instance

#2------##############################
from abc import ABC

class Shape(ABC):

    def shape_definition(self):
        pass


class Square(Shape):
    def __init__(self, shape_params):
        self.params = shape_params

    def shape_definition(self):
        return "I am square"


class Rectangle(Shape):
    def __init__(self, shape_params):
        self.params = shape_params

    def shape_definition(self):
        return "I am Rectangle"


class Circle(Shape):
    def __init__(self, shape_params):
        self.params = shape_params

    def shape_definition(self):
        return "I am Circle"


class ShapeFactory:

    @staticmethod
    def get_shape(shape_type, shape_params):
        if shape_type == "Circle":
            return Circle(shape_params)
        if shape_type == "Rectangle":
            return Rectangle(shape_params)
        if shape_type == 'Square':
            return Square(shape_params)
        raise Exception("Invalid Shape Type: Please provide supported shape type")
    
a = ShapeFactory.get_shape('Square', 10)
print(a.shape_definition())

#3-----##############################
def lsde(strr):
    n = len(strr)
    i = 0
    max_start = 0
    end = 0
    curr = 0
    char_dict = {}
    while i < n:
        if char_dict.get(strr[i]):
            if ((i-1) - curr) >= (end - max_start):
                max_start = curr
                end = i-1
                curr = i
            i += 1
        else:
            char_dict[strr[i]] = True
            i += 1
    if ((i-1)-curr) > (max_start-end):
        max_start = curr
        end = i-1
    # print(max_start, end)
    return strr[max_start:end+1]

# strr = 'defaasdf'
strr = 'aaaaaaaa'
print(lsde(strr))

#4-----##############################
def astrisks(func):

    def inner_ast(*args, **kwargs):
        val = func(*args)
        print('*'*val,val,(val+len(str(val))) )
        return val
    return inner_ast

@astrisks
def sum(a, b):
    return a+b


sum(8, 6)