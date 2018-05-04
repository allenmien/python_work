# -*-coding:utf-8-*-
"""
@author:Mark
@file: retry_unvalidated_jobs.py 
@time: 2017/12/11
"""
# _*_ coding: utf-8 _*_
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class CONFIG(object):
    # dev mysql
    mysql_url = u"rm-bp1z121orwoh64axfo.mysql.rds.aliyuncs.com"
    mysql_port = 3306
    mysql_user = u"biz_test_user"
    mysql_password = u"Pass5688"
    mysql_db = u"biz_test_db"
    mysql_autocommit = True

    # prod mysql
    # mysql_url = u"rm-bp1w55r26pr639r36.mysql.rds.aliyuncs.com"
    # mysql_port = 3306
    # mysql_user = u"biz_user"
    # mysql_password = u"tGv+^PzTJRuf7%V3IbB8"
    # mysql_db = u"biz_db"
    # mysql_autocommit = True


def start():
    try:
        pass
    except Exception as e:
        print u"program error : " + str(e)


if __name__ == u"__main__":
    start()
