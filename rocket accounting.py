# import module
from tabulate import tabulate

# def tab(actif,Sa,passif,Sp):
# # assign data
#     mydata = [
#         [actif,Sa,passif,Sp],
#         ]
# # create header
#     head = ["Actifs","somme", "Passifs","somme"]
# # display table
#     print(tabulate(mydata, headers=head, tablefmt="grid"))
    
actif=[]
passif=[]
data = []

def tab(n):
    data.append(n)
    head = ["Actifs","somme", "Passifs","somme"]
    print(tabulate(data, headers=head, tablefmt="grid"))
    # L=[n]
    print(type(n))
    # actif.append(n[2])
    # passif.append(n[4])

# def act(actif,Sa,passif,Sp):
#     L=[actif,Sa,passif,Sp]
#     print(L)
    


# ATTENTION: écrire dans console sous forme : 
    # tab(["mobilier",2000,"fournisseurs",2000])