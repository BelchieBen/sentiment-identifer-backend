from django.db import models
from users.models import User

class UserDataset(models.Model):
    datasetFile = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} uploaded {self.datasetFile} at {self.created_at}'