
a=int(input("positon of kangaroo 1 (max 10000) : "))
x=int(input("kangaroo 1 rate of jump (max 10000) : "))
b=int(input("position of kangaroo 2 (max 10000) : "))
y=int(input("kangaroo 2 rate of jump (max 10000) : "))

for i in range(10000):
  a=a+x
  b=b+y
  if(a==b):
    break
if(a==b):
  print("yes")
  print("they meet at position ",b)
else:
  print("no")


