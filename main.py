import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


data = pd.read_csv("bmi.csv")
print(len(data))
fig, axs = plt.subplots(1, 3, tight_layout=True)
axs[0].hist(data["AGE"], bins=20)
axs[1].hist(data["BP"], bins=20)
axs[2].hist2d(data["AGE"], data["BP"], bins=20)

plt.show()

