import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
from time import time

def mandelbrot(c,max_iter):
    """
    Compute the number of iterations for a complex number to escape the Mandelbrot set.

    Parameters:
    c (complex): The complex number to test.
    max_iter (int): The maximum number of iterations to perform.

    Returns:
    int: The number of iterations it took for the complex number to escape the Mandelbrot set,
            or max_iter if the number did not escape within the given iterations.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z+c
    return max_iter

def mandelbrotRow(y,width,height,min_x,max_x,min_y,max_y,max_iter):
    """
    Compute a row of the Mandelbrot set.

    Parameters:
    y (int): The row index.
    width (int): The width of the image.
    height (int): The height of the image.
    min_x (float): The minimum x-coordinate (real part) of the complex plane.
    max_x (float): The maximum x-coordinate (real part) of the complex plane.
    min_y (float): The minimum y-coordinate (imaginary part) of the complex plane.
    max_y (float): The maximum y-coordinate (imaginary part) of the complex plane.
    max_iter (int): The maximum number of iterations to determine if a point is in the Mandelbrot set.

    Returns:
    numpy.ndarray: A row of the Mandelbrot set represented as an array of integers.
    """
    row = np.zeros(width, dtype=np.uint64) #Depending on the desired resolution change of dtype may be needed
    for x in range(width):
        real = min_x + (max_x - min_y) * x/width
        imag = min_y + (max_y - min_y) * y/height
        c = complex(real,imag)
        row[x] = mandelbrot(c,max_iter)
    return row

def genMandelbrotParallel(width,height,min_x,max_x,min_y,max_y,max_iter,num_processes):
    """
    Generate a Mandelbrot set image in parallel using multiple processes.

    Parameters:
    width (int): The width of the output image.
    height (int): The height of the output image.
    min_x (float): The minimum x-coordinate (real part) of the complex plane.
    max_x (float): The maximum x-coordinate (real part) of the complex plane.
    min_y (float): The minimum y-coordinate (imaginary part) of the complex plane.
    max_y (float): The maximum y-coordinate (imaginary part) of the complex plane.
    max_iter (int): The maximum number of iterations to determine if a point is in the Mandelbrot set.
    num_processes (int): The number of processes to use for parallel computation.

    Returns:
    numpy.ndarray: A 2D array representing the Mandelbrot set image.
    """
    with Pool(num_processes) as pool:
        results = pool.starmap(
            mandelbrotRow,
            [(y, width, height, min_x, max_x, min_y, max_y, max_iter) for y in range(height)]
        )
    return np.array(results)

def countTimeForNumProcesses(width,height,min_x,max_x,min_y,max_y,max_iter,processes) -> list:
    """
    Measure the time taken to generate the Mandelbrot set using different numbers of processes.

    Args:
        width (int): The width of the image.
        height (int): The height of the image.
        min_x (float): The minimum x-coordinate of the complex plane.
        max_x (float): The maximum x-coordinate of the complex plane.
        min_y (float): The minimum y-coordinate of the complex plane.
        max_y (float): The maximum y-coordinate of the complex plane.
        max_iter (int): The maximum number of iterations for the Mandelbrot calculation.

    Returns:
        list: A list of elapsed times for generating the Mandelbrot set using 1, 2, 4, 8, and 16 processes.
    """
    times = []
    for num in processes:
        start = time()
        genMandelbrotParallel(width, height, min_x, max_x, min_y, max_y, max_iter, num)
        elapsed = time() - start
        times.append(elapsed)
    return times




if __name__ == "__main__":
    min_x, max_x = -2.0, 2.0
    min_y, max_y = -1.5, 1.5
    max_iter = 256


    print("What do you want to do?")
    print("1. Perform simulation and view fractal")
    print("2. Perform simulation and view differences in time per number of processes")
    input_value = int(input())
    width = int(input("Please enter width:\n"))
    height = int(input("Please enter height:\n"))
    if input_value == 1:
        num_processes = int(input("Please enter number of processes:\n"))
        mandelbrot_set = genMandelbrotParallel(width, height, min_x, max_x, min_y, max_y, max_iter, num_processes)
        plt.imshow(mandelbrot_set, extent=(min_x, max_x, min_y, max_y), cmap="hot")
        plt.colorbar()
        plt.title("Fraktal Mandelbrota")
        plt.xlabel("Re(z)")
        plt.ylabel("Im(z)")
        plt.show()
    elif input_value == 2:
        processes = [int(x) for x in list(input("Please enter number of processes separated with ',':\n").strip(",").split(','))]
        times = countTimeForNumProcesses(width, height, min_x, max_x, min_y, max_y, max_iter, (1,2,4,8,16,32))

        print(f"For resolution: ({width}, {height})")
        for idx, num in enumerate((1,2,4,8,16,32)):
            print(f"For {num} processes it took: {times[idx]}")

        plt.scatter((1,2,4,8,16,32), times)
        plt.show()
    else:
        print("We dont have that option you fool")
        