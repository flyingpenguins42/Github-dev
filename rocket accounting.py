from tabulate import tabulate

data = [] #la liste qui va contenir les données du tableau
order = [] #la liste qui va numéroter l'ordre d'affichage des lignes

actif=[]
passif=[] #les listes annexes pour sommer indépendement les actifs et les passifs

# ATTENTION: écrire dans console sous forme : 
    # tab(["mobilier",2000,"fournisseurs",2000])
    # ou tab([1010,2000,2000,2000])
n=0
def tab(e):
    data.append(e) #on ajoute les éléments à la liste data
    
    if e[0] == 1000:
        e[0]="caisse"
        # order.append()
        #compléter avec autres noms Actifs

    if e[2] ==2000:
        e[2]="fournisseurs"
        #compléter avec autres noms Passifs
    
    #ajouter fonction pour réaficher tableau dans le bon ordre à chaque fois
    print ("order=",order)
    n+=1
    print(n)
    
    head = ["Actifs","Valeur", "Passifs","Valeur"] #le titre
    print(tabulate(data, headers=head, tablefmt="grid")) #afficher le tableau
    
    
    actif.append(e[1]) 
    passif.append(e[3]) #on ajoute les valeurs A et P à leurs listes
    SumA= sum(actif)
    SumP= sum(passif) #2 variables égales aux sommes des A et P
    print ("ACTIFS=", SumA)
    print ("PASSIFS=", SumP) #affichage des valeurs des A et P
    
    if SumA > SumP :
        print("il doit y avoir une erreur dans vos calculs")
    elif SumA < SumP:
        print("oups,vous êtes en faillite..")
    elif SumA == SumP:
        print("les valeurs sont justes")
    
    
    
