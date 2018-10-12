'''Problème Euler 16'''



def Euler_16():
    nombre=str(2**1000)
    #le nombre est converti en chaine de caractère
    somme=0
    for k in nombre:
        #Ainsi on peut parcourir chaque chiffre de ce nombre pour l'ajouter à la somme
        somme+=int(k)
    return(somme)




'''Problème Euler 22'''



def Euler_22():
    texte_nom = open('p022_names.txt','r')
    contenu = texte_nom.read()
    liste_nom = contenu.split('","')
    # Sépare les noms du texte en fonction des "."
    liste_nom[len(liste_nom)-1] = 'ALONSO'
    liste_nom[0] = 'MARY'
    # Sert à enlever les " présents en première et dernière position du texte
    liste_nom_triée = sorted(liste_nom)
    # Ainsi on obtient la liste triée
    
    somme_totale = 0
    somme_nom = 0
    
    for i in range (1,len(liste_nom_triée)+1):
        # Cette boucle parcourt la liste pour calculer le score de chaque nom et l'additionner à la somme totale
        somme_nom = 0
        for j in liste_nom_triée[i-1]:
            # Cette sous-boucle calcule la somme de la position des lettres d'un nom dans l'alphabet 
            somme_nom += ord(j) - 64
        somme_totale += i * somme_nom
        
    texte_nom.close()
    return(somme_totale)




'''Problème Euler 55'''



def palindrome(k):
    '''prend en argument k, un entier et renvoie True si c'est un palyndrome, False sinon.'''
    chaine=str(k)
    # On convertit tout d'abord le nombre en chaîne de caractère
    n=len(chaine)
    for i in range (0,int(n/2)+1):
        if chaine[i]!=chaine[n-i-1]:
            # Ce test vérifie si le chiffre i est égal ou non au chiffre n-i du nombre
            return(False)
    return(True)

def Lychrel(k):
    '''prend en argument k, un entier et renvoie True si c'est un nombre de Lychrel, False sinon.'''
    chaine=str(k)
    n=1
    # n comptabilise le nombre d'itérations
    q=0
    # q va servir à former le 'reverse' du nombre
    for i in range (0,len(chaine)):
        q+=int(chaine[i])*(10**i)
    k+=q
    while palindrome(k)==False and n<=50:
        chaine=str(k)
        # On convertit le nombre en chaîne de caractère pour avoir acces à sa taille
        q=0
        for i in range (0,len(chaine)):
            q+=int(chaine[i])*(10**i)
        k+=q
        n+=1
    return(not(palindrome(k)))  
    
def Euler_55():
    L=[]
    for i in range (0,10001):
        if Lychrel(i)==True:
            L.append(i)
    return(len(L))