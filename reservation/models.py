from django.db import models


# Create your models here.

class Rental(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255, unique=True)


class Reservation(models.Model):
    def __str__(self):
        return self.rental_id
    rental_name = models.ForeignKey(Rental, on_delete=models.CASCADE)
    rental_id = models.CharField(max_length=255, unique=True)
    checkin = models.DateTimeField("Check in time")
    checkout = models.DateTimeField("Check out time", null=True)

    @property
    def previous_rental_id(self):
        """Filtering reservations by rental and checkin less than
           current one to get previous reservations. And sorting to get latest previous_rental_id.

        :return: rental_id or None
        :rtype: str
        """
        reservations = Reservation.objects.filter(
            rental_name=self.rental_name,
            checkin__lt=self.checkin).exclude(rental_id=self.rental_id).order_by('-checkin')
        if len(reservations):
            return reservations[0].rental_id
        return None
