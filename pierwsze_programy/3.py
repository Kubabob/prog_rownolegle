from mpi4py import MPI
comm_world = MPI.COMM_WORLD
my_rank = comm_world.Get_rank()
buffer = my_rank+1
if (my_rank == 0):
   print(f"I am {my_rank} before send ping {buffer=} ")
   comm_world.send(buffer, dest=1, tag=17)
elif (my_rank == 1):
   print(f"I am {my_rank} before recv ping {buffer=} ")
   buffer = comm_world.recv(source=0, tag=17)
   print(f"I am {my_rank} after  recv ping {buffer=} ")
