from datetime import datetime
import math


def daily_factor(at: datetime):
    """

    :param at:
    :return:
    """
    hour = at.hour + at.minute / 60.0 + at.second / 3600.0
    return math.cos(2.0 * math.pi * (hour - 18) / 24)
