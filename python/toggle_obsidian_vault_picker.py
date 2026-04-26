import os
import stat
import sys

OBS_PATH = os.path.expandvars(r"%appdata%\Obsidian\obsidian.json")

def pause():
    input('Press any key to continue...')

def set_read_only(path: str) -> None:
    current_mode = os.stat(path).st_mode
    os.chmod(path, current_mode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)


def clear_read_only(path: str) -> None:
    current_mode = os.stat(path).st_mode
    os.chmod(path, current_mode | stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)


def lock_obsidian(path: str) -> None:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    replaced = content.replace('"open": true', '"open": false')

    if replaced == content:
        print("No 'open': true entries were found in the file.")
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(replaced)
        print("Replaced 'open': true with 'open': false.")

    set_read_only(path)
    print(f"Set file as read-only: {path}")


def unlock_obsidian(path: str) -> None:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")

    clear_read_only(path)
    print(f"Removed read-only attribute: {path}")


def main() -> int:
    print(" ██████╗ ██████╗ ███████╗██╗██████╗ ██╗ █████╗ ███╗   ██╗")
    print("██╔═══██╗██╔══██╗██╔════╝██║██╔══██╗██║██╔══██╗████╗  ██║")
    print("██║   ██║██████╔╝███████╗██║██║  ██║██║███████║██╔██╗ ██║")
    print("██║   ██║██╔══██╗╚════██║██║██║  ██║██║██╔══██║██║╚██╗██║")
    print("╚██████╔╝██████╔╝███████║██║██████╔╝██║██║  ██║██║ ╚████║")
    print(" ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝")
    print("       >> Obsidian Vault Picker toggle script <<")
    print()
    print("    1. Lock*  obsidian.json  (enable  Vault Picker)")
    print("    2. Unlock obsidian.json  (disable Vault Picker)")
    print()
    print(" *Note:")
    print("    >Locking also prevents Obsidian from updating the ")
    print("    >Vault List in the Vault Picker.")
    print("    >")
    print("    >The lock mechanism is performed by setting")
    print("    >obsidian.json to 'READ-ONLY' mode in properties.")
    print()

    choice = input("Choose action: ").strip()
    if choice == "1":
        lock_obsidian(OBS_PATH)
        pause()
    elif choice == "2":
        unlock_obsidian(OBS_PATH)
        pause()
    else:
        print("Invalid choice. Please run the script again and choose 1 or 2.")
        pause()
        return 1

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)
