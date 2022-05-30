# function for utilities
import numpy as np
import pandas as pd
from pathlib import Path, PurePath
from wecare import PACKAGEDIR


def load_master(filepath):
    
    """
    This function is used to load the master carehome dataset. 
    It returns a pandas dataframe.

    Parameters:

    filepath - parameter accepts string value. 
    master file to be read

    Function will return the pandas dataframe of the master dataset.
    """
    
    dirname = str(PACKAGEDIR)
    dirname = dirname.replace("\\", "/")   
    
    file_name = dirname + '/package_data/carehome_master.csv'    
    
    master_df = pd.read_csv(filepath)
    master_df.to_csv(file_name, sep="\t", index=False,)
    return master_df
    
def load_activity(filepath):
    
    """
    This function is used to load the carehome activity dataset. 
    It returns a pandas dataframe.

    Parameters:

    filepath - parameter accepts string value. 
    master file to be read

    Function will return the pandas dataframe of the carehome activity dataset.
    """
    dirname = str(PACKAGEDIR)
    dirname = dirname.replace("\\", "/")   
    
    file_name = dirname + '/package_data/carehome_activity.csv'  
    activity_df = pd.read_csv(filepath)
    
    activity_df.to_csv(file_name, sep="\t", index=False,)    
    return activity_df


def load_population(filepath):
    
    """
    This function is used to load the population dataset. 
    It returns a pandas dataframe.

    Parameters:

    filepath - parameter accepts string value. 
    master file to be read

    Function will return the pandas dataframe of the population dataset.
    """
    master_df = pd.read_csv(filepath)
    return master_df
    
def merger_utility():
    
    """
    This function is used to join the carehome master and activity dataset using inner join. 
    It returns a pandas dataframe.

    Function will return the merged pandas dataframe for the combined dataset.
    """
    
    dirname = str(PACKAGEDIR)
    dirname = dirname.replace("\\", "/")   
    
    fmaster_fp = dirname + '/package_data/carehome_master.csv' 
    factivity_fp = dirname + '/package_data/carehome_activity.csv' 
    
    fmaster = pd.read_csv(fmaster_fp, sep="\t")
    factivity = pd.read_csv(factivity_fp, sep="\t")
    carehome = pd.merge(fmaster, factivity,
                left_on="CareHome_id", right_on="CAREHOME_id", how="inner")
    
    return carehome
    
def get_master_kpi():    
    
    """
    This function is returns some usefull KPI for the master dataset.
    """
       
    dirname = str(PACKAGEDIR)
    dirname = dirname.replace("\\", "/")   
    
    fmaster_fp = dirname + '/package_data/carehome_master.csv' 
    fmaster = pd.read_csv(fmaster_fp, sep="\t")
    
    
    print('Bed Numbers:', fmaster['Bed numbers'].sum())
    
    sol = fmaster[fmaster['box delivered'] == 'Yes'].count() 
    print('box_delivered:', sol['box delivered'])
    
    sol = fmaster[fmaster['training delivered'] == 'Yes'].count()
    print('training_delivered:', sol['training delivered'])
    
    print('\n CCG Counts: \n')
    print( fmaster["CCG"].value_counts())

def get_carehome_details(carehomeid):
    
    """
    This function is returns some usefull KPI for the master and activity dataset.
    """
    
    dirname = str(PACKAGEDIR)
    dirname = dirname.replace("\\", "/")   
    
    fmaster_fp = dirname + '/package_data/carehome_master.csv' 
    factivity_fp = dirname + '/package_data/carehome_activity.csv' 
    
    fmaster = pd.read_csv(fmaster_fp, sep="\t")
    factivity = pd.read_csv(factivity_fp, sep="\t")
           
    sol = fmaster[fmaster['CareHome_id'] == carehomeid] 
    act = factivity[factivity['CAREHOME_id'] == carehomeid] 
    
    print('Bed Numbers:', sol['Bed numbers'].sum())
    print('post_code:', sol['Postcode'].unique())
    print('box_delivered:', sol['box delivered'].unique())
    print('training_delivered:', sol['training delivered'].unique())
   
    
    print(f"Avg NEWS2: {act['NEWS2'].sum()}")
    print(f"Avg NEWS2(7+): {act['NEWS2(7+)'].sum()}")
    act = factivity[factivity['CAREHOME_id'] == carehomeid] 


        