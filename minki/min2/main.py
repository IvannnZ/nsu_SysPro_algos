def multiply_column(a, b):
    answer = 0
    c = 0
    while b != 0:
        answer += (a * (b & 1)) << c
        c += 1
        b = b >> 1

    return answer

def num_separator(a, len):
    first_half = a >> (len >> 1)
    second_half = a - (first_half << (len >> 1))
    return (first_half, second_half)


def len_of_num_in_bin_sys(num):
    # первая степень двойки которая больше чем длина числа
    pivot = 1
    len = 1
    while num > pivot:
        pivot = pivot + (pivot << len)
        len = len << 1
    return len


def _multiply(a, b, max_len):
    if max_len <= 3:
        return a * b

    halfs_a = num_separator(a, max_len)
    halfs_b = num_separator(b, max_len)
    first_step = _multiply(halfs_a[0], halfs_b[0], max_len >> 1)
    second_step = _multiply(halfs_a[1], halfs_b[1], max_len >> 1)
    third_step = _multiply(halfs_a[0] + halfs_a[1], halfs_b[0] + halfs_b[1], max_len >> 1)

    fourth_step = third_step - second_step - first_step
    return (first_step << max_len) + second_step + (fourth_step << (max_len >> 1))


def multiply(a, b):
    return _multiply(a, b, max(len_of_num_in_bin_sys(a), len_of_num_in_bin_sys(b)))




# int len_of_num_in_bin_sys(num_type num) {
#     //первая степень двойки которая больше чем длина числа
#     unsigned long long pivot = 1; // тут не знаю как заменить
#     int len = 1;
#     while (num > pivot) {
#         pivot = pivot + (pivot << len);
#         len = len << 1;
#     }
#     return len;
# }
#
# struct halves_of_num num_separator(num_type a, num_type len) {
#     struct halves_of_num answ;
#     answ.first_half = (a >> (len >> 1));
#     answ.second_half = a - (answ.first_half << (len >> 1));
#     return answ;
# }
#
#
# num_type _multiply(num_type a, num_type b, int max_len) {
#     if (max_len <= 3) {
#         return a * b;
#     }
#     struct halves_of_num halfs_a = num_separator(a, max_len);
#     struct halves_of_num halfs_b = num_separator(b, max_len);
#     num_type first_step = _multiply(halfs_a.first_half, halfs_b.first_half, max_len >> 1);
#     num_type second_step = _multiply(halfs_a.second_half, halfs_b.second_half, max_len >> 1);
#     num_type third_step = _multiply(halfs_a.first_half + halfs_a.second_half,
#                                     halfs_b.first_half + halfs_b.second_half, max_len >> 1);
#     num_type fourth_step = third_step - second_step - first_step;
#     return ((first_step << max_len) + second_step + (fourth_step << (max_len >> 1)));
# }
#
# num_type multiply(num_type a, num_type b) {
#     return _multiply(a, b, max(len_of_num_in_bin_sys(a), len_of_num_in_bin_sys(b)));
# }
#
# num_type multiply_column(num_type a, num_type b) {
#     num_type answer = 0;
#     int c = 0;
#     while (b != 0) {
#         answer += (a * (b & 1)) << c;
#         c++;
#         b = b >> 1;
#     }
#     return answer;
# }




def auto_test():
    a = 1
    b = 1
    if multiply_column(a, b) == multiply(a, b):
        print(f"{a} * {b} is correct")
    else:
        print(f"{a} * {b} isn`t correct", multiply_column(a, b), multiply(a, b))

    a = 50
    b = 0
    if multiply_column(a, b) == multiply(a, b):
        print(f"{a} * {b} is correct")
    else:
        print(f"{a} * {b} isn`t correct", multiply_column(a, b), multiply(a, b))

    a = 41849426981429864
    b = 82952956565
    if multiply_column(a, b) == multiply(a, b):
        print(f"{a} * {b} is correct")
    else:
        print(f"{a} * {b} isn`t correct", multiply_column(a, b), multiply(a, b))

    a = 500000000
    b = 100000000
    if multiply_column(a, b) == multiply(a, b):
        print(f"{a} * {b} is correct")
    else:
        print(f"{a} * {b} isn`t correct", multiply_column(a, b), multiply(a, b))

    a = -50
    b = -10
    print(f"{a} * {b} is {multiply(a, b)}") # column multiply cant work with -

    a = 50
    b = -10
    print(f"{a} * {b} is {multiply(a, b)}")

# print("Answer:", multiply(int(input("Enter a:")), int(input("Enter b:"))))

auto_test()
