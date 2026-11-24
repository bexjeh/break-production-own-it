"""Break Production, Own It — one brutally honest line, printed the instant
an AI agent breaks production."""

import os

LINE = "Rollback failed: the backup was in the database I just dropped."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    # Write exact UTF-8 bytes: no trailing newline, no platform encoding drift.
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
