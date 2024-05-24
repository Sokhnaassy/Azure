import numpy as np

#Génération du polynome de Goppa
def func_goppa(n):
    global p,coef,expo
    coef=[]
    expo=[]
    exp=[]
    while coef==[]:
        for i in range(int(n)):
            a=np.random.randint(10)%2
            if a!= 0:
                coef.append(a)
    while len(expo)!= len(coef):
        c=np.random.randint(0,int(n))
        expo.append(c)
        exp.append(c)
        # pour éviter d'avoir des doublons dans la liste des coefficients
        if expo.count(c)> 1 :
            expo.remove(c)
            exp.remove(c)
    pol=[]
    for i in range(len(expo)):
        if exp[i]==0:
            exp[i]=0x2070
        elif exp[i]==1:
            exp[i]=0x00B9
        elif exp[i]==2:
            exp[i]=0x00B2
        elif exp[i]==3:
            exp[i]=0x00B3
        elif exp[i]==4:
            exp[i]=0x2074
        elif exp[i]==5:
            exp[i]=0x2075
        elif exp[i]==6:
            exp[i]=0x2076
        elif exp[i]==7:
            exp[i]=0x2077
        elif exp[i]==8:
            exp[i]=0x2078
        elif exp[i]==9:
            exp[i]=0x2079

        t=str("x"+chr(exp[i]))
        pol.append(t)
    p="+".join([u for u in pol])
    return p
   
#Calcul
def sol_goppa(x):
    global coef
    sol=[]
    for i in range(len(coef)):
        t=int(x)**int(expo[i])
        sol.append(t)
    return(sum(sol))

#Génération d'une matrice de permutation
def perm_alea(n):
    n=int(n)
    P=[]
    for i in range(n-1):
        P.append([0]*n)
        for j in range(n-1):
            P[i][j]=np.random.randint(10)%2
    return P

#Génération d'une matrice inversible
def mat_inv(n):
    global S
    n=int(n)
    k= max_num(expo,len(expo))
    D=0
    while (D == 0):
        S = np.random.randint(10, size=(n-k,n-k))%2
        D = np.linalg.det(S)
    return S

#Génération d'un vecteur
def vecteur(k):
    global L
    L=[]
    i=np.random.randint(100)
    if sol_goppa(i) != 0 :
        for j in range(0,k-1):
            L.append(i**j)
    return L

#Détermination de l'inverse modulaire
def mod_inverse(a, b):
    r = -1
    B = b
    A = a
    eq_set = []
    full_set = []
    mod_set = []

#algorithme d'euclide
    while r!=1 and r!=0:
        r = b%a
        q = b//a
        eq_set = [r, b, a, q*-1]
        b = a
        a = r
        full_set.append(eq_set)

    for i in range(0, 4):
        mod_set.append(full_set[-1][i])

    mod_set.insert(2, 1)
    counter = 0

    for i in range(1, len(full_set)):
        if counter%2 == 0:
            mod_set[2] = full_set[-1*(i+1)][3]*mod_set[4]+mod_set[2]
            mod_set[3] = full_set[-1*(i+1)][1]

        elif counter%2 != 0:
            mod_set[4] = full_set[-1*(i+1)][3]*mod_set[2]+mod_set[4]
            mod_set[1] = full_set[-1*(i+1)][1]

        counter += 1

    if mod_set[3] == B:
        return mod_set[2]%B
    return mod_set[4]%B

#Détermination de la matrice de parité
def mat_par(n):
    n=int(n)
    h=[]
    L=vecteur(n)
    for i in range(n-1):
        h.append([0]*n)
        for j in range(n-1):
            h[i][j]=(L[i]*mod_inverse(sol_goppa(L[j]),n))%2
    return h

#Détermination du plus grand coefficient
def max_num(nums, n):
    # Condition d'arrêt: si la liste ne contient qu'un élément,
    # celui-ci est le maximum
    if n == 1:
        return nums[0]
    else:
        # On appelle récursivement la fonction pour trouver le maximum
        # des n-1 premiers éléments de la liste
        max_n_1 = max_num(nums, n-1)
        # On compare le dernier élément de la liste avec le maximum des n-1 premiers
        if nums[n-1] > max_n_1:
            return nums[n-1]
        else:
            return max_n_1
        
#Détermination de la clé publique
def niederetteK(n):
    global p,coef,expo,S,H,P,H_pub
    n=int(n)
    coef= []
    expo=[]
    exp=[]
    while coef==[]:
        for i in range(int(n)):
            a=np.random.randint(10)%2
            if a!= 0:
                coef.append(a)
    while len(expo)!= len(coef):
        c=np.random.randint(0,int(n))
        expo.append(c)
        exp.append(c)
        if expo.count(c)> 1 :
            expo.remove(c)
            exp.remove(c)
    pol=[]
    for i in range(len(expo)):
        if exp[i]==0:
            exp[i]=0x2070
        elif exp[i]==1:
            exp[i]=0x00B9
        elif exp[i]==2:
            exp[i]=0x00B2
        elif exp[i]==3:
            exp[i]=0x00B3
        elif exp[i]==4:
            exp[i]=0x2074
        elif exp[i]==5:
            exp[i]=0x2075
        elif exp[i]==6:
            exp[i]=0x2076
        elif exp[i]==7:
            exp[i]=0x2077
        elif exp[i]==8:
            exp[i]=0x2078
        elif exp[i]==9:
            exp[i]=0x2079

        t=str("x"+chr(exp[i]))
        pol.append(t)
    P = np.random.randint(10, size=(n,n))%2
    k= max_num(expo,len(expo))
    D=0
    while (D == 0):
        S = np.random.randint(10, size=(n-k,n-k))%2
        D = np.linalg.det(S)
    L=[]
    i=np.random.randint(100)
    if sol_goppa(i) != 0 :
        for j in range(0,k-1):
            L.append(i**j)
    H=[]
    L=vecteur(n)
    for i in range(n-k):
        H.append([0]*n)
        for j in range(n-1):
            H[i][j]=(L[i]*mod_inverse(sol_goppa(L[j]),n))%2
    H_pub=S.dot(H).dot(P)
    for i in range(n-k):
        for j in range(n):
            H_pub[i][j]=H_pub[i][j]%2
    return H_pub

#Encodage du message 
def encod_mess(mess,n):
    global M,C
    n=int(n)
    M=[]
    H_pub=niederetteK(n)
    for i in mess:
        M.append(list(np.binary_repr(ord(i),n)))
    M=np.transpose(M)
    M=M.astype(int)
    C=np.dot(H_pub,M)%2
    return C 

#Decodage du message 
def decod_mess(mess_c):
    global M
    n=int(n)
    pg=np.dot(np.linalg.inv(S),C)
    pd=np.dot(H,P)
    mess=np.linalg.solve(pd,pg)
    return mess
    


