import matplotlib.pyplot as plt
#use this to plot bar graph it can use for others graph
'''this function show Percent of Bus:sedan in Southern area by picking data to calculate'''
def south():
    position = [1,3,5,7,9]
    y2 = [(104021+3106)/104021,(94052+2818)/94052,(101689+6580)/101689,
          (199684+6014)/199684,(32698+1132)/32698]
          #Bus:Sedan
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
        #translate data into percent 
    p1 = plt.bar(position, sedan_per_bus, label='Sedan per Bus in Southern', color='c')
    # plot bar graph
    pos = [1.375,3.375,5.375,7.375,9.375]
    # position of bar graph's names
    plt.ylabel('percent')
    # y axis name
    plt.title('Percent of Bus:Sedan in Southern')
    # title name
    plt.xticks(pos, ('Surat Thani','Nakhon Si Thammarat','Phuket','Songkhla','Yala'))
    # bar graph's name
    plt.show()
    # show bar graph
south()
