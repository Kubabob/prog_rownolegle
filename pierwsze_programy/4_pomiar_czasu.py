from time import time

from mpi4py import MPI

comm_world = MPI.COMM_WORLD

my_index = comm_world.Get_rank()
# buffer = my_index + 1

if my_index % 2 == 0:
    print(f"{my_index}. Ping")
    comm_world.send(time(), dest=my_index + 1, tag=1)
else:
    received_time = comm_world.recv(source=my_index - 1, tag=1)
    print(f"{my_index}. Pong took: {time()-received_time} s")
