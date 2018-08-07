import numpy as np

num = np.array([[1, 2, 3], [4, 5, 6]])
print num.shape
print num.reshape(3, 2)

num1 = np.array([2, 3, 4, 5, 1], ndmin=2)
print num1.shape
print num1.reshape(5, 1)

num2 = np.array([2.5, 4.3, 5, 7, 1], dtype=complex)
print num2.shape
print num2.reshape(1, 5)

num3 = np.arange(1, 19, 2)
print num3
print num3.ndim
print num3.reshape(3, 3)
print num3.itemsize
print num3.flags #C_CONTIGUOUS,  F_CONTIGUOUS, OWNDATA, WRITEABLE, ALIGNED, UPDATEIFCOPY

# The elements in an array show random values as they are not initialized.
num4 = np.empty([4, 5], dtype=int)
print num4

zero_num = np.zeros(3)
print zero_num

zero_num1 = np.zeros((4), dtype=np.int)
print zero_num1

zero_num2 = np.zeros((3, 4), dtype=np.int)
print zero_num2

ones_num =  np.ones(7)
print ones_num

ones_num1 = np.ones((2, 5), dtype=int)
print ones_num1

convert_num = [3, 1, 6, 8]
print np.asarray(convert_num)
print np.asarray(convert_num, dtype=float)

convert_num1 = (5, 1, 8, 3, 9)
print np.asarray(convert_num1)

convert_num2 = [(2, 5, 4, 9), (0, 3, 7)]
print np.asarray(convert_num2)

changing_array = np.arange(6).reshape(2, 3)
print "array: ", changing_array
print changing_array.flatten()
print "row: ", changing_array.flatten(order='C')
print "coulmn", changing_array.flatten(order='F')


# Minimum and maximum array function
arr = np.array([[2, 4, 5], [1, 4, 7], [9, 3, 8]])
print "array is: ", arr

print "applying minimum: ", np.amin(arr, 1)
print "applying minimum: ", np.amin(arr)
print "applying minimum again: ", np.amin(arr, 0)

print "applying maximum: ", np.amax(arr, 1)
print "applying maximum: ", np.amax(arr)
print "applying maximum again: ", np.amax(arr, 0)



a = np.array([[2, 3, 4], [5, 6, 7], [2, 1, 5]])
print a
print "applying median: ", np.median(a)

print "applying median along axis 0: ", np.median(a, axis=0)
print "applying median along axis 1: ", np.median(a, axis=1)

print "applying mean: ", np.mean(a)
print "applying mean along axis 0: ", np.mean(a, axis=0)
print "applying mean along axis 1: ", np.mean(a, axis=1)

b = np.array([4, 3, 2, 1])
print "average: ", np.average(b)
weight = np.array([1, 2, 3, 4])
print "average function again: ", np.average(b, weights=weight)
print "sum of weights: ", np.average(b, weights=weight, returned=True)


print "standard deviation: ", np.std(b)
print "variance: ", np.var(b)

