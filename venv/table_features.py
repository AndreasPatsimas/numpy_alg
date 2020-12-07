import numpy

D=numpy.array([[1,2,3,4],[5,6,7,8]])
print(D)

type(D)

dims=D.ndim
print(dims)

sha=D.shape
print(sha)

siz=D.size
print(siz)

typ=D.dtype
print(typ)

byt=D.nbytes
print(byt)

isiz=D.itemsize
print(isiz)