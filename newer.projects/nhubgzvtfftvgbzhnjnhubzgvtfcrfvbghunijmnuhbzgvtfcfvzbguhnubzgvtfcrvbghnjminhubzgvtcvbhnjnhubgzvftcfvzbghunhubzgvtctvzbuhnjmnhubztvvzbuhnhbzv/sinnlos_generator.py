

import os
import sys
import time


OUTPUT_FILE = "sinnlos_anzahl_der_zeilen.py"

HEADER = '''def do_nothing(value):
    return value

'''


def completely_unnecessary_block(number):
    return f'''def completely_unnecessary_{number}(value):
    # this function exists for absolutely no reason ({number})
    result = value
    result = result
    return result


'''


def get_key():
    """Read one key without requiring the user to press Enter."""
    if os.name == "nt":
        import msvcrt

        while True:
            if msvcrt.kbhit():
                return msvcrt.getwch().lower()
            time.sleep(0.01)

    # Linux / macOS
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


def generate():
    print()
    print("🌸 sinnlos generator 🌸")
    print()
    print(f"output: {OUTPUT_FILE}")
    print()
    print("press [s] to start")
    print("press [q] to quit")
    print()

    # Wait for the initial command.
    while True:
        key = get_key()

        if key == "s":
            break

        if key == "q":
            print("okay bye ♡")
            return

    print()
    print("starting...")
    print("press [q] to stop")
    print()

    number = 1
    total_lines = len(HEADER.splitlines())

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        # This is written immediately after pressing s.
        file.write(HEADER)
        file.flush()

        while True:
            # Write one completely unnecessary function.
            block = completely_unnecessary_block(number)
            file.write(block)
            file.flush()

            total_lines += len(block.splitlines())
            number += 1

            # Update the terminal without spamming thousands of lines.
            if number % 100 == 0:
                print(
                    f"\rlines: {total_lines:,} | "
                    f"functions: {number - 1:,} | "
                    f"press [q] to stop",
                    end="",
                    flush=True,
                )

            # q ends the generation.
            key = key_was_pressed()

            if key == "q":
                break

    # IMPORTANT:
    # The generated file only gets its final UwU after q.
    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write('print("UwU")\n')

    total_lines += 1

    print()
    print()
    print("♡ stopped ♡")
    print(f"created: {OUTPUT_FILE}")
    print(f"lines: {total_lines:,}")
    print(f"functions: {number - 1:,}")
    print()
    print("the final line is:")
    print('print("UwU")')


def main():
    try:
        generate()
    except KeyboardInterrupt:
        print()
        print()
        print("stopped with Ctrl+C ♡")


if __name__ == "__main__":
    main()

