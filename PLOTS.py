import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import NOBELDATACLEANINGANDANALYSIS as ndc
import plotly.express as px
df2=ndc.df
print(df2)
pdf=ndc.plot_df
Male=df2.loc[df2['sex']=='Male'].count()[0]
Female=df2.loc[df2['sex']=='Female'].count()[0]
labels=['Male','Female']
colors=['#ccff66','#66ccff']
explode=[0.1,0]
plt.pie([Male,Female],labels=labels,colors=colors,autopct='%.2f %%',explode=explode)
plt.title('GENDER WISE DISTRIBUTION OF NOBEL LAUREATES')   
plt.show()
sns.histplot(data=df2,x='category',hue='sex',palette=["#66ccff","#91FF01"],alpha=0.6,edgecolor='black')
plt.grid(True,linestyle='--',alpha=0.6)
plt.ylabel("Number Of Prizes")
plt.xlabel("Category")
plt.title("Category Wise Distribution Of Nobel Prize")
plt.show()
#Plotting scatter and rolling average over the years.
pdf = pdf.reset_index()    #groupby ke baad ye code likhna jaruri hai to make the index ------> column.
#print(pdf)
plt.scatter(pdf['year'],pdf['prize'],color='dodgerblue',alpha=0.7)
plt.plot(pdf['year'],pdf['Rolling Average'],color='crimson',linewidth=3)
plt.xticks(ticks=np.arange(1900,2021,step=5),rotation=45,fontsize=11)
plt.yticks(fontsize=11)
plt.xlabel('Year',fontsize=16)
plt.ylabel('Number of Prizes',fontsize=16)
plt.title('Number of Nobel Prizes Awarded Every Year',fontsize=18)
plt.show()
plot_df2=df2.groupby(['birth_country_current','category']).agg({'prize':pd.Series.count})
#plot_df2=plot_df2.reset_index()
print(plot_df2)
plot_df2.sort_values('prize',ascending=False,inplace=True)
print(plot_df2)
sns.barplot(data=plot_df2.head(29),x='prize',y='birth_country_current',errorbar=None,hue='category')
plt.xlabel('Number Of Prizes',fontsize=14)
plt.title('Top 10 Nobel Prize Winning Nations')
plt.show()
plot_df3=df2.groupby(by=['birth_country_current','year',],as_index=False).count().reset_index()
prize_evry_yr=plot_df3.sort_values('year')[['birth_country_current','year','prize']]
print(prize_evry_yr)
cummulative_prizes=prize_evry_yr.groupby(by=['birth_country_current','year']).sum().groupby(level=0).cumsum().reset_index()
print(cummulative_prizes)
l_chart=px.line(cummulative_prizes,
                x='year',
                y='prize',
                color='birth_country_current',
                title='CUMMULATIVE NOBEL PRIZES WON OVER THE YEARS BY DIFFERENT COUNTRIES')
l_chart.update_layout(xaxis_title='YEAR',yaxis_title='CUMMULATIVE NUMBER OF PRIZES')
l_chart.show()







