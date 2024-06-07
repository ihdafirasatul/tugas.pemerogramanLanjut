from .parking import Parking

class User:
    def __init__(self, name):
        self.name = name
        self.parking_sessions = []

    def start_parking(self, vehicle_type):
        new_parking = Parking(self.name, vehicle_type)
        self.parking_sessions.append(new_parking)
        return new_parking

    def end_parking(self):
        if self.parking_sessions:
            current_parking = self.parking_sessions[-1]
            if current_parking.end_time is None:
                current_parking.end_parking()
                return current_parking
            else:
                return "No active parking session to end"
        else:
            return "No parking session found"

    def get_parking_history(self):
        return [session.get_parking_info() for session in self.parking_sessions]
