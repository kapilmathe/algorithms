class SpecialStack:
    def __init__(self):
        self.data = []
        self.min_data = []
        self.size = 0

    def push(self, val):
        if self.size:
            if val < self.min_data[self.size-1]:
                self.min_data.append(val)
            else:
                self.min_data.append(self.min_data[self.size-1])
            self.data.append(val)
            self.size += 1
        else:
            self.data.append(val)
            self.min_data.append(val)
            self.size += 1


    def pop(self):
        val = None
        if self.size:
            self.min_data.pop()
            val = self.data.pop()
            self.size -= 1
        return val

    def min(self):
        if self.size:
            return self.min_data[self.size-1]
        else:
            return None

if __name__ == '__main__':
    st = SpecialStack()
    st.push(18)
    st.push(19)
    st.push(29)
    st.push(28)
    st.push(15)
    print st.min_data
    print st.data
    print(st.min())
    print(st.pop())
    print(st.min())



