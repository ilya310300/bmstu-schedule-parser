import argparse

from bmstuSchedule.configs import *
from bmstuSchedule import *


def argConfig():
    parser = argparse.ArgumentParser(description='Bauman Moscow State Technical University EU Schedule iCal parser')
    parser.add_argument('-s', '--semester_first_monday', default='05-02-2018', type=str, help='Semester first week monday date')
    parser.add_argument('url', type=str, help='Schedule URL')
    return parser

def main(args=None):
    namespace = argConfig().parse_args(args)
    try:
        bmstuSchedule.run(namespace.url, namespace.semester_first_monday)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()