from datetime import datetime, timedelta
from collections import deque


from collections import deque
import time

def RateLimiter(fun, maxRate=5, timeUnit=1):
    timeUnit = timeUnit
    d = deque(maxlen=maxRate)

    def limit(*args,**kw):
        print(d)
        if d.maxlen == len(d):
            cTime = time.time()
            if cTime - d[0] > timeUnit:
                d.append(cTime)
                return fun()
            else:
                return "blocked"
        # print maxRate, timeUnit
        d.append(time.time())
        return fun()
    return limit

@RateLimiter
def test():
    return "kapil"

# for i in range(10):
#     time.sleep(.1)
#     print test()



def throtle(func, time_limit = 4):
    tl = time_limit
    last_exec = deque(maxlen=1)
    def inner(*args, **kwargs):
        ct = datetime.now()
        if len(last_exec) == 0:
            print(last_exec)
            last_exec.append(datetime.now())
            print(last_exec)
            return func(*args, **kwargs)
        else:
            lx = last_exec[0]
            td = (ct - lx).seconds
            # print(lx)
            # print(ct)
            print(td, tl)
            if td <= tl:
                print("Can't run it")
            else:
                last_exec.append(datetime.now())
                return  func(*args, **kwargs)
    return inner

@throtle
def foo():
    print("kapil")


for i in range(10):
    time.sleep(1)
    foo()


# foo2 = throtle(foo, time_limit=5)
# foo2()
