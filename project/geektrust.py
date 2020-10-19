import sys

from main.controllers.southeros_ruler_controller import SoutherosRulerController


def main():
    """
    Program User Script

    - Gets an instance of the controller
    - Gets the Output for the input file and prints it to the console
    """
    controller = SoutherosRulerController()

    input_file_path = sys.argv[1]

    print(controller.check_if_space_is_ruler_using_input_file(input_file_path))


if __name__ == '__main__':
    main()
