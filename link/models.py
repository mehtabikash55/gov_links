from django.db import models
from django.utils import timezone


class contact(models.Model):
    Name = models.CharField(max_length=30)
    Email_Id = models.EmailField()
    Phone_Number = models.CharField(max_length=10)
    Message = models.TextField()

    def __str__(self):
        return self.Name + " - " + self.Phone_Number


class gov_form(models.Model):
    Website_Title = models.CharField(max_length=150)
    Website_Link = models.CharField(max_length=100)

    def __str__(self):
        return self.Website_Title

class home_page(models.Model):
    Website_Title = models.CharField(max_length=150)
    Website_Link = models.CharField(max_length=100)

    def __str__(self):
        return self.Website_Title

class province(models.Model):
    Website_Title = models.CharField(max_length=150)
    Website_Link = models.CharField(max_length=100)

    def __str__(self):
        return self.Website_Title

class metropolitan(models.Model):
    Website_Title = models.CharField(max_length=150)
    Website_Link = models.CharField(max_length=100)

    def __str__(self):
        return self.Website_Title

class sub_metropolitan(models.Model):
    Website_Title = models.CharField(max_length=150)
    Website_Link = models.CharField(max_length=100)

    def __str__(self):
        return self.Website_Title

class municipality(models.Model):
    Website_Title = models.CharField(max_length=150)
    Website_Link = models.CharField(max_length=100)

    def __str__(self):
        return self.Website_Title

class rural_municipality(models.Model):
    Website_Title = models.CharField(max_length=150)
    Website_Link = models.CharField(max_length=100)

    def __str__(self):
        return self.Website_Title

class Social_Media_db(models.Model):
    Website_Title = models.CharField(max_length=150)
    Website_Link = models.CharField(max_length=100)

    def __str__(self):
        return self.Website_Title
