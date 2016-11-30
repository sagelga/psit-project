import matplotlib.pyplot as plt
"""this fuction has shown number of sedan cars users and bus in Northern"""
def northern():
    position = [1, 3, 5, 7, 9]
    y2 = [(100150+1828)/100150, (2349+203)/2349, (289366+6710)/289366, (31060+457)/31060, (71995+1209)/71995]
          #Bus:Sedan
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
        #translate data into percent
    p1 = plt.bar(position, sedan_per_bus, label='Sedan per Bus in Northern', color='c')
    # plot bar graph
    pos = [1.375,3.375,5.375,7.375,9.375]
    # position of bar graph's names
    plt.ylabel('percent')
    # y axis name
    plt.title('Percent of Bus:Sedan in Northern')
    # title name
    plt.xticks(pos, ('Chiang Rai','Mae Hong Son','Chiang Mai','Phayao','Lampang'))
    # bar graph's name
    plt.show()
    # show bar graph
northern()
