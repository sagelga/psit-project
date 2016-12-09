# Welcome to PSIT Project Data Analysis Jupyter file!
# This is where the code runs (and don't run) and given out results to you!
# We have a tons of analysis in this file, so please read what we have done!


"""File Initialization Part"""
from pylab import *
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd
my_data = pd.read_csv('Thailand Vehicle Stats.csv', sep=',',header=None)

# We just want to show what the CSV file looks like. It doesn't meant to do something.
print(my_data)

"""This function will draw Pie Chart from data given"""
def total_north_east_pie_chart():
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Bueng Kan', 'Amnat Charoen', 'Nong Bua Lamphu', 'Mukdahan', 'Yasothon', 'Nakhon Phanom', 'Nong Khai', 'Loei','Kalasin','Maha Sarakham','Chaiyaphum', 'Roi Et', 'Si Sa Ket', 'Surin', 'Sakon Nakhon', 'Buri Rum','Udon Thani', 'Ubon Ratchathani', 'Khon Kaen', 'Nakhon Ratchasima'
    fracs = [98111,121165,154225,155442,203899,213657,221173,259646,285970,323476,360326,387544,387703,444978,456473,485829,645826,701817,820245,1293523]
    # Replace MathPlotLib ugly color to more 'Nyan Cat' color
    cs=cm.Set1(np.arange(40)/40.)
    # Print out [Data | Data Lable | Number Percent Sig.Point | Shadows | Angle to start plot | Color use | Number Percent Location]
    pie(fracs, labels=labels, autopct='%1.1f%%',shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in North Eastern in 2016')
    show()
total_north_east_pie_chart()

"""This function will draw Pie Chart from data given"""
def total_south_pie_chart():
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Ranong', 'Pang Nya', 'Satun', 'Pattani', 'Narathiwat', 'Krabi', 'Phatthalung', 'Yala', 'Chumphon', 'Trang', 'Phuket', 'Surat Thani', 'Nakhon Si Thammarat', 'Songkhla'
    fracs = [84644, 122745, 133028, 220058, 232610, 245571,246757,266119,288511,354028,452411,597171,617511,814208]
    # Replace MathPlotLib ugly color to more 'Nyan Cat' color
    cs=cm.Set1(np.arange(40)/40.)
    # Print out [Data | Data Lable | Number Percent Sig.Point | Shadows | Angle to start plot | Color use | Number Percent Location]
    pie(fracs, labels=labels, autopct='%1.1f%%',shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in Southern in 2016')
    show()
total_south_pie_chart()

"""This function will draw Pie Chart from data given"""
def total_west_pie_chart():
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Samut Songkram', 'Samut Sakorn', 'Pechaburi', 'Phachuap Kiri Khan', 'Khanchanaburi', 'Nakhon Pahtom', 'Suphan Buri', 'Ratchaburi'
    fracs = [69583,230365,315275,323393,397001,462914,481576,492523]
    # Replace MathPlotLib ugly color to more 'Nyan Cat' color
    cs=cm.Set1(np.arange(40)/40.)
    # Print out [Data | Data Lable | Number Percent Sig.Point | Shadows | Angle to start plot | Color use | Number Percent Location]
    pie(fracs, labels=labels, autopct='%1.1f%%',shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in Western in 2016')
    show()
total_west_pie_chart()

"""This function will draw Pie Chart from data given"""
def total_north_pie_chart():
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Mae Hong Son','Uthai Thani','Tak','Nan','Phrae','Uttaradit','Phayao','Lamphun','Phichit','Sukhothai','Kamphaeng Phet','Phetchabun','Lampang','Phitsanulok','Nakhon Sawan','Chiang Rai','Chiang Mai'
    fracs = [57536,177562,221147,225384,253485,255755,264432,269853,288931,304531,353195,443819,446759,480971,554211,700936,1349910]
    # Replace MathPlotLib ugly color to more 'Nyan Cat' color
    cs=cm.Set1(np.arange(40)/40.)
    # Print out [Data | Data Lable | Number Percent Sig.Point | Shadows | Angle to start plot | Color use | Number Percent Location]
    pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in Northern in 2016')
    show()
total_north_pie_chart()

"""This function will draw Pie Chart from data given"""
def total_center_pie_chart():
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Sing Buri', 'Pathum Thani', 'Samut Prakarn', 'Ang Thong', 'Chai Nat', 'Nonthaburi', 'Lop Buri','Ayuthaya','Saraburi'
    fracs = [135628,144507,144614,150409,172429,182045,412002,416328,416705]
    # Replace MathPlotLib ugly color to more 'Nyan Cat' color
    cs=cm.Set1(np.arange(40)/40.)
    # Print out [Data | Data Lable | Number Percent Sig.Point | Shadows | Angle to start plot | Color use | Number Percent Location]
    pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in Central in 2016')
    show()
total_center_pie_chart()

"""This function will draw Pie Chart from data given"""
def total_east_pie_chart():
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Nakhon Nayok', 'Trad', 'Sra Kaew', 'Prachin Buri', 'Chanthaburi', 'Chachoengsao', 'Rayong','Chonburi'
    fracs = [123291,131348,221598,257792,362162,378693,685357,1432816]
    # Replace MathPlotLib ugly color to more 'Nyan Cat' color
    cs=cm.Set1(np.arange(40)/40.)
    # Print out [Data | Data Lable | Number Percent Sig.Point | Shadows | Angle to start plot | Color use | Number Percent Location]
    pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Total Car Registered in Eastern in 2016')
    show()
total_east_pie_chart()

"""This function will draw Pie Chart from data given"""
def top_region_pie_chart():
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Center', 'West', 'South', 'North', 'North East', 'Bangkok Metropolis', 'East'
    fracs = [2170767,2771924,4675162,6646933,8019217,9235362,11610158]
    # Replace MathPlotLib ugly color to more 'Nyan Cat' color
    cs=cm.Set1(np.arange(40)/40.)
    # Print out [Data | Data Lable | Number Percent Sig.Point | Shadows | Angle to start plot | Color use | Number Percent Location]
    pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False, startangle=180, colors=cs, pctdistance=.9)
    title('Top Regional Vehicle Registraion in Kingdom of Thailand in 2016')
    show()
top_region_pie_chart()

"""This function will draw Pie Chart from data given"""
def top_type_pie_chart():
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Motorcycle','Sedan','Van & Pick Up','Truck','Tractor'
    fracs = [20296939,8042692,6227465,1042371,498091]
    # Replace MathPlotLib ugly color to more 'Nyan Cat' color
    cs=cm.Set1(np.arange(120)/20.)
    # Print out [Data | Data Lable | Number Percent Sig.Point | Shadows | Angle to start plot | Color use | Number Percent Location]
    pie(fracs, labels=labels, autopct='%1.2f%%', shadow=False, startangle=0, colors=cs, pctdistance=.9)
    title('Top 5 Registered Vehicle in Kingdom of Thailand in 2016')
    show()
top_type_pie_chart()

"""This function will draw Pie Chart from data given"""
def total_car_pie_chart():
    figure(1, figsize=(8,8))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Mae Hong Son', 'Samut Songkram', 'Ranong', 'Bueng Kan', 'Amnat Charoen', 'Pang Nga', 'Nakhon Nayok', 'Trad', 'Satun', 'Sing Buri', 'Pathum Thani', 'Samut Prakarn', 'Ang Thong', 'Nong Bua Lamphu', 'Mukdahan', 'Chai Nat', 'Uthai Thani', 'Nonthaburi', 'Yasothon', 'Nakhon Phanom', 'Pattani', 'Tak', 'Nong Khai', 'Sra Kaew', 'Nan', 'Samut Sakorn', 'Narathiwat', 'Krabi', 'Phatthalung', 'Phrae', 'Uttaradit', 'Prachin Buri', 'Loei', 'Phayao', 'Yala', 'Lamphun', 'Kalasin', 'Chumphon', 'Phichit', 'Sukhothai', 'Petchaburi', 'Prachuap Kiri Khan', 'Maha Sarakham', 'Kamphaeng Phet', 'Trang', 'Chaiyaphum', 'Chanthaburi', 'Chachoengsao', 'Roi Et', 'Si Sa Ket', 'Khanchanaburi', 'Lop Buri', 'Ayuthaya', 'Saraburi', 'Phetchabun', 'Surin', 'Lampang', 'Phuket', 'Sakon Nakhon', 'Nakhon Pathom', 'Phitsanulok', 'Suphan Buri', 'Buri Rum', 'Ratchaburi', 'Nakhon Sawan', 'Surat Thani', 'Nakhon Si Thammarat', 'Udon Thani', 'Rayong', 'Chiang Rai', 'Ubon Ratchathani', 'Songkhla', 'Khon Kaen', 'Nakhon Ratchasima', 'Chiang Mai', 'Chonburi'
    fracs = [57536,69583,84644,98111,121165,122745,123291,131348,133028,135628,144507,144614,150409,154225,155442,172429,177562,182045,203899,213657,220058,221147,221173,221598,225384,230365,232610,245571,246757,253485,255755,257792,259646,264432,266119,269853,285970,288511,288931,304531,315275,323393,323476,353195,354028,360326,362162,378693,387544,387703,397001,412002,416328,416705,443819,444978,446759,452411,456473,462914,480971,481576,485829,492523,554211,597171,617511,645826,685357,700936,701817,814208,820245,1293523,1349910,1432816]
    # Replace MathPlotLib ugly color to more 'Nyan Cat' color
    cs=cm.Set1(np.arange(40)/40.)
    explode = []
    for i in range(len(labels)):
        explode.append(1.8)
    # Print out [Data | Data Lable | Number Percent Sig.Point | Shadows | Angle to start plot | Color use | Number Percent Location]
    pie(fracs, labels=labels, autopct='%1.2f%%', shadow=False, explode=explode, startangle=180, colors=cs, pctdistance=1.0)
    show()
total_car_pie_chart()

"""this fuction has shown number of sedan cars users and bus in Northern"""
def northern():
    position = [1, 3, 5, 7, 9]
    y2 = [(100150+1828)/100150, (2349+203)/2349, (289366+6710)/289366, (31060+457)/31060, (71995+1209)/71995]
          #Bus:Sedan
    sedan_per_bus = []
    #translate data into percent
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
    p1 = plt.bar(position, sedan_per_bus, label='Sedan per Bus in Northern', color='c')
    pos = [1.375,3.375,5.375,7.375,9.375]
    plt.ylabel('percent')
    plt.title('Percent of Bus : Sedan in Northern')
    plt.xticks(pos, ('Chiang Rai','Mae Hong Son','Chiang Mai','Phayao','Lampang'))
    plt.show()
northern()

'''this function show Percent of Bus:sedan in Southern area by picking data to calculate'''
def south():
    position = [1,3,5,7,9]
    y2 = [(104021+3106)/104021,(94052+2818)/94052,(101689+6580)/101689,(199684+6014)/199684,(32698+1132)/32698]
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
    p1 = plt.bar(position, sedan_per_bus, label='Sedan per Bus in Southern', color='c')
    pos = [1.375,3.375,5.375,7.375,9.375]
    plt.ylabel('percent')
    plt.title('Percent of Bus : Sedan in Southern')
    plt.xticks(pos, ('Surat Thani','Nakhon Si Thammarat','Phuket','Songkhla','Yala'))
    plt.show()
south()

"""this fuction has shown number of sedan cars users and bus in NEast"""
def neast():
    positions = [1, 3, 5, 7, 9]
    y2 = [(32721+978)/32721, (22857+651)/22857, (98041+2080)/98041, (43569+1051)/43569, (204231+6021)/204231]
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
    p1 = plt.bar(positions, sedan_per_bus, label='Sedan per Bus in NEast', color='c')
    pos = [1.375,3.375,5.375,7.375,9.375]
    plt.ylabel('percent')
    plt.title('Percent of Bus : Sedan in North Eastern')
    plt.xticks(pos, ('Chaiyabhumi','Yasothorn','Ubon Ratcha-Thani','Buriram','Nakhon Ratchasri-ma'))
    plt.show()
neast()

'''this function show Percent of Bus:sedan in central add bkk area by picking data to calculate'''
def central_bkk():
    position = [1,3,5,7,9]
    y2 = [43275/3937660,22604/73950,17808/62270,15648/67124,30803/66460]
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i])*100)
    p1 = plt.bar(position, sedan_per_bus, label='Sedan per Bus in central', color='c')
    pos = [1.375,3.375,5.375,7.375,9.375]
    plt.ylabel('percent')
    plt.title('Percent of Bus : Sedan in Central')
    plt.xticks(pos, ('Bangkok','Ayuthaya','Nonthaburi','Lop Buri','Saraburi'))
    plt.show()
central_bkk()

"""this fuction has shown number of sedan cars users and bus in East"""
def east():
    positions = [1, 3, 5, 7, 9]
    y2 = [(20471+369)/20471, (40202+670)/40202, (53766+2299)/53766, (248767+6091)/248767, (133334+1996)/133334]
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
    p1 = plt.bar(positions, sedan_per_bus, label='Sedan per Bus in East', color='c')
    pos = [1.375,3.375,5.375,7.375,9.375]
    plt.ylabel('percent')
    plt.title('Percent of Bus : Sedan in East')
    plt.xticks(pos, ('Nakhon Nayok','Prachinburi','Chachoengsao','Chonburi','Rayong'))
    plt.show()
east()

'''this function show Percent of Bus:sedan in Western area by picking data to calculate'''
def west():
    position = [1,3,5,7,9]
    y2 = [(316194+9021)/316194,(49983+1774)/49983,(52083+1167)/52083, (65058+1491)/65058,(57800+925)/57800]
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
    p1 = plt.bar(position, sedan_per_bus, label='Sedan per Bus in Western', color='c')
    pos = [1.375,3.375,5.375,7.375,9.375]
    plt.ylabel('percent')
    plt.title('Percent of Bus:Sedan in Western')
    plt.xticks(pos, ('Suphan Buri','Khanchana Buri','Nakhon Pathom','Ratchaburi','Samut Sakorn'))
    plt.show()
west()

'''this funtion show Percent of Bus:Sedan in any provincial that user want [as least 1 but no more than five'''
def show_stat_bus_per_sedan():
    ############################################
    #                data cal                  #
    ############################################
    file_location = "Thai Vehicle Stats.xlsx"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)
    ############################################
    #     list for collect data from file      #
    ############################################
    provincial = []
    sedan = []
    bus = []
    ############################################
    ######      data collect from User     #####
    ############################################
    want = ['Whole Kingdom', 'Bangkok', 'Central', 'North Eastern', 'Western', 'Southern', 'Northern', ]# user want to know
    pro_use = []# for calculate percent
    sedan_use = []# for calculate percent
    bus_use = []# for calculate percent
    cal_percent = []# for built grap
    ############################################
    #####       get data from file          ####
    ############################################
    for i in range(1,86):
        provincial.append(sheet.cell_value(4,i))
        sedan.append(sheet.cell_value(9,i))
        bus.append(sheet.cell_value(28,i))
    #######################################################
    #####       get number of provincial for use      #####
    #######################################################
    #print("*****number of provincial that you want to show bus per sedan.*****")
    #number = int(input())
    #################################################################
    #####       show provincial that can use for calculate      #####
    #################################################################
    #print("****** Warning : You can input data form this list only if not program will error.*****")
    #for i in range(len(provincial)):
    #    print(provincial[i])
    #print("****** Warning : You can input data form this list only if not program will error.*****")
    #################################################################
    #####                   get data from user                  #####
    #################################################################
    #for i in range(number):
    #    want.append(input())
    #################################################################
    #####       use that data to find others data from file     #####
    #################################################################
    for i in range(len(want)):
        for n in range(len(provincial)):
            if want[i] == provincial[n]:
                pro_use.append(provincial[n])
                sedan_use.append(sedan[n])
                bus_use.append(bus[n])
            else:
                pass
    ##################################################################
    #####                    check percent                      ######
    ##################################################################
    for i in range(number):
        percent = ((((float(sedan_use[i])+float(bus_use[i]))/float(sedan_use[i]))-1)*100)
        cal_percent.append(percent)
        #calculate to percent (bus:sedan)
    ################################################
    #                  Graph Zone                  #
    ################################################
    position = [1] # start position of bar in graph
    # for calculate position to plot graph in n bar
    for i in range(1,len(cal_percent)):
       position.append(position[i-1]+2)
    graph = plt.bar(position, cal_percent, label='Bus per Sedan in Thailand', color='c') # create graph formation
    pos = [1.375,2.375,3.375,4.375,5.375,6.375,7.375] # position to show bar in graph
    plt.ylabel('percent')
    #y axis name
    plt.title('Percent of Bus per Sedan')
    #title name
    plt.xticks(pos, (want))
    # bar graph's name
    plt.show()
   # show bar graph
show_stat_bus_per_sedan()

"""Show Mortorcycle Per Sedan"""
def mortor_per_sedan():
    "for Check Number of Motorcycle per 1 Sedan In Thailand"
    ############################################
    #                data cal                  #
    ############################################
    file_location = "Thai Vehicle Stats.xlsx"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)
    ############################################
    #     list for collect data from file      #
    ############################################
    provincial = []
    motorcycle = []
    sedan = []
    ############################################
    ######      data collect from User     #####
    ############################################
    want = ['Whole Kingdom', 'Bangkok', 'Central', 'North Eastern', 'Western', 'Southern', 'Northern', ]# user want to know
    pro_use = []# for calculate percent
    motorcycle_use = []# for calculate percent
    sedan_use = []# for calculate percent
    cal_percent = []# for built grap
    ############################################
    #####       get data from file          ####
    ############################################
    for i in range(1,86):
        provincial.append(sheet.cell_value(4,i))
        motorcycle.append(sheet.cell_value(20,i))
        sedan.append(sheet.cell_value(9,i))
    #######################################################
    #####       get number of provincial for use      #####
    #######################################################
    #print("*****number of provincial that you want to show motorcycle per sedan.*****")
    #number = int(input())
    #################################################################
    #####       show provincial that can use for calculate      #####
    #################################################################
    #print("****** Warning : You can input data form this list only if not program will error.*****")
    #for i in range(len(provincial)):
    #    print(provincial[i])
    #print("****** Warning : You can input data form this list only if not program will error.*****")
    #################################################################
    #####                   get data from user                  #####
    #################################################################
    #for i in range(number):
    #    want.append(input())
    #################################################################
    #####       use that data to find others data from file     #####
    #################################################################
    for i in range(len(want)):
        for n in range(len(provincial)):
            if want[i] == provincial[n]:
                pro_use.append(provincial[n])
                motorcycle_use.append(motorcycle[n])
                sedan_use.append(sedan[n])
            else:
                pass
    ##################################################################
    #####                    check percent                      ######
    ##################################################################
    for i in range(number):
        percent = (float(motorcycle_use[i])/float(sedan_use[i]))
        cal_percent.append(percent)
        #calculate to percent (sedan:motorcycle)
    ################################################
    #                  Graph Zone                  #
    ################################################
    position = [1] # start position of bar in graph
    # for calculate position to plot graph in n bar
    for i in range(1,len(cal_percent)):
       position.append(position[i-1]+1)
    graph = plt.bar(position, cal_percent, label='N motorcycle per 1 sedan in Thailand', color='c') # create graph formation
    pos = [1.375,2.375,3.375,4.375,5.375,6.375,7.375] # position to show bar in graph
    plt.ylabel('percent')
    #y axis name
    plt.title('N motorcycle per 1 sedan in Thailand')
    #title name
    plt.xticks(pos, (want))
    # bar graph's name
    plt.show()
   # show bar graph
mortor_per_sedan()
