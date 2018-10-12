from django.db import models



class Document(models.Model):

    link = models.CharField(max_length=200)
    documentId = models.IntegerField()
    name = models.CharField(max_length=200)
    projectId = models.IntegerField()

    def __str__(self):
        return self.link


class Company(models.Model):
    name = models.CharField(max_length=200)
    cid = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    salary = models.IntegerField()


    def __str__(self):
        return self.name


class Users(models.Model):

    user_name = models.CharField(max_length=200)
    user_id = models.IntegerField()
    password = models.CharField(max_length=200)
    cid = models.IntegerField()

    def __str__(self):
        return self.user_name


class Leads(models.Model):

    lead_name = models.CharField(max_length=200)
    lead_id = models.IntegerField()

    def __str__(self):
        return self.lead_name