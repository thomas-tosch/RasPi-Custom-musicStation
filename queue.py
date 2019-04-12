class Queue:

    def __init__(self):
        self.queue = list()

    def add(self, data):
        if data not in self.queue:
            self.queue.append(data)
            return True
        return False

    def add_first(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def remove(self, pos=None):
        if len(self.queue) > 0:
            if pos is not None:
                if pos >= self.size():
                    return False
                return self.queue.pop(pos)
            return self.queue.pop(0)
        return False

    def size(self):
        return len(self.queue)
