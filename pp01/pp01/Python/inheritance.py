class A:
    def __init__(self):
        self.label = "I am A"
        
    def speak(self):
        print("I am A")


class B:
    def __init__(self):
        self.label = "I am B"

    def speak(self):
        print("I am B")

class C(B,A):
    def __init__(self):
        self.label = "I am C"

#
# c_obj = C()
# c_obj.speak()
# print(c_obj.label)
#

class X(object):
    def __init__(self, a):
        self.num = a

    def doubleup(self):
        self.num *= 2


class Y(X):
    def __init__(self, a):
        X.__init__(self, a)

    def tripleup(self):
        self.num *= 3


obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)