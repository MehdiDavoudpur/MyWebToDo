message_back = "you backed to main menu".title()
message_wrong = "you typed wrong syntax.".title()


def read():
    with open('To Do List.txt', 'r') as file:
        to_do_list = file.readlines()
    return to_do_list


'''def watch():
    with open('To Do List.txt', 'r') as file:
        to_do_list = file.readlines()
    print('\n\n')
    for item in to_do_list:
        i = to_do_list.index(item) + 1
        line = f"{i}. {item}".replace('\n', '')
        print(line)
    print('\n\n') '''


def add(to_do_new):

    to_do_list = read()
    to_do_new = '\n' + to_do_new.title()
    to_do_list.append(to_do_new)
    with open('To Do List.txt', 'w') as file:
        file.writelines(to_do_list)


def delete(to_do_to_delete):
    to_do_list = read()
    to_do_list.remove(to_do_to_delete)

    with open('To Do List.txt', 'w') as file:
        file.writelines(to_do_list)



def edit(to_do_list):
    try:
        edited = input("type the number that you want to"
                       " edit from above and"
                       " new work to do instead of it"
                       " and press enter: "
                       "\nfor back to main menu enter 0: ".title())
        if edited == '0':
            print(message_back)
        else:
            number_edited = int(edited[0:1])
            to_do_edited = edited[3:].title()
            to_do_list[number_edited - 1] = f"{to_do_edited} \n"

            with open('To Do List.txt', 'w') as file:
                file.writelines(to_do_list)
    except ValueError:
        print(message_wrong)
        edit(to_do_list)
