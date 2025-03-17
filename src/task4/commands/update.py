def update_command(state: dict[str, str], username, phone):
    if not (username in state):
        print("Username is not yet assigned a phone")
        return

    state[username] = phone

    print(f"Changed {username} to {phone}")

update = (
    ['change', 'update'],
    2,
    ' -- change <name> <number>\n' +
    '    Change a contact in the contacts book.',
    update_command
)
