operators = {
    "(": 1,
    ")": 1,
    "!": 2,
    "~": 2,
    "^^": 2.5,  # возведение в степень
    "*": 3,
    "/": 3,
    "%": 3,
    "+": 4,
    "-": 4,
    ">>": 5,
    "<<": 5,
    "&": 8,
    "^": 9,  # xor
    "|": 10,
    "&&": 11,
    "||": 12,
}


def parser(expr):
    main_stek = []
    operator_stek = []
    stek_for_recursion = []
    count_parenthesis = 0
    for i in expr:
        if count_parenthesis != 0 or i == '(':# если видим "(" то пока не закроется скобка, мы постоянно тут проходим, а после отправляем то что внутри скобок в рекурсию
            if i == '(':
                count_parenthesis += 1
            elif i == ')':
                count_parenthesis -= 1

            stek_for_recursion.append(i)

            if count_parenthesis == 0:
                main_stek += parser(stek_for_recursion[1:-1])
                stek_for_recursion = []

        elif i.isdigit():# стандартное выполнение
            main_stek.append(i)
        else:
            if len(operator_stek) != 0:
                if operators[operator_stek[-1]] <= operators[i]:
                    main_stek.append(operator_stek.pop())
                operator_stek.append(i)
            else:
                operator_stek.append(i)
    while len(operator_stek) != 0:
        main_stek.append(operator_stek.pop())
    return main_stek


def some_func_name(input, correct):
    ansver = parser(input.split())
    if ' '.join(ansver) != correct:
        print(f"incorrect {input},\nanswer:  {' '.join(ansver)},\ncorrect: {correct}\n")
    # if ' '.join(ansver) != correct:
    #     print("incorrect", end=' ')
    # else:
    #     print("correct", end=' ')
    # print(f"{input},\nanswer:  {' '.join(ansver)},\ncorrect: {correct}\n")


some_test_for_list = [
    ["1 + 1 + 2", "1 1 + 2 +"],
    ["1 - 5 ^^ 3 * 2", "1 5 3 ^^ 2 * -"],
    ["1 + 3 * 5 ^^ 2", "1 3 5 2 ^^ * +"],
    ["15 / ( 7 - ( 1 + 1 ) )", "15 7 1 1 + - /"],
    ["! ( 0 && 2 ) + 4 / 2", "0 2 && ! 4 2 / +"],
    ["14 ^^ 4 * ( 3 + 51 ) % 2", "14 4 ^^ 3 51 + * 2 %"],
    ["( 54 != 50 ) && ( ( 12 < 5 ) && ( 13 > 4 ) )", "54 50 != 12 5 < 13 4 > && &&"],
]

for i in some_test_for_list:
    some_func_name(i[0], i[1])
