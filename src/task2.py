def get_cats_info(path: str) -> list[dict]:
    """
    Decodes files containing info about the cats

    Throws IOError if file could not be read, opened or decoded.

    :param path: A path to the file with salaries data
    :return: a list of dicts each containing cat's id (str), name (str) and age (int)
    """

    try:
        with open(path, 'r', encoding='utf-8') as file:
            # remove white space at the end and beginning
            lines = (line.strip() for line in file)
            # remove blank lines
            lines = [line for line in lines if line]
    except IOError as e:
        raise IOError('Failed to read cats info file') from e

    # define sub-function to handle parsing lines
    def parse_line(line: str) -> dict:
        cat_id, cat_name, cat_age = line.split(',', 3)

        try:
            return {
                "id": cat_id,
                "name": cat_name,
                "age": int(cat_age),
            }
        except ValueError as e:
            raise IOError('Failed to decode cats info from file') from e

    cats_info = [parse_line(line) for line in lines]

    return cats_info
