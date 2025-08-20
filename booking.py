# Base class
class Booking:
    def __init__(self, booking_id, customer_name, distance_km):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.distance_km = distance_km

    def calculate_base_fare(self):
        return self.distance_km * 2


# Derived class for Bus Booking
class BusBooking(Booking):
    def __init__(self, booking_id, customer_name, distance_km, seat_type):
        super().__init__(booking_id, customer_name, distance_km)
        self.seat_type = seat_type

    def calculate_fare(self):
        fare = self.calculate_base_fare()

        if self.seat_type.lower() == "sleeper":
            fare += fare * 0.10  # add 10%

        if self.distance_km > 100:
            fare += (self.distance_km * 0.5)  # Rs 0.5 per km

        return round(fare, 2)


# Derived class for Train Booking
class TrainBooking(Booking):
    def __init__(self, booking_id, customer_name, distance_km, class_type):
        super().__init__(booking_id, customer_name, distance_km)
        self.class_type = class_type

    def calculate_fare(self):
        fare = self.calculate_base_fare()

        if self.class_type.lower() == "first":
            fare += fare * 0.20  # add 20%
        elif self.class_type.lower() == "ac":
            fare += fare * 0.50  # add 50%

        if self.distance_km > 200:
            fare -= fare * 0.10  # deduct 10%

        return round(fare, 2)


# Example usage
if __name__ == "__main__":
    # Example inputs
    bus_booking = BusBooking("B001", "Alice", 120, "Sleeper")
    train_booking = TrainBooking("T001", "Bob", 250, "AC")

    print(f"Bus Booking Fare: {bus_booking.calculate_fare():.2f}")
    print(f"Train Booking Fare: {train_booking.calculate_fare():.2f}")