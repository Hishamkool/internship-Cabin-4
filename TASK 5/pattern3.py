n=int(input("enter a number"))
MAX=100
size = 2 * n - 1
front = 0
back = size - 1
a = [[0 for i in range(MAX)]   
          for i in range(MAX)] 
while (n!= 0):  
    for i in range(front, back + 1): 
        for j in range(front, back + 1): 
            if (i == front or i == back or
                j == front or j == back): 
                a[i][j] = n 
    front=front+1
    back=back-1
    n=n-1
for i in range(size):  
  for j in range(size): 
    print(a[i][j], end = '') 
  print() 
