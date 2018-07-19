def second_element(elem):
    return elem[1]

def activity_selection(meetings, n):
    if n <2:
        return n
    else:
        meetings = sorted(meetings, key=second_element)
        current_start_time = meetings[0][0]
        no_of_meetings = []
        # print(meetings)
        for i in range(n):
            # print("current_start_time={0}".format(current_start_time))
            meet = meetings[i]
            # print(meet)
            if meet[0] >= current_start_time:
                no_of_meetings.append(meet[2]+1)
                current_start_time = meet[1]
        return no_of_meetings



T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    S = [int(x) for x in input().strip().split(' ')]
    E = [int(x) for x in input().strip().split(' ')]
    SS = list(zip(S, E, list(range(n)) ))
    # print(SS)
    result = activity_selection(meetings=SS, n = n)
    print(" ".join(map(str,result)))