def yangfan(a):
    print('yangfang %s'%a)

if __name__ == '__main__':
    #其他文件导入这个python文件的时候
    #不会执行if __name__ == '__main__'
    #下面的代码

    yangfan('hhh')
