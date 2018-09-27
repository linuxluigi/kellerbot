import argparse
import kellersensortelegrambot
from kellersensortelegrambot import __version__
from kellersensortelegrambot.telegram_bot import run_bot


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('KellerSensorTelegramBot')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    return parser


def main(args=None):
    """
    Main entry point for your project.

    Args:
        args : list
            A of arguments as if they were input in the command line. Leave it
            None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    print('KellerBot is starting :)')
    run_bot()


if __name__ == '__main__':
    main()
