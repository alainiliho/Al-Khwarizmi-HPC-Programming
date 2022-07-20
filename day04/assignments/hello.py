from mpi4py import MPI
if __name__ == '__main__':
    
    COMM = MPI.COMM_WORLD
    SIZE =  RANK = COMM.Get_size()
    RANK = COMM.Get_rank()

    print(f"Hello from the rank {RANK} process")

    COMM.Barrier()
    if RANK == 0:

        print(f"Parallel execution of hello_world with {SIZE} processes")
        
