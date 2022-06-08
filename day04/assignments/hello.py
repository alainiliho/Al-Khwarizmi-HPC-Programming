from mpi4py import MPI
COMM = MPI.COMM_WORLD
SIZE =  RANK = COMM.Get_size()
RANK = COMM.Get_rank()
print(f"Hello from the rank {RANK} process")
if RANK == 2:
    print(f"Parallel execution of hello_world with {SIZE} processes")
