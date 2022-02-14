# coding:utf8

# 导入Spark的相关包
import time

from pyspark import SparkConf, SparkContext
from pyspark.storagelevel import StorageLevel

if __name__ == '__main__':
    # 0. 初始化执行环境 构建SparkContext对象
    conf = SparkConf().setAppName("test").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    # 1. 读取数据文件
    file_rdd = sc.textFile("../data/input/apache.log")

    # 2. 对数据进行切分 \t
    split_rdd = file_rdd.map(lambda x: x.split(" "))
    # 3. 因为要做多个需求, split_rdd 作为基础的rdd 会被多次使用.
    split_rdd.persist(StorageLevel.DISK_ONLY)

    # TODO: 需求1: 网站访问次数
    url_rdd = split_rdd.map(lambda x: x[4])
    url_withone_rdd = url_rdd.map(lambda x: (x, 1))
    count_rdd = url_withone_rdd.reduceByKey(lambda a,b: a+b)
    print(count_rdd.collect())

    # TODO: 需求2: 网站访问用户数
    url_user_rdd = split_rdd.map(lambda x: (x[4], x[1]))
    only_url_user_rdd = url_user_rdd.distinct()
    print(only_url_user_rdd.collect())
    count_user_rdd = only_url_user_rdd.map(lambda x: (x[0], 1)).reduceByKey(lambda a, b: a+b)
    print(count_user_rdd.collect())
