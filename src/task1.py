def total_salary(path: str) -> (float, float):
    """
    Calculates total and average salary using data read from file at `path`.

    Throws IOError if file could not be read, opened or decoded.

    :param path: A path to the file with salaries data
    :return: tuple of total and average salaries of provided data.
        Returns (0, NaN) if data file is empty
    """

    try:
        with open(path, 'r', encoding='utf-8') as file:
            # remove white space at the end and beginning
            lines = (line.strip() for line in file)
            # remove blank lines
            lines = [line for line in lines if line]
    except IOError as e:
        raise IOError('Failed to read salaries file') from e

    if len(lines) == 0:
        # since average of zero items is undefined, we return nan
        return 0, float('nan')

    # define sub-function to handle parsing lines
    def parse_line(line: str) -> float:
        _, salary = line.split(',', 2)

        try:
            return float(salary)
        except ValueError as e:
            raise IOError('Failed to decode salaries from file') from e

    salaries = [parse_line(line) for line in lines]

    salaries_sum = sum(salaries)

    salaries_avg = salaries_sum / len(salaries)

    return salaries_sum, salaries_avg
