lst = []
for i in range(0, 4):
    ele = int(input())
    lst.append(ele)
mst=[]
for i in range(0, 4):
    le = int(input())
    lst.append(le)
new_list = []
for x in range(0, 4):
    j=lst[x]*mst[x]
    new_list.append(j)
new_list.sort(reverse=True)
for x in range(0, 2):
    print(new_list[x])