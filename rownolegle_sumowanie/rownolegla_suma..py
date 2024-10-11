from mpi4py import MPI
ile=10000000

start = MPI.Wtime()
comm_world = MPI.COMM_WORLD
processes_number = comm_world.Get_size()
my_rank = comm_world.Get_rank()
