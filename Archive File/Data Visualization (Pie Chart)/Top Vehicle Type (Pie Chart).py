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
    labels = 'Motorcycle','Sedan','Van & Pick Up','Truck','Tractor'
    fracs = [20296939,8042692,6227465,1042371,498091]
    cs=cm.Set1(np.arange(40)/40.)
    pie(fracs, labels=labels, autopct='%1.2f%%', shadow=False, startangle=337, colors=cs, pctdistance=.9)
    title('Top 5 Registered Vehicle in Kingdom of Thailand in 2016')
    show()
total_car_pie_chart()
