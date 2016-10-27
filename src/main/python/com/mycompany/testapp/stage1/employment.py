from smv import *
from pyspark.sql.functions import col, sum, lit

from com.mycompany.testapp.stage1 import inputdata

__all__ = ['PythonEmploymentByState']

class PythonEmploymentByState(SmvPyModule):
    """Python ETL Example: Employment"""

    def requiresDS(self):
        return [inputdata.PythonEmployment]

    def run(self, i):
        df = i[inputdata.PythonEmployment]
        return df.groupBy(col("ST")).agg(sum(col("EMP")).alias("EMP"))


class PythonEmploymentByStateCategory(SmvPyModule):
    """Python Employment By State With Category"""

    def requiresDS(self):
        return [PythonEmploymentByState]

    def run(self, i):
        df = i[PythonEmploymentByState]
        return df.selectPlus((col("EMP") > lit(10000000)).alias("cat_high_emp"))
