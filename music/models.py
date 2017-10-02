from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist = models.CharField(max_length=10)
    genre = models.CharField(max_length=10)
    albumTitle = models.CharField(max_length=10)
    logo = models.FileField()
    isFavorite = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.id})
    def __str__(self):
        return "an album "+self.albumTitle

class Song(models.Model):
    fileType = models.CharField(max_length=5)
    songTitle = models.CharField(max_length=15)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    isFavorite = models.BooleanField(default=False)
    def __str__(self):
        return self.songTitle