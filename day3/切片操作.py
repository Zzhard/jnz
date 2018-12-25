#就是list取值的一种方式
# l = list(range(1,11))
# l = ['a','b','c','d','e','j','k','l','m','n','o']
#     0    1  2   3   4   5   6    7   8   9   10
# print(l[2:8])#顾头不顾尾
# print(l[:5])#如果最前面没写的话，代表从0开始取的
# print(l[4:])#如果冒号后面的没写的话，代表去到最后
# print(l[:])#如果冒号后面的没写的话，代表去到最后
# print(l[::3])#步长，也就是代表隔几个取一次，
# nums = list(range(1,101))
# print(nums[1::2])  #取偶数，
# print(nums[::2])  #取奇数
# 1 2 3 4 5 6 ....10
# print(nums)
# print(nums[::-1])  #取奇数
#如果最后面的步长是正数的话， 那就从左到右开始取值
#如果后面的步长是负数的话，那么久从右往左开始取值

#切片同样适用于字符串。
words='中秋节要上课'
# print(words[::-1])
for index,w in enumerate(words):
    print('每次打印的',index,w)

s='上海自来水来自海上'
# 1232321
# 1111
#回文算法，反过来倒去过都一样
#5678 8765
#
for i in range(10):
    s = input('请输入一个字符串：')
    if len(s)<2:
        print('字符串长度必须大于1')
    elif s==s[::-1]:
        print('是回文')
    else:
        print('不是回文')