
# 
# Your previous Python 3 content is preserved below:
# 
# def say_hello():
#     pr('Hello, World')
# 
# for i in range(5):
#     say_hello()
# 
# 
# # 
# # Your previous Python 2 content is preserved below:
# # 
class myxrange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.stop = int(args[0])
            self.step = 1
        elif len(args) == 2:
            self.start, self.stop, self.step = args[0], args[1], 1
        elif len(args) == 3:
            self.start = int(args[0])
            self.stop  = int(args[1]),
            self.step = int(args[2])
        else:
            raise TypeError("not valid")
        print(self.start)
        start = self.start
        stop = self.stop
        step = self.step
        
        self.counter = 0
        self.start_value = self.start - self.step
        if start < stop:
            self.iteration = (stop - start) /step
            if (stop - start) %step:
                self.iteration += 1
        elif (self.start) > (self.stop) and (self.step) < 0:
            self.iteration = ((self.start) - (self.stop) ) /abs((self.step))
            if ((self.start) - (self.stop) ) %abs((self.step)):
                self.iteration += 1
        else:
            self.iteration = 0

    def __iter__(self):
        return self

    def next(self):
        self.counter += 1
        self.start_value += self.step
        if self.counter > self.iteration:
            raise StopIteration()
        return self.start_value


print(list(myxrange(0,10,1)))

