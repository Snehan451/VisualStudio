import pyspark
from pyspark import SparkContext,SparkConf
sc=SparkContext.getOrCreate()
myRDD=sc.parallelize([('Rama',11),('krishna',23),('Meena',5),('John',45),('Alfred',13),('Vinoth',21),('Sneha',18),('Priya',19)])
mypy=sc.parallelize([12,45,767,89,9,33,55,777,223])
"""myRDD=sc.parallelize([
                     [1,2,3],
                     [3,4,6],
                     [5,6,7],
                     [10,12,14]
                     ])"""
myRDD.take(2)
mypy.take(2)
print(myRDD.collect()) # gets all the values that are present/stored in the  rdd
#print(" The number of Rdd values is ",str(myRDD.count()))

