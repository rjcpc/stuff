'''
--------------Practical 8------------------
Aim: Write a program to do the following :
1. Enter a Vector b and find the projection of b orthogonal to a given vector u.
2. Find the projection of b orthogonal to a set of given vectors.
'''


def dot(x, y):
    return sum([x[i] * y[i] for i in range(len(x))])


def scalar(a, v):
    return [a * v[i] for i in range(len(v))]


def sub(u, v):
    return [u[i] - v[i] for i in range(len(v))]


def project_algo(b, v):
    sigma = (dot(b, v) / dot(v, v)) if dot(v, v) != 0 else 0
    return scalar(sigma, v)


def project_orthogonal(b, v):
    return sub(b, project_algo(b, v))


def project_orthogonalVectorSet(b, s):
    for i in range(len(s)):
        v = s[i]
        b = project_orthogonal(b, v)
    return b


print(project_orthogonal([5, -5, 2], [8, -2, 2]))

'''
Output :
>>> 
[-1.0, -3.5, 0.5]
'''
