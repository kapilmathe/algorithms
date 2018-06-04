import math
actions = ['G', 'L', 'R']
directions = [(1,0), (-1,0), (0,1), (0,-1)]


def doesCircleExist(s, l):
    coordinates = [0,0]
    direction = (1,0)
    angle = 0
    for c in s:
        # print(c)
        if c == "G":
            # print("direction={0}".format(direction))
            coordinates = [coordinates[0]+direction[0], coordinates[1]+direction[1]]
            # print(coordinates)
        elif c == "L":
            angle = angle - 90
            direction = (int(math.cos(math.radians(angle))), int(math.sin(math.radians(angle))))
        elif c == "R":
            angle = angle + 90
            direction = (int(math.cos(math.radians(angle))), int(math.sin(math.radians(angle))))

    if coordinates == [0,0]:
        return 'YES'
    else:
        if angle%360 == 0:
            return "NO"
        elif angle%360 == 180:
            if coordinates[1] == 0:
                return 'YES'
            else:
                return 'NO'
        elif angle%360 in (270, 90):
            return "YES"


if __name__ == '__main__':
    n = int(raw_input().strip())
    result = []
    for i in range(n):
        s = list(raw_input().strip())
        l = len(s)
        result.append(doesCircleExist(s, l))
    for r in result:
        print(r)
