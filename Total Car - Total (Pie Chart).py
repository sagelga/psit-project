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
    labels = 'Mae Hong Son', 'Samut Songkram', 'Ranong', 'Bueng Kan', 'Amnat Charoen', 'Pang Nga', 'Nakhon Nayok', 'Trad', 'Satun', 'Sing Buri', 'Pathum Thani', 'Samut Prakarn', 'Ang Thong', 'Nong Bua Lamphu', 'Mukdahan', 'Chai Nat', 'Uthai Thani', 'Nonthaburi', 'Yasothon', 'Nakhon Phanom', 'Pattani', 'Tak', 'Nong Khai', 'Sra Kaew', 'Nan', 'Samut Sakorn', 'Narathiwat', 'Krabi', 'Phatthalung', 'Phrae', 'Uttaradit', 'Prachin Buri', 'Loei', 'Phayao', 'Yala', 'Lamphun', 'Kalasin', 'Chumphon', 'Phichit', 'Sukhothai', 'Petchaburi', 'Prachuap Kiri Khan', 'Maha Sarakham', 'Kamphaeng Phet', 'Trang', 'Chaiyaphum', 'Chanthaburi', 'Chachoengsao', 'Roi Et', 'Si Sa Ket', 'Khanchanaburi', 'Lop Buri', 'Ayuthaya', 'Saraburi', 'Phetchabun', 'Surin', 'Lampang', 'Phuket', 'Sakon Nakhon', 'Nakhon Pathom', 'Phitsanulok', 'Suphan Buri', 'Buri Rum', 'Ratchaburi', 'Nakhon Sawan', 'Surat Thani', 'Nakhon Si Thammarat', 'Udon Thani', 'Rayong', 'Chiang Rai', 'Ubon Ratchathani', 'Songkhla', 'Khon Kaen', 'Nakhon Ratchasima', 'Chiang Mai', 'Chonburi'
    fracs = [57536,69583,84644,98111,121165,122745,123291,131348,133028,135628,144507,144614,150409,154225,155442,172429,177562,182045,203899,213657,220058,221147,221173,221598,225384,230365,232610,245571,246757,253485,255755,257792,259646,264432,266119,269853,285970,288511,288931,304531,315275,323393,323476,353195,354028,360326,362162,378693,387544,387703,397001,412002,416328,416705,443819,444978,446759,452411,456473,462914,480971,481576,485829,492523,554211,597171,617511,645826,685357,700936,701817,814208,820245,1293523,1349910,1432816]
    cs=cm.Set1(np.arange(40)/40.)
    explode = (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    pie(fracs, labels=labels, autopct='%1.2f%%', shadow=False, explode=explode, startangle=180, colors=cs, pctdistance=.95)
    title('Registered Vehicle in Kingdom of Thailand in 2016')
    show()
total_car_pie_chart()
