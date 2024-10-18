import multiprocessing

def worker(numbers, start, end, result):
    """A worker function to calculate squares of numbers."""
    for i in range(start, end):
        result[i] = numbers[i] * numbers[i]

def main(core_count):
    numbers = range(10000)  # A larger range for a more evident effect of multiprocessing
    result = multiprocessing.Array('i', len(numbers))
    segment = len(numbers) // core_count
    processes = []

    for i in range(core_count):
        start = i * segment
        if i == core_count - 1:
            end = len(numbers)  # Ensure the last segment goes up to the end
        else:
            end = start + segment
        # Creating a process for each segment
        p = multiprocessing.Process(target=worker, args=(numbers, start, end, result))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return result

if __name__ == '__main__':
    for core_count in [2, 4, 8]:
        print(f"Using {core_count} cores:")
        result = main(core_count)
        print(f"First 10 squares: {list(result)[:10]}")  # Display the first 10 results as a sample
