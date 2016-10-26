# SMV for Data Analysis

This is a training program for people to have an idea of how to conduct various data analyses using SMV (Spark Modularized View) - a framework to use Spark to develop large scale data applications. API docs can be found [here](http://tresamigossd.github.io/SMV/scaladocs/index.html#org.tresamigos.smv.package).


## Preliminaries
* [Installation and Project Initialization](https://github.com/TresAmigosSD/SmvTraining)
* Recap: Basics and Key Concepts (e.g. project dir hierarchy, key concepts like smv stages, modules)?


## Data Quick View
By running smv-jupyter command at the project top-level directory, a jupyter notebook will start which supports the interactive mode of smv. Users are able to use smv functions and built-in functions of pyspark to do quick checks of the data. 
* [A quick peek at the data](link)
* Ad-hoc analyses
a) demonstrate other functions
b) can easily convert to pandas?


## Manipulating Various Data Types
* Binary
* [Categorical](link)
* Ordinal
* Continuous
* Others
  * Unique identifier
  * Date/Time
  * Currency


## Data Quality Management
dqm package?
* Missing Values
  * Filter / Missing value imputation

* Outliers
  * Cap / Floor
    

## Data Transformation and Merge
* demonstrate functionalities supported by smvDFHelper (e.g. column plus/minus/rename, dedup, join, union, etc.)


## Data Aggregation
* straightforward aggregations (smvGroupBy.agg(...))
* smv grouped data functions (runAgg, oneAgg, pivot, etc.)
* CDS application

----
***TBD:***
* where or whether to mention add new modules / modify existing modules?
* what sample data to use? 
