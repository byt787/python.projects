import os
import sys
import time

OUTPUT_PREFIX = "sinnlos"
TEMP_OUTPUT_FILE = "sinnlos_temp.py"
DEFAULT_FINAL_TEXT = "UwU"
HEADER = """def do_nothing(value):
    return value

"""


def completely_unnecessary_block(number):
    return f"""def completely_unnecessary_{number}(value):
    # this function exists for absolutely no reason ({number})
    result = value
    result = result
    return result


"""


def get_key():
    """Read one key without requiring the user to press Enter."""
    if os.name == "nt":
        import msvcrt

        while True:
            if msvcrt.kbhit():
                return msvcrt.getwch().lower()
            time.sleep(0.01)

    import select
    import termios
    import tty

    stdin_fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(stdin_fd)

    try:
        tty.setcbreak(stdin_fd)
        while True:
            ready, _, _ = select.select([sys.stdin], [], [], 0.01)
            if ready:
                return sys.stdin.read(1).lower()
    finally:
        termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_settings)


def key_was_pressed():
    """Check for a key press without blocking."""
    if os.name == "nt":
        import msvcrt

        if msvcrt.kbhit():
            return msvcrt.getwch().lower()

        return None

    import select
    import termios
    import tty

    stdin_fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(stdin_fd)

    try:
        tty.setcbreak(stdin_fd)
        ready, _, _ = select.select([sys.stdin], [], [], 0)
        if ready:
            return sys.stdin.read(1).lower()
        return None
    finally:
        termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_settings)


def build_final_print_line(text):
    escaped_text = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'print("{escaped_text}")\n'


def build_output_path(line_count):
    return f"{OUTPUT_PREFIX}_{line_count}_zeilen.py"


def ask_for_final_text():
    raw_value = input(f"what should be printed at the end? [{DEFAULT_FINAL_TEXT}]: ").strip()
    return raw_value or DEFAULT_FINAL_TEXT


def generate():
    print()
    print("🌸 sinnlos generator 🌸")
    print()
    print("press [s] to start")
    print("press [q] to quit")
    print()

    while True:
        key = get_key()

        if key == "s":
            break

        if key == "q":
            print("okay bye ♡")
            return

    final_text = ask_for_final_text()

    print()
    print("starting...")
    print("press [q] to stop")
    print()

    number = 1
    total_lines = len(HEADER.splitlines())

    with open(TEMP_OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(HEADER)
        file.flush()

        while True:
            block = completely_unnecessary_block(number)
            file.write(block)
            file.flush()

            total_lines += len(block.splitlines())
            number += 1

            if number % 100 == 0:
                print(
                    f"\rlines: {total_lines:,} | "
                    f"functions: {number - 1:,} | "
                    f"press [q] to stop",
                    end="",
                    flush=True,
                )

            key = key_was_pressed()
            if key == "q":
                break

    final_line = build_final_print_line(final_text)
    with open(TEMP_OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write(final_line)

    total_lines += 1
    final_output_path = build_output_path(total_lines)
    os.replace(TEMP_OUTPUT_FILE, final_output_path)

    print()
    print()
    print("♡ stopped ♡")
    print(f"created: {final_output_path}")
    print(f"lines: {total_lines:,}")
    print(f"functions: {number - 1:,}")
    print()
    print("the final line is:")
    print(final_line.rstrip())


def main():
    try:
        generate()
    except KeyboardInterrupt:
        print()
        print()
        print("stopped with Ctrl+C ♡")


if __name__ == "__main__":
    main()

