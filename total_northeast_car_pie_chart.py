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
    labels = 'Bueng Kan', 'Amnat Charoen', 'Nong Bua Lamphu', 'Mukdahan', 'Yasothon', 'Nakhon Phanom', 'Nong Khai', 'Loei','Kalasin','Maha Sarakham','Chaiyaphum', 'Roi Et', 'Si Sa Ket', 'Surin', 'Sakon Nakhon', 'Buri Rum','Udon Thani', 'Ubon Ratchathani', 'Khon Kaen', 'Nakhon Ratchasima'
    fracs = [98111,121165,154225,155442,203899,213657,221173,259646,285970,323476,360326,387544,387703,444978,456473,485829,645826,701817,820245,1293523]
    cs=cm.Set1(np.arange(40)/40.)
    explode = (0.2, 0.175, 0.15, 0.125, 0.1, 0.075, 0.05, 0.025, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    pie(fracs, labels=labels, autopct='%1.1f%%',shadow=False, explode=explode, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in North Eastern in 2556')
    show()
total_east_pie_chart()
