class Car:
    def send_be_bep(self):
        return 'bep-bep'


class Svetofor:
    def get_be_bep(self, signal):
        return 'hello'


c = Car()
s = Svetofor()

bep = c.send_be_bep()
h = s.get_be_bep(bep)
print(h)