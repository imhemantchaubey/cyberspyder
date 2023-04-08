from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Phone_accounts_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    truecaller = models.TextField()
    phone_no = models.CharField(max_length=10)
    base = models.TextField(null=True)
    facebook = models.BooleanField(null=True)
    google = models.TextField(null=True)
    twitter = models.BooleanField(null=True)
    instagram = models.BooleanField(null=True)
    yahoo = models.BooleanField(null=True)
    microsoft = models.BooleanField(null=True)
    snapchat = models.BooleanField(null=True)
    skype = models.TextField(null=True)
    whatsapp = models.TextField(null=True)
    telegram = models.TextField(null=True)
    viber = models.TextField(null=True)
    Kakao = models.BooleanField(null=True)
    ok = models.BooleanField(null=True)
    zalo = models.BooleanField(null=True)
    line = models.BooleanField(null=True)
    flipkart = models.BooleanField(null=True)
    bukalapak = models.BooleanField(null=True)
    jdid = models.BooleanField(null=True)

class Email_accounts_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email = models.CharField(max_length=255)
    base = models.TextField(null=True)
    apple = models.BooleanField(null=True)
    ebay = models.BooleanField(null=True)
    facebook = models.TextField(null=True)
    flickr = models.TextField(null=True)
    four_square = models.TextField(null=True)
    github = models.BooleanField(null=True)
    google = models.TextField(null=True)
    gravatar = models.TextField(null=True)
    instagram = models.TextField(null=True)
    telegram = models.BooleanField(null=True)
    lastfm = models.BooleanField(null=True)
    linkedin = models.TextField(null=True)
    microsoft = models.BooleanField(null=True)
    myspace = models.BooleanField(null=True)
    pinterest = models.BooleanField(null=True)
    skype = models.TextField(null=True)
    spotify = models.BooleanField(null=True)
    tumblr = models.BooleanField(null=True)
    twitter = models.BooleanField(null=True)
    vimeo = models.BooleanField(null=True)
    weibo = models.BooleanField(null=True)
    yahoo = models.BooleanField(null=True)
    discord = models.BooleanField(null=True)
    ok = models.TextField(null=True)
    kakao = models.BooleanField(null=True)
    booking = models.BooleanField(null=True)
    airbnb = models.TextField(null=True)
    amazon = models.BooleanField(null=True)
    qzone = models.BooleanField(null=True)
    adobe = models.BooleanField(null=True)
    mailru = models.BooleanField(null=True)
    wordpress = models.BooleanField(null=True)
    imgur = models.BooleanField(null=True)
    disneyplus = models.BooleanField(null=True)
    netflix = models.BooleanField(null=True)
    jdid = models.BooleanField(null=True)
    flipkart = models.BooleanField(null=True)
    bukalapak = models.BooleanField(null=True)
    archiveorg = models.BooleanField(null=True)
    lazda = models.BooleanField(null=True)
    zoho = models.BooleanField(null=True)
    samsung = models.BooleanField(null=True)
    evernote = models.BooleanField(null=True)
    envato = models.BooleanField(null=True)
    patreon = models.BooleanField(null=True)
    tokopedia = models.BooleanField(null=True)
    rambler = models.BooleanField(null=True)
    quora = models.BooleanField(null=True)
    atlassian = models.BooleanField(null=True)