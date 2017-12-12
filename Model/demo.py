import serial
import time

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

import threading

import sys

from main import getMyFeature

# style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ser = serial.Serial('/dev/ttyACM0', 115200)
xs = []
cnt = 0
margin = 100

windowSize = 200
skipSteps = 10
BASE = 520

from sklearn.externals import joblib
clf = joblib.load('ml/model.pkl')

while True:
	line = ser.readline().strip()
	if margin > 0:
		margin -= 1
		continue
	value = int(line)
	if value < 0 or value > 2000:
		continue
	xs.append(value)
	if len(xs) > windowSize:
		xs = xs[1:]
	cnt += 1
	if cnt == skipSteps:
		cnt = 0
		x = [getMyFeature(xs)]
		print clf.predict(x)[0]
