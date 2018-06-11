class stack:
    def __init__(self):
        self.data = []
        self.cnt = 0

    def push(self, val):
        self.data.append(val)
        self.cnt += 1

    def pop(self):
        a = self.data.pop()
        self.cnt -= 1
        return a

    def top(self):
        return self.data[self.cnt - 1]

    def isEmpty(self):
        return True if self.cnt == 0 else False

def max_rectangle_area(a):
    n = len(a)
    max_area = 0
    s = stack()
    i = 0
    while (i < n):
        print("a[i]={0}".format(a[i]))
        if (s.isEmpty() or a[s.top()] <= a[i]):
            s.push(i)
            i += 1
            print(s.data)
            print("--------")
        else:
            print(s.data)
            tp = s.top()
            s.pop()
            print("a[tp]={0}".format(a[tp]))
            print(s.data)
            print("--------")
            area_with_top = a[tp]* (i if s.isEmpty() else i - s.top() - 1)

            if max_area < area_with_top:
                max_area = area_with_top

    while s.isEmpty() == False:
        tp = s.top()
        s.pop()
        area_with_top = a[tp] * (i if s.isEmpty() else i - s.top() - 1)

        if max_area < area_with_top:
            max_area = area_with_top

    return max_area



a = [4,3,2,1,1,1]
n = len(a)
# print(n)
print(max_rectangle_area(a))