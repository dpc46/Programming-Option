import numpy as np

n = 0
while n == 0:
    try:
        n = int(input('Please enter the number of carbons\n'))
    except ValueError:
        print('Please enter an integer number\n')

print('\nThis is modelling a system with ' + str(n) + ' carbons\n')

M = np.zeros((n, n))        # A nxn matrix of zeros

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


i = 0                       #inputing Huckel elements to matrix
while i < n:
    M[i,i] = a              #diagonals = alpha

    if i == 0:
        M[i,i + 1] = b      #first row beta element

    elif i == n - 1:
        M[i, i - 1] = b     #last row beta element

    else:
        M[i,i - 1] = b      #elements adjacent to diagonals = beta
        M[i,i + 1] = b

    i = i + 1


print('Huckel Matrix for a linear polyene with ' + str(n) + ' carbons:\n')
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
print('\nMultiplicities of Eigenvalues:\n')
from collections import Counter                                                 #import the counter
list_evals = Counter(rounded_evals)                                             #create a new list with attached multiplicites
for k,v in list_evals.items():                                                  #printing the eiqenvalues and the degeneracies
    print('Eigenvalue:   ' + str(k      ), 'Multiplicity:   ' + str(v   ))
