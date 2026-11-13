from dataclasses import dataclass
from enum import Enum


class Direction(str, Enum):
    AUTO = "auto"
    RTL = "rtl"
    LTR = "ltr"


@dataclass(frozen=True)
class TransformOptions:
    direction: Direction = Direction.RTL
    reshape_arabic: bool = True
    reorder_bidi: bool = False
    preserve_harakat: bool = True
    delete_tatweel: bool = False


@dataclass(frozen=True)
class TransformResult:
    source: str
    output: str
    changed: bool
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class TranslationRequest:
    text: str
    source_language: str
    target_language: str


@dataclass(frozen=True)
class TranslationResult:
    translated_text: str
    provider: str
    source_language: str
    target_language: str
