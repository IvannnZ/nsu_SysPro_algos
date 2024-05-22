#https://leetcode.com/problems/is-graph-bipartite/submissions/1265239311


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

#
# def solve(graph):
#     iter = 0
#     class_elem = [None] * len(graph)
#     class_elem[iter] = True
#     for i in graph:
#         if iter in graph:
#             for j in i:
#                 if class_elem[j] == class_elem[iter]:
#                     return False
#                 else:
#                     class_elem[j] = not class_elem[iter]
#         else:
#             nei_class = None
#             for j in i:
#                 if class_elem[j] is not None:
#                     if nei_class is None:
#                         nei_class = class_elem[j]
#                     else:
#                         if nei_class != class_elem[j]:
#                             return False
#             class_elem[iter] = not nei_class
#         iter += 1
#     return True
#
#
# list1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
#
# print(solve(list1))  # corr
#
# list2 = [[1, 3], [0, 2], [1, 3], [0, 2]]
#
# print(solve(list2))  # corr
#
# list3 = [[3], [2, 4], [1], [0, 4], [1, 3]]
#
# print(solve(list3))  # corr
#
# list4 = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
#          [2, 4, 5, 6, 7, 8]]
#
# print(solve(list4))  # corr
#
# list5 = [[1], [0, 3], [3], [1, 2]]  # False
#
# print(solve(list5))
# def rebild_graph(graph):
#     iter = 0
#     new_graph = list()
#     for i in graph:
#         for j in i:
#             new_graph.append((iter, j))
#         iter +=1
#     return new_graph
#
# def solve(graph):
#     new_graph = rebild_graph(graph)
#     print(new_graph)
#     dict_elem = dict()
#     for i in new_graph:
#         if i[0] in dict_elem and i[1] in dict_elem:
#             if dict_elem[i[0]] == dict_elem[i[1]]:
#                 return False
#         elif i[0] in dict_elem:
#             dict_elem[i[1]] = not dict_elem[i[0]]
#         elif i[1] in dict_elem:
#             dict_elem[i[0]] = not dict_elem[i[1]]
#         else:
#
#     return True
#
#
# list1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
#
# print(solve(list1))
#
# list2 = [[1, 3], [0, 2], [1, 3], [0, 2]]
#
# print(solve(list2))
#
# list3 = [[3], [2, 4], [1], [0, 4], [1, 3]]
#
# print(solve(list3))
#
# list4 = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
#          [2, 4, 5, 6, 7, 8]]
#
# print(solve(list4))


# def solve(graph):
#
#     not_visited = set(range(len(graph)))
#     print(not_visited)
#     oddeven = [None] * len(graph)  # None - not visited, False - odd, True - even
#     que = list()
#     while not_visited:
#         start = not_visited.pop()
#         oddeven[start] = False
#         for node in graph[start]:
#             not_visited.remove(node)
#             oddeven[node] = True
#             que.append(node)
#
#         while que:
#             node = que.pop()
#             is_even = oddeven[node]
#
#             for other_node in graph[node]:
#                 if oddeven[other_node] == is_even:
#                     return False
#                 if oddeven[other_node] == None:
#                     not_visited.remove(other_node)
#                     oddeven[other_node] = not is_even
#                     que.append(other_node)
#     return True
#
# list4 = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
#          [2, 4, 5, 6, 7, 8]]
#
# print(solve(list4))


def solve(graph):
    class_elem = [None] * len(graph)

    # class_elem[0] = True
    def solve_rec(now):
        for i in graph[now]:
            if class_elem[i] == class_elem[now]:
                return False
            if class_elem [i] is None:
                class_elem[i] = not class_elem[now]
                if not solve_rec(i):
                    return False
        return True

    for i in range(0, len(graph)):
        if class_elem[i] is None:
            class_elem[i] = True
            if not solve_rec(i):
                return False

    return True


list4 = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
         [2, 4, 5, 6, 7, 8]]

print(solve(list4))
