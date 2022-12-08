#sarah wardlow
class Ambulance:
    """An ambulance ride"""

myAmbulance = Ambulance()

myAmbulance.priority = 1
myAmbulance.speed = 80
myAmbulance.capacity = 6



def ambulance_ride(a):
    controlled_velocity = -10(1-a.priority) + 2.37 (a.speed/10)**3.98 + 30(a.capacity + 1.2)
    return controlled_velocity

print(ambulance_ride(myAmbulance))
