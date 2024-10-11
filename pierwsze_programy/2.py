from mpi4py import MPI
import mpi4py
comm_world = MPI.COMM_WORLD
size = comm_world.Get_size()
my_rank = comm_world.Get_rank()
name = MPI.Get_processor_name()
if (my_rank == 0):
   print("Hello World!")
print(f"I am process {my_rank} out of {size} on {name}")
