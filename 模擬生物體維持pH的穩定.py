import matplotlib.pyplot as plt
import matplotlib
import numpy as np
  
matplotlib.rc('font', family='Microsoft JhengHei')

plt.title("模擬生物體維持pH的穩定")

x_axis_data = [ 0 , 5, 10, 15, 20, 25, 30]
y_axis_data1 = [ 6.4, 5.8, 5.0, 3.8, 3.3, 3.0, 2.8]
y_axis_data2 = [ 7.0, 7.0, 7.0, 7.0, 7.0 , 7.0, 7.0]
y_axis_data3 = [ 6.3, 5.8, 5.2, 4.5, 4.0, 3.6, 3.3]


plt.plot(x_axis_data, y_axis_data1, 'bo-', alpha=0.5, linewidth=1, label='自來水')
plt.plot(x_axis_data, y_axis_data2, 'ro-', alpha=0.5, linewidth=1, label='緩衝液')
plt.plot(x_axis_data, y_axis_data3, 'go-', alpha=0.5, linewidth=1, label='薯仔水')
 
  
plt.legend()
plt.xlabel('0.1mol/L的HCl滴數', rotation="horizontal")
plt.ylabel('ph值變化', rotation="vertical")
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)

plt.show()