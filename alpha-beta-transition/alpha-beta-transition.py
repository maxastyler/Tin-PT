import matplotlib.pyplot as plt

scf_energy = {'beta': -318.48639253, 'alpha': -318.48981430}
def read_energies(fname):
    temps = {}
    with open(fname) as f:
        for line in f.readlines():
            (t, e) = line.split()
            t=float(t)
            e=float(e)
            temps[t] = e
    return temps

temps_alpha = read_energies('sn.alpha.fe')
temps_beta = read_energies('sn.beta.fe')
for t in temps_alpha: temps_alpha[t]+=scf_energy['alpha']
for t in temps_beta: temps_beta[t]+=scf_energy['beta']
ts_alpha = sorted(temps_alpha.keys())
es_alpha = [temps_alpha[i] for i in ts_alpha]
ts_beta = sorted(temps_beta.keys())
es_beta = [temps_beta[i] for i in ts_beta]
crossing_i = 0
for i in range(len(ts_beta)):
    if es_beta[i]<es_alpha[i]:
        crossing_i = i
        break
a_x1 = ts_alpha[i-1]
a_x2 = ts_alpha[i]
b_x1 = ts_beta[i-1]
b_x2 = ts_beta[i]
a_y1 = es_alpha[i-1]
a_y2 = es_alpha[i]
b_y1 = es_beta[i-1]
b_y2 = es_beta[i]
a_m = (a_y2 - a_y1)/(a_x2-a_x1)
b_m = (b_y2 - b_y1)/(b_x2-b_x1)
a_c = a_y1 - a_m*a_x1
b_c = b_y1 - b_m*b_x1
cross_x = (a_c-b_c)/(b_m-a_m)
print("The crossing temperature is: {:2g}K".format(cross_x))
plt.xlabel(r"Temperature $(K)$")
plt.ylabel(r"Free Energy $(Ry)$")
plt.title(r'')
plt.plot(ts_beta, es_beta, 'red')
plt.plot(ts_alpha, es_alpha, 'blue')
plt.axvline(cross_x, color = 'black')
plt.title(r'$\alpha,\beta$-Sn Free Energy vs Temperature')
plt.legend([r'$\beta$-Sn', r'$\alpha$-Sn', r'Crossing $(T=542.88K)$'])
plt.gcf().set_size_inches(11, 5)
plt.tight_layout()
plt.savefig('../../Sodium-DFT-Project/project_presentation/tin_transition_temperature.png')
plt.show()
