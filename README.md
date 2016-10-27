# SMV for Data Analysis

This is a training program for people to have an idea of how to conduct various data analyses using SMV (Spark Modularized View) - a framework to use Spark to develop large scale data applications. API docs can be found [here](http://tresamigossd.github.io/SMV/scaladocs/index.html#org.tresamigos.smv.package).


## Preliminaries
* [Installation and Project Initialization](https://github.com/TresAmigosSD/SmvTraining)
* Recap: Basics and Key Concepts (e.g. project dir hierarchy, key concepts like smv stages, modules)?


## Data Quick View
By running smv-jupyter command at the project top-level directory, a jupyter notebook will start which supports the interactive mode of smv. Users are able to use smv functions and built-in functions of pyspark to do quick checks of the data. 
* [A quick peek at the data](https://render.githubusercontent.com/view/ipynb?commit=d41d368fdd521251fcec8a6bf637a6fa8965702b&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f73617261686e677576742f534d56666f7244617461416e616c797369732f643431643336386664643532313235316663656338613662663633376136666138393635373032622f6e6f7465626f6f6b732f446174615f517569636b5f566965772e6970796e62&nwo=sarahnguvt%2FSMVforDataAnalysis&path=notebooks%2FData_Quick_View.ipynb&repository_id=71542137#1.-A-quick-peek-at-the-data)
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
  * Date/Time (smv date/time related functions)
  * Currency


## Data Quality Management
* Missing Values
* Outliers
* smv dqm package?    

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
