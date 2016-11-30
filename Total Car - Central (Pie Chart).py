"""
Pie chart by the total registering cars.
"""
from pylab import *
from matplotlib import cm
def total_center_pie_chart():
    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Sing Buri', 'Pathum Thani', 'Samut Prakarn', 'Ang Thong', 'Chai Nat', 'Nonthaburi', 'Lop Buri','Ayuthaya','Saraburi'
    fracs = [135628,144507,144614,150409,172429,182045,412002,416328,416705]
    cs=cm.Set1(np.arange(40)/40.)
    pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in Central in 2556')
    show()
total_center_pie_chart()
