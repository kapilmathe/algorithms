from pprint import pprint
def array_left_rotation(a, n, k):
    kk = k%n
    b = a[kk:] + a[:kk]
    return b


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    ld = root.left.data
    rd = root.left.data
    d = root.data
    if ld > d:
        return False
    if rd < d:
        return False
    return True


def maximum_people(p, x, y, r):
    town_population = dict(zip(x,p))
    cloud_range = dict(zip(y,r))
    x.sort()
    y.sort()
    weight_cloud = {}
    town_dark = {}
    max_weight = 0
    for cloud in y:
        weight = 0;
        left, right = (cloud-cloud_range[cloud], cloud+cloud_range[cloud])
        for town in x:
            if town < left:
                continue
            if town > right:
                break
            if town >= left and town <= right:
                weight += town_population[town]
                town_dark[town] = True
        weight_cloud[cloud] = weight
        if max_weight < weight:
            max_weight = weight
    sunny_town_population = 0
    for town in x:
        if town_dark.get(town):
            sunny_town_population += 0
        else:
            sunny_town_population += town_population[town]
    result = sunny_town_population + max_weight
    return result


def RangeInclusive(left, right):
    return range(left,right+1)


def maximumPeople(p, x, y, r):
    location = []
    for c,r in zip(y,r):
        location += RangeInclusive(c-r, c+r)

    print(location)



def diagonal_save(pl):
    pos_map = {}
    neg_map = {}
    pos_pl_map = {}
    neg_pl_map = {}

    #postive gradient
    for coor in pl:
        x, y = coor
        c1 = y-x
        c2 = y+x
        pos_pl_exits = pos_map.get(c1)
        neg_pl_exits = neg_map.get(c2)
        if pos_pl_exits is not None:
            if len(pos_pl_exits) == 1:
                pos_pl_map[pos_pl_exits[0]] = c1
                pos_pl_exits.append(coor)
            pos_pl_map[coor] = c1
        else:
            temp = list()
            temp.append(coor)
            pos_map[c1] = temp

        if neg_pl_exits is not None:
            if len(neg_pl_exits) == 1:
                neg_pl_map[neg_pl_exits[0]] = c2
                neg_pl_exits.append(coor)
            neg_pl_map[coor] = c2
        else:
            temp = list()
            temp.append(coor)
            neg_map[c2] = temp

    pprint("postive")
    pprint(pos_map)
    pprint("pos_pl_map")
    pprint(pos_pl_map)


    pprint("negative")
    pprint(neg_map)
    pprint("neg_pl_map")
    pprint(neg_pl_map)
    pos_pl_map.update(neg_pl_map)
    print pos_pl_map
    return len(pos_pl_map)


if __name__ == "__main__":
    # pl = [(0,0), (1,1), (1,2), (2,1), (3,1), (4,1), (2,2)]
    pl = [(0,0), (1,1), (2,0)]
    result = diagonal_save(pl)
    print result