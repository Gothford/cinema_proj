from django.db import models

class Hall(models.Model):
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.color


class Seat(models.Model):
    row_number = models.IntegerField()
    seat_number = models.IntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'Hall: {self.hall.color}, row_num: {self.row_number}, seat_num: {self.seat_number}'

class Client(models.Model):
    phone_number = models.BigIntegerField()
    email = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Film(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='poster', null=True)

    def __str__(self):
        return self.title

class Session(models.Model):
    hall = models.ManyToManyField(Hall)
    is_available = models.BooleanField(default=True)
    film = models.ManyToManyField(Film)
    date = models.DateTimeField()
    price = models.IntegerField()

    def __str__(self):
        if self.is_available:
            return f'Hall: {self.hall.color}, film: {self.film.title}, date: {self.date}, price: {self.price}'
        else:
            return 'Not Available'


class Booking(models.Model):
    ticket_id = models.IntegerField()
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    client_id = models.IntegerField()
    status_id = models.IntegerField()
    bonus_flg = models.BooleanField()
    bonus_card = models.IntegerField()
    payment_by_bonuses = models.FloatField()

    #def __str__(self):


class Bonus_card(models.Model):
    client_id = models.IntegerField()
    balance = models.FloatField()

class Ticket(models.Model):
    session_id = models.IntegerField()
    client_id = models.IntegerField()
    seat_id = models.IntegerField()
