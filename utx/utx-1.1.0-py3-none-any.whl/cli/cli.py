#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  Lijiawei
@Date    :  8/17/2021 6:49 PM
@Desc    :  Command line.
"""

import argparse
import os
import random
import subprocess
import sys

from loguru import logger

from utx.cli.scaffold_web import init_parser_scaffold_web, main_scaffold_web
from utx.core.utils.tools import decryption, check_port, plat
from utx import __description__, __version__
from utx.cli.scaffold import init_parser_scaffold, main_scaffold, init_parser_install, main_install, \
    init_parser_uninstall, main_uninstall


def main():
    """Parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(description=__description__)

    parser.add_argument(
        "-v", "--version", dest="version", action="store_true", help="show version"
    )
    subparsers = parser.add_subparsers(help="sub-command help")
    sub_parser_scaffold = init_parser_scaffold(subparsers)
    sub_parser_scaffold_web = init_parser_scaffold_web(subparsers)
    sub_parser_install = init_parser_install(subparsers)
    sub_parser_uninstall = init_parser_uninstall(subparsers)
    subparsers.add_parser(
        "test", help="debug iOS devices(UTX driver needs to be installed)."
    )
    # show device info
    subparsers.add_parser(
        "list", help="show connected iOS devices."
    )
    subparsers.add_parser(
        "info", help="show current connected iOS device info."
    )
    subparsers.add_parser(
        "applist", help="list packages."
    )

    if len(sys.argv) == 1:
        # utx
        parser.print_help()
        sys.exit(0)
    elif len(sys.argv) == 2:
        # print help for sub-commands
        if sys.argv[1] in ["-v", "--version"]:
            # utx -v
            print(f"{__version__}")
        elif sys.argv[1] == "test":
            # utx -test
            logger.info('UTX will connect your IOS device.')
            logger.warning(
                'Please make sure the IOS phone is connected to the computer and the UTX driver is installed!')
            devices = '{} list'.format(decryption(b'dGlkZXZpY2U='))
            d = os.popen(devices)
            if len(d.readlines()) == 0:
                logger.error('No device detected!')
                sys.exit()

            res = subprocess.run('{} applist'.format(decryption(b'dGlkZXZpY2U=')), shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            utx_driver = res.stdout.decode("utf-8", "ignore")

            if 'WebDriverAgentRunner' not in utx_driver:
                logger.error('UTX driver(WDA.ipa) is not installed!')
                sys.exit()
            else:
                pass

            proxy = str(random.randint(50000, 60000) + 1)
            check_port(port=proxy)
            logger.info('Debug address:http://127.0.0.1:{}'.format(proxy))
            try:
                subprocess.call('{} wdaproxy --port {}'.format(decryption(b'dGlkZXZpY2U='), proxy), shell=True)
            except KeyboardInterrupt:
                check_port(port=proxy)
                sys.exit()
            finally:
                if plat() != 'Windows':
                    os.system('clear')
                else:
                    os.system('cls')
                logger.error('')
                logger.error('-------------------- utx end --------------------------')

                logger.error('Disconnect and end debugging!')

        elif sys.argv[1] in ["-h", "--help"]:
            # utx -h
            parser.print_help()

        elif sys.argv[1] == "install":
            # utx install
            sub_parser_install.print_help()

        elif sys.argv[1] == "uninstall":
            # utx uninstall
            sub_parser_uninstall.print_help()

        elif sys.argv[1] == "list":
            # utx list
            os.system('{} list'.format(decryption(b'dGlkZXZpY2U=')))

        elif sys.argv[1] == "info":
            # utx info
            os.system('{} info'.format(decryption(b'dGlkZXZpY2U=')))

        elif sys.argv[1] == "applist":
            # utx applist
            os.system('{} applist'.format(decryption(b'dGlkZXZpY2U=')))

        elif sys.argv[1] == "startproject":
            # utx startproject
            sub_parser_scaffold.print_help()

        elif sys.argv[1] == "startproject-web":
            # utx startproject-web
            sub_parser_scaffold_web.print_help()

        else:
            parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.version:
        print(f"{__version__}")
        sys.exit(0)

    if sys.argv[1] == "startproject":
        main_scaffold(args)

    if sys.argv[1] == "startproject-web":
        main_scaffold_web(args)

    if sys.argv[1] == "install":
        main_install(args)

    if sys.argv[1] == "uninstall":
        main_uninstall(args)


def cli_env():
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument("--device", type=str)
    parser.add_argument("--platform", type=str)
    parser.add_argument("--wda", type=str)
    parser.add_argument("--init", type=str)

    args = parser.parse_args()
    cli_device = args.device
    cli_platform = args.platform
    cli_wda = args.wda
    cli_init = args.init

    return cli_device, cli_platform, cli_wda, cli_init


def cli_web_env():
    parser = argparse.ArgumentParser(description='manual to this script')

    parser.add_argument("--headless", type=str)
    parser.add_argument("--driver", type=str)

    args = parser.parse_args()

    cli_headless = args.headless
    cli_driver_path = args.driver

    return cli_headless, cli_driver_path
