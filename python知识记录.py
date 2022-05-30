
# python知识记录

"""
    1、一个函数加上括号就会被执行
    2、函数可以进行赋值，如：
        a = print
        a("hello world")

        # 输出：hello world

       可以当返回值，如：
       def output():
          return print
       output()("hello world")

       # 输出：hello world

       可以被函数调用，如：
       def output():
          print("hello world")

       def act(func):
          func()

       act(output)

       # 输出：hello world
"""