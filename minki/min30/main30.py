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

class ElemLinkedList:
    def __init__(self, name, before_item, prev=None):#, group
        self.prev = prev
        self.name = name
        self.before_item = before_item
        # self.group = group
        # self._in_group = False

    def __str__(self):
        return f"name:{self.name}, BI:{self.before_item}, prev:{self.prev}"  # , group:{self.group}

    def add_elem(self, elem, number_before_us):
        for i in elem.before_item:
            number_before_us[i] += 1
        return self._add_elem(elem, number_before_us)

    def _add_elem(self, elem, number_before_us):
        for i in elem.before_item:
            if self.name == i and number_before_us[self.name] != 0:
                number_before_us[self.name] -= 1
        # if self.group == elem.group:
        #     elem._in_group = True
        if self.prev:
            # if elem._in_group and self.prev.group != elem.group:
            #     elem.prev = self.prev
            #     self.prev = elem
            #     return True

            for i in elem.before_item:
                if self.prev.name == i:
                    # if elem._in_group or self.prev.group == elem.group:
                    if number_before_us[elem.name] != 0:
                        return False
                    elem.prev = self.prev
                    self.prev = elem
                    return True
                    # else:
                    #     return False
            return self.prev._add_elem(elem, number_before_us)
        else:
            self.prev = elem
            return True
        # for i in elem.before_item:
        #     if i == self.name:
        #         return False
        # if elem.group == self.group:
        #     if self.prev and self.prev.group == self.group:
        #         for i in elem.before_item == self.prev.name:
        #
        #     else:
        #         elem.prev = self.prev
        #         self.prev = elem
        #         return True
        #
        # if self.prev:
        #     if self.
        #         return self.prev.add_elem(elem)
        # else:
        #     self.prev = elem
        #     return True


def solution(n, m, group, beforeItems):
    c = m
    for i in range(n):
        if group[i] == -1:
            group[i] = c
            c += 1

    before_group = [[] for i in range(c)]
    elem_in_group = [[] for i in range(c)]
    print(before_group)
    for i in range(n):
        for j in beforeItems[i]:
            if group[i] != group[j]:
                before_group[group[i]].append(group[j])
        elem_in_group[group[i]].append(i)
    print(before_group)

    root_group = ElemLinkedList(0, before_group[0])
    number_before_group = [0 for i in range(c)]

    print(number_before_group)
    for i in range(1, c):
        if not root_group.add_elem(ElemLinkedList(i, before_group[i]), number_before_group):
            return []
    print(root_group)
    answ = []
    iter = root_group
    for i in range(c):
        now_elem = elem_in_group[iter.name][0]
        root_item = ElemLinkedList(now_elem, beforeItems[now_elem])
        len_now_group = len(elem_in_group[iter.name])
        elem_befor_us = [0 for i in range(n)]
        for j in range(1, len_now_group):
            now_elem = elem_in_group[iter.name][j]
            if not root_item.add_elem(ElemLinkedList(now_elem, beforeItems[now_elem]), elem_befor_us):
                return []

        # answ_group = [None] * len_now_group
        # for i in range(len_now_group -1, -1, -1):
        #     answ_group[i] = root_item.name
        #     root_item = root_item.prev
        # answ += answ_group
        while root_item is not None:
            answ.append(root_item.name)
            root_item = root_item.prev
        iter = iter.prev
    return answ

    # root = ElemLinkedList(0, group[0], beforeItems[0])
    # number_before_us = [0 for i in range(n)]
    # for i in range(1, n):
    #     if not root.add_elem(ElemLinkedList(i, group[i], beforeItems[i]), number_before_us):
    #         return []
    # answ = [0] * n
    # iter = root
    # for i in range(n - 1, -1, -1):
    #     answ[i] = iter.name
    #     iter = iter.prev
    # return answ


# print(solution(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []]))  # Cor

# print(solution(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []]))  # Cor

print(
    solution(10, 4, [0, 1, 1, 2, 3, -1, 0, 0, 0, 1], [[2, 5], [3, 5, 4, 6, 8, 7, 2], [7], [], [], [], [], [], [], []]))
