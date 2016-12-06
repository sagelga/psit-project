import xlrd
import matplotlib.pyplot as plt
def test():
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
    want = []# user want to know
    pro_use = []# for calculate percent
    sedan_use = []# for calculate percent
    bus_use = []# for calculate percent
    cal_percent = []# for built graph
    ############################################
    #####       get data from file          ####
    ############################################
    for i in range(86):
        provincial.append(sheet.cell_value(4,i))
        sedan.append(sheet.cell_value(9,i))
        bus.append(sheet.cell_value(28,i))
    #######################################################
    #####       get number of provincial for use      #####
    #######################################################
    print("*****number of provincial that you want to show sedan per bus.*****")
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
    graph = plt.bar(position, cal_percent, label='Sedan per Bus in Thailand', color='c') # create graph formation
    pos = [1.375,3.375,5.375,7.375,9.375] # position to show bar in graph
    plt.ylabel('percent')
    #y axis name
    plt.title('Percent of Bus:Sedan')
    #title name
    plt.xticks(pos, (want))
    # bar graph's name
    plt.show()
   # show bar graph
test()
