def read_messages_from_file(file_path):

    messages_dict = {}

    with open(file_path) as file:

        for line in file:
            line_arr = line.strip().split()
            kingdom_name = line_arr[0]
            message = " ".join(line_arr[1:])

            if not kingdom_name in messages_dict:
                messages_dict[kingdom_name] = set()
            messages_dict[kingdom_name].add(message)

    return messages_dict