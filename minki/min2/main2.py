from math import ceil


def bit_len(n: int) -> int:
    out = n != 0
    while n := n >> 1:
        out += 1
    return out


def karatsuba(n1, n2):
    n1, n2 = sorted((n1, n2), key=bit_len, reverse=True)
    # if n1 >> 1 == 0:
    #     return n1 and n2
    if n1<10 and n2<10:
        return n1*n2


    half_ln = ceil(bit_len(n1) / 2)
    a = n1 >> half_ln
    b = n1 ^ (a << half_ln)
    c = n2 >> half_ln
    d = n2 ^ (c << half_ln)

    k1 = karatsuba(a, c)
    k2 = karatsuba(b, d)
    k3 = karatsuba(a + b, c + d)
    k4 = k3 - k2 - k1
    out = (k1 << half_ln * 2) + (k4 << half_ln) + k2

    return out


if __name__ == "__main__":
    for i in range(0,100000,10000):
        for j in range(0,100000,10000):
            assert i * j == karatsuba(i, j)

    print("correct")