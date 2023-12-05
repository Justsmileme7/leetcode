class MyHashMap:
    def __init__(self):
        self.map = []

    def put(self, key, value):
        for i in self.map:
            if i[0] == key:
                i.pop()
                i.append(value)
        else:
            self.map.append([key, value])
        print(self.map)

    def get(self, key):
        for i in self.map:
            if i[0] == key:
                print(i[1])
        return -1


    def remove (self, key):
        for i, value in enumerate(self.map):
            if value[0] == key:
                self.map.pop(i)
                print(self.map)



myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
myHashMap.put(3, 2)
myHashMap.put(3, 5)
myHashMap.get(3)
myHashMap.get(1)
myHashMap.remove(2)