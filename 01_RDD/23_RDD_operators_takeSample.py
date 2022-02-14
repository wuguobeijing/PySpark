# coding:utf8

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName("test").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([1, 3, 5, 3, 1, 3, 2, 6, 7, 8, 6], 2)
    print(rdd.first())
    print(rdd.take(2))
    print(rdd.top(3))
    print(rdd.takeSample(False, 5, 1))
