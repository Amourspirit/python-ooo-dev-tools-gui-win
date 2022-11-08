#!/usr/bin/env python
# coding: utf-8
import argparse
import sys
import os
from pathlib import Path
from src.cmds import uno_lnk
from src.utils import util

# region parser
# region        Create Parsers


def _create_parser(name: str) -> argparse.ArgumentParser:
    return argparse.ArgumentParser(description=name)


# endregion     Create Parsers

# region        process arg command
def _args_cmd_link(parser: argparse.ArgumentParser) -> None:
    add_grp = parser.add_argument_group()
    add_grp.add_argument(
        "-a",
        "--add",
        help="Add uno links to virtual environment.",
        action="store_true",
        dest="add",
        default=False,
    )

    add_grp.add_argument(
        "-s",
        "--uno-src",
        help="Optional source directory that contains uno.py and unohelper.py. If ommited then defaults are used.",
        action="store",
        dest="src_dir",
        default=None,
    )
    parser.add_argument(
        "-r",
        "--remove",
        help="Remove uno links to virtual environment.",
        action="store_true",
        dest="remove",
        default=False,
    )


def _args_action_cmd_link(a_parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    if not (args.add or args.remove):
        a_parser.error("No action requested, add --add or --remove")
    if args.add:
        uno_lnk.add_links(args.src_dir)
    elif args.remove:
        uno_lnk.remove_links()


def _args_process_cmd(a_parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    if args.command == "cmd-link":
        _args_action_cmd_link(a_parser=a_parser, args=args)
    else:
        a_parser.print_help()


# endregion        process arg command
# endregion parser


def main() -> int:
    os.environ["project_root"] = str(Path(__file__).parent)
    os.environ["env-site-packages"] = str(util.get_site_packeges_dir())
    parser = _create_parser("main")
    subparser = parser.add_subparsers(dest="command")

    if os.name != "nt":
        # linking is not useful in Windows.
        cmd_link = subparser.add_parser(
            name="cmd-link",
            help="Add/Remove links in virtual environments to uno files.",
        )
        _args_cmd_link(parser=cmd_link)

    # region Read Args
    args = parser.parse_args()
    # endregion Read Args
    _args_process_cmd(a_parser=parser, args=args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())