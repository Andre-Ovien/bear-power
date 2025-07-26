from django.db import models

# Create your models here.

class Home(models.Model):
    image = models.ImageField(upload_to="Home", blank=False)
    description = models.TextField(max_length=264,blank=False)

    def __str__(self):
        return self.description
    

class About(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=264, blank=False)

    def __str__(self):
        return self.title
    

class Client(models.Model):
    text = models.TextField(max_length=264,blank=False)
    name = models.CharField(max_length=30, blank=False)
    profession = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to="Client", blank=False)

    def __str__(self):
        return self.name
    

class Service(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=264,blank=False)

    def __str__(self):
        return self.name


class Features(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=264,blank=False)
    header = models.CharField(max_length=50, blank=False)
    image1 = models.ImageField(upload_to="Features", blank=False)
    image2 = models.ImageField(upload_to="Features", blank=False)
    image3 = models.ImageField(upload_to="Features", blank=False)
    header2 = models.CharField(max_length=50, blank=False)
    description2 = models.TextField(max_length=264,blank=False)
    text1 = models.CharField(max_length=100, blank=False)
    text2 = models.CharField(max_length=100, blank=False)
    text3 = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title


class Project(models.Model):
    image = models.ImageField(upload_to="Project", blank=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Team(models.Model):
    image = models.ImageField(upload_to="Team", blank=False)
    name = models.CharField(max_length=30, blank=False)
    position = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    image = models.ImageField(upload_to="Testimonial", blank=False)
    name = models.CharField(max_length=30, blank=False)
    position = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    question = models.CharField(max_length=250, blank=False)
    answer = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.question
    
class ContactForm(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=150, blank=False)
    message = models.TextField(max_length=500,blank=False)

    def __str__(self):
        return self.name


class ServiceDetail(models.Model):
    title = models.CharField(max_length=50, blank=False)
    intro = models.TextField(max_length=150, blank=False)
    image = models.ImageField(upload_to="ServiceDetails", blank=False)
    image1 = models.ImageField(upload_to="ServiceDetails", blank=False)
    image2 = models.ImageField(upload_to="ServiceDetails", blank=False)
    image3 = models.ImageField(upload_to="ServiceDetails", blank=False)

    def __str__(self):
        return self.title
    
class CTA(models.Model):
    description = models.TextField(max_length=250, blank=False)
    image = models.ImageField(upload_to="CTA", blank=False)

    def __str__(self):
        return self.description
    
class Gallery(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to="Gallery", blank=False)

    def __str__(self):
        return self.title