# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "{0} {1}".format(self.name, self.score)

    def comparator(a, b):
        if a.score - b.score == 0:
            if min(a.name, b.name) == a.name:
                return -1
            else:
                return 1
        else:
            return b.score - a.score


n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, cmp=Player.comparator)
for i in data:
    print i.name, i.score