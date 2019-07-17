#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'test module'

__author__ = 'ycn'
# 第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 第6行使用__author__变量把作者写进去
# Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用
# 我们以内建的sys模块为例，编写一个hello的模块

import sys  # 导入sys模块,导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!', args[0])
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该module模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__ == '__main__':
    test()

# 作用域
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
# 在Python中，是通过_前缀来实现的。
# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
# module模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
# 是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量

#################  安装第三方模块  ###################
# 在Python中，安装第三方模块，是通过包管理工具pip完成的。
# 如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。
# 在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip。
# 注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。
# 例如，我们要安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。
# 不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3。
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，
# 可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：pip install Pillow

# 安装常用模
# 在使用Python时，我们经常需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。
# 用pip一个一个安装费时费力，还需要考虑兼容性。我们推荐直接使用Anaconda，
# 这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，
# 我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。
# 可以从Anaconda官网下载GUI安装包，安装包有500~600M，所以需要耐心等待下载。
# 下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，
# 并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录

# 模块搜索路径
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
print(sys.path)
# 如果我们要添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录
sys.path.append('path')
# 这种方法是在运行时修改，运行结束后失效。
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响
