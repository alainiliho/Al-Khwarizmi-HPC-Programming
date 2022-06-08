# write your program here
from mpi4py import MPI

def share():

	COMM = MPI.COMM_WORLD
	SIZE = COMM.Get_size()
	RANK = COMM.Get_rank()
	data_to_send = []

	if RANK == 0:
		entered = int(input('Enter an inter : '))
		while entered > 0:
			data_to_send.append(entered)
			entered = int(input('Enter an inter : '))

	recv_data = COMM.bcast(data_to_send, root=0)

	print(f"Process {RANK} got {recv_data}")

if __name__ == '__main__':
	share()
