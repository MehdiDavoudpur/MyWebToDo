from pythonProject.To_Do_Functions import watch, add, delete, edit

to_do_list = []


while True:

    user_prompt = input("just type the number that you want to do from:"
                        "\n            1. watch to dos list" 
                        "\n            2. add new to do"
                        "\n            3. delete a to do"
                        "\n            4. edit a to do" 
                        "\nand press enter: ".title())

    match user_prompt:
        case '1':
            watch()

        case '2':
            to_do_list = watch()
            add(to_do_list)
            watch()
        case '3':
            to_do_list = watch()
            delete(to_do_list)
            watch()
        case '4':
            to_do_list = watch()
            edit(to_do_list)
            watch()
