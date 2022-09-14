class Person:
    def __init__(self, name):
        self.name = name

class Party:
    def __init__(self):
        self.peple = []

    def invite(self, person):
        self.peple.append(person)

    def name_of_attendees(self):
        return ", ".join([person.name for person in self.peple])

    def number_of_guests(self):
        return len(self.peple)
party = Party()

while True:
    command = input()
    if command == "End":
        break

    name = command
    person = Person(name)
    party.invite(person)

print(f"Going: {party.name_of_attendees()}")
print(f"Total: {party.number_of_guests()}")
