#class Point():
    #def __init__(self, input1 , input2):
#init orders the code to do
        #self.x = input1
        #self.y = input2

#p = Point(2, 8)

#print(p.x)
#print(p.y)


class Flight():
    def __init__(self, capacity):

        self.capacity = capacity
        self.passanger = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passanger.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passanger)

flight = Flight(3)

people = ["Jake", "Hannah", "Ron", "Hen"]
for person in people:
    success = flight.add_passanger(person)
    if success:
        print(f"We added {person} to flight sucessfully")
    else:
        print(f"No available seats for {person}")