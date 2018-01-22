import numpy as np
import matplotlib.pyplot as plt

#This function gets the pressure and energy for a given lattice parameter and k value
def get_p_e(k, lat):
    with open("sn.a.{lat}/sn.a.scf.{lat}.{k}.out".format(lat=lat, k=k)) as f:
        for line in f.readlines():
            if "kbar" in line:
                p=line.split()[-1]
            if "!" in line:
                E=line.split()[-2]
    return float(p), float(E)

lats = np.arange(12.2, 12.7, 0.08)
ks = [6, 8, 10, 12, 14, 16, 18, 20]

k_dict={}

for k in ks:
    es={}
    ps={}
    for a in lats:
        p, e = get_p_e(k, a)
        ps[a]=p
        es[a]=e
    k_dict[k]=(ps, es)

e_side=plt.twinx()

def plot_pressure(k, colour=None):
    plot_either(k, colour, 0)

def plot_energy(k, colour=None):
    plot_either(k, colour, 1)

def plot_either(k, colour, e_or_p): 
    vals = []
    for key in sorted (k_dict[k][e_or_p]):
        if e_or_p==0: vals.append(abs(k_dict[k][e_or_p][key]))
        else: vals.append(k_dict[k][e_or_p][key])
    if colour == None: 
        if e_or_p==0: plt.plot(lats, vals)
        else: e_side.plot(lats, vals)
    else: 
        if e_or_p==0: plt.plot(lats, vals, "{col}".format(col=colour))
        else: e_side.plot(lats, vals, "{col}".format(col=colour))


for k in ks:
    plot_energy(k)
plt.show()
