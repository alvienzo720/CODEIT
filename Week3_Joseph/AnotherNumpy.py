import numpy as np

cit_array = np.arange(50).reshape(2, 25)
print(cit_array)
print("This is our original array")

cit_array[:, [2, 0]] = cit_array[:, [0, 2]]
print("After swapping")
print(cit_array)

cit_array2 = np.arange(144).reshape(12, 12)
print(cit_array2)


# def swapp_city_array(array, start_index, last_index):
#     array[:, [start_index, last_index]] = array[: [last_index, start_index]]
#
#
# swapp_city_array(cit_array2, 0, 5)
# print("After")
# print(cit_array2)

my_class_in_cit = np.arange(7 * 7).reshape(7, 7)
print(my_class_in_cit)

# array multiplication using numpy.expand_dims()

x = np.zeros((3, 4))

y = np.expand_dims(x, axis=1).shape
print(y)


cit_students = np.arange(6 * 6).reshape(4, 9)
print(cit_students)
new_axis_cit = (0, 3, -1)
cit_students_5D = np.expand_dims(cit_students, axis=new_axis_cit)
print("\n", "*" * 43)
print(cit_students_5D.shape)


# numpy.hstack(tuple)

'''
Tuples :dequence of a ndarray, tup, les  containing array to be stacked
The array must have the same shape along all the second axis

Return : staocked ndarray, the stakced of the input arrays

Here we go 
'''
Cit_in_array = np.array([1,2,34,4,6,8,9])
print("This is the first array creation from user: ", Cit_in_array)

Cit_in_array2 = np.array([3,5,65,6,7,8])
print("This is the second array creation from the user: ", Cit_in_array2)

print()






