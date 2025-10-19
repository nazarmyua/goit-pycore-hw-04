from colorama import Fore
import sys
from pathlib import Path


def display_structure(base_path: Path, level: int = 0):

    for item in sorted(base_path.iterdir()):
        if item.is_file():
            print("   " * level + Fore.YELLOW + f"{item.name}")
        else:
            print("   " * level + Fore.BLUE + f"{item.name}/")
            display_structure(item, level=level + 1)


def main():
    if len(sys.argv) < 2:
        return

    base_path = Path(sys.argv[1])

    if not base_path.exists():
        print(Fore.RED + f"Path doesn't exist: {base_path}")
        return

    if not base_path.is_dir():
        print(Fore.RED + f"Path is not a folder: {base_path}")
        return

    display_structure(base_path)


if __name__ == "__main__":
    main()
