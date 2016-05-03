from unittest import TestCase
from ElevatorRide import ElevatorRide
from BadInput import BadInput
from NoTravel import NoTravelError


class ElevatorTests(TestCase):
    def testNormalFunctionalityA(self):
        ride_mode = 'A'
        elevator_input = '7:11-6,10-5,6-8,7-4,12-7,8-9'

        elevator = ElevatorRide(elevator_input)
        result = elevator.floor_traversal(ride_mode)
        self.assertEquals('7 11 6 10 5 6 8 7 4 12 7 8 9 (40)', result)

    def testNormalFunctionalityB(self):
        ride_mode = 'B'
        elevator_input = '7:11-6,10-5,6-8,7-4,12-7,8-9'

        elevator = ElevatorRide(elevator_input)
        result = elevator.floor_traversal(ride_mode)
        self.assertEquals('7 11 10 6 5 6 8 12 7 4 8 9 (30)', result)

    def testNoRiders(self):
        ride_mode = 'A'
        elevator_input = '5:'

        elevator = ElevatorRide(elevator_input)
        result = elevator.floor_traversal(ride_mode)
        self.assertEquals('5 (0)', result)

    def testBadCharacterInput(self):
        ride_mode = 'A'
        elevator_input = '5:1-5,a-4'

        elevator = ElevatorRide(elevator_input)
        with self.assertRaises(BadInput):
            elevator.floor_traversal(ride_mode)

    def testNoTravel(self):
        ride_mode = 'A'
        elevator_input = '5:1-5,3-3,2-4'

        elevator = ElevatorRide(elevator_input)
        with self.assertRaises(NoTravelError):
            elevator.floor_traversal(ride_mode)
