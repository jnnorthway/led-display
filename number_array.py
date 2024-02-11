def get_number_array(number, pc, sc, max_digits):
    number_str = str(number)
    number_str_len = len(number_str)
    number_list = []
    if number_str_len < max_digits:
        for _ in range(max_digits - number_str_len):
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [sc, sc, sc, sc, sc],
                    [sc, sc, sc, sc, sc],
                    [sc, sc, sc, sc, sc],
                    [sc, sc, sc, sc, sc],
                    [sc, sc, sc, sc, sc],
                    [sc, sc, sc, sc, sc],
                    [sc, sc, sc, sc, sc],
                ]
            )
    elif number_str_len > max_digits:
        if number_str_len == 4:
            number_str = f"{number_str[0]}.{number_str[1]}{number_str[2]}k"
        elif number_str_len == 5:
            number_str = f"{number_str[0]}{number_str[1]}.{number_str[2]}k"
        elif number_str_len == 6:
            number_str = f"{number_str[0]}{number_str[1]}{number_str[2]}k"
        elif number_str_len == 7:
            number_str = f"{number_str[0]}.{number_str[1]}m"
        elif number_str_len == 8:
            number_str = f"{number_str[0]}{number_str[1]}m"
        elif number_str_len == 9:
            number_str = f"{number_str[0]}{number_str[1]}{number_str[2]}m"
        elif number_str_len == 10:
            number_str = f"{number_str[0]}.{number_str[1]}b"
        elif number_str_len == 11:
            number_str = f"{number_str[0]}{number_str[1]}b"
        elif number_str_len == 12:
            number_str = f"{number_str[0]}{number_str[1]}{number_str[2]}b"
        elif number_str_len == 13:
            number_str = f"{number_str[0]}.{number_str[1]}t"
        elif number_str_len == 14:
            number_str = f"{number_str[0]}{number_str[1]}t"
        elif number_str_len == 15:
            number_str = f"{number_str[0]}{number_str[1]}{number_str[2]}t"
    for number in number_str:
        if number == ".":
            number_list.append(
                [
                    [sc, sc],
                    [sc, sc],
                    [sc, sc],
                    [sc, sc],
                    [sc, sc],
                    [sc, sc],
                    [sc, sc],
                    [pc, sc],
                ]
            )
        elif number == "k":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, pc, sc, sc],
                    [sc, pc, sc, sc, sc],
                    [pc, sc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                ]
            )
        elif number == "m":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc, sc],
                    [pc, sc, sc, sc, pc, sc],
                    [pc, pc, sc, pc, pc, sc],
                    [pc, sc, pc, sc, pc, sc],
                    [pc, sc, sc, sc, pc, sc],
                    [pc, sc, sc, sc, pc, sc],
                    [pc, sc, sc, sc, pc, sc],
                    [pc, sc, sc, sc, pc, sc],
                ]
            )
        elif number == "b":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [pc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, pc, pc, sc, sc],
                ]
            )
        elif number == "t":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc, sc],
                    [pc, pc, pc, pc, pc, sc],
                    [sc, sc, pc, sc, sc, sc],
                    [sc, sc, pc, sc, sc, sc],
                    [sc, sc, pc, sc, sc, sc],
                    [sc, sc, pc, sc, sc, sc],
                    [sc, sc, pc, sc, sc, sc],
                    [sc, sc, pc, sc, sc, sc],
                ]
            )
        elif number == "0":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [sc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, pc, pc, sc, sc],
                ]
            )
        elif number == "1":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [sc, sc, pc, sc, sc],
                    [sc, sc, pc, sc, sc],
                    [sc, sc, pc, sc, sc],
                    [sc, sc, pc, sc, sc],
                    [sc, sc, pc, sc, sc],
                    [sc, sc, pc, sc, sc],
                    [sc, sc, pc, sc, sc],
                ]
            )
        elif number == "2":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [sc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, sc, sc, pc, sc],
                    [sc, sc, pc, sc, sc],
                    [sc, pc, sc, sc, sc],
                    [pc, sc, sc, sc, sc],
                    [pc, pc, pc, pc, sc],
                ]
            )
        elif number == "3":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [sc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, sc, sc, pc, sc],
                    [sc, pc, pc, sc, sc],
                    [sc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, pc, pc, sc, sc],
                ]
            )
        elif number == "4":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, pc, pc, pc, sc],
                    [sc, sc, sc, pc, sc],
                    [sc, sc, sc, pc, sc],
                    [sc, sc, sc, pc, sc],
                ]
            )
        elif number == "5":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [pc, pc, pc, pc, sc],
                    [pc, sc, sc, sc, sc],
                    [pc, sc, sc, sc, sc],
                    [pc, pc, pc, sc, sc],
                    [sc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, pc, pc, sc, sc],
                ]
            )
        elif number == "6":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [sc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, sc, sc],
                    [pc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, pc, pc, sc, sc],
                ]
            )
        elif number == "7":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [pc, pc, pc, sc, sc],
                    [sc, sc, sc, pc, sc],
                    [sc, sc, sc, pc, sc],
                    [sc, sc, pc, sc, sc],
                    [sc, sc, pc, sc, sc],
                    [sc, pc, sc, sc, sc],
                    [sc, pc, sc, sc, sc],
                ]
            )
        elif number == "8":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [sc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, pc, pc, sc, sc],
                ]
            )
        elif number == "9":
            number_list.append(
                [
                    [sc, sc, sc, sc, sc],
                    [sc, pc, pc, sc, sc],
                    [pc, sc, sc, pc, sc],
                    [pc, sc, sc, pc, sc],
                    [sc, pc, pc, pc, sc],
                    [sc, sc, sc, pc, sc],
                    [sc, sc, sc, pc, sc],
                    [sc, sc, sc, pc, sc],
                ]
            )
    number_list.append(
        [
            [
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
            ],
            [
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
            ],
            [
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
            ],
            [
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
            ],
            [
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
            ],
            [
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
            ],
            [
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
            ],
            [
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
                sc,
            ],
        ]
    )
    return number_list
