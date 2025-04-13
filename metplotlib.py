import matplotlib.pyplot as plot
# set up lists
numlist = [10, 7, 4, 2]
namelist = ['Cats', 'Dogs', 'Chickens', 'Fish']
colorlist = ['orange', 'salmon', 'pink', 'yellow' ]
explodelist = [0.4, 0.3, 0.2, 0.1] #the distance of the pieces of the chart from the center
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist, # autopct =  decimal places of number
    	explode = explodelist, startangle = 60)
plot.axis('equal')
plot.savefig('piechart.png')


