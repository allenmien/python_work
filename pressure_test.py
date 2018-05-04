# -*-coding:utf-8-*-
import io

import requests
from gevent import pool


class Pressure(object):
    def __init__(self):
        self.thread_size = 50
        self.Pool = pool.Pool(self.thread_size)
        self.url = "http://10.0.1.74:9090/getHtml"
        self.html = ""
        with open("./text.txt") as f:
            self.html = str(f.read())
        self.data = {"html": self.html}

    def start(self):
        for i in range(self.thread_size):
            self.Pool.spawn(self.request_core)
        self.Pool.join()

    def request_core(self):
        while True:
            try:
                resp = requests.post(url=self.url, data=self.data)
                resp_text = resp.text

                if resp_text:
                    foo()
                if foo.success_count % 50 == 0:
                    log = u"Success Count :" + str(foo.success_count)
                    write_log(log)
            except Exception as e:
                write_log("error" + str(e))


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


@static_vars(success_count=0)
def foo():
    foo.success_count += 1


def write_log(line):
    file_obj = io.open(u"./pressure_log.txt", mode=u"a", encoding=u"utf-8")
    file_obj.write(line + u"\n")
    file_obj.close()


if __name__ == u"__main__":
    pressure = Pressure()
    pressure.start()
