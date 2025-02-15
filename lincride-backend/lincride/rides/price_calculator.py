import datetime
from decimal import Decimal

from django.conf import settings


base_fare = Decimal(settings.BASE_FARE)

per_km_rate = Decimal(settings.PER_KM_RATE)
peak_start = settings.PEAK_TIME_START 
peak_end = settings.PEAK_TIME_END     

traffic_multipliers = {'low': Decimal('1.0'), 'normal': Decimal('1.2'), 'high': Decimal('1.5')}
demand_multipliers = {'normal': Decimal('1.0'), 'peak': Decimal('1.8')}


def calculate_fare(distance, traffic_level='low', demand_level='normal'):

    now = datetime.datetime.now().time()
    time_multiplier = Decimal('1.3') if peak_start <= now <= peak_end else Decimal('1.0')

    traffic_multiplier = traffic_multipliers.get(traffic_level.lower(), Decimal('1.0'))
    demand_multiplier = demand_multipliers.get(demand_level.lower(), Decimal('1.0'))

    distance_fare = Decimal(distance) * per_km_rate
    total_fare = (base_fare + distance_fare) * traffic_multiplier * demand_multiplier * time_multiplier

    return {
        'base_fare': base_fare,
        'distance': distance,
        'traffic_level': traffic_level,
        'demand_level': demand_level,
        'traffic_multiplier': traffic_multiplier,
        'demand_multiplier': demand_multiplier,
        'distance_fare': distance_fare,
        'time_multiplier': time_multiplier,
        'total_fare': total_fare.quantize(Decimal('0.00'))
    }