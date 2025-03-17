def add_command(state: dict[str, str], username: str, phone: str) -> str:
    if username in state:
        return f"Contact for '{username}' already exists"

    state[username] = phone

    return f"Contact for '{username}' is now {phone}"

add = (
    ['add'],
    2,
    ' -- add <name> <number>\n' +
    '    Add a contact to the contacts book.',
    add_command
)
