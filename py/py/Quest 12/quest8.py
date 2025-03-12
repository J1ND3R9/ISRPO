def mix(li1, li2):
  if len(li1) == len(li2):
    for i in range(len(li1)):
      yield li1[i]
      yield li2[i]
      
li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

li = mix(li1, li2)
for i in li:
  print(i, end=", ")
  
for i in li:
  print(i)