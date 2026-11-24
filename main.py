#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — entry for
u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.

Writes a single warning label (at most 120 characters) to
<output dir>/entry.txt, with no trailing newline.
"""

import os  # stdlib only: no network, no third-party deps
import stat
from pathlib import Path

LABEL = (
    "WARNING: Do not look out the window in transit. "
    "The passenger staring back is you, "
    "holding your return ticket hostage."
)

# Gate: entry.txt must be UTF-8 text of 1 to 120 characters.
MAX_LABEL_CHARS = 120
# 118 characters: the whole joke fits the gate with room to spare.
assert len(LABEL) <= MAX_LABEL_CHARS, "label exceeds the 120-character gate"
assert 1 <= len(LABEL) <= 120, f"label is {len(LABEL)} characters long"
assert LABEL.strip(), "label must not be only whitespace"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True, mode=0o755)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LABEL, encoding="utf-8", errors="strict")
    # Outputs must be readable by every user (the grader collects them
    # as another user): files 0644, folders 0755.
    os.chmod(entry_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    os.chmod(output_dir, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP
             | stat.S_IROTH | stat.S_IXOTH)


if __name__ == "__main__":
    # Deadpan notice, hostage ticket: the laugh lands on the last word.
    main()
