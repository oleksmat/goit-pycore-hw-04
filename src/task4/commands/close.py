def close_command(_: any):
    exit(0)

close = (
    ['close', 'exit'],
    0,
    ' -- close\n' +
    '    Closes the program',
    close_command
)
