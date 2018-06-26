import nidaqmx
import matplotlib.pyplot as plt

plt.ion()

i = 0

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev3/ai0:1")
    while i<30:
        data = task.read(number_of_samples_per_channel=1)
        plt.scatter(i,data[0],c='r')
        plt.scatter(i,data[1],c ='b')
        plt.pause(0.05)
        i = i+1
        print(data)