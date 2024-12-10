import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data

if __name__ == '__main__':
    folder_path = r'C:\PycharmProjects\pythonProject\pythonProject1\python_M10'
    filenames = [os.path.join(folder_path, f'file_{number}.txt') for number in range(1, 5)]

    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейный вызов занял: {end_time - start_time:.6f} секунд")

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессный вызов занял: {end_time - start_time:.6f} секунд")
