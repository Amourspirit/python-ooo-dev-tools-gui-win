.. ooo-dev-tools-gui-win documentation master file, created by
   sphinx-quickstart on Sat Nov 12 14:23:45 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Docs for |app_name|.
=================================================

|app_name| extends |odev_tools|_.

Automation classes are:

.. cssclass:: ul-list

   * :ref:`class_dialog_auto`
   * :ref:`class_draw_dispatcher`
   * :ref:`class_robot_keys`
   * :ref:`class_focus`

See example |impress_make_slides|_.

.. seealso::

   |odev_part3|_

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   src/index

Installation
------------

``ooo-dev-tools-gui-win`` is also available via an `Extension <https://extensions.libreoffice.org/en/extensions/show/41986>`__ for LibreOffice

Install from `pypi.org <https://pypi.org/project/ooo-dev-tools-gui-win/>`__:

.. code::

   pip install ooo-dev-tools-gui-win

Example Code
------------

.. cssclass:: screen_shot

   .. _fig_draw_cloud:
   .. figure:: https://user-images.githubusercontent.com/4193389/200589660-9ccede18-b0b5-4052-a36c-ef3f5002ea7c.png
        :alt: Draw page cloud callout
        :figclass: align-center

        :Draw page cloud callout

This code adds the cloud seen in :numref:`fig_draw_cloud` to a Draw page.

.. tabs::

    .. code-tab:: python

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


Indices and tables
==================

* :ref:`genindex`

