from django.db import models, connection


# Custom manager for AddConcert
class ConcertManager(models.Manager):
    def get_concerts_for_artist(self, artist_id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM appname_addconcert 
                WHERE artist_id = %s
            """, [artist_id])
            result_list = []
            for row in cursor.fetchall():
                p = self.model(date=row[0], time=row[1], artist_id=row[2], venue=row[3])
                result_list.append(p)
            return result_list


#Defines a Django model 'Artist' with two fields: 'name' and 'description', both limited to 100 characters. 
#The __str__ method returns the artist's name, which is used to represent the Artist instances in the Django admin and shell.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#Defines a Django model 'Concert' that represents a concert with a date, time, associated artist, and venue. 
#'artist' is a ForeignKey linking to the Artist model, with CASCADE delete behavior (deleting an artist will delete related concerts). 
#'venue' is a text field with a max length of 100 characters.        
class AddConcert(models.Model):
    date = models.DateField()
    time = models.TimeField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)

    objects = ConcertManager()  # Attach the custom manager to the AddConcert model

    class Meta:
        indexes = [
            # This is a composite index on both date and artist fields
            models.Index(fields=['date', 'artist']),
            # Additional indexes can be added here if necessary
        ]
        