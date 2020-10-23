import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  np_arr = np.array(list).reshape(3,3)
  calculations = {
    'mean': [np_arr.mean(axis=0).tolist(), np_arr.mean(axis=1).tolist(), np_arr.mean()],
    'variance': [np_arr.var(axis=0).tolist(), np_arr.var(axis=1).tolist(), np_arr.var()],
    'standard deviation': [np_arr.std(axis=0).tolist(), np_arr.std(axis=1).tolist(), np_arr.std()],
    'max': [np_arr.max(axis=0).tolist(), np_arr.max(axis=1).tolist(), np_arr.max()],
    'min': [np_arr.min(axis=0).tolist(), np_arr.min(axis=1).tolist(), np_arr.min()],
    'sum': [np_arr.sum(axis=0).tolist(), np_arr.sum(axis=1).tolist(), np_arr.sum()]
  }
  return calculations