class non_groving_piramide:
    def __init__(self):
        self.arr = []

    def _sift_from_the_bottom(self):
        iter = len(self.arr) - 1
        before_iter = (iter - 1) // 2
        while self.arr[before_iter][1] > self.arr[iter][1] and iter != 0:
            self.arr[before_iter], self.arr[iter] = self.arr[iter], self.arr[before_iter]
            iter = before_iter
            before_iter = (iter - 1) // 2

    def _sift_from_the_up(self):
        iter = 0
        while True:
            if iter * 2 + 2 >= len(self.arr):
                if iter * 2 + 1 >= len(self.arr):
                    break
                iter_next = iter * 2 + 1
            else:
                if self.arr[iter * 2 + 1][1] < self.arr[iter * 2 + 2][1]:
                    iter_next = iter * 2 + 1
                else:
                    iter_next = iter * 2 + 2

            if self.arr[iter][1] <= self.arr[iter_next][1]: break

            self.arr[iter], self.arr[iter_next] = self.arr[iter_next], self.arr[iter]
            iter = iter_next

    def add(self, value, priority):
        self.arr.append([value, priority])
        self._sift_from_the_bottom()

    def take_min(self):
        last_min, self.arr[0] = self.arr[0], self.arr[-1]
        self.arr.pop()
        self._sift_from_the_up()
        return last_min
