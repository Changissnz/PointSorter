import numpy as np
import math

def equal_iterables(i1, i2, roundPlaces = 5):

    if len(i1) != len(i2): return False
    if np.all(np.equal(np.round(i1, roundPlaces), np.round(i2, roundPlaces)) == True): return True
    return False

def is_2dmatrix(m):
    if type(m) is not np.ndarray: return False
    if len(m.shape) != 2: return False
    return True

def is_vector(m):
    if type(m) is not np.ndarray: return False
    if len(m.shape) != 1: return False
    return True

def is_valid_point(point):
    assert not type(point) is np.ndarray, "point cannot be np.ndarray"
    if len(point) != 2: return False
    if not type(point[0]) in [int, float, np.int64, np.float64]: return False# or type(point[0]) is float): return False
    if not type(point[1]) in [int, float, np.int64, np.float64]: return False
    return True
