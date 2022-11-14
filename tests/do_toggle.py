import sys
import time
import inspect
import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from odevgui_win.keys.writer_key_codes import WriterKeyCodes
from odevgui_win.kind.keys_kind import KeyCodes
from ooodev.utils.lo import Lo
from ooodev.office.write import Write
from ooodev.dialog.msgbox import MsgBox, MessageBoxType, MessageBoxButtonsEnum, MessageBoxResultsEnum
from ooodev.utils.gui import GUI


def main() -> int:
    loader = Lo.load_office(Lo.ConnectPipe())
    try:
        doc = Write.create_doc(loader)

        GUI.set_visible(is_visible=True, odoc=doc)
        Lo.delay(1_000)  # delay to make sure zoom takes
        GUI.zoom(GUI.ZoomEnum.PAGE_WIDTH)
        Lo.delay(1_000)
        cursor = Write.get_cursor(doc)
        Write.append_para(cursor, "Hello World")
        Write.append_para(cursor, "Wonderful World")
        app = Application().connect(title_re=".*LibreOffice Writer", class_name="SALFRAME")

        win = app.window(title_re=".*LibreOffice Writer")
        # print(dir(win))
        win.set_focus()
        GUI.show_memu_bar()
        time.sleep(0.5)
        # print("Title Bar:", GUI.get_title_bar())
        send_keys(WriterKeyCodes.KB_SELECT_ALL)

        time.sleep(0.5)
        inc = WriterKeyCodes.KB_INCREASE_SIZE * 5
        send_keys(inc)
        # send_keys(WriterKeyCodes.FORMAT_LOWERCASE)

        time.sleep(0.5)
        single = True
        code = WriterKeyCodes.FORMAT_CAP_EVERY_WORD
        print("Code:", code)
        if single:
            send_keys(code)
        else:
            for _ in range(4):
                time.sleep(1.0)
                # send_keys(ImpressKeysKind.IMPRESS_TOGGLE_SLIDE_PANEL)
                # send_keys(ImpressKeysKind.IMPRESS_TOGGLE_STATUS_BAR)
                send_keys(code)

        Lo.delay(1_000)
        msg_result = MsgBox.msgbox(
            "Do you wish to close document?",
            "All done",
            boxtype=MessageBoxType.QUERYBOX,
            buttons=MessageBoxButtonsEnum.BUTTONS_YES_NO,
        )
        if msg_result == MessageBoxResultsEnum.YES:
            Lo.close_doc(doc=doc, deliver_ownership=True)
            Lo.close_office()
        else:
            print("Keeping document open")

    except Exception:
        Lo.close_office()
        raise
    return 0


if __name__ == "__main__":
    SystemExit(main())
