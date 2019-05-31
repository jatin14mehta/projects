class HashItems:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        hv = 0
        mult = 1
        for ch in key:
            hv += mult*ord(ch)
            mult += 1
        return hv % self.size

    def put(self, key, value):
        item = HashItems(key, value)
        h = self._hash(key)

        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h+1) % self.size

        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
