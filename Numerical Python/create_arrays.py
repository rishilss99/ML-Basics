import numpy as np

a = np.empty((3,4),int)
b = np.empty_like(a)
c = np.eye(3)
d = np.identity(4)
e = np.full(4,np.inf)

f = np.geomspace(2,8,4,True)

r = np.array([1,2,3,4,5])
v = np.vander(r,4,True)
diag = np.diag(v)

print(v)
print(diag)
print(f)

print(a)

