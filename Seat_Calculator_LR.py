# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:32:10 2021

@author: danie
"""

import numpy as np

# take data from file
P = np.loadtxt('Input_PVS.csv', dtype=str, delimiter=',', skiprows=1, usecols=0)
V = np.loadtxt('Input_PVS.csv', dtype=float, delimiter=',', skiprows=1, usecols=1)
S = np.zeros(len(P))

# determine no. of seats still to allocate
totSeats = int(input('How many seats should be apportioned?\n'))

# calculate number of seats for each party
Quota = np.sum(V) / totSeats
Q = V / Quota # calculates 'ideal' fractional number of seats for each party
S = Q.astype(int) # floors quotients to calculate initial seat numbers
R = Q - S
add = totSeats - np.sum(S)
Rs = R.argsort()[-add:] # add extra seat to parties with largest remainder vote
S[Rs] = S[Rs] + 1

# output apportionment into CSV file
np.savetxt('seat_output.csv', S, fmt='%d', delimiter=',')