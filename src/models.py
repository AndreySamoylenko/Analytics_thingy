class User:
    user_id: int
    phone_number: int
    name: str
    is_corporate: bool


class TravelType:
    ONFOOT = "on foot"
    BICYCLE = "bicycle"
    EBIKE = "ebike"
    SCOOTER = "scooter"
    BIKE = "bike"
    CAR = "car"

class CourierStatus:
    ACTIVE = "active"
    ON_BREAK = "on break"
    FIRED = "fired"

class Courier:
    courier_id: int
    full_name: str
    travel_type: TravelType
