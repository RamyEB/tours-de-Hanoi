from tkinter import *
import time



# Fonction hanoi recurssive qui gere l'algorithme et les deplacements 
#
# ids : liste d'element du canvas (rectangle)
# source, destination, temp : tiges
# hateur: liste d'hauteurs en int des tiges 0 1 2
#
def hanoi(ids,source,destination,temp,hauteurs):
    if len(ids) == 1:
        # time.sleep(0.3)
        
        # Deplacement et mise a jour des hauteurs
        move(ids[0],(source,etage(hauteurs[source]-1)),(destination, etage(hauteurs[destination])))
        hauteurs[source] -= 1
        hauteurs[destination] += 1
        root.update()
        return
    
    #On rappelle hanoi en inversant des et tmp
    hanoi(copieWithoutLast(ids),source,temp,destination,hauteurs)    
    
    # Deplacement, mise a jour des hauteurs
    # time.sleep(0.3)
    move(ids[len(ids)-1],(source, etage(hauteurs[source]-1)),(destination, etage(hauteurs[destination])))
    hauteurs[source] -= 1
    hauteurs[destination] += 1
    root.update()
    
    #On rappelle hanoi en inversant tmp et src
    hanoi(copieWithoutLast(ids),temp,destination,source,hauteurs)    
    

# Fonction copieWithoutLast prend une liste et la retourne sans le dernier element
#
# listeInit : liste
#    
def copieWithoutLast(listeInit):
    listeReturn = []
    for i in range(len(listeInit)):
        if i < (len(listeInit)-1):
            listeReturn.append(listeInit[i])
    return listeReturn

# Fonction passageY prend une coordonee Y et retourne une coordones y adaptée au repère de la fenetre
#
# y : int
#    
def passageY(y):
    return height-y

# Fonction move deplace un disque d'un point à un autre avec animation
#
# nro : numéro de l'element
# src : liste composée de la tige source en int et de l'etage de depart
# des : liste composée de la tige destination en int et de l'etage de destination
#  
def move(nro,src,des):
    position = des[0]-src[0]
    etage = des[1]-src[1]
    for i in range(60):
        time.sleep(0.01)
        cv.move(nro,position/60,etage/60)
        root.update()

# Fonction etage retourne un numbre de pixel correspondant à un etage x
#
# x : etage en int
#  
def etage(x):
    return passageY(0)-25-(35*x)-(5*x)



nbDisque = -1
while(nbDisque <1 or nbDisque>6):
    nbDisque = int(input("Veuillez entrer un nombre de disque inférieur à 7 : "))
width = 900
tige0 = 250
tige1 = 450
tige2 = 650
largeurDisque = 35
height = 100+largeurDisque*nbDisque
longeurDisqueInit = 200
root = Tk()
root.minsize(width, height) # taille minimum de la fenetre
root.resizable(width=False, height=False) # taille minimum de la fenetre
root.title("Les tours de Hanoï | EL BEHEDY Ramy")
frame = Frame( root )
frame.pack(fill=BOTH, expand=YES)
cv = Canvas(frame, width=25, height=25, bg='bisque')
cv.pack(fill=BOTH, expand=YES)

tiges=[]
tiges.append(cv.create_rectangle(60, passageY(0), width-60, passageY(20), fill="black"))
tiges.append(cv.create_rectangle(240, passageY(0), 260, 50, fill="black"))
tiges.append(cv.create_rectangle(440, passageY(0), 460, 50, fill="black"))
tiges.append(cv.create_rectangle(640, passageY(0), 660, 50, fill="black"))

ids=[]
for i in range(nbDisque):
    longeurDisqueInit -= i*(15-nbDisque)
    ids.append(cv.create_rectangle(240-(longeurDisqueInit-20)/2, etage(i), 260+(longeurDisqueInit-20)/2, etage(i)-largeurDisque, fill="red"))

ids.reverse()
root.update()
time.sleep(1)
hanoi(ids,tige0,tige2,tige1,{tige0 : nbDisque, tige1 : 0, tige2 : 0})    
root.mainloop()

