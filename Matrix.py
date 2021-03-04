import numpy as np



raw_evals, evecs = np.linalg.eig(M)                                             #getting a array of eigenvalues and matrix of eigenvectors
rounded_evals = np.around(np.array(raw_evals),2)                                #rounding the eigenvalues to 1 d.p


print('Eigenvectors and eigenvalues:\n')
i = 0
while i < max(M.shape):
    print('The eigenvector ' + str(evecs[:,i])
    + ' has the corresponding eigenvalue ' + str(rounded_evals[i]))
    i = i + 1

#prints unique eigenvalues and degeneracies
print('\nReal Eigenvalues and Degeneracies\n')
from collections import Counter                                                 #import the counter
list_evals = Counter(rounded_evals)                                             #create a new list with attached multiplicites
for k,v in list_evals.items():                                                  #printing the eiqenvalues and the degeneracies
    print('Eigenvalue:   ' + str(k      ), 'Multiplicity:   ' + str(v   ))
