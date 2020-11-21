import tkinter as tk
from numpy.core.fromnumeric import size
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

data1 = {'Country': np.random.randint(1,10, size=100),
         'GDP_Per_Capita': np.random.randint(1,10, size=100)
        }
df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])
 
root= tk.Tk() 
  
figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
df1.plot(kind="line", legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

root.mainloop()