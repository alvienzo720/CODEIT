import numpy as np

ourArray = np.arange(100).reshape(10, 10)

print(ourArray)
print()
print("We will print the vsplit here :")
print()
print("we get {} for the vsplit which is {}".format(ourArray, np.vsplit(ourArray, 10), sep="\n\n"))




