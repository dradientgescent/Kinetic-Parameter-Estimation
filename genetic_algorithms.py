import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd
import random
from pyeasyga import pyeasyga
from sklearn.metrics import mean_squared_error
import math
import scipy.optimize as optimize
from odesolver import solveODES

#Genetic Algorithm using pyeasyga
class GA():

    def __init__(self, data):
        self.data = data

    def create_individual(self, data):

        random_list=np.around(np.arange(0, 100, 0.01), decimals=2)
        random_list_2 = np.around(np.arange(0, 10, 0.05), decimals=2)
        individual = [random.choice(random_list_2), random.choice(random_list_2), random.choice(random_list_2)]
        return individual


    def fitness(self, individual, data):
        fitness_val = self.findlsq(individual)
        return fitness_val

    def findlsq(self, individual):
        individual=list(individual)

        ODE = solveODES(self.data, individual[0], individual[1], individual[2])

        ODEsoln = ODE.solve()

        error_sum = mean_squared_error(self.data['MKKK'], ODEsoln[:, 0]) + mean_squared_error(self.data['MKKK_P'],
                                                                                 ODEsoln[:, 1]) + mean_squared_error(
            self.data['MKK'], ODEsoln[:, 2]) + mean_squared_error(self.data['MKK_P'], ODEsoln[:, 3]) + mean_squared_error(self.data['MKK_PP'], ODEsoln[:,
                                                                                                        4]) + mean_squared_error(
            self.data['MAPK'], ODEsoln[:, 5]) + mean_squared_error(self.data['MAPK_P'], ODEsoln[:, 6]) + mean_squared_error(self.data['MAPK_PP'],
                                                                                                  ODEsoln[:, 7])
        return error_sum

    def run_ga(self):

        seed_data = [0.00, 0.00, 0.00]
        ga = pyeasyga.GeneticAlgorithm(seed_data,
                                       population_size=1000,
                                       generations=5,
                                       crossover_probability=0.8,
                                       mutation_probability=0.05,
                                       elitism=True,
                                       maximise_fitness=False)  # initialise the GA with data

        ga.create_individual = self.create_individual
        ga.fitness_function = self.fitness # set the GA's fitness function
        ga.run()  # run the GA

        #print(ga.best_individual())  # print the GA's best solution
        return(ga.best_individual())


#I tried to write my own GA and failed
class GA_custom():

    def __init__(self, data):
        self.data = data

    def create_individual(self):
        random_list=np.around(np.arange(0, 10000, 1), decimals=2)
        random_list_2 = np.around(np.arange(0, 1, 0.01), decimals=2)
        individual = [bin(random.choice(random_list))[2:], bin(random.choice(random_list))[2:], bin(random.choice(random_list))[2:]]
        return individual

    def create_population(self, pop_size):
        population=[]
        for i in range(pop_size):
            population.append(self.create_individual())

        return population

    def crossover(self, individual1, individual2):
        decider=np.random.random()
        if(decider<=0.33):
            individual1[0], individual2[0] = individual2[0], individual1[0]
        elif(0.33<decider<=0.66):
            individual1[1], individual2[1] = individual2[1], individual1[1]
        elif(decider>0.66):
            individual1[2], individual2[2] = individual2[2], individual1[2]
        return(individual1, individual2)

    def fitness(self, individual):
        fitness_value = self.findlsq(individual)
        return fitness_value

    def findlsq(self, individual):

        ODE = solveODES(self.data, int(individual[0], 2)/100, int(individual[1], 2)/100, int(individual[2], 2)/100)

        ODEsoln = ODE.solve()

        error_sum = mean_squared_error(self.data['MKKK'], ODEsoln[:, 0]) + mean_squared_error(self.data['MKKK_P'],
                                                                                              ODEsoln[:,
                                                                                              1]) + mean_squared_error(
            self.data['MKK'], ODEsoln[:, 2]) + mean_squared_error(self.data['MKK_P'],
                                                                  ODEsoln[:, 3]) + mean_squared_error(
            self.data['MKK_PP'], ODEsoln[:,
                                 4]) + mean_squared_error(
            self.data['MAPK'], ODEsoln[:, 5]) + mean_squared_error(self.data['MAPK_P'],
                                                                   ODEsoln[:, 6]) + mean_squared_error(
            self.data['MAPK_PP'],ODEsoln[:, 7])
        return error_sum

    def run_GA(self, crossover_thresh):
        pop_size=1024
        population=self.create_population(pop_size)
        print(population)
        n=1

        for i in range(n):

            for j in range(len(population)):
                crossover_point=np.random.uniform(0,1)
                if (crossover_point>crossover_thresh):
                    player1 = np.random.randint(len(population))
                    player2 = np.random.randint(len(population))
                    population[player1], population[player2] = self.crossover(population[player1], population[player2])
            fitness_val = []
            new_population=[]
            #print(len(population))
            for j in range(len(population)):
                fitness_val.append(self.fitness(population[j]))
                #print(fitness_val[j])


            while(len(population)>1):
                print(len(population))
                player1 = np.random.randint(len(population)-1)
                player2 = np.random.randint(len(population)-1)
                #print(player1, player2)
                if not player1==player2:
                    if fitness_val[player1]<fitness_val[player2]:
                        new_population.append(population[player1])
                    else:
                        new_population.append(population[player2])
                    population.pop(player1)
                    population.pop(player2)

            population=new_population

        return population
