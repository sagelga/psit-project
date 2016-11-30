import matplotlib.pyplot as plt
"""this fuction has shown number of sedan cars users and bus in NEast"""
def neast():
    positions = [1, 3, 5, 7, 9]
    y2 = [(32721+978)/32721, (22857+651)/22857, (98041+2080)/98041, (43569+1051)/43569, (204231+6021)/204231]
          #Bus:Sedan
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
        #translate data into percent 
    p1 = plt.bar(positions, sedan_per_bus, label='Sedan per Bus in NEast', color='c')
    # plot bar graph
    pos = [1.375,3.375,5.375,7.375,9.375]
    # position of bar graph's names
    plt.ylabel('percent')
    # y axis name
    plt.title('Percent of Bus:Sedan in NEast')
    # title name
    plt.xticks(pos, ('Chaiyabhumi','Yasothorn','Ubon Ratcha-Thani','Buriram','Nakhon Ratchasri-ma'))
    # bar graph's name
    plt.show()
    # show bar graph
neast()
