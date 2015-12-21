class Crawler:
    def __init__(self):
        self.name="Base"
        self.status="OK"
        self.sadsa="SAdsa"
        print self.name
    def fetch(self):
        raise NotImplementedError()
