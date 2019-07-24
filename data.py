import math
import numpy as np

def prepare_data(path):

    MAPK_cascade = np.loadtxt(path, skiprows=1)

    columns = ['time', 'MKKK', 'MKKK_P', 'MKK', 'MKK_P', 'MKK_PP', 'MAPK', 'MAPK_P', 'MAPK_PP']
    data_dict =  {}

    for i, item in enumerate(columns):
        data_dict[item] = MAPK_cascade[:, i]
    '''
    time = MAPK_cascade[:, 0]
    MKKK = MAPK_cascade[:, 1]
    MKKK_P = MAPK_cascade[:, 2]
    MKK = MAPK_cascade[:, 3]
    MKK_P = MAPK_cascade[:, 4]
    MKK_PP = MAPK_cascade[:, 5]
    MAPK = MAPK_cascade[:, 6]
    MAPK_P = MAPK_cascade[:, 7]
    MAPK_PP = MAPK_cascade[:, 8]
    '''

    #Prepare experimental data
    for column in np.ndarray.transpose(MAPK_cascade[:,2:8]):
        for i in range(len(data_dict['MKKK'])):
            if math.isnan(column[i])==True:
                column[i] = np.around(np.nanmean(column), decimals=2)

    for i in range(len(data_dict['MAPK_PP'])):
        if math.isnan(data_dict['MAPK_PP'][i]) == True:
            data_dict['MAPK_PP'][i] = 300 - data_dict['MAPK_P'][i] - data_dict['MAPK'][i]

    for i in range(len(data_dict['MKKK'])):
        if math.isnan(data_dict['MKKK'][i])==True and math.isnan(data_dict['MKKK_P'][i])==False:
            data_dict['MKKK'][i]=100 - data_dict['MKKK_P'][i]
        if math.isnan(data_dict['MKKK_P'][i])==True and math.isnan(data_dict['MKKK'][i])==False:
            data_dict['MKKK_P'][i]=100 - data_dict['MKKK'][i]
        elif math.isnan(data_dict['MKKK'][i])==True and math.isnan(data_dict['MKKK_P'][i])==True:
            data_dict['MKKK'][i] = np.around(np.nanmean(data_dict['MKKK']), decimals=2)
            data_dict['MKKK_P'][i] = np.around(np.nanmean(data_dict['MKKK_P']), decimals=2)

    return(data_dict)

if __name__=='__main__':
    pass