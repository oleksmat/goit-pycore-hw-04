def delete_command(state: dict[str, str], username):
    if not (username in state):
        print(f"Contact for {username} does not exist")
        return

    del state[username]

    print(f"Contact for {username} is deleted")

delete = (
    ['delete'],
    1,
    ' -- delete <username>\n' +
    '    Delete phone contact of <username>.',
    delete_command
)
