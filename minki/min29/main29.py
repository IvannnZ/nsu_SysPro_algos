# def solve(list):
#     dict_elem = dict()
#     for i in list:
#         if i[0] in dict_elem and i[1] in dict_elem:
#             if dict_elem[i[0]] == dict_elem[i[1]]:
#                 return False
#             elif i[0] in dict_elem:
#                 dict_elem[i[1]] = not dict_elem[i[0]]
#             elif i[1] in dict_elem:
#                 dict_elem[i[0]] = not dict_elem[i[1]]
#             else:
#                 dict_elem[i[0]] = True
#                 dict_elem[i[1]] = False
#     return True
#
# listt =
#
#
# print(solve())


def solve(graph):
    iter = 0
    dict_elem = dict()
    dict_elem[iter] = True
    for i in graph:
        for j in i:
            if iter in dict_elem:
                if j in dict_elem:
                    if dict_elem[j] == dict_elem[iter]:
                        return False
                else:
                    dict_elem[j] = not dict_elem[iter]
            else:
                dict_elem[iter] = not dict_elem[j]
        iter +=1
    return True

list1 = [[1,2,3],[0,2],[0,1,3],[0,2]]

print(solve(list1))

list2 = [[1,3],[0,2],[1,3],[0,2]]

print(solve(list2))