# coding=utf=8
import os
import jpype

jvmArg = '-Djava.class.path='
for (root, dirs, files) in os.walk("./lib"):
    for filename in files:
        jvmArg = jvmArg + './lib/' + filename + ";"
jvmPath = jpype.getDefaultJVMPath()
jpype.startJVM(jvmPath, jvmArg)
Foo = jpype.JPackage('com.AlphaX').Foo
foo = Foo()
format_html = foo.start(u"hahaha")
jpype.shutdownJVM()
