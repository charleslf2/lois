# verison 0.4.0

# import usefull package 

import numpy as np 
import pandas as pd 
from rich.traceback import install
from rich.console import Console
from rich.theme import Theme
from rich import print
from rich.panel import Panel
from rich.tree import Tree
#from rich.console import group
from rich.table import Table
import matplotlib.pyplot as plt 
import seaborn as sns

## custom theme
custom_theme=Theme({"warning":"red"})

install()
console = Console()



def lois_ds_report(data, target_variable:str, report_complexity="simple"):

    """
    lois_ds_report generate clean and insightful data science report based on your params

    Params:
    -----

    . data (df|required) = Should be pandas dataframe

    .target_variable(str|required) = The target variable of your dataset (should be the same as in your dataset)

    . report_complexity (str|default ="simple" or "advanced") = Indicate the level  of details  of the report 

    Usages:
    ------

    >>> from lois import lois_ds_report
    >>> lois_ds_report(data, target_variable="gender", report_complexity="simple")
    """

    def simple_analytics():


        ####################################################################################################################
        # the title

        console.print(Panel(" ", title="Exploratory Data Anlysis" ,subtitle="EDA|simple| Suitable for data scientist",
                        title_align="center", subtitle_align="center") )

        ####################################################################################################################
        # the report tree summary

        tree=Tree("Shape Analysis", guide_style="bold")

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


        ddtypes=data.dtypes.value_counts()
        print(Panel.fit(f"{ddtypes}", title="Data types output", title_align="center"))
    

        #visuallize the data types

        plt.figure(figsize=(4,4))
        plt.title("Variables types in your dataset")
        data.dtypes.value_counts().plot.pie()
        plt.show()

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
        ####################################################################################################################









        ####################################################################################################################
        ####################################################################################################################
        ####################################################################################################################

    def advanced_analysis():

        ####################################################################################################################
        # the title

        console.print(Panel(" ", title="Exploratory Data Anlysis" ,subtitle="EDA|advanced| Suitable for data scientist",
                        title_align="center", subtitle_align="center") )

        ####################################################################################################################
        
        ####################################################################################################################
        # the report tree summary

        tree=Tree("Background Analysis", guide_style="bold")

        back_analysis_tree= tree.add("Dataset Background Analysis")
        back_analysis_tree.add("Analyze the target variable")
        back_analysis_tree.add("Analyze the float variables")
        back_analysis_tree.add("Analyze the object variables")
        back_analysis_tree.add("The corrleation between float and integer variables")
        back_analysis_tree.add("Plot all numerical variables ")
     

        print(tree)


        print(Panel("", title="DATASET BACKGROUND ANALYSIS", title_align="center",expand=True))

        ####################################################################################################################

        # analyze the target variable
        console.print("-------------------- ANALYZE THE TARGET VARIABLE --------------------", justify="center")

        type_target_var=data[target_variable].dtype
        print(type_target_var)
        if type_target_var == 'object':
            stat_target_var=data[target_variable].value_counts()
            pd.set_option('display.max_column', data.shape[1])
            pd.set_option('display.max_row', data.shape[1])
            print(Panel.fit(f"{stat_target_var}", title="Target variable count output", title_align="center"))
            fig=plt.figure(figsize=(4,4))
            fig.suptitle("Visualize your target variable")
            stat_target_var.plot.pie()
            plt.show()
        if type_target_var == 'float':
            plt.figure(figsize=(4,4))
            plt.title("Visualize your target variable")
            sns.displot(data[target_variable])
            plt.show()
        if type_target_var =='int64':
            plt.figure(figsize=(4,4))
            plt.title("Visualize your target variable")
            sns.displot(data[target_variable])
            plt.show()
        if type_target_var == 'bool':
            stat_target_var=data[target_variable].value_counts()
            print(Panel.fit(f"{stat_target_var}", title="Target variable count output", title_align="center"))
            fig=plt.figure(figsize=(4,4))
            fig.suptitle("Visualize your target variable")
            data[target_variable].value_counts().plot.pie()
            plt.show()
        ####################################################################################################################
        # analyze the float variables
        console.print("-------------------- ANALYZE THE FLOAT VARIABLES --------------------", justify="center")
        
        for col in data.select_dtypes("float"):
            print(Panel.fit(f"{data[col].describe()}", title="Float variables" ,title_align="center"))

        ####################################################################################################################
        # analyze the object variables
        console.print("-------------------- ANALYZE THE OBJET VARIABLES --------------------", justify="center")
        for col in data.select_dtypes("object"):
            print(Panel.fit(f"{col :-<40} {data[col].unique()}", title="Object variables unique value" ,title_align="center"))

        ####################################################################################################################
        # analyze the object variables
        console.print("-------------------- ANALYZE THE INTEGER VARIABLES --------------------", justify="center")
        for col in data.select_dtypes("int64"):
            print(Panel.fit(f"{data[col].describe()}", title="Integer variables" ,title_align="center"))
        #################################################################################################
        # correlation between float and integer variables

        console.print("-------------------- CORRELATION BETWEEN FLOAT AND INTEGER VARIABLES --------------------", justify="center")
        #print(Panel.fit(f"{data.corr()}", title="The correlation", title_align="center"))
        plt.figure(figsize=(6,6))
        plt.title("Correlation between variables")
        sns.heatmap(data.corr(), annot=True)
        plt.show()

        #################################################################################################
        #console.print("-------------------- YOUR DATASET IN ONE  PLOTS --------------------", justify="center")
        #fig=plt.figure()
        #fig.suptitle("Your pairplot")
        #sns.pairplot(data)
        #plt.show()

        ##################################################################################################
        console.print("-------------------- PLOT ALL NUMERICAL VARIABLES --------------------", justify="center")
        data.hist(bins=50, figsize=(20,15))
        plt.show()


        #################################################################################################

        console.print("#################### END ####################", justify="center")


    if isinstance(data, pd.DataFrame):
        pass
    else:
        raise ValueError("The data should be a pandas Dataframe")
    # the report_complexity

    if report_complexity == "simple":
        simple_analytics()
    elif report_complexity == "advanced":
        advanced_analysis()
    else:
        raise ValueError(' The report_complexity should be "simple" or "advanced"  \n e.g. report_complexity="simple" or "advanced" ')
    
    # the target variable
    if target_variable ==None :
        raise Warning("The report will be limited if you don't pass any target variable")


  
   


    



