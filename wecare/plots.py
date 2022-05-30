# function for plots
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path, PurePath
from wecare import PACKAGEDIR

def comp_training(postcode = 'all'): 
    
    fmaster = pd.read_csv("C:/Users/Gourib/preint/wecare/package_data/carehome_master.csv", sep="\t")
    if postcode =='all':
                
        comp = fmaster.loc[fmaster['training delivered']=='Yes'].count()[0]
        other = fmaster.loc[fmaster['training delivered']!='Yes'].count()[0]
        label = ['Yes','Not Known']
        plt.pie([comp,other], labels=label, autopct='%.2f')
    
    else:
        
        temp_df = fmaster[fmaster['Postcode'] == postcode] 
        comp = temp_df.loc[temp_df['training delivered']=='Yes'].count()[0]
        other = temp_df.loc[temp_df['training delivered']!='Yes'].count()[0]
        label = ['Yes','Not Known']
        plt.pie([comp,other], labels=label, autopct='%.2f')
        
def comp_box(postcode = 'all'): 
    
    fmaster = pd.read_csv("C:/Users/Gourib/preint/wecare/package_data/carehome_master.csv", sep="\t")
    if postcode =='all':
                
        comp = fmaster.loc[fmaster['box delivered']=='Yes'].count()[0]
        other = fmaster.loc[fmaster['box delivered']!='Yes'].count()[0]
        label = ['Yes','Not Known']
        plt.pie([comp,other], labels=label, autopct='%.2f')
    
    else:
        
        temp_df = fmaster[fmaster['Postcode'] == postcode] 
        comp = temp_df.loc[temp_df['box delivered']=='Yes'].count()[0]
        other = temp_df.loc[temp_df['box delivered']!='Yes'].count()[0]
        label = ['Yes','Not Known']
        plt.pie([comp,other], labels=label, autopct='%.2f')
        
        
def news2_trend(): 
    
    factivity = pd.read_csv("C:/Users/Gourib/preint/wecare/package_data/carehome_activity.csv", sep="\t")
    factivity['reading_date'] = factivity["wmd.caseload_yr -8"].astype(str) + "/" + factivity["caseload_month"]
    factivity['reading_date'] = factivity['reading_date'].replace('\n','')
    
    
    factivity = factivity.rename(columns={'NEWS2(0-4)': 'NEWS2_0-4', 'NEWS2(5-6)': 'NEWS2_5-6', 'NEWS2(7+)':'NEWS2_7_'})
    
    f_news2_7=factivity.groupby(['reading_date'])['NEWS2_7_'].sum()
    f_news2_5=factivity.groupby(['reading_date'])['NEWS2_5-6'].sum()
    f_news2_4=factivity.groupby(['reading_date'])['NEWS2_0-4'].sum()
    f_rd_date=factivity['reading_date'].unique()
    
    
    
    plt.figure(figsize=(20,10))
    plt.plot(f_rd_date,f_news2_7,label="NEWS2 7 Score",linewidth=2,color='red',marker="*")
    plt.plot(f_rd_date,f_news2_5,label="NEWS2 5-6 Score",linewidth=2,color='orange',marker="*")
    plt.plot(f_rd_date,f_news2_4,label="NEWS2 0-4Score",linewidth=2,color='green',marker="*")
    plt.title("NEWS2 Trend")
    plt.xlabel("Period")
    plt.ylabel("Score")
    plt.xticks(ticks=f_rd_date)
    plt.legend()
    
    