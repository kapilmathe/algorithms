import time


def sub_routine():
    while True:
        val = yield
        time.sleep(val)
        print("completed sub_routine for:{}".format(val))


def my_routine():
    sr = sub_routine()
    sr.__next__()
    while True:
        received = yield
        sr.send(received)


if __name__ == '__main__':
    pt = my_routine()
    pt.__next__()
    pt.send(4)
