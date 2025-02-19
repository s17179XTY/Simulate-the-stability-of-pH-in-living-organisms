import matplotlib.pyplot as plt
import matplotlib
import numpy as np
  
matplotlib.rc('font', family='Microsoft JhengHei')

plt.title("模擬生物體維持pH的穩定")

x_axis_data = [ 0 , 5, 10, 15, 20, 25, 30]
y_axis_data1 = [ 7.4, 7.8, 8.2, 9.1, 10.2, 10.7, 11.3]
y_axis_data2 = [ 7.2, 7.5, 7.7, 7.7, 7.8 , 8.0, 8.0]
y_axis_data3 = [ 6.9, 7.0, 7.2, 7.7, 8.0, 8.3, 8.6]


plt.plot(x_axis_data, y_axis_data1, 'bo-', alpha=0.5, linewidth=1, label='自來水', color="blue")
plt.plot(x_axis_data, y_axis_data2, 'ro-', alpha=0.5, linewidth=1, label='緩衝液', color="red")
plt.plot(x_axis_data, y_axis_data3, 'go-', alpha=0.5, linewidth=1, label='薯仔水', color="green")


for a, b in zip(x_axis_data, y_axis_data1):
    plt.text(a, b, str(b), ha='center', va='bottom', fontsize=8, color="blue")
for a, b1 in zip(x_axis_data, y_axis_data2):
    plt.text(a, b1, str(b1), ha='center', va='bottom', fontsize=8, color="red") 
for a, b2 in zip(x_axis_data, y_axis_data3):
    plt.text(a, b2, str(b2), ha='center', va='bottom', fontsize=8, color="green")
 
  
plt.legend()
plt.xlabel('0.1mol/L的NaOH滴數', rotation="horizontal")
plt.ylabel('ph值變化', rotation="vertical")
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)

plt.show()
