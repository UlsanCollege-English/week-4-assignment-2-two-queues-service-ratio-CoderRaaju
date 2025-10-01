from collections import deque

class Gate:
    def __init__(self):
        # pattern: F, R, R, R repeating
        self._pattern = ["fastpass", "regular", "regular", "regular"]
        self._idx = 0
        # queues
        self._fast = deque()
        self._reg = deque()

    def arrive(self, line, person_id):
        """Add a person to the specified line."""
        if line == "fastpass":
            self._fast.append(person_id)
        elif line == "regular":
            self._reg.append(person_id)
        else:
            raise ValueError("Unknown line type")

    def serve(self):
        """Serve next person according to the repeating pattern."""
        for _ in range(len(self._pattern)):
            choice = self._pattern[self._idx]
            self._idx = (self._idx + 1) % len(self._pattern)

            if choice == "fastpass" and self._fast:
                return self._fast.popleft()
            elif choice == "regular" and self._reg:
                return self._reg.popleft()
            # else skip empty line but still move pointer

        # If both queues are empty
        raise IndexError("No one to serve")

    def peek_next_line(self):
        """Return the next line that would be served according to pattern (skip empties)."""
        idx = self._idx
        for _ in range(len(self._pattern)):
            choice = self._pattern[idx]
            idx = (idx + 1) % len(self._pattern)

            if choice == "fastpass" and self._fast:
                return "fastpass"
            elif choice == "regular" and self._reg:
                return "regular"

        return None  # both queues empty
