from tabulate import tabulate

dataA = [] #la liste qui va contenir les données du tableau
dataP = []
# order = [] #la liste qui va numéroter l'ordre d'affichage des lignes

Vactif=[]
Vpassif=[] #les listes annexes pour sommer indépendement les actifs et les passifs

# ATTENTION: écrire dans console sous forme : 
    # tab(["mobilier",2000,"fournisseurs",2000])
    # ou tab([1010,2000,2000,2000])

def tab(a,p):
    dataA.append(a) #on ajoute les éléments à la liste data
    
    if a[0] == 1000:
        a[0]="caisse"
        # order.append(1)
        #compléter avec autres noms Actifs
    
    
    head = ["Actifs","Valeur"] #le titre
    print(tabulate(dataA, headers=head, tablefmt="grid")) #afficher le tableau
    
    dataP.append(p)
    
    if p[0] == 2000:
        p[0]="fournisseurs"
        #compléter avec autres noms Passifs
   
    head=["Passifs","Valeur"]
    print(tabulate(dataP, headers=head, tablefmt="grid"))
    
    
    Vactif.append(a[1]) 
    Vpassif.append(p[1]) #on ajoute les valeurs A et P à leurs listes
    SumA= sum(Vactif)
    SumP= sum(Vpassif) #2 variables égales aux sommes des A et P
    print ("ACTIFS=", SumA)
    print ("PASSIFS=", SumP) #affichage des valeurs des A et P
    
    if SumA > SumP :
        print("il doit y avoir une erreur dans vos calculs")
    elif SumA < SumP:
        print("oups,vous êtes en faillite..")
    elif SumA == SumP:
        print("les valeurs sont justes")
    
