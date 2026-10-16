"""A vendored compatibility helper."""


def text_type(value):
    return str(value)


class Compat:
    def ensure_text(self, value):
        return text_type(value)
