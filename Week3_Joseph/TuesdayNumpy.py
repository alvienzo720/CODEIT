import numpy as np
# vsplit method on an array
ourArray = np.arange(100).reshape(10, 10)

print(ourArray)
print()
print("We will print the vsplit here :")
print()
print("we get {} for the vsplit which is {}".format(ourArray, np.vsplit(ourArray, 10), sep="\n\n"))


# displit on our array

ourArray2 = np.arange(27).reshape(3, 3, 3)

print("this is the original array as \n\n{} \n\nbut here when it has been worked on \n\n{}".format(ourArray2, np.dsplit(ourArray2, 3)))


# comparison function

fred_cit = np.array([2,3,5])

samuel_cit = np.array([4,5,6])

comparison = fred_cit == samuel_cit

print(comparison)

# numpy unique

a = np.array([[11, 22, 44, 4],
              [23, 45, 56, 77],
              [33, 56, 66, 70],
             [49, 22, 34, 51],
              [11, 44, 34, 56]])

print("the output is: ", a, sep="\n")

Unique_function = np.unique(a, axis=0)

print("Unique rows:", Unique_function, sep="\n")

b = np.array([1, 3, 77, 8, 8, 9, 0, 0])
print("original b array", b)

unique_b_array = np.unique(b)

print(unique_b_array)

# trim_zero()

a = np.array([0,0,0,0,0,0,0,0,1,2,3,4,5,6,0,0,0,0,0])

A = np.trim_zeros(a)
A_ = np.trim_zeros(a, 'f')
B_ = np.trim_zeros(b, 'f')
print(A)
print(A_)
print(B_)


# 4 matrix in mumpy
l = np.array([[2, 3], [4, 5]])
m = np.array([[4, 7], [6, 8]])

print("Get the addition of two matrices which is:")
print(np.add(l, m))

# using the sub traction function
print(np.subtract(l, m))

# Using Division
print(np.divide(l, m))

# use the dot function on the matrix
# use the sqrt() function on the matrix
# use the T function on the matrix
print()
print()
print("The square root of l is :", np.sqrt(l))

print("The square root of m is :", np.sqrt(m))

