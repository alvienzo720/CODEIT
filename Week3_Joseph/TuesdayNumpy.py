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


# numpuy unique
a = np.array([[11, 22, 44, 4],
              [23, 45, 56, 77],
              [33, 56, 66, 70],
             [49, 22, 34, 51],
              [11, 44, 34, 56]])

print("the output is: ", a, sep="\n")

Unique_function = np.unique(a, axis=0)

print("Unique rows:", Unique_function, sep="\n")