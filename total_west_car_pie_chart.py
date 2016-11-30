"""
Pie chart by the total registering cars.
"""
from pylab import *
from matplotlib import cm
def total_west_pie_chart():
    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Samut Songkram', 'Samut Sakorn', 'Pechaburi', 'Phachuap Kiri Khan', 'Khanchanaburi', 'Nakhon Pahtom', 'Suphan Buri', 'Ratchaburi'
    fracs = [69583,230365,315275,323393,397001,462914,481576,492523]
    cs=cm.Set1(np.arange(40)/40.)
    pie(fracs, labels=labels, autopct='%1.1f%%',shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in West in 2556')
    show()
total_west_pie_chart()
