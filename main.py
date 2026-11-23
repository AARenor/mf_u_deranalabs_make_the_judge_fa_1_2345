"""Write one short text for make.fun's bounty."""

import os
import sys
from pathlib import Path

TEXT = "For three years my father called the dog by my name. The dog has been dead since 2019. I answer anyway."

assert 1 <= len(TEXT) <= 280

output_dir = Path(
    os.environ.get("MAKEFUN_OUTPUT_DIR")
    or os.environ.get("OUTPUT_DIR")
    or "/output"
)
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
print(len(TEXT), file=sys.stderr)
