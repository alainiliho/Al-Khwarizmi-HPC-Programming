
from mpi4py import MPI

COMM = MPI.COMM_WORLD
RANK = COMM.Get_rank()
SIZE = COMM.Get_size()

if RANK == 0:
    #data_send = int(input("Enter data : "))
    data_send = 77
    COMM.send(data_send, dest = RANK+1)

if RANK != 0:
    RECEIVER = RANK - 1
    received = COMM.recv(source=RECEIVER)
    print("\n")
    print(f"Process {RANK} got {received} from process {RECEIVER}".format(RANK, received, RECEIVER))

    if RANK < SIZE - 1:
        COMM.send(received, dest = RANK+1)
