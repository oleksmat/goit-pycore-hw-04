def add_command(state: dict[str, str], username, phone):
    if username in state:
        print(f"Contact for {username} already exists")
        return

    state[username] = phone

    print(f"Contact for {username} is {phone}")

add = (
    ['add'],
    2,
    ' -- add <name> <number>\n' +
    '    Add a contact to the contacts book.',
    add_command
)
