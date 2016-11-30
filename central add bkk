"""
central add bkk
"""
import matplotlib.pyplot as plt
#use this to plot bar graph it can use for others graph
'''this function show Percent of Bus:sedan in central add bkk area by picking data to calculate'''
def central_bkk():
    position = [1,3,5,7,9]
    y2 = [43275/3937660,22604/73950,17808/62270,
          15648/67124,30803/66460]
          #Bus:Sedan
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i])*100)
        #translate data into percent 
    p1 = plt.bar(position, sedan_per_bus, label='Sedan per Bus in central', color='c')
    # plot bar graph
    pos = [1.375,3.375,5.375,7.375,9.375]
    # position of bar graph's names
    plt.ylabel('percent')
    # y axis name
    plt.title('Percent of Bus:Sedan in central')
    # title name
    plt.xticks(pos, ('Bangkok','Ayuthaya','Nonthaburi','Lop Buri','Saraburi'))
    # bar graph's name
    plt.show()
    # show bar graph
central_bkk()