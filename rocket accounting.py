from tabulate import tabulate

data = [] #la liste qui va contenir les données du tableau

actif=[]
passif=[] #les listes annexes pour sommer indépendement les actifs et les passifs

# ATTENTION: écrire dans console sous forme : 
    # tab(["mobilier",2000,"fournisseurs",2000])
    # ou tab([1010,2000,2000,2000])

def tab(n):
    
    data.append(n) #on ajoute les éléments à la liste data
    if n[0] == 1000:
        n[0]="caisse"
    if n[0] == 10:
        n[0]="caisse"
        #compléter avec autres noms

    if n[3] ==2000:
        n[3]="fournisseurs"
        #compléter avec autres noms
    
    head = ["Actifs","somme", "Passifs","somme"] #le titre
    print(tabulate(data, headers=head, tablefmt="grid")) #afficher le tableau
    
    actif.append(n[1]) 
    passif.append(n[3]) #on ajoute les valeurs A et P à leurs listes
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
        
    
