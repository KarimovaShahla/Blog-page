from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    def __str__(self) -> str:
        return f"{self.name}"


class Advertisements(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(max_length=3000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    image_1 = models.ImageField(upload_to="uploads/advertisements/images/%Y/%m/%d/", null=True, blank=True)
    image_2 = models.ImageField(upload_to="uploads/advertisements/images/%Y/%m/%d/", null=True, blank=True)
    image_3 = models.ImageField(upload_to="uploads/advertisements/images/%Y/%m/%d/", null=True, blank=True)


    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"


    def __str__(self) -> str:
        return f"{self.title}"
    

    def get_thumbnail_image_url(self) -> str:
        #image_url = self.images.first()
        if self.image_1:
            return self.image_1.url
        return ""
    

class PostImage(models.Model):
    post = models.ForeignKey(Advertisements, on_delete=models.CASCADE, related_name="images")
    img = models.ImageField(upload_to="post_images/%Y/%m/%d/")
    order = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Post Image"
        verbose_name_plural = "Post Images"

    def __str__(self):
        return f"{self.post.title}"
    
from django.db import models

from django.db import models

class SocialMedia(models.Model):
    platform = models.CharField(max_length=100)  
    likes = models.IntegerField()  
    image1 = models.ImageField(upload_to="uploads/platform/images/%Y/%m/%d/", null=True, blank=True)  
    image2 = models.ImageField(upload_to="uploads/platform/images/%Y/%m/%d/", null=True, blank=True) 
    link = models.CharField(max_length=256, null=True, blank=True) 

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Medias"

    def __str__(self):
        return f"{self.platform}"
