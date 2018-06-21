def foo(x):
    x[2] = 12
    print(x)


x = {1:22}
print(x)
foo(x)
print(x)