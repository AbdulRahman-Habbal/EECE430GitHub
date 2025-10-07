from django.db import models

class Video(models.Model):
    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=100, blank=True)
    Actor2Name = models.CharField(max_length=100, blank=True)
    DirectorName = models.CharField(max_length=100, blank=True)

    GENRE_CHOICES = [
        ('Comedy','Comedy'), ('Romance','Romance'), ('Action','Action'),
        ('Drama','Drama'), ('Sci-Fi','Sci-Fi'), ('Horror','Horror'),
        ('Documentary','Documentary'),
    ]
    MovieGenre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='Action')
    ReleaseYear = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
