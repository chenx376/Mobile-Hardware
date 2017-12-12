from TSfeature import feature_core
import numpy as np
import os

root = 'standup/'
output = 'output/'
root_invalid = 'others/'

spl = ' '
window_size = 200
f_all_window = open(output + 'window_all', 'w')
f_all_nowindow = open(output + 'no_window_all', 'w')

def import_data(path):
    f = open(path)
    data = []
    for line in f:
        data.append(line)

    a = np.empty((len(data), 1))
    for i in range(0, len(data)):
        a[i] = data[i]
    return a

def output_data_window(window, res, label, all_window):
    f1 = open(window, 'w')
    for list in res:
        for features in list:
            f1.write(str(features) + spl)
            f_all_window.write(str(features) + spl)
        f1.write(label + '\n')
        all_window.write(label + '\n')
    f1.close()

def output_data_nowindow(nowindow, res, label, all_nowindow):
    f2 = open(nowindow, 'w')
    for features in res:
        f2.write(str(features) + spl)
        f_all_nowindow.write(str(features) + spl)
    f2.write(label + '\n')
    all_nowindow.write(label + '\n')
    f2.close()


def train(root, label):
    for fn in os.listdir(root):
        a = import_data(root + fn)
        res1 = feature_core.sequence_feature(a, window_size, 4)  # with window
        window = output + 'window/' + fn
        noWindow = output + 'nowindow/'+fn
        output_data_window(window, res1, label, f_all_window)
        res2 = feature_core.sequence_feature(a, 0, 4)
        output_data_nowindow(noWindow, res2, label, f_all_nowindow)

def getMyFeature(data):
    a = np.array(data).reshape((len(data), 1))
    return feature_core.get_feature(a)  # with window


if __name__ == '__main__':
    train(root, '1')
    train(root_invalid, '0')
    #tmp = getMyFeature([1] * window_size)
