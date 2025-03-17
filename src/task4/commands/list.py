def list_command(state: dict[str, str]):
    if len(dict):
        print("No contacts yet")

    for username in state.keys():
        print(f" -- '{username}' - {state[username]}")

list = (
    ['list', 'all'],
    0,
    ' -- all\n' +
    '    View all phone contacts',
    list_command
)
