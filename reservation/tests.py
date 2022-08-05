import datetime

from django.test import TestCase

from reservation.models import Reservation, Rental


class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        rental = Rental.objects.create(name="Rental-1")
        cls.sample_data = {
            "rental_name": rental,
            "rental_id": 'res-1 ID',
            "checkin": datetime.datetime.now() - datetime.timedelta(days=100),
            "checkout": datetime.datetime.now() - datetime.timedelta(days=80),
        }
        Reservation.objects.create(**cls.sample_data)
        # modify checkin data and entry new reservation
        cls.sample_data = {
            "rental_name": rental,
            "rental_id": 'res-2 ID',
            "checkin": datetime.datetime.now() - datetime.timedelta(days=30),
            "checkout": datetime.datetime.now() - datetime.timedelta(days=10),
        }
        Reservation.objects.create(**cls.sample_data)

    def test_check_previous_rental_id(self):
        reservations = Reservation.objects.all()
        self.assertNotEqual(reservations[0].rental_id, reservations[1].rental_id)
        self.assertEqual(reservations[0].rental_id, reservations[1].previous_rental_id)
        self.assertGreater(reservations[1].checkin, reservations[0].checkin)

    def test_check_previous_rental_id_for_current(self):
        reservations = Reservation.objects.all()
        self.assertEqual(reservations[0].previous_rental_id, None)
