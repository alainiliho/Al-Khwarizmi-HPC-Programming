
from mpi4py import MPI

if __name__ == '__main__':
    COMM = MPI.COMM_WORLD
    RANK = COMM.Get_rank()

    if RANK == 0 :
        #data_send = int(input(" Enter data : "))
        data_send = 77
    else :
        data_send = None

    received = COMM.bcast(data_send , root=0)
    print("\n")
    print(f"Proces {RANK} got {received}".format(RANK, received))
