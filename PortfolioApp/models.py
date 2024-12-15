from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="profile_image/")

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects_image/")
    response = models.TextField(blank=True)

    def __str__(self):
        return self.category
