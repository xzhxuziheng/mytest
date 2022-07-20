# 生成指定大小文件
# def gen_file(path, size):
#     file = open(path, 'w')
#     file.seek(1024*1024*size)
#     file.write('\x00')
#     file.close()
#
#
# if __name__ == '__main__':
#     gen_file('./test.bmp', 2.99)

#-
#  name: 乐迪出行登录
#  url: /api/account/platform/account/login
#  method: get
#  data:
#    phone: 18408229871
#    code: 930619
#  asserts: '成功'

# def mp_sort_algorithm(_list):
#     if len(_list) <= 1:
#         return '列表无需排序，该列表为：%s' % _list
#     elif len(_list) >= 2:
#         for i in range(len(_list)):
#             for j in range(i+1, len(_list)):
#                 if _list[i] > _list[j]:
#                     _list[i], _list[j] = _list[j], _list[i]
#         return _list
#
#
# l0 = [2]
# l1 = [8, 2, 1, 5, 3, 7, 4, 9, 6]
# print(mp_sort_algorithm(l1))

# def fun():
#     for i in range(10):
#         yield i
#
#
# def __iter__():
#     for i in range(6):
#         return i
#
#
# print(fun().__next__())
# print(fun().__next__())

# msg = {'code': '00000', 'message': '成功', 'data': {'total': 339, 'list': [
#             {'id': 10149, 'orderNo': '4122051317291800491525', 'userPhone': '19180930619', 'bikeNo': '1000991',
#              'mileage': 0.0, 'payableMoney': 11, 'paidTotalMoney': 0, 'state': 4,
#              'startTime': '2022-05-13 17:29:18', 'endTime': '2022-05-03 17:29:23', 'groupId': 7},
#             {'id': 10141, 'orderNo': '4122051316402682441525', 'userPhone': '19180930619', 'bikeNo': '1000991',
#              'mileage': 0.0, 'payableMoney': 11, 'paidTotalMoney': 0, 'state': 4,
#              'startTime': '2022-05-13 16:40:26', 'endTime': '2022-05-13 16:40:30', 'groupId': 7},
#             {'id': 10130, 'orderNo': '4122051316362710341525', 'userPhone': '19180930619', 'bikeNo': '1000991',
#              'mileage': 0.0, 'payableMoney': 11, 'paidTotalMoney': 0, 'state': 2,
#              'startTime': '2022-05-13 16:36:27', 'endTime': '2022-04-13 16:36:32', 'groupId': 7},
#             {'id': 10145, 'orderNo': '4122051316362710341525', 'userPhone': '19180930619', 'bikeNo': '1000991',
#              'mileage': 0.0, 'payableMoney': 11, 'paidTotalMoney': 0, 'state': 2,
#              'startTime': '2022-05-13 16:36:27', 'endTime': '2022-06-13 16:36:32', 'groupId': 7}]}}
# new_msg = sorted(msg['data']['list'], key=lambda x: x['endTime'], reverse=True)
# print(new_msg)
# def twoSum(nums, target):
#     hashmap={}
#     for ind,num in enumerate(nums):
#         hashmap[num] = ind
#     for i,num in enumerate(nums):
#         j = hashmap.get(target - num)
#         if j is not None and i!=j:
#             return [i,j]
#
# print(twoSum([1,5,8,7], 8))

def twoSum(nums, target):
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


# print(twoSum([1,7,3,9], 5))

def addTwoNumbers(l1, l2):
    str_l1 = ''.join(list(map(lambda x: str(x), l1)))
    str_l2 = ''.join(list(map(lambda y: str(y), l2)))
    new_str = int(str_l1) + int(str_l2)
    new_list = []
    for k in str(new_str):
        new_list.append(int(k))
    new_list.reverse()
    return new_list

def isPalindrome(x):
    y = str(x)
    if x%2 == 1:
        mudium = len(y)//2+1
        for i in range(0, mudium):
            first = list(y)[i]
        for j in range(mudium+1,len(list(y))):
            last = list(y)[j]
        if first == last:
            return True
        else:
            return False
    if x%2 == 0:
        mudium = len(y)//2
        for i in range(0, mudium):
            first = list(y)[i]
        for j in range(mudium,len(list(y))):
            last = list(y)[j]
        if first == last:
            return True
        else:
            return False

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif len(l1) < len(l2):
            l1 = self.mergeTwoLists(l1, l2)
            return l1
        else:
            l2 = self.mergeTwoLists(l1, l2)
            return l2


def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n-1):
            a, b = b, a + b
        return b
print(fib(4))