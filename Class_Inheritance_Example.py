class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):

    def bark(self):
        print("Dog Barks...!")

d = Dogs()
d.bark()