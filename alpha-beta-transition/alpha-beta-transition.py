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
plt.plot(ts_beta, es_beta)
plt.plot(ts_alpha, es_alpha)
plt.show()
