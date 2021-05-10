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

# using fromiter function

mr_Hue_report = "cit studnets are good to go for thier friday presentation"

response = np.fromiter(mr_Hue_report, dtype="U2")
print(response)

# we are to demostrate how full() function is used

cit_full = np.full([3, 5], 55)
print(cit_full)

list1 = [2,4,7,8,9]
list2 = [4,5,6,7,8]

vector1 = np.array(list1)
vector2 = np.array(list2)

addition = vector1 + vector2

print("additional vector : "+ str(addition))
sub = vector1 + vector2
print("Subtraction vector:" + str(sub))

multi = vector1 * vector2
print("Multiplication vector :" + str(multi))

# how to use fromrecords() function
# syntax format
# numpy.core.fromrecoreds([(tuple1),(tuple2)], metadata)
# returns a records array

cit_record = np.core.records.fromrecords([(1, 'Dashone',27),(2, 'Elijah',34)], names ='Joseph,Name,Age')
print(cit_record[:1])

# using view() function in numpy

Array = np.array([1,2,3,4,4,5,5,9])
#creating the view
V1 = Array.view()
print("identity of array", id(Array))
print("identity of array",id(V1))
Array[3] = 4
# printinting array and view
print("original array", Array)
print("view", V1)

# making use of copy() function to operate on array
Cpy = np.array([3,4,5,6,66,7,75,6])
#createing a copy array
C = Cpy.copy()
# print out our original arry Cpy ids in the memory
print(id(Cpy))
print(id(C))

# changing the value of an elemnt in the position
Cpy[3] = 100
# pprint Cpy
print("original copy array", Cpy)
print("copy", C)

# using np.empty_like() function
# np.empty_like(a, dtype=None, order='K', subok= True)

Like = np.array([13, 45, 56, 5, 6, 77, 8, 67, 7, 8
                 , 9, 900, 64])
print(Like)
Copy_like = np.empty_like(Like)
Copy_like[:] = Like
print("\n copy of the given array")
print(Copy_like)

