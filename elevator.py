"""Main Function"""

from ElevatorRide import ElevatorRide


def main():
    elevator_inp = [line.rstrip('\n') for line in open('C:/Coding/Monticello/input.txt')]
    elevator_out = open('C:/Coding/Monticello/output.txt', 'w')

    elevator_out.write("Mode A:\n")
    for item in elevator_inp:
        elevator = ElevatorRide(item)
        elevator_out.write('%s \n' % elevator.floor_traversal('A'))

    elevator_out.write("\nMode B:\n")
    for item in elevator_inp:
        elevator = ElevatorRide(item)
        elevator_out.write('%s \n' % elevator.floor_traversal('B'))

if __name__ == "__main__":
    main()
