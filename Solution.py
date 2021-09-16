import numpy
numpy.set_printoptions(legacy='1.13')

arr = input()
arr = arr.split(" ")

for x in range(len(arr)):
    arr[x] = float(arr[x])

#floor
#ceil
#rint

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
