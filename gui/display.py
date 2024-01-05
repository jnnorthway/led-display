import tkinter as tk
import time

PIXEL_SIZE = 20
WIDTH = PIXEL_SIZE * 32
HEIGHT = PIXEL_SIZE * 8
MAX_DIGITS = 4
DC = "black"
RC = "red"
WC = "white"

window = tk.Tk()
window.title("led display")
canvas = tk.Canvas(height=HEIGHT, width=WIDTH)

def get_number_array(number):
    number_str = str(number)
    number_str_len = len(number_str)
    number_list = []
    if number_str_len < MAX_DIGITS:
        for _ in range(MAX_DIGITS-number_str_len):
            number_list.append([
                [DC,DC,DC,DC,DC],
                [DC,DC,DC,DC,DC],
                [DC,DC,DC,DC,DC],
                [DC,DC,DC,DC,DC],
                [DC,DC,DC,DC,DC],
                [DC,DC,DC,DC,DC],
                [DC,DC,DC,DC,DC],
                [DC,DC,DC,DC,DC],
            ])
    elif number_str_len > MAX_DIGITS:
        if number_str_len == 5:
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
            number_list.append([
                [DC,DC],
                [DC,DC],
                [DC,DC],
                [DC,DC],
                [DC,DC],
                [DC,DC],
                [DC,DC],
                [WC,DC],
            ])
        elif number == "k":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,WC,DC,DC],
                [DC,WC,DC,DC,DC],
                [WC,DC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
            ])
        elif number == "m":
            number_list.append([
                [DC,DC,DC,DC,DC,DC],
                [WC,DC,DC,DC,WC,DC],
                [WC,WC,DC,WC,WC,DC],
                [WC,DC,WC,DC,WC,DC],
                [WC,DC,DC,DC,WC,DC],
                [WC,DC,DC,DC,WC,DC],
                [WC,DC,DC,DC,WC,DC],
                [WC,DC,DC,DC,WC,DC],
            ])
        elif number == "b":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [WC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [WC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [WC,WC,WC,DC,DC],
            ])
        elif number == "t":
            number_list.append([
                [DC,DC,DC,DC,DC,DC],
                [WC,WC,WC,WC,WC,DC],
                [DC,DC,WC,DC,DC,DC],
                [DC,DC,WC,DC,DC,DC],
                [DC,DC,WC,DC,DC,DC],
                [DC,DC,WC,DC,DC,DC],
                [DC,DC,WC,DC,DC,DC],
                [DC,DC,WC,DC,DC,DC],
            ])
        elif number == "0":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [DC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [DC,WC,WC,DC,DC],
            ])
        elif number == "1":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [DC,DC,WC,DC,DC],
                [DC,DC,WC,DC,DC],
                [DC,DC,WC,DC,DC],
                [DC,DC,WC,DC,DC],
                [DC,DC,WC,DC,DC],
                [DC,DC,WC,DC,DC],
                [DC,DC,WC,DC,DC],
            ])
        elif number == "2":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [DC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [DC,DC,DC,WC,DC],
                [DC,DC,WC,DC,DC],
                [DC,WC,DC,DC,DC],
                [WC,DC,DC,DC,DC],
                [WC,WC,WC,WC,DC],
            ])
        elif number == "3":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [DC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [DC,DC,DC,WC,DC],
                [DC,WC,WC,DC,DC],
                [DC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [DC,WC,WC,DC,DC],
            ])
        elif number == "4":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [DC,WC,WC,WC,DC],
                [DC,DC,DC,WC,DC],
                [DC,DC,DC,WC,DC],
                [DC,DC,DC,WC,DC],
            ])
        elif number == "5":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [WC,WC,WC,WC,DC],
                [WC,DC,DC,DC,DC],
                [WC,DC,DC,DC,DC],
                [WC,WC,WC,DC,DC],
                [DC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [DC,WC,WC,DC,DC],
            ])
        elif number == "6":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [DC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,DC,DC],
                [WC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [DC,WC,WC,DC,DC],
            ])
        elif number == "7":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [WC,WC,WC,DC,DC],
                [DC,DC,DC,WC,DC],
                [DC,DC,DC,WC,DC],
                [DC,DC,WC,DC,DC],
                [DC,DC,WC,DC,DC],
                [DC,WC,DC,DC,DC],
                [DC,WC,DC,DC,DC],
            ])
        elif number == "8":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [DC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [DC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [DC,WC,WC,DC,DC],
            ])
        elif number == "9":
            number_list.append([
                [DC,DC,DC,DC,DC],
                [DC,WC,WC,DC,DC],
                [WC,DC,DC,WC,DC],
                [WC,DC,DC,WC,DC],
                [DC,WC,WC,WC,DC],
                [DC,DC,DC,WC,DC],
                [DC,DC,DC,WC,DC],
                [DC,DC,DC,WC,DC],
            ])
    number_list.append([
        [DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,],
        [DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,],
        [DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,],
        [DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,],
        [DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,],
        [DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,],
        [DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,],
        [DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,DC,],
    ])
    return number_list

youtube = [
    [DC,RC,RC,RC,RC,RC,RC,RC,RC,DC,DC],
    [RC,RC,RC,RC,RC,RC,RC,RC,RC,RC,DC],
    [RC,RC,RC,RC,WC,RC,RC,RC,RC,RC,DC],
    [RC,RC,RC,RC,WC,WC,RC,RC,RC,RC,DC],
    [RC,RC,RC,RC,WC,WC,WC,RC,RC,RC,DC],
    [RC,RC,RC,RC,WC,WC,RC,RC,RC,RC,DC],
    [RC,RC,RC,RC,WC,RC,RC,RC,RC,RC,DC],
    [DC,RC,RC,RC,RC,RC,RC,RC,RC,DC,DC],
]

subs = 767

def pack_subs(subscribers):
    num_array = get_number_array(subscribers)
    current_number = 0
    current_pixel = 0
    for i in range(0, WIDTH, PIXEL_SIZE):
        x = int(i/PIXEL_SIZE)
        for j in range(0, HEIGHT, PIXEL_SIZE):
            y = int(j/PIXEL_SIZE)
            if x < 11:
                colour = youtube[y][x]
            else:
                colour = num_array[current_number][y][current_pixel]
            canvas.create_rectangle(i, j, i + PIXEL_SIZE, j + PIXEL_SIZE, outline="black", fill=colour, width=2)
        if x >= 11:
            current_pixel += 1
            if current_pixel == len(num_array[current_number][y]):
                current_number += 1
                current_pixel = 0
    canvas.pack()

for i in range(10000000):
    pack_subs(i)
    window.update()
    time.sleep(0.8)

