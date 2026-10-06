"""Added on the ahead branch."""
from .edge_util import EdgeHelper, edge_new_only


class EdgeMore(EdgeHelper):
    def loud(self):
        return edge_new_only(self.book)
