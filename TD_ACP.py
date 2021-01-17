import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
import matplotlib.patches as mpatches


x = np.matrix([[-8 ,-1],
              [6 ,10],
              [-2 ,-10],
              [8 ,1],
              [0 ,3],
              [-6 ,-6],
              [0 ,-3],
              [2 ,6]])


u = np.matrix([[0.6 ,0.8],
               [0.8 ,-0.6]])

x1 = x[: ,0]
x2 = x[: ,1]

v = x.dot(u)


v1 = v[: ,0]
v2 = v[: ,1]

plt.title("Exercice 1") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 

red_patch = mpatches.Patch(color='red', label='le nuage des points individus')
plt.legend(handles=[red_patch])



plt.plot(x1 ,x2 ,"ob") #X en Bleu
plt.plot(v1 ,v2 ,"or") #V en Rouge
plt.savefig('exo1.png')






