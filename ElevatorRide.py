"""Elevator Ride Class"""

from BadInput import BadInput
from NoTravel import NoTravelError


class ElevatorRide(object):
    """Class for elevator rides"""
    def __init__(self, elevator_input):
        self.inp = elevator_input.split(':')
        self.starting_floor = int(self.inp[0])

    def rider_split(self):
        """Splits the riders up and checks for bad characters"""
        riders = []

        if self.inp[1]:
            for item in self.inp[1].split(','):
                r = item.split('-')
                try:
                    riders.append((int(r[0]), int(r[1])))
                except:
                    raise BadInput
        return riders

    def floor_traversal(self, ride_mode):
        """Function used to travel through a building

        args:
            ride_mode(char): letter determining method of travel

        return:
            the list of floors travelled to and the total distance in parenthesis
        """
        riders = self.rider_split()
        answer_list = [self.starting_floor]

        for item in riders:
            if item[0] == item[1]:
                raise NoTravelError

        if ride_mode == 'A':
            for item in riders:
                answer_list.append(item[0])
                answer_list.append(item[1])

            return self.list_format(answer_list)

        elif ride_mode == 'B':
            i = 0
            while i < len(riders):
                if riders[i][0] > riders[i][1]:
                    for floor in self.elevator_down(riders, i):
                        answer_list.append(floor)
                else:
                    for floor in self.elevator_up(riders, i):
                        answer_list.append(floor)
                i = (len(answer_list)-1)/2
            return self.list_format(answer_list)

    @staticmethod
    def elevator_down(riders, n):
        """Function for going down the building

        args:
            riders(list): tuples of rider's current floor and destination
            n(int): placeholder in rider list

        return:
            a sorted group of floors travelling down
        """
        group = []
        while n < len(riders) and riders[n][0] > riders[n][1]:
            group.append(riders[n][0])
            group.append(riders[n][1])
            n += 1
        return sorted(group)[::-1]

    @staticmethod
    def elevator_up(riders, n):
        """Function for going up the building

        args:
            riders(list): tuples of rider's current floor and destination
            n(int): placeholder in rider list

        return:
            a sorted group of floors travelling up
        """
        group = []
        while n < len(riders) and riders[n][0] < riders[n][1]:
            group.append(riders[n][0])
            group.append(riders[n][1])
            n += 1
        return sorted(group)

    @staticmethod
    def list_format(answer_list_dupe):
        """Formats list for results

        args:
            answer_list_dupes(list): a list of floors with possible duplicates

        return:
            a formatted list with no duplicates
        """
        results = []
        distance = 0
        answer_list = [answer_list_dupe[0]]

        for i in range(1, len(answer_list_dupe)):
            if answer_list_dupe[i] != answer_list_dupe[i-1]:
                answer_list.append(answer_list_dupe[i])

        for item in answer_list:
            results.append(str(item))

        for i in range(len(answer_list)-1):
            if answer_list[i] > answer_list[i+1]:
                distance += (answer_list[i] - answer_list[i+1])
            else:
                distance += (answer_list[i+1] - answer_list[i])

        distance_str = ''.join(['(', str(distance), ')'])
        results.append(distance_str)

        return ' '.join(results)
