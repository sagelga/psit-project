import xlrd
import matplotlib.pyplot as plt
"""PSIT Project 02 : Mortorcycle Per Sedan"""
def mortor_per_sedan():
    "for Check Number of Motorcycle per 1 Sedan In Thailand"
    ############################################
    #                data cal                  #
    ############################################
    file_location = "C:/Users/SODA/Desktop/python/panda/Thai Vehicle Stats.xlsx"
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
    want = []# user want to know
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
    print("*****number of provincial that you want to show motorcycle per sedan.*****")
    number = int(input())
    #################################################################
    #####       show provincial that can use for calculate      #####
    #################################################################
    print("****** Warning : You can input data form this list only if not program will error.*****")
    for i in range(len(provincial)):
        print(provincial[i])
    print("****** Warning : You can input data form this list only if not program will error.*****")
    #################################################################
    #####                   get data from user                  #####
    #################################################################
    for i in range(number):
        want.append(input())
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