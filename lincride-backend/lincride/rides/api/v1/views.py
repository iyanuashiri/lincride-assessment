from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from lincride.rides.price_calculator import calculate_fare
from lincride.rides.models import Ride, Rider
from lincride.rides.api.v1.serializers import RideSerializer


class CalculateFareAPIView(APIView):
    def get(self, request):
        serializer = RideSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            distance = Decimal(request.query_params['distance'])
            if distance <= 0:
                return Response({'error': 'Distance must be positive'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error': 'Invalid distance value'}, status=status.HTTP_400_BAD_REQUEST)

        traffic_level = request.query_params.get('traffic_level')
        demand_level = request.query_params.get('demand_level')
        
        fare_details = calculate_fare(distance, traffic_level, demand_level)
        
        # Create and save Ride instance
        ride = Ride.objects.create(
            distance=distance,
            traffic_level=traffic_level,
            demand_level=demand_level,
            traffic_multiplier=fare_details['traffic_multiplier'],
            demand_multiplier=fare_details['demand_multiplier'],
            time_multiplier=fare_details['time_multiplier'],
            distance_fare=fare_details['distance_fare'],
            total_fare=fare_details['total_fare']
        )
        
        response_serializer = RideSerializer(ride)
        response_data = response_serializer.data
        response_data.update({
            'base_fare': fare_details['base_fare'],
            # 'time_multiplier': fare_details['time_multiplier']
        })
        
        return Response(response_data, status=status.HTTP_200_OK)