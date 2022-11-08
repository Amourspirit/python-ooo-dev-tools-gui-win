import sys
import time
import inspect
import pywinauto
from pywinauto.application import Application

# Untitled 1 - LibreOffice Draw
# ahk_class SALFRAME
# ahk_exe soffice.bin


def print_rect(rect, name: str = "") -> None:
    if name:
        print(name)
    try:
        print("rect top:", rect.top)
    except Exception:
        pass
    try:
        print("rect left:", rect.left)
    except Exception:
        pass
    try:
        print("rect right:", rect.right)
    except Exception:
        pass
    try:
        print("rect bottom:", rect.bottom)
    except Exception:
        pass
    print()


def main() -> int:
    app = Application().connect(title_re=".*LibreOffice Draw", class_name="SALFRAME")

    win = app.window(title_re=".*LibreOffice Draw")
    print(dir(win))
    win.set_focus()
    time.sleep(0.5)
    # print(win)

    time.sleep(2.0)

    print(app)
    # print(app.SALFRAME)
    dlg = app.SALFRAME.WrapperObject()
    # print(dir(dlg))

    # print(inspect.signature(dlg.drag_mouse))
    # (button='left', press_coords=(0, 0), release_coords=(0, 0), pressed='')

    # print(inspect.getfullargspec(dlg.move_mouse))
    # FullArgSpec(args=['self', 'coords', 'pressed', 'absolute'], varargs=None, varkw=None, defaults=((0, 0), '', False), kwonlyargs=[], kwonlydefaults=None, annotations={})

    # print(inspect.signature(dlg.move_mouse))
    # (coords=(0, 0), pressed='', absolute=False)

    # dlg.move_mouse(coords=(1000, 800), pressed="left", absolute=False)

    # print(inspect.getfullargspec(app.SALFRAME.drag_mouse))
    # FullArgSpec(args=['self', 'button', 'press_coords', 'release_coords', 'pressed'], varargs=None, varkw=None, defaults=('left', (0, 0), (0, 0), ''), kwonlyargs=[], kwonlydefaults=None, annotations={})

    # https://pywinauto.readthedocs.io/en/latest/code/pywinauto.mouse.html
    print(inspect.signature(pywinauto.mouse.move))
    # (coords=(0, 0))

    # pywinauto.mouse.move(coords=(100, 100))

    rect = win.Rectangle()

    # rect = dlg.Rectangle()
    # print("rect:", dir(rect))
    print_rect(rect, "Dlg Rectangle")
    print(rect.mid_point)
    center_x = round((rect.right - rect.left) / 2) + rect.left
    center_y = round((rect.bottom - rect.top) / 2) + rect.top
    print("Center X:", center_x)
    print("Center Y:", center_y)
    # print_rect(rect.width, "dlg.rect.width")
    # print_rect(rect.height, "dlg.rect.height")

    # pywinauto.mouse.move(coords=(center_x, center_y))
    pywinauto.mouse.press(button="left", coords=(center_x, center_y))
    pywinauto.mouse.release(button="left", coords=(center_x + 50, center_y + 50))

    return 0


if __name__ == "__main__":
    SystemExit(main())
