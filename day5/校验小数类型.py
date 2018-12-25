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
    return False
print(check_float(1.3))
print(check_float(-1.3))
print(check_float('01.3'))
print(check_float('-1.3'))
print(check_float('-a.3'))
print(check_float('a.3'))
print(check_float('1.3a3'))
print(check_float('---.3a3'))











#1.5 1.34
#-0.5  -8.4
# 1.5
# a.3
    # -----1.3
#正小数
#1、小数点个数为1
#2、小数点左边和右边都是整数
#负小数
# 1、小数点个数为1
# 2、小数点左边和右边都是整数
# 3、负号开头，并且只有一个负号