from ooodev.office.draw import Draw, DrawingBitmapKind, ShapeDispatchKind
from ooodev.utils.lo import Lo
from ooodev.utils.gui import GUI
from odevgui_win.draw_dispatcher import DrawDispatcher


def main() -> int:
    loader = Lo.load_office(Lo.ConnectPipe())

    try:
        doc = Draw.create_draw_doc(loader)
        slide = Draw.get_slide(doc=doc, idx=0)

        GUI.set_visible(is_visible=True, odoc=doc)
        Lo.delay(1_000)
        GUI.zoom(view=GUI.ZoomEnum.ENTIRE_PAGE)

        shape = Draw.add_dispatch_shape(
            slide=slide,
            shape_dispatch=ShapeDispatchKind.CALLOUT_SHAPES_CLOUD_CALLOUT,
            x=140,
            y=60,
            width=50,
            height=30,
            fn=DrawDispatcher.create_dispatch_shape,
        )
        Draw.set_bitmap_color(shape, DrawingBitmapKind.LITTLE_CLOUDS)
    except Exception:
        Lo.close_office()
        raise
    return 0


if __name__ == "__main__":
    SystemExit(main())
