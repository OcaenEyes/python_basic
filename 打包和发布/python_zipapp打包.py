#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190624
    version:0.1.0
'''

'''
    zipapp 模块的命令行语法如下：

    python -m zipapp source [options]
    在上面命令中，source 参数代表要打包的 Python 源程序或目录，该参数既可以是单个的 Python 文件，也可以是文件夹。如果 source 参数是文件夹，那么 zipapp 模块会打包该文件夹中的所有 Python 文件。

    该命令的 options 支持如下选项：

    -o <output>，--output=<output>：应选项指定输出档案包的文件名。如果不指定该选项，所生成的档案包的文件名默认为 source 参数值，并加上 .pyz 后缀。
    -p <interpreter>，--python=<interpreter>：改选项用于指定 Python 解释器。
    -m <mainfn>，--main=<mainfn>：该选项用于指定 Python 程序的入口函数。该选项应该为 pkg.mod:fn 形式，其中 pkg.mod 是一个档案包中的包或模块，fn 是指定模块中的函数。如果不指定该选项，则默认从模块中的 __main__.py 文件开始执行。
    -c，--compress：从 Python 3.7 开始支持该选项。该选项用于指定是否对档案包进行压缩来减小文件的大小，默认是不压缩。
    --info：该选项用于在诊断时显示档案包中的解释器。
    -h，--help：该选项用于显示 zipapp 模块的帮助信息。


'''