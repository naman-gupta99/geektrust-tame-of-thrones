def read_messages_from_file(file_path):
    """
    Reads the file path specified and makes a dictionary of kindom_names and an array of messages
        sent to the kingdom

    : file_path : Absolute path to the input file
    return dictionary of messages
    """

    messages_dict = {}

    with open(file_path) as file:

        try:
            for line in file:
                line_arr = line.strip().split()
                kingdom_name = line_arr[0]
                message = " ".join(line_arr[1:])

                if not kingdom_name in messages_dict:
                    messages_dict[kingdom_name] = set()
                messages_dict[kingdom_name].add(message)
        except:
            raise RuntimeError(
                "The input file was not in the specified format." +
                " (Please refer to README.md to find the correct file format)")

    return messages_dict