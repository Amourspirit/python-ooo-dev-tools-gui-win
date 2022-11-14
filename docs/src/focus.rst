.. _class_focus:

Class Focus
===========

Intro
-----

The Focus class allows for setting foucs of a LibreOffice Window.

For example to focus on the default windows created with :external+odev:py:meth:`ooodev.utils.lo.Lo.load_office`.

.. code-block:: python
    :emphasize-lines: 5, 6, 7, 8, 9, 22, 23

    from ooodev.office.draw import Draw
    from ooodev.utils.gui import GUI
    from ooodev.utils.lo import Lo

    try:
        # only windows
        from odevgui_win.focus import Focus
    except ImportError:
        Focus = None

    def main() -> int:
        loader = Lo.load_office(Lo.ConnectPipe())

        try:
            doc = Draw.create_draw_doc(loader)
            slide = Draw.get_slide(doc=doc, idx=0)

            GUI.set_visible(is_visible=True, odoc=doc)
            Lo.delay(1_000)
            GUI.zoom(view=GUI.ZoomEnum.ENTIRE_PAGE)

            if Focus:
                Focus.focus_current()

            # do other document processing
        except Exception:
            Lo.close_office()
            raise
        return 0

    if __name__ == "__main__":
        SystemExit(main())

Class
-----

.. autoclass:: odevgui_win.focus.Focus
    :members:

