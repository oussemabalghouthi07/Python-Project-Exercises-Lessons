def saisir(nmax):
    global n
    ok=False
    while not(ok):
        n=int(input("donner un entier "))
        ok=2<=n<=nmax
def remplir(fr,eng,n):
    for i in range(n):
        ok=False
        while not(ok):
            fr[i]=input("fr["+str(i)+"]:")
            eng[i]=input("eng["+str(i)+"]:")
            ok=len(fr[i])<=15 and len(eng[i])<=15 and verif(fr[i]) and verif(eng[i])
def verif(ch):
    i=0
    test=True
    while (i<len(ch) and test):
        test="a"<=ch[i]<="z" or "A"<=ch[i]<="Z"
        i+=1
    return test
def saisir2():
    global ph
    ok=False
    while not(ok):
        ph=input("donner un chaine de caractére" )
        ok=verif2(ph) and len(ph)!=0 and ph.find("  ")==-1 and ph[len(ph)-1]!=" "
def verif2(ch):
    i=0
    test=True
    while (i<len(ch) and test):
        test=(ord("a")<=ord(ch[i])<=ord("z")) or (ord("A")<=ord(ch[i])<=ord("Z")) or (ch[i]==" ")
        i+=1
    return test
def afficher(n,ph,fr,eng):
    nb=0
    ch=ph+" "
    res=""
    ok=False
    while not(ok):
        chh=ch[0:ch.find(" ")]
        ind=rechercheind(chh,fr,n)
        if ind==-1:
            res+="{"+chh+"}"
            nb+=1
        else:
            res+=eng[ind]+" "
        ch=ch[ch.find(" ")+1:len(ch)]
        ok=ch==""
    if nb==0:
        res+=":traduction totale "
    else:
        res+=":traduction partielle "+str(nb)+"mot(s) non traduits "
    print(res)
def rechercheind(ch,fr,n):
    i=0
    p=-1
    while(i<n and p==-1):
        if fr[i]==ch:
            p=i
        else:
            i+=1
    return p            
from numpy import*
nmax=100
saisir(nmax)
fr=array([str]*n)
eng=array([str]*n)
remplir(fr,eng,n)
saisir2()
afficher(n,ph,fr,eng)