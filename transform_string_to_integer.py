number_word_dict = {
    "ты": 1000,
    "м": 1000000,
    "сто": 100,
    "двес": 200,
    "трис": 300,
    "четырес": 400,
    "пятьс": 500,
    "шестьс": 600,
    "семьс": 700,
    "восемьс": 800,
    "девятьс": 900,
    "одинн": 11,
    "двен": 12,
    "трин": 13,
    "четырн": 14,
    "пятн": 15,
    "шестн": 16,
    "семн": 17,
    "восемн": 18,
    "девятн": 19,
    "двад": 20,
    "трид": 30,
    "сор": 40,
    "пятьд": 50,
    "шестьд": 60,
    "семьд": 70,
    "восемьд": 80,
    "девяно": 90,
    "деc": 10,
    "н": 0,
    "о": 1,
    "дв": 2,
    "т": 3,
    "ч": 4,
    "п": 5,
    "ш": 6,
    "с": 7,
    "в": 8,
    "д": 9,
}


def transform_string_to_integer(text: str,
                                dictionary: dict[str, int] = number_word_dict
                                ) -> int:
    numbers = text.split()
    tmp = 0  # для тысяч
    flag = 0  # метка для тысяч
    result = 0

    for number_by_text in numbers[::-1]:  # с конца списка
        for key, value in dictionary.items():
            if number_by_text.startswith('тысяч'):
                flag = 1
                break
            elif number_by_text.startswith(key) and not flag:
                result += value
                break
            elif number_by_text.startswith(key) and flag:
                tmp += value
                break

    if flag:
        result += tmp * 1000

    return result


assert transform_string_to_integer('один') == 1
assert transform_string_to_integer('двадцать') == 20
assert transform_string_to_integer('двести сорок шесть') == 246
assert transform_string_to_integer('пятьсот') == 500
assert transform_string_to_integer(
    'семьсот восемьдесят три тысячи девятьсот девятнадцать') == 783919
assert transform_string_to_integer('ноль') == 0
assert transform_string_to_integer('миллион') == 1000000
assert transform_string_to_integer(
    'девятьсот девяносто девять тысяч девятьсот девяносто девять') == 999999
assert transform_string_to_integer(
    'девятьсот девяносто тысяч девятьсот девяносто девять') == 990999
assert transform_string_to_integer('три тысячи') == 3000
assert transform_string_to_integer('одна тысяча') == 1000
