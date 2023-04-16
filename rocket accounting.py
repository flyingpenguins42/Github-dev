# import module
from tabulate import tabulate

data = [] #la liste qui va contenir les données du tableau

actif=[]
passif=[] #les listes annexes pour sommer indépendement les actifs et les passifs

def tab(n):
    data.append(n) #on ajoute les éléments à la liste data
    head = ["Actifs","somme", "Passifs","somme"] #le titre
    print(tabulate(data, headers=head, tablefmt="grid")) #afficher le tableau
    
    actif.append(n[1]) 
    passif.append(n[3]) #on ajoute les valeurs A et P à leurs listes
    SumA= sum(actif)
    SumP= sum(passif)
    print ("ACTIFS=", SumA)
    print ("PASSIFS=", SumP)

    
# ATTENTION: écrire dans console sous forme : 
    # tab(["mobilier",2000,"fournisseurs",2000])
    
