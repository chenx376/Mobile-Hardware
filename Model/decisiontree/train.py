import matplotlib.pyplot as plt
import numpy as np

def load(fil):
	y = []
	x = []
	with open(fil) as fi:
		for l in fi:
			l = map(lambda x: float(x), l.strip().split(' '))
			x.append(l[:-1])
			y.append(int(l[-1]))
	return (x, y)

ori_x = []
x = []
y = []

import os

# path = 'data/'
ori_path = '../raw_data/'
path = '../output/window/'

for fil in os.listdir(path):
	xx, yy = load(path + fil)
	x += xx
	y += yy
	with open(ori_path + fil) as fi:
		ori_x += map(lambda x: int(x), fi)

print len(ori_x), len(x)

from sklearn import tree
clf = tree.DecisionTreeClassifier()

# model = clf.fit(x, y)
# print(clf.predict([[-0.8, -1]]))#

stepSiz = 4
BASE = 520

from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report

y_pred = cross_val_predict(clf, x, y)
y_expanded = []
for eachy in y_pred:
	y_expanded += [eachy * BASE] * stepSiz

with open("result.txt", "w") as fo:
	for i in range(len(y_pred)):
		fo.write("%d %d\n"%(y[i], y_pred[i]))

model = clf.fit(x, y)
from sklearn.externals import joblib
joblib.dump(model, 'model.pkl')

'''
for i in range(len(x)):
	print x[i], y_pred[i]
'''
plt.plot(ori_x)
plt.plot(y_expanded)
plt.show()

