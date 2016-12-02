import matplotlib.pyplot as plt
"""this fuction has shown number of sedan cars users and bus in East"""
def east():
    positions = [1, 3, 5, 7, 9]
    y2 = [(20471+369)/20471, (40202+670)/40202, (53766+2299)/53766, (248767+6091)/248767, (133334+1996)/133334]
          #Bus:Sedan
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
        #translate data into percent 
    p1 = plt.bar(positions, sedan_per_bus, label='Sedan per Bus in East', color='c')
    # plot bar graph
    pos = [1.375,3.375,5.375,7.375,9.375]
    # position of bar graph's names
    plt.ylabel('percent')
    # y axis name
    plt.title('Percent of Bus:Sedan in East')
    # title name
    plt.xticks(pos, ('Nakhon Nayok','Prachinburi','Chachoengsao','Chonburi','Rayong'))
    # bar graph's name
    plt.show()
    # show bar graph
east()
