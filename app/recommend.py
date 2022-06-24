import itertools
# import pandas as pd
from itertools import combinations
# from collections import Counter
import json
from os.path import dirname, join



# csv_data = pd.read_csv("course_list.csv")
# data = []
    
# for i, row in csv_data.iterrows():
#     single = []
#     single.append("T" + str((i+1)))
#     single.append(list(row))
#     data.append(single)


# with open('data_text.txt', 'w') as testfile:
#     for row in data:
#         testfile.write(' '.join(str(a) for a in row) + '\n')

# init = []
# expected_subjects = ['Parallel Algorithms','Natural Language Processing','Professional Ethics in Engineering','Green Computing','Information Retrieval Techniques']
# for i in data:
#     for q in i[1]:
#         if(q not in init):
#             init.append(q)
# init = sorted(init)
# sp = 0.4
# s = int(sp*len(init))

# c = Counter()
# for i in init:
#     for d in data:
#         if(i in d[1]):
#             c[i]+=1
# l = Counter()
# for i in c:
#     if(c[i] >= s):
#         l[frozenset([i])]+=c[i]

# pl = l
# pos = 1
# for count in range (2,1000):
#     nc = set()
#     temp = list(l)
#     for i in range(0,len(temp)):
#         for j in range(i+1,len(temp)):
#             t = temp[i].union(temp[j])
#             if(len(t) == count):
#                 nc.add(temp[i].union(temp[j]))
#     nc = list(nc)
#     c = Counter()
#     for i in nc:
#         c[i] = 0
#         for q in data:
#             temp = set(q[1])
#             if(i.issubset(temp)):
#                 c[i]+=1

#     l = Counter()
#     for i in c:
#         if(c[i] >= s):
#             l[i]+=c[i]

#     if(len(l) == 0):
#         break
#     pl = l
#     pos = count

# rules = {}
# for l in pl:
#     c = [frozenset(q) for q in combinations(l,len(l)-1)]
#     mmax = 0
#     for a in c:
#         b = l-a
#         ab = l
#         sab = 0
#         sa = 0
#         sb = 0
#         for q in data:
#             temp = set(q[1])
#             if(a.issubset(temp)):
#                 sa+=1
#             if(b.issubset(temp)):
#                 sb+=1
#             if(ab.issubset(temp)):
#                 sab+=1
#         temp = sab/sa*100
#         if(temp > mmax):
#             mmax = temp
#         temp = sab/sb*100
#         if(temp > mmax):
#             mmax = temp
#         if(b.issubset(set(expected_subjects))):
#             rule = []
#             rec = []
#             conf = str(sab/sa*100)
#             for x in a:
#                 rule.append(x)
            
#             for y in b:
#                 rec.append(y)

#             flag = True

#             for r in rule:
#                 if(set(r).issubset(set(expected_subjects))):
#                     flag = False
#                     break

#             if(str(rule) not in rules.keys()) and flag:
#                 res = {
#                     "recommendation": rec,
#                     "confidence": conf
#                 }
#                 rules.update({str(rule): res})
#     curr = 1

#     for a in c:
#         b = l-a
#         ab = l
#         sab = 0
#         sa = 0
#         sb = 0
#         for q in data:
#             temp = set(q[1])
#             if(a.issubset(temp)):
#                 sa+=1
#             if(b.issubset(temp)):
#                 sb+=1
#             if(ab.issubset(temp)):
#                 sab+=1
#         temp = sab/sa*100
#         curr += 1
#         temp = sab/sb*100
#         curr += 1
# result = # print(json.dumps(rules, indent=4, sort_keys=True))


here = dirname(__file__)
rules_json = open(join(here,"rules.json"))

rules_data = json.load(rules_json)



def make_recommendations(subjects = []):
    electives = set()
    result_dict = {}
    
    if(len(subjects) == 5):
        combinations = itertools.combinations(subjects, 2)
        for x in combinations:
            for rule in rules_data:
                if set(list(x)) == set(rule.split(',')):
                    resp = rules_data[rule]
                    # print(f"{str(list(x))} : {resp}")
                    if(rule in result_dict):
                        if(int(result_dict.get(rule)) > int(resp['confidence']) ):
                            pass
                        else:
                            result_dict.update({rule: resp['confidence']})
                            electives.add(resp['recommendation'][0])
                    else:
                            result_dict.update({rule: resp['confidence']})
                            electives.add(resp['recommendation'][0])                    
        result_dict.clear()
        if(len(electives) == 1):
            subject = electives.pop()
            for s in subjects:
                for rule in rules_data:
                    if set([subject, s]) == set(rule.split(',')):
                        resp = rules_data[rule]
                        # print(f"{str([subject, s])} : {resp}")
                        if(rule in result_dict):
                            if(int(result_dict.get(rule)) > int(resp['confidence']) ):
                                pass
                            else:
                                result_dict.update({rule: resp['confidence']})
                                electives.add(resp['recommendation'][0])
                        else:
                            result_dict.update({rule: resp['confidence']})
                            electives.add(resp['recommendation'][0])
            electives.add(subject)
        else:
            # print(electives)
            return list(electives)

    else:
        return "invalid input"


