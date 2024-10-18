from random import random, seed

from mpi4py import MPI

start = MPI.Wtime()
comm_world = MPI.COMM_WORLD
size = comm_world.Get_size()
my_rank = comm_world.Get_rank()

seed(my_rank)

n_points: int = 2_000_000_000


# @njit
def get_pi_part(n_points: float) -> int:
    pi_part: int = 0
    for i in range(int(n_points)):
        if random() ** 2 + random() ** 2 < 1:
            pi_part += 1
    return pi_part


pi_part = get_pi_part(n_points / size)

pi = comm_world.reduce(pi_part, op=MPI.SUM, root=0)
if my_rank == 0:
    finish = MPI.Wtime()
    print(
        f"Pi({4*pi/n_points}) calculated with {size} processes took: {finish - start}"
    )
    with open("pi_results.csv", "a") as f:
        f.write(f"{size}, {n_points}, {4*pi/n_points}, {finish}\n")
