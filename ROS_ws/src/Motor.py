class Motor:
    def __init__(self, name, min, max, publisher):
        self.name = name
        self.min = min
        self.max = max
        self.publisher = publisher

    def setPos(self, value):
        posDelta = self.max - self.min
        pos = (float(value) / 100.0) * posDelta + self.min
        print '{}: {} ({}%)'.format(self.name, pos, value)
        self.publisher.publish(pos)
