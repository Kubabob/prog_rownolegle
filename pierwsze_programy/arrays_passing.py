from typing import Mapping
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# passing MPI datatypes explicitly
if rank == 0:
    start = MPI.Wtime()
    data = numpy.arange(1_000_000_000, dtype='i')
    comm.send(start, dest=1, tag=78)
    comm.Send([data, MPI.INT], dest=1, tag=77)
elif rank == 1:
    data = numpy.empty(1_000_000_000, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)
    start = comm.recv(source=0, tag=78)
    end1 = MPI.Wtime() - start
    print(f"Explicit type took: {end1}s")

# automatic MPI datatype discovery
if rank == 0:
    start = MPI.Wtime()
    data = numpy.arange(1_000_000_000, dtype=numpy.float64)
    comm.send(start, dest=1, tag=78)
    comm.Send(data, dest=1, tag=13)
elif rank == 1:
    data = numpy.empty(1_000_000_000, dtype=numpy.float64)
    comm.Recv(data, source=0, tag=13)
    start = comm.recv(source=0, tag=78)
    end2 = MPI.Wtime() - start
    print(f"Discovered type took: {end2}s")
