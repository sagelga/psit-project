"""
Pie chart by the total registering cars.
"""
from pylab import *
from matplotlib import cm
def total_north_pie_chart():
    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Chiang Rai', 'Mae Hong Son', 'Chiang Mai', 'Phayao', 'Nan', 'Lamphun', 'Lampang', 'Phrae', 'Uttaradit', 'Sukhothai', 'Tak', 'Phitsanulok', 'Kamphaeng Phet', 'Phichit', 'Phetchabun', 'Nakhon Sawan', 'Uthai Thani'
    fracs = [700936, 57536, 1349910, 264432, 225384, 269853, 446759, 253485, 255755, 304531, 221147, 480971, 353195, 288931, 443819, 554211, 177562]
    cs=cm.Set1(np.arange(40)/40.)
    pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, colors=cs)
    title('Total Car Registered in Northern in 2556')
    show()
total_north_pie_chart()
