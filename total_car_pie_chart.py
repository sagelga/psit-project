"""
Pie chart by the total registering cars.
"""
from pylab import *
from matplotlib import cm
def total_car_pie_chart():
    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Central', 'West', 'South', 'North', 'North East', 'Bangkok', 'East'
    fracs = [2170767, 2771924, 4675162, 6646933, 8019217, 9235362, 11610158]
    explode=(0, 0, 0, 0, 0, 0, 0)
    a=np.random.random(40)
    cs=cm.Set1(np.arange(40)/40.)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, colors=cs)
    title('Total Car Registered in Thailand in 2556')
    show()
total_car_pie_chart()
