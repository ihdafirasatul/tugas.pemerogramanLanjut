from datetime import datetime, timedelta

def culture_cash(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")

class Parking:
    def __init__(self, user_name, vehicle_type):
        self.user_name = user_name
        self.vehicle_type = vehicle_type
        self.start_time = datetime.now()
        self.end_time = None
        self.cost = 0

    def end_parking(self):
        self.end_time = datetime.now()
        self.calculate_cost()

    def calculate_cost(self):
        duration = self.end_time - self.start_time
        hours = duration.total_seconds() // 3600 + (1 if duration.total_seconds() % 3600 > 0 else 0)
        if self.vehicle_type.lower() == "mobil":
            rate = 5000
        elif self.vehicle_type.lower() == "sepeda motor":
            rate = 2000
        else:
            rate = 1000

        self.cost = rate * hours

    def get_parking_info(self):
        return {
            "Nama pengguna": self.user_name,
            "Jenis kendaraan": self.vehicle_type,
            "Waktu awal": self.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            "Waktu akhir": self.end_time.strftime('%Y-%m-%d %H:%M:%S') if self.end_time else None,
            "Biaya parkir": culture_cash(self.cost)
        }
