a1=[]
a2=[]
b=0
num=int(input())
item=input().split()
for i in item:
  a1.append(int(i))
for i in range(0,num-1):
  b=0
  for j in range(i+1,num):
    if a1[i]==a1[j]:
      b=b+1
      break
  if b>=1 and a1[i] not in x2:
    a2.append(a1[i])
c=len(a2)
if c==0:
  print("unique")
else:
  for i in a2:
    print(i,end=" ")
