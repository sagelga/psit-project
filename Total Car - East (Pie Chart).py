"""
Pie chart by the total registering cars.
"""
from pylab import *
from matplotlib import cm
def total_east_pie_chart():
    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Nakhon Nayok', 'Trad', 'Sra Kaew', 'Prachin Buri', 'Chanthaburi', 'Chachoengsao', 'Rayong','Chonburi'
    fracs = [123291,131348,221598,257792,362162,378693,685357,1432816]
    cs=cm.Set1(np.arange(40)/40.)
    pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in East in 2556')
    show()
total_east_pie_chart()
