import json, os

with open("data.json", "r") as file:
    data = json.load(file)

def get_action():
    action = int(
        input(
            "What do you want to do? \n[1]: Add new birthday \n[2]: Remove Birthday \n[3]: Update Birthday \n[4]: Stops the program\n[5]: Display birthday\n[6]: Clear all data\n"
        )
    )
    while action not in {1, 2, 3, 4, 5, 6}:
        print("Invalid option")
        action = int(
            input(
                "What do you want to do? \n[1]: Add new birthday \n[2]: Remove Birthday \n[3]: Update Birthday \n[4]: Stops the program\n[5]: Display birthday\n[6]: Clear all data\n"
            )
        )
    
    print()
    if action in {1, 2, 3}:
        name = input("Name of the person \n").upper()
    else:
        name = None
    return action, name


def action1(name):
    if name not in data["names"]:

        print("Adding new user")
        user_birthday = input(f"What is {name}'s birthday? dd/mm/yyyy \n")
        data["names"][name] = {"birthday": user_birthday}
        print("Birthday added!\n")

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        start_process()

    else:
        response = input(
            "User already found, Would you like to update the birthday?\n[y]/[n]\n"
        ).lower()
        if response == "y":
            action3(name)
        if response == "n":
            response = input(
                "Would you like to remove the birthday?\n[y]/[n]:\n"
            ).lower()
            if response == "y":
                action2(name)
            else:
                get_action()


def action2(name):
    if name not in data["names"]:
        print(f"User ({name}) not found")
        action = int(
            input(
                "What do you want to do? \n[1]: Reselect Name \n[2]: Return to original action\n"
            )
        )
        if action == 1:
            name = input("Name of the person \n").upper()
            action2(name)
        elif action == 2:
            start_process()

    else:
        user_birthday = data["names"][name]
        confirm_deletion = input(
            f"Are you sure you want to delete '{name}': {user_birthday}?\n[y]/[n]:\n"
        ).lower()
        while confirm_deletion not in {"y", "n"}:
            print("invalid action")
            confirm_deletion = input(
                f"Are you sure you want to delete '{name}': {user_birthday}?\n[y]/[n]:\n"
            ).lower()
        if confirm_deletion == "y":
            del data["names"][name]
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            start_process()

        elif confirm_deletion == "n":
            action = int(
                input(
                    "What do you want to do? \n[1]: Reselct Name \n[2]: Return to orginal action"
                )
            )
            while action not in {
                1,
                2,
            }:
                print("invalid action")
                action = int(
                    input(
                        "What do you want to do? \n[1]: Reselct Name \n[2]: Return to orginal action\n"
                    )
                )
            if action == 1:
                name = input("Name of the person \n").upper()
                action2(name)
            elif action == 2:
                start_process()


def action3(name):
    if name not in data["names"]:
        print(f"({name}) User not found")
        response = input("Would you like to add the birthday?\n[y]/[n]\n")
        if response == "y":
            action1(name)
        if response == "n":
            start_process()
    else:
        change = input(f"What do you want to change {name}'s birthday to?\n")
        data["names"][name] = {"birthday": change}
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        start_process()


def action4():
    os._exit()


def action5():
    for name in data["names"]:
        birthday_date = data["names"][name]
        birthday = birthday_date["birthday"]
        print(name, birthday)

def action6():
    data["names"] = {}
    print("Data deleted!\n")
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)



def start_process():
    print()
    action, name = get_action()

    # add a birthday
    if action == 1:
        action1(name)
    # remove a birthday
    elif action == 2:
        action2(name)

    # update a birthday
    elif action == 3:
        action3(name)
    elif action == 4:
        print("Closing program...")
        action4()
    elif action == 5:
        action5()
    elif action == 6:
        confirmation = input("Are you sure you want to delete ALL birthdays?\n[y]/[n]\n")
        if confirmation == 'y':
            action6()
        else:
            start_process()

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


start_process()

