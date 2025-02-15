from rest_framework import serializers

from lincride.rides.models import Ride


class RideSerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(max_digits=19, decimal_places=2, required=True)
    traffic_level = serializers.ChoiceField(choices=Ride.TRAFFIC_LEVEL, required=True)
    demand_level = serializers.ChoiceField(choices=Ride.DEMAND_LEVEL, required=True)
    
    class Meta:
        model = Ride
        fields = (
            'id', 'distance', 'traffic_level', 'demand_level',
            'traffic_multiplier', 'demand_multiplier', 'distance_fare',
            'total_fare'
        )       
        
        read_only_fields = [
            'traffic_multiplier', 'demand_multiplier', 'distance_fare', 'total_fare', 
            # 'time_multiplier'
        ]