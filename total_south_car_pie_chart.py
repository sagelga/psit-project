"""
Pie chart by the total registering cars.
"""
from pylab import *
from matplotlib import cm
def total_south_pie_chart():
    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Ranong', 'Pang Nya', 'Satun', 'Pattani', 'Narathiwat', 'Krabi', 'Phatthalung', 'Yala', 'Chumphon', 'Trang', 'Phuket', 'Surat Thani', 'Nakhon Si Thammarat', 'Songkhla'
    fracs = [84644, 122745, 133028, 220058, 232610, 245571,246757,266119,288511,354028,452411,597171,617511,814208]
    cs=cm.Set1(np.arange(40)/40.)
    explode = (0.1,0.05,0,0,0,0,0,0,0,0,0,0,0,0)
    pie(fracs, labels=labels, autopct='%1.1f%%',shadow=False, explode=explode, startangle=90, colors=cs, pctdistance=.9)
    title('Total Car Registered in Southern in 2556')
    show()
total_south_pie_chart()
