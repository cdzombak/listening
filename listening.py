#!/usr/bin/env python3

import argparse
import platform
import subprocess
import sys

__LISTENING_VERSION__ = "<dev>"


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def str2bool(v):
    if v.casefold() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.casefold() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


def cmd_macos(port=None, transport=None, ipv=None):
    return "lsof -nP -i{ipv:s}{transport:s}{port:s}".format(
        ipv="{:d}".format(ipv) if ipv else "",
        transport=transport.upper() if transport else "",
        port=":{:d}".format(port) if port else "",
    )


def cmd_linux(port=None, transport=None, ipv=None):
    if ipv == 4:
        ipv_part = ' | grep --color=never -v -e "tcp6" -e "udp6"'
    elif ipv == 6:
        ipv_part = ' | grep --color=never -e "tcp6" -e "udp6"'
    else:
        ipv_part = ""
    return "netstat -lnp{transport:s}".format(
        ipv=ipv_part,
        transport=transport[0].lower() if transport else "tu",
        port=' | grep --color=never ":{:d}"'.format(port) if port else "",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="List processes listening for network connections. "
        "(Wraps lsof on macOS; netstat on Linux.)",
        prog="listening",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=None,
        help="Filter to processes listening on the given port. "
        "Default: none (all ports).",
    )
    parser.add_argument(
        "-t",
        "--transport",
        type=str,
        default=None,
        choices=["tcp", "udp"],
        help="Specifies TCP or UDP. Default: none (both).",
    )
    parser.add_argument(
        "-i",
        "--ip",
        type=int,
        default=None,
        choices=[4, 6],
        help="Specifies IPv4 or IPv6. Default: none (both).",
    )
    parser.add_argument(
        "-d",
        "--debug",
        type=str2bool,
        default="false",
        help="Whether to print (to stderr) the lsof/netstat command to "
        "be executed. Default: False.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s " + __LISTENING_VERSION__,
    )
    args = parser.parse_args()

    if "darwin" in platform.system().lower():
        cmd = cmd_macos(port=args.port, transport=args.transport, ipv=args.ip)
    elif "linux" in platform.system().lower():
        cmd = cmd_linux(port=args.port, transport=args.transport, ipv=args.ip)
    else:
        eprint("Platform {:s} is unsupported.".format(platform.system()))
        sys.exit(1)

    if args.debug:
        eprint("+ {:s}".format(cmd))
        eprint("")
    p = subprocess.Popen(cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)
    sys.exit(p.wait())
