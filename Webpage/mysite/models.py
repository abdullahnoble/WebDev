from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class info(models.Model):
    profilepic = models.FileField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='xyz')
    designation = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    education = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('mysite:profile_view', kwargs={'pk': self.pk})


