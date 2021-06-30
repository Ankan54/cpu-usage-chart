'''
Create CPU and RAM usage chart
Author: Ankan Bera
Created: 30-06-2021
'''
import matplotlib.pyplot as plt
import psutil
import time

def plotting():
    cpu_use = []
    ram_use = []
    SEC = 60
    minute = 1 # change value to manage the time limit
    final_time= time.time() + (SEC * minute)

    while time.time() < final_time:
        cpu_use.append(psutil.cpu_percent())
        ram_usage= psutil.virtual_memory()._asdict()
        ram_use.append(ram_usage['percent'])
        time.sleep(1)
    
    plt.figure(figsize=(7,5))
    plt.cla()
    plt.plot(cpu_use,'r',label= 'CPU usage')
    plt.plot(ram_use,'g',label= 'RAM usage')
    plt.ylim(0,100)
    plt.xlabel('Time (sec)')
    plt.ylabel('CPU/RAM Usage (%)')
    plt.legend(loc= 'upper right')
    plt.tight_layout()
    #plt.show()
    plt.savefig('cpu_usage.png')

if __name__== '__main__':
    plotting()
