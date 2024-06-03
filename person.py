class Brain:
    def __init__(self, usage):
        self.usage = usage

    @property
    def state(self):
        return "tired" if self.usage > 90 else "rested"


class Heart:
    def __init__(self, usage):
        self.usage = usage

    @property
    def state(self):
        return "high blood pressure" if self.usage > 70 else "feeling good"


class Person:
    def __init__(self, name, age, heart_usage, brain_usage):
        self.name = name
        self.age = age
        self.heart = Heart(heart_usage)
        self.brain = Brain(brain_usage)


class Leg:
    def __init__(self, person, moving_speed):
        self.person = person
        self.moving_speed = moving_speed

    @property
    def state(self):
        if self.moving_speed > 10:
            return "running"
        elif self.moving_speed > 0:
            return "walking"
        else:
            return "standing"


person = Person(name="Gvantsa", age=26, heart_usage=87, brain_usage=100)
leg = Leg(person=person, moving_speed=12)

print(f"{person.name}'s heart state: {person.heart.state}")
print(f"{person.name}'s brain state: {person.brain.state}")
print(f"Leg state: {leg.state}")
