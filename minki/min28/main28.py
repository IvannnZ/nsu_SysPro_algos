from math import ceil, log, modf
from random import randint, sample

class Bloom_Filter:

    def __init__(self, number_request, error_probability):
        # self.__num_hash = ceil(log(error_probability, 1 / 2) / log(2))
        self.__num_hash=ceil(log(error_probability, 1 / 2))
        # self.__number_bucket = ceil(self.__num_hash * number_request)
        self.__number_bucket = ceil(self.__num_hash * number_request / log(2))
        self.__data = [False] * self.__number_bucket
        self.__hash_seed = [randint(0, 100000000) / 100000000 for i in range(self.__num_hash)]
        print(number_request, error_probability, self.__num_hash, self.__number_bucket)

    def check(self, val):
        for i in range(self.__num_hash):
            if self.__data[self.__hash(val, i)] == False:
                return False
        return True

    def insert(self, val):
        for i in range(self.__num_hash):
            self.__data[self.__hash(val, i)] = True

    def __hash(self, val, i):
        return ceil(modf(val * self.__hash_seed[i])[0] * self.__number_bucket)-1


if __name__ == "__main__":
    TEST_RANGE = 50000
    PROB = 0.01
    test = sample(range(1, 0xffffffff), TEST_RANGE * 2)
    includes, not_includes = test[0:TEST_RANGE], test[TEST_RANGE:]

    blm = Bloom_Filter(TEST_RANGE, PROB)
    for e in includes:
        blm.insert(e)

    for e in includes:
        assert blm.check(e)

    cntr = 0
    for e in not_includes:
        if blm.check(e) and e not in includes:
            cntr += 1

    print(cntr / TEST_RANGE)

