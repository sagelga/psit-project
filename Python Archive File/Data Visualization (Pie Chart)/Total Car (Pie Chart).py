"""
Pie chart by the total registering cars.
"""
from pylab import *
from matplotlib import cm
def total_region_pie_chart():
    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Center', 'West', 'South', 'North', 'North East', 'Bangkok Metropolis', 'East'
    fracs = [2170767,2771924,4675162,6646933,8019217,9235362,11610158]
    cs=cm.Set1(np.arange(40)/40.)
    pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in Kingdom of Thailand (Regional) in 2556')
    show()
total_region_pie_chart()
