#! python3.
import numbers
import algorithms
import time


a = []
l = 15
d = False


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Grzegorz')
    numbers.generate(a, l, d)
    a2 = a.copy()

    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))
    print(a)
    algorithms.pancake(a, l)
    print(a)
    print("--- %s seconds ---" % (time.time() - start_time))
""""
    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))
    #print(a2)
    algorithms.merge2(a2, l)
    #print(a2)
    print("--- %s seconds ---" % (time.time() - start_time))
"""
