from numpy import*
def saisir():
    global l,c
    l=int(input("donner le nombre de ligne:"))
    c=int(input("donnerle nombre de colonne:"))
    while not (2<=l<=10 and 2<=c<=10):
        l=int(input("donner le nombre de ligne:"))
        c=int(input("donnerle nombre de colonne:"))
def remplir1(v,n):
    for i in range(n):
        v[i]=input("v["+str(i)+"]:")
        while not(v[i]!=""):
            v[i]=input("v["+str(i)+"]:")
    print(v)
def remplir2(M,l,c):
    for i in range(l):
        for j in range(c):
            while not ("A"<=M[i,j]<="Z" or "a"<=M[i,j]<="z"):
                M[i,j]=input("M["+str(i)+","+str(j)+"]:")

def afficher(v,M,t,n,l,c):
    global ne
    ne=0
    for k in range(n):
        if len(v[k])<=c:
            for i in range(l):
                ch=""
                for j in range(c):
                    ch=ch+M[i,j]
                if recherche_ind(v[k],ch):
                    t[ne]=dict()
                    t[ne]["Mot"]=v[k]
                    t[ne]["Num_ligne"]=i+1
                    ne=ne+1
    print(M)
    print(t)
def recherche_ind(ch1,ch2):
    test=True
    i=0
    while test and i<len(ch1):
        p=ch2.find(ch1[i])
        if p==-1:
            test=False
        else:
            i=i+1
            ch2=ch2[p+1:len(ch2)]
    return test

            
            


n=3
saisir()
e=dict(Mot=str,Num_ligne=int)
t=array([e]*l)
v=array([str]*n)
remplir1(v,n)
M=array([[str()]*c]*l)
remplir2(M,l,c)
afficher(v,M,t,n,l,c)