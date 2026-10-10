#!/usr/bin/env python3
"""Rebuild docs/demo.gif (needs Pillow: pip install pillow).

docs/demo.tape is the same demo for charmbracelet/vhs.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import termgif as t  # noqa: E402

DICTATED = ("hey can you deploy the pine cone shop checkout fix no wait\n"
            "      dont push yet just commit it and uh bump the version to one point four oh")


def main():
    term = t.Term(cols=88, rows=19, size=17, title="demo: say-it-badly")
    steps = [
        ("type", DICTATED),
        ("pause", 0.6),
        ("outc", [[("", t.FG)]]),
        ("outc", [[("Without the rule", t.RED)],
                  [("  Did you mean Pinecone Shop? Do you want me to push or not? "
                    "What is 'one point four oh'?", t.FG)]]),
        ("pause", 2.2),
        ("outc", [[("", t.FG)]]),
        ("outc", [[("With the rule", t.GREEN)],
                  [("  Understood as: ", t.YELLOW), ("commit the checkout fix in pinecone-shop, "
                                                       "don't push, version 1.4.0.", t.FG)],
                  [("  Committed. Version bumped to 1.4.0. Not pushed.", t.FG)]]),
        ("pause", 1.5),
    ]
    term.run(steps, prompt="you> ", type_chunk=3, type_dt=0.04)
    term.save(HERE / "demo.gif")


if __name__ == "__main__":
    main()
