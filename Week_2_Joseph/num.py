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


Jacob = cit.array([[4, 3, 5, 8], [3, 7, 9, 10]])
fredrich = cit.array([[5, 6, 10, 5], [3, 5, 7, 8]])
print("adding 1 to Jacob", Jacob + 1)

# constructing a data type object
print(Jacob.dtype)

samuel = cit.array([1.5, 8.6, 9.9, 0.0])
print(samuel.dtype)

