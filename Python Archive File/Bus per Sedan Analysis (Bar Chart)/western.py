import matplotlib.pyplot as plt
#use this to plot bar graph it can use for others graph
'''this function show Percent of Bus:sedan in Western area by picking data to calculate'''
def west():
    position = [1,3,5,7,9]
    y2 = [(316194+9021)/316194,(49983+1774)/49983,(52083+1167)/52083,
          (65058+1491)/65058,(57800+925)/57800]
          #Bus:Sedan
    sedan_per_bus = []
    for i in range(len(y2)):
        sedan_per_bus.append((y2[i]-1)*100)
        #translate data into percent 
    p1 = plt.bar(position, sedan_per_bus, label='Sedan per Bus in Western', color='c')
    # plot bar graph
    pos = [1.375,3.375,5.375,7.375,9.375]
    # position of bar graph's names
    plt.ylabel('percent')
    # y axis name
    plt.title('Percent of Bus:Sedan in Western')
    # title name
    plt.xticks(pos, ('Suphan Buri','Khanchana Buri','Nakhon Pathom','Ratchaburi','Samut Sakorn'))
    # bar graph's name
    plt.show()
    # show bar graph
west()
