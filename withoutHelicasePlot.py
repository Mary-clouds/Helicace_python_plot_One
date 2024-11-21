#import matplolib
import matplotlib.pyplot as plt
#data for plotting
ntc = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01, 0.01, 0.03, 0.08, 0.17, 0.35, 0.68, 1.27, 2.26, 3.85, 6.29, 9.85, 14.72, 20.94, 28.32, 36.38, 44.50, 52.09, 58.75, 64.37, 68.98, 72.72, 75.76, 78.21]
pcc=[0.00023409, 0.005710821, 0.037607552, 0.14426721, 0.410474025,	0.964104752, 1.977231371, 3.656826876,	6.21940422,	9.846621333, 14.62751274, 20.50613663, 27.26200691, 34.54222462, 41.93778159, 49.07107261,	55.65889077, 61.53485281,	66.63787878, 70.98371556,	74.63441357, 77.67373478,	80.19057318,	82.26934514,	83.98534638,	85.40320809, 86.57707366,	87.55160358, 88.36328343, 89.04175343]
cya = [0, 0.000191321, 0.003378467, 0.026198694, 0.129081655, 0.47586267, 1.427901814, 3.646466029,	8.087585485, 15.65545621, 26.43950791, 39.18452325,	51.85541354, 62.80637286, 71.35686279, 77.60130112,	81.98535034, 85.00360243, 87.06859687, 88.48441202]
x_achse = list(range(1, 31))

#create the plot
plt.plot(x_achse, ntc)
plt.plot(x_achse, pcc)
plt.plot(x_achse, cya)


#styling the plot 
plt.plot( x_achse, ntc, label ='NTC (n=5)', color = 'b')
plt.plot( x_achse, pcc, label ='PCC 7806 (n=2)', color = 'g')
plt.plot( x_achse, cya, label ='CYA 126 (n=3)', color = 'r')


#add labels and title

plt.title('Without Helicase')
plt.xlabel('Cycles')
plt.ylabel('dRn')
plt.legend()

#saving the plot in as a jpg
plt.savefig('plot_image.jpg', dpi= 300)
#display the plot
plt.show()