def check_float(s):
    '''
    这个函数的作用就是判断传入的字符串是否是合法的小数
    :param s: 传入一个字符串
    :return: True/false
    '''
    s = str(s)
    if s.count('.')==1:
        s_split = s.split('.')
        left,right = s_split
        if left.isdigit() and right.isdigit():
            return True
        elif left.startswith('-') and left[1:].isdigit() \
            and right.isdigit():
            return True
        else:
            return False
    else:
        return False



