import sys

from main.controllers.SoutherosRulerController import SoutherosRulerController


def main():

    controller = SoutherosRulerController()

    input_file_path = sys.argv[1]

    print(controller.check_if_space_is_ruler_using_input_file(input_file_path))


if __name__ == '__main__':
    main()
