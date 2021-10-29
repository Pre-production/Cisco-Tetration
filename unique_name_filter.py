
from os import write

List2 = open('servers_to_be_removed.txt', 'r')

two = []
twolist=[]
duplicates=[]

for b in List2:
  two.append(b.strip())
twolist=sorted(two)
with open ('unique_list.txt', 'w+') as f:
    for x in twolist:
        if twolist[40:].count(x)>1:
          duplicates.append(x)
        else:
          f.write(x+'\n')
print (duplicates)



