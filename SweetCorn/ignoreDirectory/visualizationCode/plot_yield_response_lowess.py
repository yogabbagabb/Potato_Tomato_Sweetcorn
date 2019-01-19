import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import os

lowess = sm.nonparametric.lowess
homePath = os.getcwd()

# Load data
os.chdir("../")
with open("csvNameFile.txt") as f:
    content = f.readlines()
os.chdir(homePath)
cropName = content[1].strip()
dataLocation = ""
if (cropName == "potato"):
    dataLocation = '../dataFiles/potato_with_anomaly.csv'
if (cropName == "tomato"):
    dataLocation = '../dataFiles/tomato_with_anomaly.csv'
if (cropName == "sweetcorn"):
    dataLocation = '../dataFiles/sweetcorn_with_anomaly.csv'

data = pd.read_csv(dataLocation,dtype={'FIPS':str})

# Add logical filter to the yield Data
area_con = data['area'].notnull()
data = data[area_con]

# Convert to t/ha
data.loc[:,'yield_ana'] = data.loc[:,'yield_ana'] * 0.0628


# Plot figure
# x_var = [['vpdave5','vpdave6','vpdave7','vpdave8','vpdave9'],['tave5','tave6','tave7','tave8','tave9'], 
         # ['precip5','precip6','precip7','precip8','precip9']]]

x_var = [['tmin5','tmin6','tmin7','tmin8','tmin9'],['tmax5','tmax6','tmax7','tmax8','tmax9'], 
         ['vpdmin5','vpdmin6','vpdmin7','vpdmin8','vpdmin9'], ['vpdmax5','vpdmax6','vpdmax7','vpdmax8','vpdmax9']]

y_var = 'yield_ana'

con = data['year']>1980
#con = data['year']>2015


numberMonths = 5
variableTypes = 4
fig, axes = plt.subplots(numberMonths, variableTypes, figsize=(12,6))
for row in range(0,numberMonths):
    for col in range(0,variableTypes):
        Z = lowess(data.loc[con,y_var],
                   data.loc[con, x_var[col][row]],
                   frac=0.3,it=3)
        
        axes[row,col].plot(Z[:,0], Z[:,1], 'r-', lw=4)
        axes[row,col].scatter(data.loc[con, x_var[col][row]], data.loc[con,y_var],s=1, 
                              color='grey',rasterized=True)
        if col !=0:
            axes[row,col].set_yticklabels('')

# axes[0,0].set_title('VPD (hPa)')        
# axes[0,1].set_title(u'Air temperature (\xb0C)')        
# axes[0,2].set_title('Precipitation (mm)')
axes[0,0].set_title('tmin')        
axes[0,1].set_title('tmax')        
axes[0,2].set_title('vpdmin')
axes[0,3].set_title('vpdmax')

        
axes[0,-1].text(1.05,0.5,'May',transform=axes[0,-1].transAxes, fontsize=12)
axes[1,-1].text(1.05,0.5,'June',transform=axes[1,-1].transAxes, fontsize=12)        
axes[2,-1].text(1.05,0.5,'July',transform=axes[2,-1].transAxes, fontsize=12)        
axes[3,-1].text(1.05,0.5,'August',transform=axes[3,-1].transAxes, fontsize=12)        
axes[4,-1].text(1.05,0.5,'September',transform=axes[4,-1].transAxes, fontsize=12)        


axes[1,0].text(-0.4,0.7,'Yield Anomaly (t/ha)',transform=axes[1,0].transAxes, 
               fontsize=10,rotation=90)

# Add knots

# VPD
# axes[1,0].text(1,0.925,'knots: 6.825,11.975,21.124',transform=axes[1,0].transAxes, 
               # fontsize=8,ha='right')
# axes[2,0].text(1,0.925,'knots: 8.816, 13.071, 24.728',transform=axes[2,0].transAxes, 
               # fontsize=8,ha='right')
# axes[3,0].text(1,0.925,'knots: 7.626, 9.482, 22.801',transform=axes[3,0].transAxes, 
               # fontsize=8,ha='right')
# # Tave
# axes[1,1].text(1,0.925,'knots: 15.434,20.784,25.129',transform=axes[1,1].transAxes, 
               # fontsize=8,ha='right')
# axes[2,1].text(1,0.925,'knots: 19.730,21.224,23.179,27.604',transform=axes[2,1].transAxes, 
               # fontsize=8,ha='right')
# axes[3,1].text(1,0.925,'knots: 18.980,21.866,26.7816',transform=axes[3,1].transAxes, 
               # fontsize=8,ha='right')

# # Precip
# axes[1,2].text(1,0.925,'knots: 87.768',transform=axes[1,2].transAxes, 
               # fontsize=8,ha='right')
# axes[2,2].text(1,0.925,'knots: 50.357',transform=axes[2,2].transAxes, 
               # fontsize=8,ha='right')
# axes[3,2].text(1,0.925,'knots: 50.607, 95.075',transform=axes[3,2].transAxes, 
               # fontsize=8,ha='right')





plt.subplots_adjust(top=0.95, bottom=0.05, left=0.075, right=0.925, hspace=0.3)

# # plt.xticks(range(5,30,2))
# # plt.xticks(range(0,400,25))
plt.savefig('./figures/figure_yield_response_lowess.png')
print('figure saved')
