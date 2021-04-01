# import matplotlib.pyplot as plt
# import random as rd
#
# #constantes
# taille = 100
#
# #etats
# arbre = 0
# feu = 1
# vide = 2
#
# #matrice foret
# foret = [[0 for i in range(taille)] for j in range(taille)]
#
# #init feu
# start = (rd.randint(0,taille-1), rd.randint(0,taille-1))
# foret[start[0]][start[1]] = feu
#
# #regles de propagation
# for i in range(taille):
#     for j in range(taille):
#         if foret[i][j] == feu:
#             foret[i][j+1] = feu
#             foret[i+1][j] = feu
#             foret[i][j-1] = feu
#             foret[i-1][j] = feu
#             foret[i+1][j+1] = feu
#             foret[i-1][j-1] = feu
#             foret[i-1][j+1] = feu
#             foret[i+1][j-1] = feu
#
# #affichage


import random as rd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# etats
vide = 0
arbre = 1
feu = 2

# constantes
taille = 100
frames = 200
fire_prob = 0.72
interval = 75
density = 0.9 #still to do

# init foret
foret = []
for i in range(frames):
    foret.append([[arbre for i in range(taille)] for j in range(taille)])

#init feu
start = (rd.randint(0,taille-1), rd.randint(0,taille-1))
foret[1][start[0]][start[1]] = feu

# regles de propagation
def propagation(k, i, j):
    global foret, frames
    if foret[k][i][j] == feu:
        foret[k+1][i][j] = vide
        for l in range(-1, 2):
            for m in range(-1, 2):
                (ni, nj) = (i+l, j+m)
                if(ni < taille and ni >= 0 and nj < taille and nj >= 0):
                    if(foret[k+1][i+l][j+m] == arbre):
                        if(rd.random() > fire_prob):
                            foret[k+1][i+l][j+m] = feu
    elif(foret[k][i][j] == vide):
        foret[k+1][i][j] = vide

for k in range(frames-1):
    for i in range(taille):
        for j in range(taille):
            propagation(k,i,j)

# affichage
fig = plt.figure()
im = plt.imshow(foret[1], animated=True, vmin = 0, vmax = 2)

n = 0
def updatefig(*args):
    global n
    n = (n+1) % frames
    im.set_array(foret[n])
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=interval)
plt.show()
