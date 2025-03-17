def update_command(state: dict[str, str], username, phone):
    if not (username in state):
        return f"Contact for '{username}' does not exists"

    state[username] = phone

    return f"Changed contact for '{username}' to {phone}"

update = (
    ['change', 'update'],
    2,
    ' -- change <name> <number>\n' +
    '    Change a contact in the contacts book.',
    update_command
)
