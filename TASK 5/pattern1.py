n=int(input("entr no."))
s=" "
a=n
for i in range(1,n+1):
  n=n-1
  if n==0:
    for i in range(0,a):
        print(" ")
        print(s*i,end=" ")
        a=a-1 
        for j in range(a+1):
            print("*",end=" ")
  print(" ") 
  print(s*n,end=" ")
  for j in range(i):
    if n==0:
        break
    print("*",end=" ")