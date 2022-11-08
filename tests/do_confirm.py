from __future__ import annotations
import threading
import time
from typing import TYPE_CHECKING
import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

if TYPE_CHECKING:
    from typing import Literal

# Confirmation
# ahk_class SALSUBFRAME
# ahk_exe soffice.bin


# algs.odp - LibreOffice Impress
# ahk_class SALFRAME
# ahk_exe soffice.bin


class DrawDialogConfirm:
    @staticmethod
    def monitor_dialog(send_key: str, title: str = "Confirmation", is_re_title: bool = False) -> None:

        # start thread
        x = threading.Thread(target=DrawDialogConfirm._confirmation, args=(send_key, title, is_re_title), daemon=True)
        x.start()

    @staticmethod
    def _confirmation(key: str, title: str, is_re_tile: bool) -> None:
        while 1:
            try:
                if is_re_tile:
                    app = Application().connect(title_re=title, class_name="SALSUBFRAME")
                else:
                    app = Application().connect(title=title, class_name="SALSUBFRAME")

            except pywinauto.ElementNotFoundError:
                print("Element not found")
            else:
                print("sending keys")
                send_keys("{VK_MENU down}" f"{key}" "{VK_MENU up}")
            time.sleep(0.7)


def do_yes() -> None:
    send_keys("{VK_MENU down}" "y" "{VK_MENU up}")


def _main() -> int:
    try:
        app = Application().connect(title="Confirmation", class_name="SALSUBFRAME")
        # app = Application().connect(title_re="*.LibreOffice Impress", class_name="SALFRAME")
    except pywinauto.ElementNotFoundError:
        print("Element not found")
        return 0
    win = app.top_window()
    win.set_focus()
    time.sleep(0.2)
    # print(app.windows())
    # app.window.print_control_identifiers()

    # https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
    # send alt+y for yes button
    send_keys("{VK_MENU down}" "y" "{VK_MENU up}")
    # win = app.window(title_re=".*LibreOffice Draw")

    return 0


def main() -> int:
    time.sleep(5)
    DrawDialogConfirm.monitor_dialog("y")
    time.sleep(30)
    return 0


if __name__ == "__main__":
    SystemExit(main())
