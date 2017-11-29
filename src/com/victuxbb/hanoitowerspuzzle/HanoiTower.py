class HanoiTower:
    def __init__(self, disks):
        self.origin_tower = list(reversed(range(1, disks + 1)))
        self.destination_tower = []
        self.moves = 0

    def run(self):
        print self.start(origin=self.origin_tower, aux=[], destination=self.destination_tower)
        return self.moves

    def start(self, origin, aux, destination):
        if len(origin) == 1:
            self.move(source_tower=origin, destination_tower=destination)
            return destination

        last = origin.pop(0)
        aux = self.start(origin=origin, aux=[], destination=aux)
        destination.append(last)
        self.moves += 1
        return self.start(origin=aux, aux=origin, destination=destination)

    def move(self, source_tower, destination_tower):
        value = source_tower.pop()
        destination_tower.append(value)
        self.moves += 1

