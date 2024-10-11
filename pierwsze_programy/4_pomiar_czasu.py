from mpi4py import MPI
from time import time_ns

comm_world = MPI.COMM_WORLD

my_index = comm_world.Get_rank()
#buffer = my_index + 1

if my_index % 2 == 0:
    print(f'{my_index}. Ping')
    comm_world.send(time_ns(), dest=my_index+1, tag=1)
else:
    received_time = comm_world.recv(source=my_index-1, tag=1)
    print(f'{my_index}. Pong took: {time_ns()-received_time} ns')
