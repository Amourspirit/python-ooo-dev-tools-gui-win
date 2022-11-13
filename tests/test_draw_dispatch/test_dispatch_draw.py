from ooodev.office.draw import Draw, DrawingBitmapKind, DrawingHatchingKind, DrawingGradientKind, ShapeDispatchKind
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
    shape = DrawDispatcher.create_dispatch_shape(slide=slide, shape_dispatch=ShapeDispatchKind.BASIC_SHAPES_DIAMOND)
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
        shape_dispatch=ShapeDispatchKind.BASIC_SHAPES_DIAMOND,
        x=20,
        y=60,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
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
        shape_dispatch=ShapeDispatchKind.CALLOUT_SHAPES_CLOUD_CALLOUT,
        x=140,
        y=60,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
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
        shape_dispatch=ShapeDispatchKind.FLOW_CHART_SHAPES_FLOWCHART_CARD,
        x=150,
        y=60,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
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
        shape_dispatch=ShapeDispatchKind.STAR_SHAPES_STAR_12,
        x=20,
        y=140,
        width=40,
        height=40,
        fn=DrawDispatcher.create_dispatch_shape,
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
        shape_dispatch=ShapeDispatchKind.SYMBOL_SHAPES_HEART,
        x=80,
        y=140,
        width=40,
        height=40,
        fn=DrawDispatcher.create_dispatch_shape,
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
        shape_dispatch=ShapeDispatchKind.ARROW_SHAPES_LEFT_RIGHT_ARROW,
        x=140,
        y=140,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
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
        shape_dispatch=ShapeDispatchKind.THREE_D_CYRAMID,
        x=160,
        y=120,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
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
        shape_dispatch=ShapeDispatchKind.THREE_D_HALF_SPHERE,
        x=80,
        y=60,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
    )
    Lo.delay(delay)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert shape is not None


# def test_dispatch_sample(loader) -> None:
#     from odevgui_win.draw_dispatcher import DrawDispatcher

#     delay = 2_000
#     doc = Draw.create_draw_doc(loader)
#     slide = Draw.get_slide(doc=doc, idx=0)

#     GUI.set_visible(is_visible=True, odoc=doc)
#     Lo.delay(1_000)
#     GUI.zoom(view=GUI.ZoomEnum.PAGE_WIDTH)
#     shape = Draw.add_dispatch_shape(
#         slide=slide,
#         shape_dispatch=ShapeDispatchKind.FLOW_CHART_SHAPES_FLOWCHART_COLLATE,
#         x=40,
#         y=60,
#         width=50,
#         height=30,
#         fn=DrawDispatcher.create_dispatch_shape_win,
#     )
#     Lo.delay(delay)
#     Lo.close(closeable=doc, deliver_ownership=False)
#     assert shape is not None
