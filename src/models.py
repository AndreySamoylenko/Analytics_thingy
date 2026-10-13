class User:
    id: int
    name: str
    phone_number: int
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
    id: int
    name: str
    travel_type: TravelType
    staus: CourierStatus
