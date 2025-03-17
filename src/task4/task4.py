# import list of commands from commands package
# every command is exported as a tuple:
# (list_of_names>: list[str], number_of_parameters: int,
# description: str, command_routine: CommandRoutine)
#
# CommandRoutine = (contacts: dict[str,str], *args: [str])
from commands import commands

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    # storing contact information in here
    state = ({})

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command_name, *args = parse_input(user_input)

        # help command
        if command_name == 'help':
            if len(args) == 0:
                for command in commands:
                    print(command[2])
                continue
            if len(args) > 0:
                print("Invalid usage. Try `help`")

        # match a command by name
        command = next((command for command in commands if command_name in command[0]), None)

        # if no commands match, we print error message
        if command is None:
            print("Invalid command. Check `help` to list all commands")
            continue

        # get command parameters for checking arity
        _, args_num, _, command_function = command

        if len(args) != args_num:
            print(f"Invalid number of arguments. Must be {args_num}. Check `help`")

        # execute command with supplied arguments
        command_function(state, *args)

if __name__ == "__main__":
    main()
