import numpy as np

n = 0
while n != 4 and n != 6 and n != 8 and n != 12 and n != 20 and n !=60:
    try:
        n = int(input('Please enter the number of carbons (4, 6, 8, 12, 20 or 60)\n'))
    except ValueError:
        print('Please enter an integer number\n')

M = np.zeros((n, n))            #A nxn matrix of zeros

a = 'unassigned'
b = 'unassigned'
while a == 'unassigned':
    try:
        a = int(input('Please enter a value for alpha (suggest a = 0):\n'))
    except ValueError:
        print('Please enter an integer number\n')
while b == 'unassigned':
    try:
        b = int(input('Please enter a value for beta (suggest b = -1):\n'))
    except ValueError:
        print('Please enter an integer number\n')

if n == 4:                      #naming polyhedron
    shape = 'a tetrahedron'
elif n == 6:
    shape = 'an octahedron'
elif n == 8:
    shape = 'a cube'
elif n == 12:
    shape = 'an icosahedron'
elif n == 20:
    shape = 'a dodecahedron'
elif n == 60:
    shape = 'Buckminster Fullerene'

if shape != 0:
    print('\nThis is modelling ' + shape)


i = 0                           #assign the Huckel elements
while i < n:
    M[i,i] = a                  #diagonals = alpha
    M[i,(i - 1) % n] = b        #elements adjacent to diagonals = beta
    M[i,(i + 1) % n] = b        #elements adjacent to diagonals = beta
    p = i // 2
    if p % 2 == 0:
        q = i + 2
    else:
        q = i - 2
    M[i,q % n] = b              #3rd beta element in each row alternates between
    i = i + 1                   #i+2 and i-2 to form correct matrix

print('\nHuckel Matrix for ' + shape + ':\n')
print(M)

raw_evals, evecs = np.linalg.eig(M)                                             #getting a array of eigenvalues and matrix of eigenvectors
rounded_evals = np.around(np.array(raw_evals),2)                                #rounding the eigenvalues to 1 d.p


print('\nEigenvectors and eigenvalues:\n')
i = 0
while i < max(M.shape):
    print('The eigenvector ' + str(evecs[:,i])
    + ' has the corresponding eigenvalue ' + str(rounded_evals[i]))
    i = i + 1

#prints unique eigenvalues and degeneracies
print('\nMultiplicities of Eigenvalues\n')
from collections import Counter                                                 #import the counter
list_evals = Counter(rounded_evals)                                             #create a new list with attached multiplicites
for k,v in list_evals.items():                                                  #printing the eiqenvalues and the degeneracies
    print('Eigenvalue:   ' + str(k      ), 'Multiplicity:   ' + str(v   ))
