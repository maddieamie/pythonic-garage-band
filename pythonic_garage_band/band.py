from abc import ABC, abstractmethod


class Musician(ABC):

    def __init__(self, name):
        self.name = name
        self.instrument = None
        self.solo = None

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    def __init__(self, name, instrument="guitar", solo="face melting guitar solo"):
        super().__init__(name)
        self.instrument = instrument
        self.solo = solo

    def play_solo(self):
        return self.solo

    def get_instrument(self):
        return self.instrument


class Bassist(Musician):
    def __init__(self, name, instrument="bass", solo="bom bom buh bom"):
        super().__init__(name)
        self.instrument = instrument
        self.solo = solo

    def play_solo(self):
        return self.solo

    def get_instrument(self):
        return self.instrument


class Drummer(Musician):
    def __init__(self, name, instrument="drums", solo="rattle boom crash"):
        super().__init__(name)
        self.instrument = instrument
        self.solo = solo

    def play_solo(self):
        return self.solo

    def get_instrument(self):
        return self.instrument


class Band:
    instances = []

    def __init__(self, name="Band", members=[]):
        self.name = name
        self.members = members
        self.instruments = [member.instrument for member in self.members]
        self.solos = [member.solo for member in self.members]
        Band.instances.append(self)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Name: {self.name}, Members: {self.members}, Instruments: {self.instruments}, Solos: {self.solos}"

    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(self):
        return self.solos


if __name__ == '__main__':
    guitarist1 = Guitarist("Dwayne Beckson")
    bassist1 = Bassist("Hot Girl")
    drummer1 = Drummer("Dream Boat")
    print(guitarist1)
    print(guitarist1.name)
    print(guitarist1.get_instrument())
    print(guitarist1.instrument)
    print(guitarist1.solo)
    print(guitarist1.play_solo())
    print(guitarist1.__str__())
    print(guitarist1.__repr__())

    band1 = Band(name="Lesbeans", members=[guitarist1, bassist1, drummer1])
    print(band1)
    print(band1.solos)
    print(band1.play_solos())
    print(band1.instruments)
    print(band1.members)
    print(band1.__str__())
    print(band1.__repr__())
    # print(jedi1.attacking())
