import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd
import random
from pyeasyga import pyeasyga
from sklearn.metrics import mean_squared_error
import math
import scipy.optimize as optimize

class solveODES():

    def __init__(self, data, p1, p2, p3):
        self.data = data
        self.p1=p1
        self.p2=p2
        self.p3=p3

    @staticmethod
    def f(y, t, params):
        x1, x2, x3, x4, x5, x6, x7, x8 = y  # unpack current values of y
        V1, K1, p3, p1, p2, K2, K3, K4, K5, K6, K7, K8, K9, K10, KI, V9, V10 = params  # unpack parameters

        # define derivatives
        r1 = V1 * x1 / (((1 + x8 / KI) ** 2) * (K1 + x1))
        r2 = p3 * x2 / (K2 + x2)
        r3 = p1 * x2 * x3 / (K3 + x3)
        r4 = p1 * x2 * x4 / (K4 + x4)
        r5 = p2 * x5 / (K5 + x5)
        r6 = p2 * x4 / (K6 + x4)
        r7 = p1 * x5 * x6 / (K7 + x6)
        r8 = p1 * x5 * x7 / (K8 + x7)
        r9 = V9 * x8 / (K9 + x8)
        r10 = V10 * x7 / (K10 + x7)

        derivs = [r2 - r1, r1 - r2, r6 - r3, r3 + r5 - r4 - r6, r4 - r5, r10 - r7, r7 + r9 - r8 - r10, r8 - r9]
        return derivs

    def solve(self):
        # Parameters
        KI, V1, V9, V10, K1, K2 = 9, 2.5, 0.5, 0.5, 10, 8
        K3 = K4 = K5 = K6 = K7 = K8 = K9 = K10 = 15
        # p1=0.04
        # p2=2
        # p3=1

        # Initial values
        x10, x20, x30, x40, x50, x60, x70, x80 = 90, 10, 280, 10, 10, 280, 10, 10

        # Bundle parameters for ODE solver
        params = [V1, K1, self.p3, self.p1, self.p2, K2, K3, K4, K5, K6, K7, K8, K9, K10, KI, V9, V10]

        # Bundle initial conditions for ODE solver
        y0 = [x10, x20, x30, x40, x50, x60, x70, x80]

        # Make time array for solution
        # tStop = 8000.
        # tInc = 0.01
        # t = np.arange(0., tStop, tInc)
        t = self.data['time']

        # Call the ODE solver
        psoln = odeint(self.f, y0, t, args=(params,), full_output=True)
        '''
        # Plot results
        fig = plt.figure(1, figsize=(8,8))

        ax1 = fig.add_subplot(211)
        #ax1.plot(t, psoln[:,0], 'r')
        ax1.plot(t, psoln[:,1], 'b')


        ax1.plot(t, psoln[:,2], 'g')
        ax1.plot(t, psoln[:,3], 'orange')
        ax1.plot(t, psoln[:,4], 'black')
        ax1.plot(t, psoln[:,5], 'g')

        #ax2 = fig.add_subplot(312)
        #ax2.plot(time, MKKK)

        ax3 = fig.add_subplot(212)
        ax3.plot(time, MKKK_P)
        plt.show()
        '''
        #print(self.p1, self.p2, self.p3)
        #print(psoln[0])
        return psoln[0]