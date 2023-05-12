message_back = "you backed to main menu".title()
message_wrong = "you typed wrong syntax.".title()


def read(a_filepath):
    with open(a_filepath, 'r') as file:
        to_do_list = file.readlines()
    return to_do_list


def add(a_filepath, to_do_new):
    to_do_list = read(a_filepath)
    to_do_new = to_do_new.title() + '\n'
    to_do_list.append(to_do_new)
    with open(a_filepath, 'w') as file:
        file.writelines(to_do_list)


def delete(a_filepath, to_do_to_delete):
    to_do_list = read(a_filepath)
    to_do_list.remove(to_do_to_delete)

    with open(a_filepath, 'w') as file:
        file.writelines(to_do_list)
