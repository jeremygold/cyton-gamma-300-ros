class Motor:
    def __init__(self, name, min, max, publisher):
        self.name = name
        self.min = min
        self.max = max
        self.posDelta = self.max - self.min
        self.publisher = publisher

    def percentToRaw(self, percentPos):
        rawPos = (float(percentPos) / 100.0) * self.posDelta + self.min
        return rawPos

    def rawToPercent(self, rawPos):
        percentPos = int(100.0 * (rawPos - self.min) / self.posDelta)
        return percentPos

    def setPercentPos(self, percentPos):
        rawPos = self.percentToRaw(percentPos)
        print '{}: {} ({}%)'.format(self.name, rawPos, percentPos)
        self.publisher.publish(rawPos)

    def setRawPos(self, rawPos):
        percentPos = self.rawToPercent(rawPos)
        print '{}: {} ({}%)'.format(self.name, rawPos, percentPos)
        self.publisher.publish(rawPos)



