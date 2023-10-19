from django.db import models

# Create your models here.

class ImageType(models.Model):
    ImgTypes = models.CharField(max_length=100, null=True)
    new_img = models.CharField(max_length=2,default=1)

    def __str__(self):
        return self.ImgTypes



class Imgs(models.Model):
     ID_Type = models.ForeignKey(ImageType, null=True, on_delete=models.SET_NULL)
     pic = models.ImageField(upload_to='')
     new_img = models.CharField(max_length=2, null=True,default=1)
     image_url = models.URLField(null=True, blank=True)
    