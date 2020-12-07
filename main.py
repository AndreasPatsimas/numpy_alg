import numpy as np

if __name__ == '__main__':

    my_array = np.array([1, 2, 3, 4])
    print(my_array)

    my_array = np.zeros((2,4))
    print(my_array)

    my_array = np.ones((2,4))
    print(my_array)

    my_array = np.diag((1, 3, 5, 7))
    print(my_array)

    my_array = np.empty((2,4))
    print(my_array)

    print("---------------------------")

    my_array = np.arange(3.4,22,3.1)
    print(my_array)

    my_array = np.linspace(3.0, 12.0, num=5, endpoint=False)
    print(my_array)

    print("---------------------------")
    x = np.array([-1, 0, 1])
    y = np.array([-2, 0, 2])
    X, Y = np.meshgrid(x, y)
    Z = (X + Y) ** 2
    print("x: ", X)
    print("y: ", Y)
    print("z: ", Z)