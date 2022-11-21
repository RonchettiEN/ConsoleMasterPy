import os
import sys
import datetime
import pathlib
import ctypes

from sty import bg, fg, rs
from playsound import playsound
import cursor

if sys.platform == "win32":
    os.system("color")


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            playsound(str(pathlib.Path(__file__).parent.absolute()) + "\error.mp3")
            timestamp = datetime.datetime.now().isoformat()
            f = open("log.txt", "a")
            f.write(timestamp)
            f.write(f" {func.__name__} {e}\n")
            f.close()

    return inner_function


@exception_handler
def pause():
    input()


@exception_handler
def print_with_color(rgb_background, rgb_foreground, element_to_print):
    print(
        fg(rgb_foreground[0], rgb_foreground[1], rgb_foreground[2])
        + bg(rgb_background[0], rgb_background[1], rgb_background[2])
        + element_to_print
        + rs.all
    )


class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    def __init__(self, x, y):
        self.X = x
        self.Y = y


@exception_handler
def go_xy(x, y):
    INIT_POS = COORD(y, x)
    STD_OUTPUT_HANDLE = -11
    hOut = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetConsoleCursorPosition(hOut, INIT_POS)


LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11


class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_ulong),
        ("nFont", ctypes.c_ulong),
        ("dwFontSize", COORD),
        ("FontFamily", ctypes.c_uint),
        ("FontWeight", ctypes.c_uint),
        ("FaceName", ctypes.c_wchar * LF_FACESIZE),
    ]


@exception_handler
def change_pixel_size(size):
    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    # font.nFont = 12
    font.dwFontSize.X = size
    font.dwFontSize.Y = size
    # font.FontFamily = 54
    # font.FontWeight = 400
    # font.FaceName = "Lucida Console"

    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font)
    )


@exception_handler
def change_windows_size(width, height):
    cmd = "mode " + str(width) + "," + str(height)
    os.system(cmd)


@exception_handler
def show_cursor():
    cursor.show()


@exception_handler
def hide_cursor():
    cursor.hide()


@exception_handler
def change_windows_title(title):
    os.system("title " + str(title))
