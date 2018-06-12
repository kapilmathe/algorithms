import urllib
from collections import deque
import heapq


def fetch_url(url):
    res_object = urllib.urlopen(url)
    return res_object.read()


def get_score(s):
    v = {'a', 'e', 'i', 'o', 'u'}
    score = 0
    for x in s:
        if v.__contains__(x):
            score += 1
    return score


def get_all_url_data(filename, max_len=10, threshold=1000000):
    file_object = open(filename)
    top_q = []
    min_score = 0
    cnt = 0
    for line in file_object:
        line = line.rstrip()
        cnt += 1
        s = fetch_url(line)
        score = get_score(s)
        record = (score, line, s)
        if cnt >= max_len:
            if score > min_score:
                top_q.append(record)
                min_record = top_q[0]
                top_q.remove(min_record)
                top_q.sort()
                min_score = top_q[0][0]
        else:
            top_q.append(record)
            top_q.sort()
            min_score = top_q[0][0]

        if cnt > threshold:
            break
        # print(record)
        # print("{0}=={1}=={2}".format(line,s,score))
    return top_q


# print(fetch_url(r'http://localhost:10043/?id=6'))
result = get_all_url_data('data/urls.txt', 10)
for rec in result:
    print(rec)
#
# 100000
# {'url': 'http://localhost:10043/?id=6743', 'score': 11, 'value': 'aminoacetophenetidine'}
# {'url': 'http://localhost:10043/?id=6744', 'score': 9, 'value': 'aminoacetophenone'}
# {'url': 'http://localhost:10043/?id=7916', 'score': 10, 'value': 'anatomicobiological'}
# {'url': 'http://localhost:10043/?id=7917', 'score': 9, 'value': 'anatomicochirurgical'}
# {'url': 'http://localhost:10043/?id=7919', 'score': 9, 'value': 'anatomicopathologic'}
# {'url': 'http://localhost:10043/?id=7920', 'score': 10, 'value': 'anatomicopathological'}
# {'url': 'http://localhost:10043/?id=7921', 'score': 9, 'value': 'anatomicophysiologic'}
# {'url': 'http://localhost:10043/?id=7922', 'score': 10, 'value': 'anatomicophysiological'}
# {'url': 'http://localhost:10043/?id=7930', 'score': 9, 'value': 'anatomopathological'}
# {'url': 'http://localhost:10043/?id=12169', 'score': 10, 'value': 'aquopentamminecobaltic'}
#
# 10000
# {'url': 'http://localhost:10043/?id=2381', 'score': 9, 'value': 'adenocarcinomatous'}
# {'url': 'http://localhost:10043/?id=6743', 'score': 11, 'value': 'aminoacetophenetidine'}
# {'url': 'http://localhost:10043/?id=6744', 'score': 9, 'value': 'aminoacetophenone'}
# {'url': 'http://localhost:10043/?id=7916', 'score': 10, 'value': 'anatomicobiological'}
# {'url': 'http://localhost:10043/?id=7917', 'score': 9, 'value': 'anatomicochirurgical'}
# {'url': 'http://localhost:10043/?id=7919', 'score': 9, 'value': 'anatomicopathologic'}
# {'url': 'http://localhost:10043/?id=7920', 'score': 10, 'value': 'anatomicopathological'}
# {'url': 'http://localhost:10043/?id=7921', 'score': 9, 'value': 'anatomicophysiologic'}
# {'url': 'http://localhost:10043/?id=7922', 'score': 10, 'value': 'anatomicophysiological'}
# {'url': 'http://localhost:10043/?id=7930', 'score': 9, 'value': 'anatomopathological'}
#
# 1000
# {'url': 'http://localhost:10043/?id=41', 'score': 7, 'value': 'abalienation'}
# {'url': 'http://localhost:10043/?id=59', 'score': 7, 'value': 'abarticulation'}
# {'url': 'http://localhost:10043/?id=141', 'score': 8, 'value': 'abdominoanterior'}
# {'url': 'http://localhost:10043/?id=142', 'score': 7, 'value': 'abdominocardiac'}
# {'url': 'http://localhost:10043/?id=143', 'score': 7, 'value': 'abdominocentesis'}
# {'url': 'http://localhost:10043/?id=144', 'score': 5, 'value': 'abdominocystic'}
# {'url': 'http://localhost:10043/?id=145', 'score': 7, 'value': 'abdominogenital'}
# {'url': 'http://localhost:10043/?id=146', 'score': 7, 'value': 'abdominohysterectomy'}
# {'url': 'http://localhost:10043/?id=147', 'score': 7, 'value': 'abdominohysterotomy'}
# {'url': 'http://localhost:10043/?id=148', 'score': 8, 'value': 'abdominoposterior'}

#
# (10, 'http://localhost:10043/?id=16096', 'autodifferentiation')
# (10, 'http://localhost:10043/?id=20922', 'benzofuroquinoxaline')
# (10, 'http://localhost:10043/?id=7916', 'anatomicobiological')
# (10, 'http://localhost:10043/?id=7920', 'anatomicopathological')
# (10, 'http://localhost:10043/?id=7922', 'anatomicophysiological')
# (11, 'http://localhost:10043/?id=137214', 'palaeometeorological')
# (11, 'http://localhost:10043/?id=142454', 'pericardiomediastinitis')
# (11, 'http://localhost:10043/?id=235538', 'zoologicoarchaeologist')
# (11, 'http://localhost:10043/?id=6743', 'aminoacetophenetidine')
#
# Process finished with exit code 0
# http://localhost:10043/?id=6743     aminoacetophenetidine                              11
# http://localhost:10043/?id=137214   palaeometeorological                               11
# http://localhost:10043/?id=142454   pericardiomediastinitis                            11
# http://localhost:10043/?id=235538   zoologicoarchaeologist                             11
# http://localhost:10043/?id=7916     anatomicobiological                                10
# http://localhost:10043/?id=7920     anatomicopathological                              10
# http://localhost:10043/?id=7922     anatomicophysiological                             10
# http://localhost:10043/?id=12169    aquopentamminecobaltic                             10
# http://localhost:10043/?id=15999    autobasidiomycetous                                10
# http://localhost:10043/?id=16087    autodepolymerization                               10
