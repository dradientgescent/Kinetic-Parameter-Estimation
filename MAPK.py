import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd
import random
from pyeasyga import pyeasyga
from sklearn.metrics import mean_squared_error
import math
import scipy.optimize as optimize
from genetic_algorithms import *
from data import *
from odesolver import *


class Nelder_Mead():

    def __init__(self, data, initial_estimates):
        self.data = data
        self.initial_estimates = initial_estimates

    def findlsq(self, params):

        param1, param2, param3 = params
        ODE = solveODES(self.data, param1, param2, param3)
        ODEsoln = ODE.solve()

        error_sum = mean_squared_error(self.data['MKKK'], ODEsoln[:, 0]) + mean_squared_error(self.data['MKKK_P'],
                                                                                     ODEsoln[:, 1]) + mean_squared_error(
                self.data['MKK'], ODEsoln[:, 2]) + mean_squared_error(self.data['MKK_P'], ODEsoln[:, 3]) + mean_squared_error(self.data['MKK_PP'], ODEsoln[:,
                                                                                                            4]) + mean_squared_error(
                self.data['MAPK'], ODEsoln[:, 5]) + mean_squared_error(self.data['MAPK_P'], ODEsoln[:, 6]) + mean_squared_error(self.data['MAPK_PP'],
                                                                                                      ODEsoln[:, 7])
        return error_sum

    def run_NM(self):

        if self.initial_estimates != None:
            #Feed initial estimates to Nelder-Mead
            initial=np.array([self.initial_estimates[1][0], self.initial_estimates[1][1], self.initial_estimates[1][2]])
        else:
            initial = np.array([4.5, 5, 5.5])


        ret = optimize.minimize(self.findlsq, initial, method='Nelder-Mead', options={'maxiter':500})
        #ret_random = optimize.minimize(self.findlsq, initial2, method='Nelder-Mead', options={'maxiter':500})
        mybounds=[(0,10), (0,10), (0,10)]


        #print('GA solution=', self.initial_estimates)

        print('optimum after GA=', ret.x, ret.fun)
        #print('optimum on random sampling=', ret_random.x, ret_random.fun)
        return ret.x


if __name__=='__main__':
    # prepare_data
    data_dict = prepare_data("dataset2.dat")

    Genetic_Algorithm = GA_custom(data_dict)
    # get initial estimates from GA

    initial_estimates = Genetic_Algorithm.run_GA(crossover_thresh=0.5)

    print('GA Estimates:', initial_estimates[1][0], initial_estimates[1][1], initial_estimates[1][2])

    NM = Nelder_Mead(data_dict, initial_estimates)

    final_estimates = NM.run_NM()