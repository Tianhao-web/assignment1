import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys

final_data = pd.read_csv('owid-covid-data-2020-monthly.csv',encoding = 'ISO-8859-1')
name = sys.argv[1:]
groups = final_data.groupby("location")
for name, group in groups:
    plt.plot(group["new_cases"], group["case_fatality_rate"], marker="o", linestyle="", label=name) #https://stackoverflow.com/questions/21654635/scatter-plots-in-pandas-pyplot-how-to-plot-by-category

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
          fancybox=True, shadow=True, ncol=5) #https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot#:~:text=To%20place%20the%20legend%20outside,left%20corner%20of%20the%20legend.&text=A%20more%20versatile%20approach%20is,placed%2C%20using%20the%20bbox_to_anchor%20argument.

plt.ylabel("case_fatality_rate")
plt.xlabel("new_cases")
plt.grid(True)
plt.savefig(name[0])

groups = final_data.groupby("location")
for name, group in groups:
    plt.plot(group["new_cases"], group["case_fatality_rate"], marker="o", linestyle="", label=name)
plt.xscale("log") #https://www.kite.com/python/answers/how-to-plot-on-a-log-scale-with-matplotlib-in-python
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
          fancybox=True, shadow=True, ncol=5)

plt.ylabel("case_fatality_rate")
plt.xlabel("new_cases")
plt.grid(True)
plt.savefig(name[1])