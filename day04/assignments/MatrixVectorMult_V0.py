
import time 
import numpy as np
from scipy.sparse import lil_matrix
from numpy.random import rand, seed
from numba import njit
from mpi4py import MPI

COMM = MPI.COMM_WORLD
PRECESSES = COMM.Get_size()
RANK = COMM.Get_rank()


def MatProduct(A, B, C):
    
    rows, columns = A.shape
    for i in range(rows):
        a = A[i]
        for j in range(columns):
            C[i] += a[j] * B[j]

    return 0


LENGTH = 1000
LOCAL_LENGTH = LENGTH // PRECESSES

process_block = LOCAL_LENGTH * LENGTH
counts =  [process_block for i in range(PRECESSES)]

if RANK == 0:
    A = lil_matrix((LENGTH, LENGTH))
    A[0, :100] = rand(100)
    A[1, 100:200] = A[0, :100]

    A.setdiag(rand(LENGTH))
    A = A.toarray()
    b = rand(LENGTH)
else :
    A = None
    b = None

localMatrix = np.empty((LOCAL_LENGTH, LENGTH), dtype = np.float64)
b = COMM.bcast(b, root = 0)

COMM.Scatterv([A, counts, MPI.DOUBLE], localMatrix, root = 0)

localC = np.zeros(LOCAL_LENGTH)
START = MPI.Wtime()
MatProduct(localMatrix, b, localC)

END = MPI.Wtime()
if RANK == 0:
    print("\n")
    print("CPU time of parallel multiplication using", PRECESSES,"processes is ", (END - START)*1000)


sendcounts = [LOCAL_LENGTH for i in range(PRECESSES)] 
if RANK == 0: 
    C = np.empty(LENGTH, dtype = np.float64)
else :
    C = None

COMM.Gatherv(localC,[C, sendcounts, MPI.DOUBLE], root = 0)

if RANK == 0 :
    C_TRUE = A.dot(b)
    print("The error comparing to the dot product is :", np.max(C_TRUE - C))
