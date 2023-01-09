#找出10000以内的完美数
"""
说明：
完美数又称为完全数或完备数，
它的所有的真因子（即除了自身以外的因子）的
和（即因子函数）恰好等于它本身。
例如：6（6=1+2+3）和28（28=1+2+4+7+14）就是完美数。
完美数有很多神奇的特性，有兴趣的可以自行了解。
总结：完美数是除自身外其他所有因子的和正好等于这个数本身的数
"""
import math

for num in range(2,10000):
    result = 0
    for factor in range(1,int(math.sqrt(num)) +1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)