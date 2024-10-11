from random import random, seed

from mpi4py import MPI

seed(1)
ilosc_liczb = 1_000_000

with open("liczby.txt", "w") as f:
    for _ in range(ilosc_liczb):
        f.write(str(random()) + "\n")

start = MPI.Wtime()
suma = 0

with open("liczby.txt") as f:
    for line in f:
        suma += float(line)

finish = MPI.Wtime()
print(suma)
print(f"czas sumowania: {finish - start}")
