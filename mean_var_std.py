import numpy as np

def calculate(list):
    aux = np.array(list)
    media, variancia, standard, maximo, minimo, soma = aux.mean(), aux.var(), aux.std(), aux.max(), aux.min(), aux.sum()
    try:
      aux = aux.reshape((3,3))
    except ValueError:
      raise ValueError("List must contain nine numbers.")
    med1, var1, std1, max1, min1, som1 = aux.mean(axis=0), aux.var(axis=0), aux.std(axis=0), aux.max(axis=0), aux.min(axis=0), aux.sum(axis=0)
    med2, var2, std2, max2, min2, som2 = aux.mean(axis=1), aux.var(axis=1), aux.std(axis=1), aux.max(axis=1), aux.min(axis=1), aux.sum(axis=1)
    calculations = {
      'mean':[med1.tolist(), med2.tolist(), media],
      'variance':[var1.tolist(), var2.tolist(), variancia],
      'standard deviation':[std1.tolist(), std2.tolist(), standard],
      'max':[max1.tolist(),max2.tolist(),maximo],
      'min':[min1.tolist(),min2.tolist(),minimo],
      'sum':[som1.tolist(),som2.tolist(),soma],
    }
    return calculations
