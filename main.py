from math import sin, cos, pi
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
interval = 75
vent = True
rad = pi # entre 0 et 2*pi
prob = 0.68
prob_max = 0.68
prob_min = 0.3 # prob_min < prob_max
unit_list = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]

# init foret
foret = []
for i in range(frames):
    foret.append([[arbre for i in range(taille)] for j in range(taille)])

#init feu
start = (rd.randint(0,taille-1), rd.randint(0,taille-1))
foret[1][start[0]][start[1]] = feu

# regles de propagation
def f(x):
    if vent:
        nx = x - rad
        return (prob_max-prob_min)*((sin(nx) + 1)/2 + prob_min)
    else:
        return 1-prob

def get_prob_list():
    prob_list = [0]*8
    for i in range(8):
        prob_list[i] = f(i*pi/4)

    return prob_list

prob_list = get_prob_list();
print(prob_list);


def propagation(k, i, j):
    global foret, frames
    if foret[k][i][j] == feu:
        foret[k+1][i][j] = vide
        for n in range(8):
            (l,m) = unit_list[n]
            (ni, nj) = (i+l, j+m)
            if(ni < taille and ni >= 0 and nj < taille and nj >= 0):
                if(foret[k+1][i+l][j+m] == arbre):
                    if(rd.random() < prob_list[n]):
                        foret[k+1][i+l][j+m] = feu
    elif(foret[k][i][j] == vide):
        foret[k+1][i][j] = vide

for k in range(frames-1):
    for i in range(taille):
        for j in range(taille):
            propagation(k,i,j)

# affichage
fig = plt.figure()
im = plt.imshow(foret[0], animated=True, vmin = 0, vmax = 2)

n = 0
def updatefig(*args):
    global n
    n = (n+1) % frames
    im.set_array(foret[n])
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=interval)
plt.show()
