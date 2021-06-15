import numpy as np
from scipy.optimize import minimize
import random
import matplotlib.pyplot as plt
import time

from numpy.linalg import inv
from numpy import linalg as LA


import math
from scipy.sparse.linalg import svds


import sys
sys.path.append('fluidity-master')
import vtktools

####################################################

ug = vtktools.vtu('cube_disp_5.vtu')

ug.GetFieldNames()

yourvector = ug.GetScalarField('tracer1')

print(yourvector)

target = yourvector*10

ug.AddScalarField('tracer1', target)

ug.Write('cube_disp_5_copy.vtu')

ug2 = vtktools.vtu('cube_disp_5_copy.vtu')

ug2.GetFieldNames()

tr = ug2.GetScalarField('tracer1')

print(tr)












