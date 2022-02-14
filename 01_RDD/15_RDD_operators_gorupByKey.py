# coding:utf8

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName("test").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([('a', 1), ('a', 1), ('b', 1), ('b', 1), ('b', 1)])

    rdd2 = rdd.groupByKey()
    print(rdd2.collect())
    print(rdd2.map(lambda x: (x[0], x[1])).collect())   # 需要强转为list
    print(rdd2.map(lambda x: (x[0], list(x[1]))).collect())

