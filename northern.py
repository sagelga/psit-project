import matplotlib.pyplot as plt
#use this to plot bar graph it can use for others graph
'''this function show Percent of Bus:sedan in Northern area by picking data to calculate'''

def northern():
    """create graph for northern"""
    position = [1,3,5,7,9]
    y2 = [23566/1326344,15697/685239,9521/437238,
          13895/467076,6869/214278]
          #Bus:Sedan
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i])*100)
        #translate data into percent 
    p1 = plt.bar(position, sedan_per_bus, label='Sedan per Bus in Northern', color='c')
    # plot bar graph
    pos = [1.375,3.375,5.375,7.375,9.375]
    # position of bar graph's names
    plt.ylabel('percent')
    # y axis name
    plt.title('Percent of Bus:Sedan in Northern')
    # title name
    plt.xticks(pos, ('Chiang Mai','Chiang Rai','Lampang','Phitsanulok','Tak'))
    # bar graph's name
    plt.show()
    # show bar graph
northern()