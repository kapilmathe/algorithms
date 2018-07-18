import functools

def multiply3(n):
    variable_store = []
    def h(*args):
        for x in args:
            variable_store.append(x)

        if len(variable_store) >=n:
            val =1
            for x in variable_store[:n]:
                val *= x
            return val
        return h
    return h

multi = multiply3(3)
print(multi)
b = multi(4)
print(b)
c = b(3)
print(c)
d = c(2)
print(d)