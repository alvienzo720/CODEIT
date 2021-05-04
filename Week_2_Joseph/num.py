import numpy as cit

CIT = cit.array([1, 3, 4, 5, 7])

print("array with rank 1:   \n", CIT)


CIT3 = cit.array((1, 4, 7, 0))
print("\n array createing using tuples:  \n", CIT3)

CIT2 = cit.array([[2, 3, 4, 6, 7, 1, 5],
                 [4, 5, 6, 8, 9, 12, 13],
                 [4, 9, 7, 5, 5, 10, 11]])

print("Array with rank 2:  \n", CIT2)

slice_CIT = CIT2[:3, ::3]
print("print the array using slicing method \n", slice_CIT)