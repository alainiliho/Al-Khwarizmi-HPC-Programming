
import random 
import timeit
from mpi4py import MPI

COMM = MPI.COMM_WORLD
PROCESSES = COMM.Get_size()
RANK = COMM.Get_rank()

INTERVAL = 1000 ** 2

LOCAL_INT = INTERVAL // PROCESSES 
random.seed(42)  

def generate_points():

    points = 0
    
    for _ in range(LOCAL_INT):

        x = random.uniform(0, 2) 
        y = random.uniform(0, 2) 

        if (x - 1)**2 + (y - 1)**2 <= 1: 
            points += 1
    
    return points 


start = timeit.default_timer()
POINTS = generate_points()
end = timeit.default_timer()

POINTS = COMM.reduce(POINTS, op = MPI.SUM, root = 0)
if RANK == 0:
    
    PI = 4 * POINTS/ INTERVAL
    print("\n")
    print("Circle points => ", POINTS)
    print("PI estimation => ", PI)
    print("CPU TIME => ", (end - start) * 1000)
