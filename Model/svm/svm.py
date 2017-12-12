import numpy as np
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score
from random import shuffle

# Init the default matrix for training model
# x: features       y: label
x = []
y = []
with open('../output/window_all') as fp:
    for line in fp:
        parts = line.replace("\n", "").split(" ")
        temp = []
        for i in range(0, len(parts) - 1):
            temp.append(parts[i])
        x.append(temp)
        y.append(parts[len(parts) - 1])
fp.close()

shuf = list(zip(x, y))
shuffle(shuf)
x, y = zip(*shuf)

# Create model for svm
clf = SVC()
clf.fit(x, y)

# Cross Validation
y_pred = cross_val_predict(clf, x, y)

f_label = open("input_label", "w")
for i in range(0, len(y)):
    f_label.write(y[i] + " " + y_pred[i] + "\n")

f_label.close()

print (accuracy_score(y, y_pred))

# # Predict for other input
# xTest = [];
# yTest = [];
# with open('../output/Window1') as fp:
#     for line in fp:
#         parts = line.replace("\n", "").split(" ");
#         temp = [];
#         for i in range(0, len(parts) - 1):
#             temp.append(parts[i])
#         xTest.append(temp);
#         yTest.append(parts[len(parts) - 1]);
#
# res = clf.predict(xTest);
# correct = 0;
# for i in range (0, len(res)):
#     if res[i] == yTest[i]:
#         correct += 1;
#
# print (correct / len(res) * 100);
