from sys import argv, exit
from pathlib import Path
from colorama import Fore

def print_dir(path: Path, prefix: int = 0):
    is_dir = path.is_dir()

    print("\t" * prefix + (Fore.BLUE if is_dir else Fore.GREEN) + path.name)

    if not is_dir:
        return

    for path in path.iterdir():
        print_dir(path, prefix + 1)

directory = Path("../..")

def main() -> None:
    if len(argv) != 2:
        print('Usage: python ./task3 <path-to-dir>')

        # invalid program usage
        exit(1)

    print_dir(Path(argv[1]).absolute())

if __name__ == "__main__":
    main()