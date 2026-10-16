def saisir():
    global n
    n=int(input("donner n:"))
    while not 2<=n<=15:
        n=int(input("donner n:"))
def afficher(u,n):
    u[0]=0
    print(u[0])
    for i in range(1,n):
        x=str(u[i-1])
        s=""
        for j in range (len(x)):
                s=s+occurence(x[j],x)+x[j]
        u[i]=s
        print(u[i])
def occurence(c,x):
    nb=0
    for i in range(len(x)):
        if x[i]==c:
            nb=nb+1
    return str(nb)
        
from random import*    
from numpy import*
saisir()
u=array([str]*n)
afficher(u,n)