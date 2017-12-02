#Phonons are at 0.050000  0.550000 -0.850000
#              -0.925000 -0.175000  0.000000
#              -0.550000  0.550000  0.950000
phonons = [(0.05, 0.55, -0.85), (-0.925, -0.175, 0), (-0.55, 0.55, 0.95)]
sim_freqs = [[ 48.902400, 56.260037, 118.820029, 130.497601, 168.753287, 169.145131 ],
[ 42.022230, 42.651243, 130.618682, 143.832517, 169.313370, 169.442592 ],
[ 39.207425, 51.038814, 92.462542, 151.554859, 173.427760, 174.890652]]
calc_freqs = [[ 49.7764, 57.5315, 120.1028, 134.0122, 169.8094, 172.1224 ],
              [ 48.2145, 48.6509, 130.9656, 143.7324, 169.8254, 170.4830 ],
              [ 41.0749, 53.9518, 93.2524,  154.5862, 173.5408, 175.8468 ]]

diffs = [[abs(sim_freqs[i][j]-calc_freqs[i][j]) for j in range(len(sim_freqs[0]))] for i in range(len(sim_freqs))]
diff_ratio = [[diffs[i][j]/sim_freqs[i][j] for j in range(len(sim_freqs[0]))] for i in range(len(sim_freqs))]

for i in range(len(phonons)):
    print("For phonon ", (i+1), " ", phonons[i], ":", sep='')
    print("{:^25}{:^25}{:^25}".format("Simulated Phonon(cm^-1)", "Matdyn Phonons(cm^-1)", "Percentage difference"))
    for j in range(len(sim_freqs[0])):
        print("{:^25}{:^25}{:^25,.2%}".format(sim_freqs[i][j], calc_freqs[i][j], diff_ratio[i][j]))
    print()
