# line sapce function return number spaces evenly w.r.t interval

# example of the line space

# numpy.linespace(start, stop, num=50, endpoint = "True", retstep = "False" dtype = None)


import numpy as np
print("B\n", np.linspace(2, 0, num=5, retstep=True), "\n")
print()
cit_2 = np.linspace(2, 4, 45)
print("A\n", np.sin(cit_2))


#  using eye function in numpy

fred = np.eye(3, 5, dtype=float)

print("matrix of the array can be given as: \n", fred)

jos = np.eye(5, 8, k=-1)

print("Get the matrix of jose \n", jos)

cit = np.linspace(-2, 4, 8)

cit_3 = np.linspace(-9, 9, 12)

cit, cit_3 = np.meshgrid(cit, cit_3)
print("cit =")
print(cit)
print("cit_3 =")
print(cit_3)
