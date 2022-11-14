from typing import cast
from ooodev.office.draw import Draw, DrawingBitmapKind, DrawingHatchingKind, DrawingGradientKind, ShapeDispatchKind
from ooodev.utils.color import CommonColor
from ooodev.utils.lo import Lo

from ooodev.utils.props import Props
from ooodev.utils.gui import GUI

from ooo.dyn.drawing.line_style import LineStyle
from ooo.dyn.drawing.hatch import Hatch


def test_create_dispatch_shapes_impress(loader) -> None:
    from odevgui_win.draw_dispatcher import DrawDispatcher

    doc = Draw.create_impress_doc(loader)
    curr_slide = Draw.get_slide(doc=doc, idx=0)

    Draw.title_only_slide(slide=curr_slide, header="Dispatched Shapes")

    GUI.set_visible(is_visible=True, odoc=doc)
    Lo.delay(1_000)

    Draw.goto_page(doc=doc, page=curr_slide)

    # first row
    y = 38
    _ = Draw.add_dispatch_shape(
        slide=curr_slide,
        shape_dispatch=ShapeDispatchKind.BASIC_SHAPES_DIAMOND,
        x=20,
        y=y,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
    )
    _ = Draw.add_dispatch_shape(
        slide=curr_slide,
        shape_dispatch=ShapeDispatchKind.THREE_D_HALF_SPHERE,
        x=80,
        y=y,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
    )
    dshape = Draw.add_dispatch_shape(
        slide=curr_slide,
        shape_dispatch=ShapeDispatchKind.CALLOUT_SHAPES_CLOUD_CALLOUT,
        x=140,
        y=y,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
    )
    Draw.set_bitmap_color(shape=dshape, name=DrawingBitmapKind.LITTLE_CLOUDS)

    dshape = Draw.add_dispatch_shape(
        slide=curr_slide,
        shape_dispatch=ShapeDispatchKind.FLOW_CHART_SHAPES_FLOWCHART_CARD,
        x=200,
        y=y,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
    )
    Draw.set_hatch_color(shape=dshape, name=DrawingHatchingKind.BLUE_NEG_45_DEGREES)
    # convert blue to black manually
    dhatch = cast(Hatch, Props.get(dshape, "FillHatch"))
    dhatch.Color = CommonColor.BLACK
    Props.set(dshape, LineColor=CommonColor.BLACK, FillHatch=dhatch)
    # Props.show_obj_props("Hatch Shape", dshape)

    # second row
    y = 100
    dshape = Draw.add_dispatch_shape(
        slide=curr_slide,
        shape_dispatch=ShapeDispatchKind.STAR_SHAPES_STAR_12,
        x=20,
        y=y,
        width=40,
        height=40,
        fn=DrawDispatcher.create_dispatch_shape,
    )
    Draw.set_gradient_color(shape=dshape, name=DrawingGradientKind.SUNSHINE)
    Props.set(dshape, LineStyle=LineStyle.NONE)

    dshape = Draw.add_dispatch_shape(
        slide=curr_slide,
        shape_dispatch=ShapeDispatchKind.SYMBOL_SHAPES_HEART,
        x=80,
        y=y,
        width=40,
        height=40,
        fn=DrawDispatcher.create_dispatch_shape,
    )
    Props.set(dshape, FillColor=CommonColor.RED)

    _ = Draw.add_dispatch_shape(
        slide=curr_slide,
        shape_dispatch=ShapeDispatchKind.ARROW_SHAPES_LEFT_RIGHT_ARROW,
        x=140,
        y=y,
        width=50,
        height=30,
        fn=DrawDispatcher.create_dispatch_shape,
    )
    dshape = Draw.add_dispatch_shape(
        slide=curr_slide,
        shape_dispatch=ShapeDispatchKind.THREE_D_CYRAMID,
        x=200,
        y=y - 20,
        width=50,
        height=50,
        fn=DrawDispatcher.create_dispatch_shape,
    )
    Draw.set_bitmap_color(shape=dshape, name=DrawingBitmapKind.STONE)
    num_shapes = curr_slide.getCount()
    Lo.delay(2000)
    Lo.close(closeable=doc, deliver_ownership=False)
    assert num_shapes == 9
