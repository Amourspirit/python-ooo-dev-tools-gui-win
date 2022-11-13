.. _class_robot_keys:

Class RobotKeys
===============

Intro
-----

``RobotKeys`` class allows for a quick way to emulate keyboard input.
Keyboard input can be directed a active window or a Specific window can be specified.

Many ready made keyboard command have been put together.
The following list can be found in :ref:`keys_index`.

.. cssclass:: ul-list

    * :py:class:`~.calc_key_codes.CalcKeyCodes`
    * :py:class:`~.draw_key_codes.DrawKeyCodes`
    * :py:class:`~.impress_key_codes.ImpressKeyCodes`
    * :py:class:`~.writer_key_codes.WriterKeyCodes`


**Examples:**

This Simple example sends ``ALT+s`` to the current focused window.



.. code-block:: python

    from odevgui_win.robot_keys import RobotKeys
    from odevgui_win.class_args.send_key_info import SendKeyInfo, KeyCodes
    from odevgui_win.keys.writer_key_codes import WriterKeyCodes

    RobotKeys.send(SendKeyInfo.from_code_str(KeyCodes.ALT, "s"))

Sometimes you may need to focus window before sending keys.
In this example key are sent specifically to Calc Window with ``myfile.ods`` open.

.. code-block:: python

    from odevgui_win.robot_keys import RobotKeys, SendKeyInfo, WindowTitle
    from odevgui_win.keys.calc_key_codes import CalcKeyCodes

    RobotKeys.send(
        SendKeyInfo(CalcKeyCodes.TOGGLE_GRID_LINES),
        WriterKeyCodes(title="myfile.ods - LibreOffice Calc")
    )

Class
-----

.. autoclass:: odevgui_win.robot_keys.RobotKeys
    :members:

