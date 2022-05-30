# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 11:17:04 2022

@author: Grégoire Mercier
"""

import numpy as np
import matplotlib.pyplot as plt
from math import *
#%% Données [unités S.I.]
g = 9.81 #[m*s**-2], accélération de la pesanteur
E = 210000*10**6 #[Pa], [kg*m**-1*s**-2], module de Young
F = 80*9.81 #[N], [kg*m*s**-2], effort appliqué à déterminée (charge réparti du poids de la poutre et poids de la lentille) 
L = 6 #[m], longueur de la poutre étudiée
d = 550*10**-3 #[m], diamètre du tube 
r = 7800 #[kg/(m**3)], masse volumique

#%% Fonctions - Q1
def S(e):
    y = pi*((d**2)/4-(d/2-e)**2)
    return y
def I(e):
    y = (pi*(d**4-(d-2*e)**4))/64
    return y

def v(x,e):
    y = (-(F*x**3)/6+(F*L*x**2)/2+r*S(e)*g*((L**2*x**2)/4-(L*x**3)/6+(x**4)/24))/(E*I(e))
    return y 

#%% Vecteur - Q2
x = np.linspace(0, L, 200)
e = 25*10**-3 #[mm]
plt.plot(x, v(x,e))
#PROBLEME RESOLU : pour la commande d'affichage ci-dessus, il fallait indiquer "x" avant la fonction pour afficher la bonne abscisse correspondant à des valeurs d'abscisses et non des positions dans le vecteur x.
plt.show()
#PROBLEME : Il reste le souci d'ordre de grandeur pour la flèche (1e9) beaucoup trop important, pour l'instant
#PROBLEME RESOLU : soucis d'unité pour la force F, on multiplait une masse [kg] avec une accélération de la pesanteur en [mm*s**-3] : ça ne donnait donc pas des [N]

#%% - Q3
# D'après nous, la flèche maximale aura lieu en l'ascisse x = L, soit x = 6 m. Donc, on pose x = 6 m.
x = 6
def f(e):
    y = v(x,e)
    return y
f(e) = 0 
# Donc I(e) différent de 0 (car division par 0 impossible)
# -(F*x**3)/6+(F*L*x**2)/2+r*S(e)*g*((L**2*x**2)/4-(L*x**3)/6+(x**4)/24) = 0
# (F*x**3)/6-(F*L*x**2)/2 = r*S(e)*g*((L**2*x**2)/4-(L*x**3)/6+(x**4)/24)
# ((F*x**3)/6-(F*L*x**2)/2)/(r*g*((L**2*x**2)/4-(L*x**3)/6+(x**4)/24)) = S(e)
# ((F*x**3)/6-(F*L*x**2)/2)/(r*g*((L**2*x**2)/4-(L*x**3)/6+(x**4)/24)) = pi*((d**2)/4-(d/2-e)**2)
# (((F*x**3)/6-(F*L*x**2)/2)/(r*g*((L**2*x**2)/4-(L*x**3)/6+(x**4)/24)))/(pi*(d**2)/4) = pi*(-(d/2-e)**2)
# (((F*x**3)/6-(F*L*x**2)/2)/(r*g*((L**2*x**2)/4-(L*x**3)/6+(x**4)/24)))/(pi*((d**2)/4-((d**2)/4)-d)) = e**2
# sqrt((((F*x**3)/6-(F*L*x**2)/2)/(r*g*((L**2*x**2)/4-(L*x**3)/6+(x**4)/24)))/(pi*(d**2)/4)) = e

def ev(e):
    e = 0
    while not v(x,e) == 0:
        for i in range(0,n):
            e = i+1
            y = v(x,e)
            return y 
        return e
    return e

        