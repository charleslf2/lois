# verison 0.0.7

# import usefull package 

import numpy as np 
import pandas as pd 
from rich.traceback import install
from rich.console import Console
from rich.theme import Theme
#from rich.markdown import Markdown
from rich import print
from rich.panel import Panel
from rich.tree import Tree
#from rich.console import group
from rich.table import Table
import matplotlib.pyplot as plt 
import seaborn as sns
#from rich.layout import Layout
import time
from rich.progress import track

## custom theme
custom_theme=Theme({"warning":"red"})

install()
console = Console()


## this is the main function for our mvp the params are limited

def lois_ds_report(data, target_variable:str, report_complexity="simple"):

    """
    lois_report generate clean and insightful data science report based on your params

    Prams:
    -----

    . data (df|required) = Should be pandas dataframe

    .target_variable("str"|required) = The target variable of your dataset (same as in your dataset)

    . report_complexity ("str"|default ="simple) = Indicate the level  of details  of the report 

    Usages:
    ------

    >>> from lois import lois_ds_report
    >>> lois_ds_report(data, target_variable="gender", report_complexity="simple")
    """

    ## some check and error raise

    # the data

    if isinstance(data, pd.DataFrame):
        pass
    else:
        raise ValueError("The data should be a pandas Dataframe")
    # the report_complexity

    if report_complexity != "simple":
        raise ValueError(' The report_complexity should be "simple"  \n e.g. report_complexity="simple" ')
    

    # the target variable
    elif target_variable ==None :
        raise Warning("The report will be limited if you don't pass any target variable")

    ####################################################################################################################
    ##TODO if everything is good make a progress bar before showing the report
    #for i in track(range(5), description="Processing..."):
    #    time.sleep(1)  # Simulate work being done
    ####################################################################################################################
    ## THE REPORT START

    # the title

    ## style the pannel a better way
    console.print(Panel(" ", title="Exploratory Data Anlysis" ,subtitle="EDA|simple| Suitable for data scientist",
                    title_align="center", subtitle_align="center") )

    ####################################################################################################################
    # the report tree summary

    tree=Tree("EDA", guide_style="bold")

    shape_analysis_tree= tree.add("Dataset Shape Analysis")
    shape_analysis_tree.add("Dataset head")
    shape_analysis_tree.add("General info ")
    shape_analysis_tree.add("The target variable")
    shape_analysis_tree.add("Number of rows and columns")
    different_dtypes_tree=shape_analysis_tree.add("The different data types")
    different_dtypes_tree.add("The sum of different variable type")
    different_dtypes_tree.add("Visual representation of different variable type")
    misssing_value_tree=shape_analysis_tree.add("Analyze missing value")
    misssing_value_tree.add("The percentage of missing value in each columns")
    misssing_value_tree.add("The missing value counts")
    misssing_value_tree.add("Visual representation of missing value")

    print(tree)


    print(Panel("", title="DATASET SHAPE ANALYSIS", title_align="center",expand=True))

    ####################################################################################################################
    # The dataset head
    #TODO data head display

    console.print("-------------------- THE HEAD OF YOUR DATASET --------------------", justify="center",)

    table = Table(title="The Dataset", expand=True)

    if data.shape[1]>8:
        console.print("Your dataset is too large ; only the first 8 columns will be display")
        for  col in data.columns[0:9]:
            table.add_column(col, justify="right", style="cyan", no_wrap="true")
            
        #for row in data.index[0:5]:
            #table.add_row(row)
    
    else:
        for col in data.columns[0:data.shape[1]]:
            table.add_column(col, justify="right", style="cyan", no_wrap="true")
    
        
    #for row in data.index[0:6]:
        #table.add_row(row)

    console.print(table)


    ####################################################################################################################
    # Some general info about dataset
    console.print("-------------------- SOME GENERAL INFO ABOUT YOUR DATASET --------------------", justify="center")
    data.info()

    #######################################################################################################################
    # the target variable 

    console.print("-------------------- THE TARGET VARIABLE OF YOUR DATASET --------------------", justify="center")
    print(Panel.fit(f"The Target variable is : '{target_variable}' "))

    ####################################################################################################################
    # the shape of dataset

    console.print("-------------------- ROWS AND COLUMNS IN YOUR DATASET --------------------", justify="center")    

    dshape=data.shape
    row=dshape[0]
    columns=dshape[1]

    print(Panel.fit(f"{dshape}" , title="Shape output", title_align="center"))

    print(Panel.fit(f"Your dataset contains {row} Rows and {columns} Columns"))


    ####################################################################################################################
    # data types

    console.print("-------------------- THE DATA TYPES IN YOUR DATASET --------------------", justify="center")

    
    # TODO render the number of categorical and numerical varible


    ddtypes=data.dtypes.value_counts()
    print(Panel.fit(f"{ddtypes}", title="Data types output", title_align="center"))
   

    #visuallize the data types

    plt.figure(figsize=(4,4))
    plt.title("Variables types in your dataset")
    data.dtypes.value_counts().plot.pie()
    plt.show()
   


    # summary of data types

    #for col in data.select_dtypes("object"):
        #data[col].value_count()
    
    #print(categorical)


    ####################################################################################################################
    # Some basic statistic
    #console.print("########## YOUR DATASET BASIC STATISTIC ##########", justify="center")
    #print(data.describe())
    #console.print("########## END ##########", justify="center")
    ####################################################################################################################
    # misisng value

    console.print("-------------------- MISSING VALUE IN YOUR DATASET --------------------", justify="center")


    missing_value=(data.isna().sum()/data.shape[0]).sort_values(ascending=True)
    
    print(Panel.fit(f"{missing_value}", title="Missing value output", title_align="center"))

    # missing value count
    missing_value_counts=(data.isna().sum()/data.shape[0]).value_counts(ascending=True)

    
    print(Panel.fit(f"{missing_value_counts}", title="Missing value counts output" ,title_align="center"))


    # visualiaze missing value
    plt.figure(figsize=(5,4))
    plt.title("Missing value  in your dataset")
    sns.heatmap(data.isna())
    plt.show()


    console.print("#################### END ####################", justify="center")

    ####################################################################################################################


    ####################################################################################################################


    # Analyz The target variable 

    #target= data[target_variable]
    #print_target_variable=print(f"{target_variable}")

    #if target.dtypes == 'float' or "int":
    #    target_numerical_stat=target.describe()
    #    console.print("target_numerical", target_numerical_stat, "\n")
    #else :
    #    target_categorical_unique= target.unique()
    #    console.print("target_categorical_unique", target_categorical_unique, "\n")

    
   



    



