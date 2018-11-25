from django.db import models

# Create your models here.

class MemberGroup(models.Model):
    name = models.CharField(max_length=64)


class MemberAddress(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.CharField(max_length=64)
    apartment_number = models.CharField(max_length=64)

class MemberPhone(models.Model):
    name = models.CharField(max_length=64)


class MemberEmail(models.Model):
    name = models.CharField(max_length=64)


class Member(models.Model):
    nick = models.CharField(max_length=64, null=True, default="empty")
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    description = models.TextField()
    adress = models.ForeignKey(MemberAddress, null=True, on_delete=models.SET(None), related_name="member_adress")
    phone = models.ForeignKey(MemberPhone, null=True, on_delete=models.SET(None), related_name="member_phone")
    email = models.ForeignKey(MemberEmail, null=True, on_delete=models.SET(None), related_name="member_email")
    group = models.ManyToManyField(MemberGroup, related_name="member_group")

