# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:56:09 2021

@author: Tim
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mplAnim



nIter=1001       # nombre d'itérations temporelles
#Rapport : Taille réseau / Taille particule = 1 particule / cellule (visuellement) : impossible car taille de la particule STATIQUE


#-----------------------------------------------------CREATION DE L'ESPACE-----------------------------------------------------------------------------------------------
Nx = 100                 #longueur en x de l'espace
Ny = 100                 #longueur en y de l'espace
#------------------------------------------------------------------------------------------------------------------------



#-----------------------------CREATION DES PARTICULES-----------------------------------------------------------------------------------------------
N=10                                  # nombre de particule
x=np.random.uniform(Nx/5,Nx+1-Nx/5,N) # position initiale des particules en x
y=np.random.uniform(Ny/5,Ny+1-Ny/5,N) # position initiale des particules en y

m=1.67265e-27 #kg             #masse des particules d'hydrogène (quantité fixe)
r=1                           # rayon = 1 signifie que le rayon fait la largeur d'une cellule

v_max = 5
v_x=np.random.uniform(-v_max,v_max,N)  #vitesse initiale des particules suivant x
v_y=np.random.uniform(-v_max,v_max,N)  #vitesse initiale des particules suivant y
v = [v_x,v_y]                          #vecteur vitesse
E_cin = (1/2)*m*(v_x**2 + v_y**2)      # Energie cinétique des parti
#------------------------------------------------------------------------------------------------------------------------



# Fonction d'itération temporelle : mise à jour des particules et du système / réseau
def fonctionIter():
    global x,y,v_x,v_y,Nx,Ny,nu,m
    
    x=np.clip(x+v_x,1,Nx-1)             # Déplacement des particules en s'assurant
    y=np.clip(y+v_y,1,Ny-1)             # qu'elles ne quittent pas le réseau
    
    # Algorithme de collision particules-particules (deux à deux)
    i_col, j_col = [], []
    for i in range(len(x)):
        for j in range(len(x)):
            i_index = np.where(i_col==j)
            j_index = np.where(j_col==i)
            if i == j or i_index == j_index:
                None
            else:
                sigma = np.sqrt((abs(x[i]-x[j]))**2 + (abs(y[i]-y[j]))**2) - (r+r) # Section efficace
                if sigma > 0:  # condition de collision
                    None
                else:
                    i_col.append(i)
                    j_col.append(j)
                    #print('Collision !')
                    
                    #Calcul de collision v2 ♥
                    vxx = (1/2) * (abs(v_x[i])+abs(v_x[j]))
                    v_x[i] = vxx
                    v_x[j] = -vxx
                    vyy = (1/2) * (abs(v_y[i])+abs(v_y[j]))
                    v_y[i] = vyy
                    v_y[j] = -vyy
                    
                    
    #print('\nvx =', v_x, '\nvy =', v_y)
    
    #Calcul des collisions : Bordure Gauche
    x_index = np.where(x==1)
    v_x[x_index] = -v_x[x_index]
    #Calcul des collisions : Bordure Droite
    x_index = np.where(x==Nx-1)
    v_x[x_index] = -v_x[x_index]   
    #Calcul des collisions : Bordure Basse
    y_index = np.where(y==1)
    v_y[y_index] = -v_y[y_index]
    #Calcul des collisions : Bordure Haute
    y_index = np.where(y==Ny-1)
    v_y[y_index] = -v_y[y_index]
    
    E_cin = (1/2)*m*(v_x**2 + v_y**2)       # Mise à jour de l'énergie cinétique des particules
    #print('E_cin =',E_cin)

    


# Fonction d'animation
def animIter(k): #k=nIter
    fonctionIter()
    scat.set_offsets(np.array([x,y]).T)   # Mise à jour de la position des particules
    E_cin = (1/2)*m*(v_x**2 + v_y**2)     # Mise à jour de l'énergie cinétique des particules
    scat.set_array(E_cin)                 # Mise à jour de la couleur (=énergie) des particules
    titre.set_text("Simulation : Répartition de l'énergie\n(Itération {})".format(k))
    return scat,titre


# Initialisation de la figure
fig=plt.figure(dpi=120,figsize=[6,6]) #on crée l'objet figure
ax=plt.axes(xlim=(0,Nx),ylim=(0,Ny))
scat=plt.scatter(x,y,s=r*50,cmap='Reds', c=E_cin) #map adaptée: Reds, plasma, seismic
cb = plt.colorbar(scat)
cb.set_label('Energie cinétique (J)', labelpad=5, fontsize=15)
titre=plt.title("Simulation : Répartition de l'énergie\n(Itération {})".format(0))
plt.xlabel('X')
plt.ylabel('Y')

# Appel à la fonction d'animation
a=mplAnim.FuncAnimation(fig, animIter, frames=nIter, interval=10, repeat=False)
#a.save('animation4.gif', fps=30)  # Sauvegarde de l'animation en gif
plt.show()
