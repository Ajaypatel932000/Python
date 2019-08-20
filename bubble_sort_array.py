import array as ar
#a=ar.array('i',(a for a in int(input("Enter a number = ").split())))
a=ar.array('i',(int(a) for a in input("Enter a number = ").split()))
#print(a)
n=len(a)
print(n)
for i in range(0,n):
    print(i,end=" ")
print()
for j in range(1,n):
           print(j,end=" ")
           '''if a[i]>a[j]:
              c=a[i]
              a[i]=a[j]
              a[j]=c

for e in a:
 print(e)
              
'''
