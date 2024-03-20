# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:32:10 2021

@author: danie
"""

import numpy as np

# take data from file
P = np.loadtxt('Input_PVS.csv', dtype=str, delimiter=',', skiprows=1, usecols=0)
V = np.loadtxt('Input_PVS.csv', dtype=float, delimiter=',', skiprows=1, usecols=1)
S = np.loadtxt('Input_PVS.csv', dtype=int, delimiter=',', skiprows=1, usecols=2)

# determine no. of seats still to allocate
totSeats = int(input('How many seats should be apportioned?\n'))
rounds = totSeats - np.sum(S)
if rounds < 0:
    print('Error: more initial seats allocated than total seats availabe')
    exit()

# choose between apportionment formulae
m = int(input('''Which formula should be used?
1 -- D'Hondt method
2 -- Sainte-Laguë method
'''))

# calculate number of seats for each state
for i in range(rounds):
    Q = V / (m*S+1)
    a = np.argmax(Q)
    S[a] = S[a] + 1

# output apportionment into CSV file
np.savetxt('seat_output.csv', S, fmt='%d', delimiter=',')


