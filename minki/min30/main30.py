# from typing import List
#
#
# def solve(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
#     c = m
#     for i in range(n):
#         if group[i] == -1:
#             group[i] = c
#         c += 1
#     print(group)
#
# print(solve(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3,6],[],[],[]]))

# class Solution(object):
#     def kahn(self, graph):
#         origins = set(graph.keys())
#         inflw = dict(zip(graph.keys(), [0] * len(graph)))
#         for e in graph.values():
#             origins -= set(e)
#             for g in e:
#                 if g not in graph:
#                     continue
#                 inflw[g] += 1
#
#         out = []
#         while origins:
#             node = origins.pop()
#             out.append(node)
#             for e in graph[node]:
#                 if e not in graph:
#                     continue
#                 inflw[e] -= 1
#                 if inflw[e] == 0:
#                     origins.add(e)
#         out.reverse()  # \U0001f921
#         if len(out) == len(graph):
#             return out
#         return []
#
#     def sortItems(self, n, m, group, beforeItems):
#         now_group = max(group) + 1
#         for i in range(len(group)):
#             if group[i] == -1:
#                 group[i] = now_group
#                 now_group += 1
#                 m += 1
#
#         beforeGroup = dict(zip(range(m), [set() for i in range(n)]))
#         for node, before in enumerate(beforeItems):
#             grp = group[node]
#             for node in before:
#                 if grp != group[node]:
#                     beforeGroup[grp].add(group[node])
#
#         beforeByGroup = [dict() for i in range(m)]
#         for node, before in enumerate(beforeItems):
#             beforeByGroup[group[node]][node] = before
#
#         outGroup = self.kahn(beforeGroup)
#         out = []
#         for grp in outGroup:
#             res = self.kahn(beforeByGroup[grp])
#             if res == [] and beforeByGroup[grp]:
#                 return []
#             out += res
#         return out
#
#
# sol = Solution()


# print(sol.sortItems(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []]))







# class ElemLinkedList:
#     def __init__(self, name, before_item, prev=None):
#         self.prev = prev
#         self.name = name
#         self.before_item = before_item
#
#     def __str__(self):
#         return f"name:{self.name}, BI:{self.before_item}, prev:{self.prev}"
#
#     def add_elem(self, elem, number_before_us):
#         for i in elem.before_item:
#             number_before_us[i] += 1
#         return self._add_elem(elem, number_before_us)
#
#     def _add_elem(self, elem, number_before_us):
#         for j in self.before_item:
#             if elem.name == j and number_before_us[elem.name] != 0:
#                 number_before_us[elem.name] -= 1
#                 break
#
#         # for i in elem.before_item:
#         #     if self.name == i and number_before_us[self.name] != 0:
#         #         number_before_us[self.name] -= 1
#         #         break
#         if self.prev:
#             for i in elem.before_item:
#                 if self.prev.name == i:
#                     if number_before_us[elem.name] != 0:
#                         return False
#                     elem.prev = self.prev
#                     self.prev = elem
#                     number_before_us[i]-=1
#                     return True
#
#             return self.prev._add_elem(elem, number_before_us)
#         else:
#             if number_before_us[elem.name] != 0:
#                 print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa")
#                 return False
#             self.prev = elem
#             return True
#
#
# def solution(n, m, group, beforeItems):
#     c = m
#     for i in range(n):
#         if group[i] == -1:
#             group[i] = c
#             c += 1
#
#     before_group = [[] for i in range(c)]
#     elem_in_group = [[] for i in range(c)]
#     # print(before_group)
#     for i in range(n):
#         for j in beforeItems[i]:
#             if group[i] != group[j]:
#                 before_group[group[i]].append(group[j])
#         elem_in_group[group[i]].append(i)
#     # print(before_group)
#
#     root_group = ElemLinkedList(-1, [])
#     number_before_group = [0 for i in range(c)]
#     # for i in root_group.before_item:
#     #     number_before_group[i] += 1
#     # print(number_before_group)
#
#     for i in range(c):
#         if not root_group.add_elem(ElemLinkedList(i, before_group[i]), number_before_group):
#             return []
#     if number_before_group[0] != 0:
#         return []
#     # print(root_group)
#     answ = []
#     iter = root_group.prev
#
#     for i in range(c):
#         now_elem = elem_in_group[iter.name][0]
#         root_item = ElemLinkedList(now_elem, beforeItems[now_elem])
#         len_now_group = len(elem_in_group[iter.name])
#         elem_befor_us = [0 for i in range(n)]
#         for j in root_item.before_item:
#             elem_befor_us[j] += 1
#         for j in range(1, len_now_group):
#             now_elem = elem_in_group[iter.name][j]
#             if not root_item.add_elem(ElemLinkedList(now_elem, beforeItems[now_elem]), elem_befor_us):
#                 return []
#         if number_before_group[0]!= 0:
#             return []
#         now_answ = [None] * len_now_group
#         for i in range(len_now_group-1, -1, -1):
#             now_answ[i] = root_item.name
#             root_item = root_item.prev
#         answ+=now_answ
#         # while root_item is not None:
#         #     answ.append(root_item.name)
#         #     root_item = root_item.prev
#         iter = iter.prev
#     return answ
#
#
#
# print(solution(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []]))  # Cor
# #                                   0, 1, 2, 3, 4, 5, 6,  7
#
# print(solution(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []]))  # Cor
#
# print(
#     solution(10, 4, [0, 1, 1, 2, 3, -1, 0, 0, 0, 1], [[2, 5], [3, 5, 4, 6, 8, 7, 2], [7], [], [], [], [], [], [], []]))
# #                                [0, 1, 2, 3, 4, 5, 6, 7, 8,  9















def solution(n, m, group, beforeItems):
    c = m
    for i in range(n):
        if group[i] == -1:
            group[i] = c
            c += 1

    before_group = [[] for i in range(c)]
    for i in range(n):
        if





print(solution(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []]))  # Cor
#                                   0, 1, 2, 3, 4, 5, 6,  7

print(solution(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []]))  # Cor

print(
    solution(10, 4, [0, 1, 1, 2, 3, -1, 0, 0, 0, 1], [[2, 5], [3, 5, 4, 6, 8, 7, 2], [7], [], [], [], [], [], [], []]))
#                                [0, 1, 2, 3, 4, 5, 6, 7, 8,  9