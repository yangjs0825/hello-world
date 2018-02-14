import numpy as np
from random import shuffle

components = ["Microphone", "Screen", "FPU", "LED0", "LED1", "Converter",
                        "Speaker", "Buzzer", "Microchip0", "Microchip1"]
n = len(components)

rawdata = np.random.rand(n, n + 1)
Araw = rawdata[:, :-1]
rawx = np.random.rand(n,)
print("rawx", rawx)
rawdata[:, -1] = Araw.dot(rawx)
test_data = {}

for i in range(n):
    some_data = rawdata[i, :]
    test_measurements = []
    for j, component in enumerate(components):
        test_measurements.append((component, some_data[j]))
    test_measurements.append(("PowerConsumed", rawdata[i, -1]))
    shuffle(test_measurements)
    test_data["Test" + str(i)] = test_measurements

a = np.ones((n, n))
b = np.ones(n)
it_n = 0
for key in test_data.keys():
    for i in range(n):
        if test_data[key][i][0] == "PowerConsumed":
            b[it_n] = test_data[key][i][1]
            del test_data[key][i]
        index = components.index(test_data[key][i][0])
        a[it_n][index] = test_data[key][i][1]
    it_n += 1
# print (b)
x = np.linalg.solve(a, b)
# x = np.dot(b,np.linalg.inv(a))
# print (np.dot(a,x))
print("x", x)
