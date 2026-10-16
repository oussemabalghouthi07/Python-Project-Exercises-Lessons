from numpy import*
def saisir(N):
    global n
    n=int(input("donner n:"))
    while not (2<=n<=N):
        n=int(input("donner n:"))
def remplir(fr,eng,n):
    for i in range(n):
        while not (len(str(eng[i]))<=15 and len(str(fr[i]))<=15 and fr[i]!="" and eng[i]!="" and verif(eng[i]) and verif(fr[i])):
            fr[i]=input("fr["+str(i)+"]:")
            eng[i]=input("eng["+str(i)+"]:")
def verif(ch):
    test=True
    i=0
    while i<len(ch) and test:
        test='A'<=ch[i]<='Z' or 'a'<=ch[i]<='z'
        i=i+1
    return(test)
def afficher(fr,eng,n):
    p=input("donner la phrase à traduire:")
    while not  p!="":
        p=input("donner la phrase à traduire:")
    v=p+" "
    chf=""
    nb=0
    while not p=="" :
        s=v.find(" ")
        M=v[0:s]
        ind=recherche_indice(M,fr,n)
        if ind==-1 :
            chf=chf+'{'+M+'}'+" "
            nb=nb+1
        else:
            chf=chf+eng[ind]+" "
        p=p[p.find(" ")+1:len(p)]
    if nb==0 :
        chf=chf+":traduction totalle"
    else:
        chf=chf+":traduction partielle,"+str(nb)+"mot(s) non traduit(s)"
    print(chf)

def recherche_indice(M,fr,n):
    i=0
    while i<n-1 and fr[i]!=M:
        i=i+1
    tr=(fr[i]==M)
    if tr==True:
        return i
    else:
        return -1
    
    
        
      

N=100
saisir(N)
fr=array([str]*n)
eng=array([str]*n)
remplir(fr,eng,n)
afficher(fr,eng,n)
