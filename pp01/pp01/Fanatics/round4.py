# input
# l = [
# set(["Kobe Bryant", "Jordan Clarkson"]),
# set(["Julius Randle", "Jordan Clarkson"]),
# set(["Stephen Curry", "Shaun Livingston"]),
# set(["Andrew Bogut", "Jason Thompson"]) ,
# set(["Jason Thompson","Shaun Livingston"]),
# ]

#output
# set(["Stephen Curry", "Shaun Livingston", "Andrew Bogut", "Jason Thompson"])
# set(["Kobe Bryant", "Jordan Clarkson", "Julius Randle"])

def get_disjoint_set(list_of_set):
    curr_set = list_of_set[0]
    joined_set_list = []
    res =curr_set
    flag = False
    for i in range(1,len(list_of_set)):

            match_set = list_of_set[i]
            if not curr_set.isdisjoint(match_set):
                temp =curr_set.union(match_set)
                res = res.union(temp)
                flag =True
            else:
                joined_set_list.append(match_set)
    joined_set_list.append(res)
    if flag is False:
        return joined_set_list
    else:
        return get_disjoint_set(joined_set_list)



x = get_disjoint_set(l)
print(x)