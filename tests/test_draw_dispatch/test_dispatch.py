from ooodev.office.draw import Draw, DrawingBitmapKind, DrawingHatchingKind, DrawingGradientKind
from ooodev.utils.color import CommonColor
from ooodev.utils.lo import Lo

from ooodev.utils.props import Props
from ooodev.utils.gui import GUI

from ooo.dyn.drawing.line_style import LineStyle


def test_create_dispatch_shape_win(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    doc = Draw.create_draw_doc(loader)
    slide = Draw.get_slide(doc=doc, idx=0)

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)
    GUI.zoom(view=GUI.ZoomEnum.PAGE_WIDTH)
    # Lo.delay(1_000)
    shape = DrawDispatcher.create_dispatch_shape_win(slide=slide, shape_dispatch="BasicShapes.diamond")
    assert shape is not None
    Lo.close(closeable=doc, deliver_ownership=False)


def test_dispatch_basic_diamond(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    delay = 2_000
    doc = Draw.create_draw_doc(loader)
    slide = Draw.get_slide(doc=doc, idx=0)

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)
    GUI.zoom(view=GUI.ZoomEnum.PAGE_WIDTH)
    # dShape = Draw.addDispatchShape(currSlide, "BasicShapes.diamond", 20, 60, 50, 30);
    shape = Draw.add_dispatch_shape(
        slide=slide,
        shape_dispatch="BasicShapes.diamond",
        x=20,
        y=60,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape_win,
    )
    Lo.delay(delay)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert shape is not None


def test_dispatch_callout_shapes_cloud_callout(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    delay = 2_000
    doc = Draw.create_draw_doc(loader)
    slide = Draw.get_slide(doc=doc, idx=0)

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)
    GUI.zoom(view=GUI.ZoomEnum.PAGE_WIDTH)

    shape = Draw.add_dispatch_shape(
        slide=slide,
        shape_dispatch="CalloutShapes.cloud-callout",
        x=140,
        y=60,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape_win,
    )
    Draw.set_bitmap_color(shape, DrawingBitmapKind.LITTLE_CLOUDS)
    Lo.delay(delay)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert shape is not None


def test_dispatch_flow_chart_shape_flow_chart_card(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    delay = 2_000
    doc = Draw.create_draw_doc(loader)
    slide = Draw.get_slide(doc=doc, idx=0)

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)
    GUI.zoom(view=GUI.ZoomEnum.ENTIRE_PAGE)
    shape = Draw.add_dispatch_shape(
        slide=slide,
        shape_dispatch="FlowChartShapes.flowchart-card",
        x=150,
        y=60,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape_win,
    )
    Draw.set_hatch_color(shape, DrawingHatchingKind.BLUE_NEG_45_DEGREES)
    Lo.delay(delay)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert shape is not None


def test_dispatch_star_shapes_star12(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    delay = 2_000
    doc = Draw.create_draw_doc(loader)
    slide = Draw.get_slide(doc=doc, idx=0)

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)
    GUI.zoom(view=GUI.ZoomEnum.PAGE_WIDTH)
    shape = Draw.add_dispatch_shape(
        slide=slide,
        shape_dispatch="StarShapes.star12",
        x=20,
        y=140,
        width=40,
        height=40,
        fn=DrawDispatcher.create_dispatch_shape_win,
    )
    Draw.set_gradient_color(shape, DrawingGradientKind.NEON_LIGHT)
    Props.set(shape, LineStyle=LineStyle.NONE)
    Lo.delay(delay)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert shape is not None


def test_dispatch_symbol_shapes_heart(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    delay = 2_000
    doc = Draw.create_draw_doc(loader)
    slide = Draw.get_slide(doc=doc, idx=0)

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)
    GUI.zoom(view=GUI.ZoomEnum.PAGE_WIDTH)
    shape = Draw.add_dispatch_shape(
        slide=slide,
        shape_dispatch="SymbolShapes.heart",
        x=80,
        y=140,
        width=40,
        height=40,
        fn=DrawDispatcher.create_dispatch_shape_win,
    )
    Props.set(shape, FillColor=CommonColor.RED)
    Lo.delay(delay)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert shape is not None


def test_dispatch_arrow_shapes_left_right_arrow(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    delay = 2_000
    doc = Draw.create_draw_doc(loader)
    slide = Draw.get_slide(doc=doc, idx=0)

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)
    GUI.zoom(view=GUI.ZoomEnum.ENTIRE_PAGE)
    shape = Draw.add_dispatch_shape(
        slide=slide,
        shape_dispatch="ArrowShapes.left-right-arrow",
        x=140,
        y=140,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape_win,
    )
    Lo.delay(delay)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert shape is not None


def test_dispatch_3d_cyramid(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    delay = 2_000
    doc = Draw.create_draw_doc(loader)
    slide = Draw.get_slide(doc=doc, idx=0)

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)
    GUI.zoom(view=GUI.ZoomEnum.ENTIRE_PAGE)
    shape = Draw.add_dispatch_shape(
        slide=slide,
        shape_dispatch="Cyramid",
        x=160,
        y=120,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape_win,
    )
    Lo.delay(delay)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert shape is not None


def test_dispatch_3d_HalfSphere(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    delay = 2_000
    doc = Draw.create_draw_doc(loader)
    slide = Draw.get_slide(doc=doc, idx=0)

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)
    GUI.zoom(view=GUI.ZoomEnum.PAGE_WIDTH)
    # dShape = Draw.addDispatchShape(currSlide, "BasicShapes.diamond", 20, 60, 50, 30);
    shape = Draw.add_dispatch_shape(
        slide=slide,
        shape_dispatch="HalfSphere",
        x=80,
        y=60,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape_win,
    )
    Lo.delay(delay)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert shape is not None
