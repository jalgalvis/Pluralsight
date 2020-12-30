class Reader:
    def __init__(self, filename):
        self._filename = filename
        self.f = open(filename, mode='rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()