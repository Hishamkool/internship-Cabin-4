n=int(input("entr no."))
m=int(input("enter no2:"))
s=" "
a=n
t=n*2
for i in range(1,n+1):
  n=n-1
  t=t-2
  if n==0:
    for i in range(0,a):
        print(" ")
        print(s*i,end=" ")
        a=a-1 
        for k in range(0,m):
          for j in range(a+1):
            print("*",end=" ")
          print(s*t,end=" ")
        t=t+2        
  print(" ") 
  print(s*n,end=" ")
  for k in range(0,m):
    for j in range(i):
      if n==0:
        break
      print("*",end=" ")
    print(s*t,end=" ")