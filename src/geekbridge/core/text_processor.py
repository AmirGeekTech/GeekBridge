from __future__ import annotations

from arabic_reshaper import ArabicReshaper
from bidi.algorithm import get_display

from .models import Direction, TransformOptions, TransformResult


class PersianTextProcessor:
    """Prepare Persian/Arabic text for legacy renderers.

    Shape-only mode preserves logical character order. BiDi visual-order
    conversion is optional because many target editors already apply RTL.
    """

    def transform(self, text: str, options: TransformOptions | None = None) -> TransformResult:
        options = options or TransformOptions()
        if not text:
            return TransformResult(text, text, False)

        reshaper = ArabicReshaper(configuration={
            "delete_harakat": not options.preserve_harakat,
            "support_ligatures": True,
            "shift_harakat_position": False,
            "delete_tatweel": options.delete_tatweel,
        })
        base_dir = {Direction.RTL: "R", Direction.LTR: "L", Direction.AUTO: None}[options.direction]
        output_lines = []
        warnings = []
        for line in text.splitlines(keepends=True):
            body = line.rstrip("\r\n")
            ending = line[len(body):]
            if not body:
                output_lines.append(ending)
                continue
            shaped = reshaper.reshape(body) if options.reshape_arabic else body
            if options.reorder_bidi:
                try:
                    shaped = get_display(shaped, base_dir=base_dir)
                except Exception as exc:
                    warnings.append(f"BiDi reorder skipped: {exc}")
            output_lines.append(shaped + ending)
        result = "".join(output_lines)
        return TransformResult(text, result, result != text, tuple(warnings))
