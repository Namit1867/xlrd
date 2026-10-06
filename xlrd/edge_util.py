"""Helpers added on the edge-test base branch."""
from .formatting import nearest_colour_index


class EdgeHelper(object):
    def __init__(self, book):
        self.book = book

    def colour_of(self, rgb):
        return nearest_colour_index(self.book.colour_map, rgb)

    def describe(self):
        return "book with %d sheets" % self.book.nsheets


def edge_summary(book):
    return EdgeHelper(book).describe()


def edge_old_only(book):
    return edge_summary(book).upper()
