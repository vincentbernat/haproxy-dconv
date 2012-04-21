__all__ = [
    'arguments',
    'example',
    'keyword',
    'seealso',
    'table',
    'underline'
]


class Parser:
    def __init__(self, pctxt):
        self.pctxt = pctxt

    def parse(self, line):
        return line


class PContext:
    def __init__(self, templates):
        self.set_content("")
        self.templates = templates

    def set_content(self, content):
        self.lines = content.split("\n")
        self.nblines = len(self.lines)
        self.i = 0
        self.stop = False

    def get_lines(self):
        return self.lines

    def eat_lines(self):
        count = 0
        while self.lines[self.i].strip():
            count += 1
            self.next()
        return count

    def eat_empty_lines(self):
        count = 0
        while not self.lines[self.i].strip():
            count += 1
            self.next()
        return count

    def next(self, count=1):
        self.i += count

    def has_more_lines(self, offset=0):
        return self.i + offset < self.nblines

    def get_line(self, offset=0):
        return self.lines[self.i + offset].rstrip()


