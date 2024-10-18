import polars as pl


def worker(numbers, start, end, result):
    for idx, number in enumerate(numbers[start:end]):
        result[idx] = number**2


def main(core_count):
    numbers = range(10_000)
    pl.Array
