def watch():
    with open('To Do List.txt', 'r') as file:
        to_do_list = file.readlines()
    print('\n\n')
    for item in to_do_list:
        i = to_do_list.index(item) + 1
        line = f"{i}. {item}".replace('\n', '')
        print(line)
    print('\n\n')
    return to_do_list


def delete(to_do_list):
    number_deleted = int(input("type the number that you want to"
                               " delete from above and"
                               " press enter: ".title()))
    number_deleted = number_deleted - 1
    del to_do_list[number_deleted]

    with open('To Do List.txt', 'w') as file:
        file.writelines(to_do_list)


def add(to_do_list):
    to_do_new = input("type new work to do and press enter: ".title())
    to_do_new = '\n' + to_do_new
    to_do_list.append(to_do_new)
    with open('To Do List.txt', 'w') as file:
        file.writelines(to_do_list)


def edit(to_do_list):
    edited = input("type the number that you want to"
                   " edit from above and"
                   " new work to do instead of it"
                   " and press enter: ".title())
    number_edited = int(edited[0:1])
    to_do_edited = edited[3:]
#    print(f"{number_edited}. {to_do_edited}")
    to_do_list[number_edited-1] = f"{to_do_edited} \n"

    with open('To Do List.txt', 'w') as file:
        file.writelines(to_do_list)
