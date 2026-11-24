"""Entry for One Word for the Boss (make.fun).

Writes exactly one word describing the boss, to /output/entry.txt.
"""
import os

ENTRY = "micromanager"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
