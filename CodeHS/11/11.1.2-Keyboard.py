import sys
import termios
import tty

class KeyListener:
    def __init__(self):
        if sys.platform.startswith("linux") or sys.platform == "darwin":  # Linux/macOS
            self._get_key = self._unix_get_key
        else:
            raise NotImplementedError("Unsupported platform: This only works on Linux/macOS.")

    def _unix_get_key(self):
        """Reads a single keystroke (non-blocking) on Unix-like systems."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key  # Return as a normal string

    def get_key(self):
        """Returns a single keypress as a string."""
        return self._get_key()

# Example usage
if __name__ == "__main__":
    listener = KeyListener()
    print("Press keys (Press 'w' to exit)...")

    while True:
        key = listener.get_key()
        if key:
            print(f"Key pressed: {key}")
            if key == 'w':  # Check for 'w' key
                print("Exiting...")
                break
