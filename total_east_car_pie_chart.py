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
    labels = 'Chaiyaphum','Yasothon','Ubon Ratchathani','Si Sa Ket','Buri Rum','Nakhon Ratchasima','Surin','Amnat Charoen','Nong Bua Lamphu','Bueng Kan','Nong Khai','Loei','Udon Thani','Nakhon Phanom','Sakon Nakhon','Khon Kaen','Kalasin','Maha Sarakham','Roi Et','Mukdahan'
    fracs = [360326,203899,701817,387703,485829,1293523,444978,121165,154225,98111,221173,259646,645826,213657,456473,820245,285970,323476,387544,155442]
    cs=cm.Set1(np.arange(40)/40.)
    explode=(0.05, 0, 0, 0, 0, 0, 0, 0.4, 0.3, 0.2, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0.1)
    pie(fracs, labels=labels, autopct='%1.1f%%',explode=explode,shadow=False, startangle=90, colors=cs, pctdistance=.9)
    title('Total Car Registered in Eastern in 2556')
    show()
total_east_pie_chart()
