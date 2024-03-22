class Bin_heap:
    class Tree:
        def __init__(self, priority, value, children=None, parent=None, right_neighbour=None, degree=0):
            self.priority = priority
            self.value = value
            self._children = children
            self._parent = parent
            self._right_neighbour = right_neighbour
            self.degree = degree

        def merge(self, anouther):
            less, more = sorted((self, anouther), key=lambda tree: tree.priority)
            more._right_neighbour = less._children
            more._parent = less
            less._children = more
            less.degree += 1
            return less

        def __str__(self) -> str:
            return str((self.value, self.priority))

    def __init__(self):
        self.trees = dict()
        self._minimum = None

    def merge(self, tree: Tree):
        if tree.degree in self.trees and self.trees[tree.degree]:
            tree = tree.merge(self.trees[tree.degree])
            self.trees[tree.degree - 1] = None
            self.merge(tree)
        else:
            self.trees[tree.degree] = tree
        self._update_min()

    def insert(self, value, priority):
        new_tree = self.Tree(priority=priority, value=value)
        self.merge(new_tree)

    def peek_min(self):
        return self._minimum

    def _update_min(self):
        self._minimum = None
        for i in self.trees:
            if self._minimum:
                if self.trees[i] and self._minimum.priority > self.trees[i].priority: self._minimum = self.trees[i]
            else:
                self._minimum = self.trees[i]

    def delete(self, elem: Tree):
        if elem._parent:
            elem._parent.degree -= 1
        else:
            self.trees[elem.degree] = None

        children = elem._children
        while children:
            self.merge(children)
            children = children._right_neighbour
        self._update_min()
        del elem

    def extract_min(self):
        answ = self._minimum
        self.delete(self._minimum)
        return answ

    def decrease_key(self, elem: Tree, priority):
        elem.priority = priority
        while elem._parent and elem.priority > elem._parent.priority:
            elem.value, elem._parent.value = elem._parent.value, elem.value
            elem.priority, elem._parent.priority = elem._parent.priority, elem.priority
            elem = elem._parent


heap = Bin_heap()
heap.insert(10, 1)
heap.insert(1, -1)
node = heap.peek_min()
heap.insert(-1, -2)
heap.delete(node)
print(heap.extract_min())
print(heap.extract_min())
