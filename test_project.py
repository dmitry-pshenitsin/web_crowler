# incorrect4 = [['a', 'b', 'c'],
#               ['b', 'c', 'f'],
#               ['c', 'a', 'b']]
#
# incorrect5 = [[1, 1.5],
#               [1.5, 1]]
#
# incorrect2 = [[1,2,3,4],
#              [2,3,1,4],
#              [4,1,2,3],
#              [3,4,1,2]]
#
#
# def check_sudoku(sud):
#     n = len(sud)
#     k = [[] for i in range(n)]
#     for r in sud:
#         for i in range(0, n):
#             k[i].append(r[i])
#     for i in range(n):
#         for j in range(1, n + 1):
#             if sud[i].count(j) != 1 or k[i].count(j) != 1:
#                 return False
#     return True
#
#
# print(check_sudoku(incorrect4))
# print(check_sudoku(incorrect2))
#
#
# def numbers_in_lists(string):
#     if string == []:
#         return []
#     sublist = []
#     max_el = 0
#     result = []
#     for i in string:
#         k = int(i)
#         if k > max_el:
#             if sublist != []:
#                 result.append(sublist)
#                 sublist = []
#             max_el = k
#             result.append(max_el)
#             continue
#         sublist.append(k)
#     if sublist != []:
#         result.append(sublist)
#     return result
#
# print(len('ops'))
# op = 'ops'
# print(op.count('o'))
#
#
# print(numbers_in_lists('543987'))
#
# print(round(0.8**6, 2))

addo = []
if addo[0] == 5:
    print('hi')
print('ho')

