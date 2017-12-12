
import serial
import time

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# from matplotlib import style

import threading

import sys

# style.use('fivethirtyeight')

with open(sys.argv[1] + ".txt") as fi:
	y = map(lambda x: int(x), fi.readlines())
	plt.plot(y)
	plt.show()
