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


c_obj = C()
c_obj.speak()
print(c_obj.label)