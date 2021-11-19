List1 = open('active_sensors_list.txt', 'r')
List2 = open('servers_to_be_removed.txt', 'r')
one = []
two = []

for a in List1:
  one.append(a.strip())
for b in List2:
  two.append(b.strip())
with open('uuids_list.txt', 'w+') as f:
  for i in one:  
    for t in two:
      if i.endswith(t):
        f.write(i+'\n')
