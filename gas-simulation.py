# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:56:09 2021

@author: Tim
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mplAnim
from time import sleep


nIter=1001       # nombre d'itérations temporelles



#-----------------------------------------------------CREATION DE L'ESPACE-----------------------------------------------------------------------------------------------
Nx = 100                                              #longueur en x de l'espace
Ny = 100                                              #longueur en y de l'espace
Espace=np.zeros([Nx+2,Ny+2],dtype='int')              # initialisation de l'espace (aucune particule)
                                                      #code physique de l'espace : -1 bordure, 0 vide, 1 occupé
Espace[0,:]=Espace[-1,:]=Espace[:,0]=Espace[:,-1]=-1  #bordures de l'espace

E_total = 1                                           #Energie totale conservée dans l'espace
#------------------------------------------------------------------------------------------------------------------------



#-----------------------------CREATION DES PARTICULES-----------------------------------------------------------------------------------------------
N=42                         # nombre de particule
x=np.random.randint(Nx/5,Nx+1-Nx/5,N) # position initiale des particules en x
y=np.random.randint(Ny/5,Ny+1-Ny/5,N) # position initiale des particules en y
Espace[x,y] = 1                       #occupation de l'espace par les particules
v_x=np.random.randint(-3,3,N)  #vitesse initiale des particules suivant x
v_y=np.random.randint(-3,3,N)  #vitesse initiale des particules suivant y
v = [v_x,v_y]                 #vecteur vitesse
E=1                           #état énergétique des particules (état fondamental, 1er état excité, 2ème état excité, ...)
m=1                           #masse des particules (quantité fixe)
#------------------------------------------------------------------------------------------------------------------------




etat=np.zeros(N,dtype='int') # etat d'excitation des particules (0: fondamental, 1: 1er, 2: 2eme, ...)

jj=np.random.randint(0,N)  # sélection au hasard d'une particule
etat[jj:jj+10] = 1         # excitation niveau 1 de cette particule
tt=np.random.randint(0,N)  # sélection au hasard d'une particule
etat[tt]=2                 # excitation niveau 2 de cette particule

#initialisation de la figure
#im=plt.imshow(grille,vmin=0,vmax=2.2,origin='lower',cmap='nipy_spectral',interpolation='nearest')

jj=(etat==1).nonzero()


#-----------------------------INTERACTIONS ENTRE PARTICULE-----------------------------------------------------------------------------------------------
#Il faut d'abord faire le test du voisin pour vérifier si une particule se trouve à côté d'une autre
#Possibilités de voisin :
    #  x_voisin = x+1 ; y_voisin=y+1   # en haut à droite
    #  x_voisin = x   ; y_voisin=y+1   # en haut au milieu
    #  x_voisin = x-1 ; y_voisin=y+1   # en haut à gauche
    
    #  x_voisin = x+1 ; y_voisin=y     # même hauteur à droite
    #  x_voisin = x-1 ; y_voisin=y     # même hauteur à gauche

    #  x_voisin = x+1 ; y_voisin=y-1   # en bas à droite
    #  x_voisin = x   ; y_voisin=y-1   # en bas au milieu
    #  x_voisin = x-1 ; y_voisin=y-1   # en bas à gauche

#Une fois un voisin localisé, il faut vérifier si à la prochaine itération temporelle les deux particules se supperpose
#ce qui signifie qu'une collision a lieu 


#OU

#Calculer la norme de la distance entre deux particules :
    #d = np.abs(x_p1 - xp2) + np.abs(y_p1 - y_p2)
    #Si la distance est inférieur à 1 ou 2 alors on considère une collision
    
#OU

#Simplement regarder si deux particules sont sur la même "cellule" du réseau, si oui il y a collision


#------------------------------------------------------------------------------------------------------------------------



def fonctionIter(): #une itération de la simulation, on met à jour le réseau
    global x,y,v_x,v_y,Nx,Ny
    
    """
    theta=(np.random.randint(0,5,N))*(np.pi/2)
    Espace[x,y] = 0                   #Les particules quittent leur ancienne position
    x=np.clip(x+np.cos(v_x),1,Nx)     # déplacement des particules en s'assurant
    y=np.clip(y+np.sin(v_y),1,Ny)     # qu'ils ne quittent pas le réseau 
    """
    
    Espace[x,y] = 0                   # Les particules quittent leur ancienne position
    x=np.clip(x+v_x,1,Nx-1)             # Déplacement des particules en s'assurant
    y=np.clip(y+v_y,1,Ny-1)             # qu'elles ne quittent pas le réseau 
    Espace[x,y] = 1                   #Les particules arrivent sur une nouvelle cellule de l'espace
    
    #Evolution de l'espace
    #evol=np.zeros([Nx+2,Ny+2],dtype='int') # tableau d'évolution (à ajouter à l'espace)
    #i,j=(Espace==1).nonzero()  # indices (i,j) des sites occuppés par une particule
    
    
    
    #Calcul des collisions : Bordure Gauche
    x_index = np.where(x==1)
    v_x[x_index] = -v_x[x_index]
    #Calcul des collisions : Bordure Droite
    x_index = np.where(x==99)
    v_x[x_index] = -v_x[x_index]   
    #Calcul des collisions : Bordure Basse
    y_index = np.where(y==1)
    v_y[y_index] = -v_y[y_index]
    #Calcul des collisions : Bordure Haute
    y_index = np.where(y==99)
    v_y[y_index] = -v_y[y_index]
    
    
    #Calcul des collisions entre Particules
    
    
    #la vitesse change aléatoirement
    #v_rand=(np.random.randint(0,420,N))*(np.pi/2)
    #v_x=np.clip(v_x+np.cos(v_rand),-5,5)
    #v_y=np.clip(v_y+np.sin(v_rand),-5,5)


def animIter(k): #k=nIter
    fonctionIter()
    scat.set_offsets(np.array([x,y]).T)
   # scat.set_offsets(np.array([x[2],y[2]]).T)

    titre.set_text('Simulation (Itération {})'.format(k))
    return scat,titre


#initialisation de la figure
fig=plt.figure(dpi=120,figsize=[6,6]) #on crée l'objet figure
ax=plt.axes(xlim=(0,Nx),ylim=(0,Ny))
scat=plt.scatter(x,y,s=20,c=etat) #particule de gaz dans l'état fondamental #eceeed
#scat=plt.scatter([x[1],x[2]],[y[1],y[2]],s=20,color=['#eceeed','red'])    

titre=plt.title('Itération {}'.format(0))
plt.xlabel('X')
plt.ylabel('Y')

#appel à la fonction d'animation
a=mplAnim.FuncAnimation(fig, animIter, frames=nIter, interval=10, repeat=False)
plt.show()




