# SMV for Data Analysis

This is a training program for people to have an idea of how to conduct various data analyses using SMV (Spark Modularized View) - a framework to use Spark to develop large scale data applications. API docs can be found [here](http://tresamigossd.github.io/SMV/scaladocs/index.html#org.tresamigos.smv.package).


## Preliminaries
* [Installation and A Sample Project](https://github.com/TresAmigosSD/SmvTraining)


## Data Quick View
***TOWRITE: why this is important?***
By running smv-jupyter command at the project top-level directory, a jupyter notebook will start which supports the interactive mode of smv. Users are able to use smv functions and built-in functions of pyspark to do quick checks of the data. Employment data in the sample project in [SmvTraining](https://github.com/TresAmigosSD/SmvTraining) will be used.
* [Input data overview](https://github.com/sarahnguvt/SMVforDataAnalysis/blob/master/notebooks/Data_Quick_View.ipynb)
* Data Quality Control
* Profiling for Insights

## Smv Application: airline case study
Points to mention:
* Project hierarchy
* Dependency
* Relationships between Smv frameworks (stages, modules, etc.) and how Smv provides the convenience to manage all these

### Data Transformation and Merge
* demonstrate functionalities supported by smvDFHelper (e.g. column plus/minus/rename, dedup, join, union, etc.)


### Data Aggregation
* straightforward aggregations (smvGroupBy.agg(...))
* smv grouped data functions (runAgg, oneAgg, pivot, etc.)
* CDS application


### Manipulating Various Data Types 
Manipulate/recode different data types for an analytic view
* Binary Variable
* [Categorical Variable](https://github.com/sarahnguvt/SMVforDataAnalysis/blob/master/notebooks/Manipulating_Various_Data_Types.ipynb)
* Ordinal Variable
* Continuous Variable
* Others
  * Unique identifier (dup)
  * Date/Time (smv date/time related functions)
  * Money


### Data Quality Control
* QC throughout the process
  * check input as real data always have flaws
  * QC data output after manipulation/transformation/aggregation
* Missing Values 
* Outliers 
smv dqm package?    

----
***Comments***
* employment data for quick view; airline data for application
* show the progress of how a project / data can grow in the airline case
