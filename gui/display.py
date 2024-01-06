import tkinter as tk

PIXEL_SIZE = 20
WIDTH = PIXEL_SIZE * 32
HEIGHT = PIXEL_SIZE * 8

window = tk.Tk()
window.title("led display")
canvas = tk.Canvas(height=HEIGHT, width=WIDTH)


def pack_subs(logo, number_array):
    current_number = 0
    current_pixel = 0
    logo_width = len(logo[0])
    for i in range(0, WIDTH, PIXEL_SIZE):
        x = int(i / PIXEL_SIZE)
        for j in range(0, HEIGHT, PIXEL_SIZE):
            y = int(j / PIXEL_SIZE)
            if x < logo_width:
                color = logo[y][x]
            else:
                color = number_array[current_number][y][current_pixel]
            canvas.create_rectangle(
                i,
                j,
                i + PIXEL_SIZE,
                j + PIXEL_SIZE,
                outline="black",
                fill=color,
                width=2,
            )
        if x >= logo_width:
            current_pixel += 1
            if current_pixel == len(number_array[current_number][y]):
                current_number += 1
                current_pixel = 0
    canvas.pack()
    window.update()


def wipe(color, brightness=None):
    for i in range(0, WIDTH, PIXEL_SIZE):
        for j in range(0, HEIGHT, PIXEL_SIZE):
            canvas.create_rectangle(
                i,
                j,
                i + PIXEL_SIZE,
                j + PIXEL_SIZE,
                outline="black",
                fill=color,
                width=2,
            )
    canvas.pack()
    window.update()
