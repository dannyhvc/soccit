import sys
import os
import compileall
import typing
import matplotlib.pyplot as plt
import numpy as np

def main(argv: typing.List[typing.AnyStr]) -> None:
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    z = np.linspace(0, 15, 1000)
    x = np.sin(z)
    y = np.cos(z)
    ax.plot3D(x, y, z, 'gray')

    # Data for three-dimensional scattered points
    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
    plt.show()
    
if __name__ == "__main__":
    compileall.compile_dir(os.curdir)
    main(sys.argv)