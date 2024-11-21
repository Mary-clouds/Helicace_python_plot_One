#import matplolib
import matplotlib.pyplot as plt
#data for plotting
x = []
y=[]
z = []
#create the plot
plt.plot(x,y)
plt.plot(x,z)

#add labels and title
plt.xlabel('')
plt.ylabel('')
plt.title('')
#styling the plot
#saving the plot in as a jpg
plt.savefig('plot_image.jpg', dpi= 300)
#display the plot
plt.show()