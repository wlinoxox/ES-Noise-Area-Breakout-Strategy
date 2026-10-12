#!/usr/bin/env python3
"""列出模板中所有版型 (layout) 與其 placeholder idx / 類型 / 位置。

用法: python3 inspect_layouts.py [template.pptx]
"""
import sys
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu

DEFAULT = Path(__file__).resolve().parent.parent / "assets" / "template.pptx"


def cm(v):
    return f"{Emu(v).cm:.1f}"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    prs = Presentation(path)
    print(f"# {path}  ({cm(prs.slide_width)} x {cm(prs.slide_height)} cm)\n")
    for i, layout in enumerate(prs.slide_layouts):
        print(f"[{i}] {layout.name}")
        for ph in layout.placeholders:
            f = ph.placeholder_format
            print(f"    idx={f.idx:<3} {str(f.type).split('.')[-1].split(' ')[0]:<8} "
                  f"x={cm(ph.left)} y={cm(ph.top)} w={cm(ph.width)} h={cm(ph.height)}  {ph.name}")


if __name__ == "__main__":
    main()
