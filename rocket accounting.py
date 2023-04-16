# import module
from tabulate import tabulate

actif=[]
passif=[]
data = []

def tab(n):
    data.append(n)
    head = ["Actifs","somme", "Passifs","somme"]
    print(tabulate(data, headers=head, tablefmt="grid"))
    actif.append(n[1])
    passif.append(n[3])

# ATTENTION: écrire dans console sous forme : 
    # tab(["mobilier",2000,"fournisseurs",2000])