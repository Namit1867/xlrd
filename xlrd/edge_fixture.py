"""Fixture for the incremental-merge subtree test: deleted as a whole later."""
from enum import Enum

from .formatting import nearest_colour_index


class SheetKind(str, Enum):
    WORKSHEET = "worksheet"
    CHART = "chart"
    MACRO = "macro"


class EdgeFixture:
    """A class with methods, properties and parameters."""

    kind: SheetKind = SheetKind.WORKSHEET
    limit: int = 10

    def __init__(self, book, limit=10):
        self.book = book
        self.limit = limit

    @property
    def sheet_count(self):
        return self.book.nsheets

    def colour(self, rgb, fallback=None):
        return nearest_colour_index(self.book.colour_map, rgb) or fallback

    def describe(self, verbose=False):
        return f"{self.kind.value}:{self.sheet_count}" if verbose else self.kind.value
