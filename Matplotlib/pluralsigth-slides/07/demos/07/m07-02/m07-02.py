import plotly.plotly as py 

import login 

py.sign_in(login.USERNAME, login.API_KEY)

import numpy as np
import matplotlib.pyplot as plt 
import helper

heights = [month[1] for month in helper.precip_sums_for_year()]

fig, ax = plt.subplots()
ax.bar(np.arange(len(heights)), heights)

py.plot_mpl(fig)
