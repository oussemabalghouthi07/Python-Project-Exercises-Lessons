from numpy import*
i=0
n=4
t=array([int]*n)
for j in range(1,n):
    t[j]=int(input("donner l'entier:"))
def inconnue(t,i,n):
    temp=t[n]
    if n>1:
        inconnue(t,i+1,n-1)
    t[i]=temp
    print(t)
inconnue(t,i,n)