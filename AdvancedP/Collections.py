#Collections: Counter,nametuple,OrderedDict,defaultdict,deque
# from collections import Counter
# a="aaaabbbbcc"
# my_counter=Counter(a)
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common())
# print(my_counter.most_common(1)[0][0])
# print(list(my_counter.keys()))


# from collections import namedtuple
# point=namedtuple('Point','x,y')
# pt=point(1,4)
# print(pt.x,pt.y)


# from collections import OrderedDict
# OrderedDict=OrderedDict()
# OrderedDict['a']=1
# OrderedDict['b']=2
# OrderedDict['c']=3
# OrderedDict['d']=4
# OrderedDict['e']=5
# print(OrderedDict)


# from collections import defaultdict
# d=defaultdict(float)
# d['a']=1
# d['b']=2
# d['c']=3
# print(d['e'])


from collections import deque
d=deque()

d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)

d.extendleft(6)
d.rotate(d=1)

print(d)
