__author__ = 'Gaurav'

class hash_entry(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next


class hash_table(object):
    def __init__(self, size_hash_table):
        self.size_of_hash_table = size_hash_table
        self.table = [None for x in range(self.size_of_hash_table)]

    def set(self, key, value):
        """
		set value for given key
        """
        hash = key % 10
        if self.table[hash] is None:
            self.table[hash] = hash_entry(key, value)
        else:
            entry = self.table[hash]
            while entry is not None and entry.get_key() != key:
                previous = entry
                entry = entry.next
            if entry is None:
                new_entry = hash_entry(key, value)
                previous.next = new_entry
            else:
                entry.set_value(value)

    def get(self, key):
	"""
	given key, returns value
	"""
        hash = key % 10
        if self.table[hash] is None:
            return -1
        else:
            entry = self.table[hash]
            while entry is not None and entry.get_key() != key:
                entry = entry.next
            if entry is None:
                return -1
            else:
                return entry.get_value()

def main():
    custom_hash_table = hash_table(10)
    for x in range(31):
        custom_hash_table.set(x, x+2)
    for x in range(31):
        print custom_hash_table.get(x)
if __name__ == "__main__":
    main()