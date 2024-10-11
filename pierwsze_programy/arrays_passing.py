from typing import Mapping
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# passing MPI datatypes explicitly
if rank % 2 == 0:
    start = MPI.Wtime()
    data = numpy.arange(1_000_000, dtype='i')
    comm.send(start, dest=rank+1, tag=100+rank)
    comm.Send([data, MPI.INT], dest=rank+1, tag=rank)
elif rank % 2 == 1:
    data = numpy.empty(1_000_000, dtype='i')
    comm.Recv([data, MPI.INT], source=rank-1, tag=rank)
    start = comm.recv(source=rank-1, tag=100+rank)
    end1 = MPI.Wtime() - start
    print(f"Explicit type took: {end1}s")

# automatic MPI datatype discovery
if rank % 2 == 0:
    start = MPI.Wtime()
    data = numpy.arange(1_000_000, dtype=numpy.float64)
    comm.send(start, dest=rank+1, tag=100+rank)
    comm.Send(data, dest=rank+1, tag=rank)
elif rank % 2 == 1:
    data = numpy.empty(1_000_000, dtype=numpy.float64)
    comm.Recv(data, source=rank-1, tag=rank)
    start = comm.recv(source=rank-1, tag=100+rank)
    end2 = MPI.Wtime() - start
    print(f"Discovered type took: {end2}s")
