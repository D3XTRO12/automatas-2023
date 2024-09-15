import os

def clear_console():
    if os.name == 'posix':  # Sistema tipo Unix (Linux, macOS)
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')