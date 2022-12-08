"""
    author: poyeezy
    create_time: 2022-12-09 00:26:49
    email: po10z0oyee2y@gmail.com
    work_wechat: poyeezy996
    require：
    1. old_function() 没有清理例表中所有的偶数，为什么？
        python列表的remove 方法在去掉列表中数据时，会缩短列表的长度，当索引的对应值被移除后，
        后续索引的值，自动补位到上一个索引的值，从而跳过了全部数据遍历的预期。详情见test_function()
    2. 重写old_function() 达成偶数全部清理的效果， 最小的代价？
        new_function_one()
    3. 如果方法的时间复杂度为O(n)，空间复杂度为O(1)，要怎么实现？
       new_function_one() new_function_two() one_line_function()
"""

lista = [1,2,4,4,10,6,7,5,20]
def old_function(lista):
    for i in lista:
        if i % 2 == 0:
            lista.remove(i)
    return lista

def test_function(arg):
    for i in arg:
        print('[arg]: ', arg)
        print('[i]: ', i)
        if i % 2 == 0:
            arg.remove(i)
    return arg
# test_result = test_function(lista)
# print('[test_result]: ', test_result)

def new_function_one(arg):
    """
        时间复杂度 O(n) 空间复杂度 O(1)
    :param arg:
    :return:
    """
    for i in arg.copy():
        if i % 2 == 0:
            arg.remove(i)
    return arg

def new_function_two(arg):
    """
        时间复杂度 O(n) 空间复杂度 O(1)
    :param arg:
    :return:
    """
    for i in arg[:]:
        print(i)
        if i % 2 == 0:
            arg.remove(i)
    return arg

def one_line_function(arg):
    """
        时间复杂度 O(n) 空间复杂度 O(1)
    :param arg:
    :return:
    """
    print('[arg]: ', arg)
    [arg.remove(i) for i in arg.copy() if i%2==0]
    return arg

if __name__ == '__main__':
    # old_result = old_function(lista)
    # print('[old_result]: ', old_result)
    # test_result = test_function(lista)
    # print('[test_result]: ', test_result)
    # new_result_one = one_line_function(lista)
    # print('[new_result_one]: ', new_result_one)
    # new_result_two = new_function_two(lista)
    # print('[new_result_two]: ', new_result_two)
    one_line_result = one_line_function(lista)
    print('[one_line_result]: ', one_line_result)