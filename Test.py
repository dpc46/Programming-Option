import numpy as np

n = 10 #dimensions of Huckel Matrix
M = np.zeros((n, n)) # A nxn matrix of zeros

a = 0 #define alpha
b = -1 #define beta

#assign the Huckel elements
i = 0
while i < n - 1:
    M[i,i] = a #diagonals = alpha
    M[i,i - 1] = b #elements adjacent to diagonals = beta
    M[i,i + 1] = b
    i = i + 1
M[n - 1,n - 1] = a #nxn element
M[n - 1,n - 2] = b #nx(n-1) element
M[n - 1,0] = b #nx(n-1) element
print('Huckel Matrix:\n')
print(M)

#Generates evals[i] the eigenvectors and evecs[:,i] the corresponding normalised eigenvectors for a square matrix
raw_evals, evecs = np.linalg.eig(M)                 #getting a array of eigenvalues and matrix of eigenvectors
rounded_evals = np.around(np.array(raw_evals),2)    #rounding the eigenvalues to 1 d.p

#prints eigenvectors and corresponding eigenvalues
print('\nEigenvectors and eigenvalues:\n')
i = 0
while i < max(M.shape):
    print('\nThe eigenvector ' + str(evecs[:,i])
    + ' has the corresponding eigenvalue ' + str(rounded_evals[i]))
    i = i + 1

#prints unique eigenvalues and degeneracies
print('\nDegeneracies of the Eigenvalues\n')
from collections import Counter                #import the counter
list_evals = Counter(rounded_evals)            #create a new list with attached multiplicites
for k,v in list_evals.items():                 #printing the eiqenvalues and the degeneracies
    print('Eigenvalue:   ' + str(k      ), 'Multiplicity:   ' + str(v   ))
