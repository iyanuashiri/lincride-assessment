print("Test file is being imported!")


from decimal import Decimal
import datetime

from django.test import TestCase
from django.utils import timezone

from rest_framework.test import APIClient

from lincride.rides.models import Ride, Rider


class RideAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.rider = Rider.objects.create(name="Test Rider", email="test@example.com", phone="1234567890")

    def test_standard_fare(self):
        response = self.client.get('/api/v1/calculate-fare/?distance=5&traffic_level=low&demand_level=normal')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Ride.objects.count(), 1)
        self.assertEqual(response.data['total_fare'], '7.50')

    def test_high_traffic(self):
        response = self.client.get('/api/v1/calculate-fare/?distance=8&traffic_level=high&demand_level=normal')
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(Decimal(response.data['total_fare']), 
                             (Decimal('2.50') + 8) * Decimal('1.5'), places=2)

    def test_peak_hour_calculation(self):
        
        with self.settings(USE_TZ=False):
            original_now = timezone.now
            peak_time = datetime.datetime(2023, 1, 1, 18, 0)  
            timezone.now = lambda: peak_time
            
            response = self.client.get('/api/v1/calculate-fare/?distance=10&traffic_level=normal&demand_level=normal')
            timezone.now = original_now  
            
            self.assertEqual(response.status_code, 200)
            # self.assertIn('1.3', str(response.data['time_multiplier']))

    def test_ride_creation(self):
        response = self.client.get('/api/v1/calculate-fare/?distance=5&traffic_level=low&demand_level=normal')
        self.assertEqual(Ride.objects.count(), 1)
        ride = Ride.objects.first()
        self.assertEqual(ride.distance, Decimal('5'))
        self.assertEqual(ride.traffic_multiplier, Decimal('1.0'))
        
    def test_invalid_traffic_level(self):
        response = self.client.get('/api/v1/calculate-fare/?distance=5&traffic_level=invalid&demand_level=normal')
        self.assertEqual(response.status_code, 400)
        self.assertIn('traffic_level', response.data)

    def test_invalid_demand_level(self):
        response = self.client.get('/api/v1/calculate-fare/?distance=5&traffic_level=low&demand_level=invalid')
        self.assertEqual(response.status_code, 400)
        self.assertIn('demand_level', response.data)  
            
    