from django.db import models
from cloudinary.models import CloudinaryField


class Cards(models.Model):
    icon = CloudinaryField("image", blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title
    
class Landing_page(models.Model):
    heading = models.CharField(max_length=255)
    background_img = CloudinaryField("image", blank=True, null=True)
    sub_title = models.CharField(max_length=255)
    card_id = models.ForeignKey(Cards, on_delete=models.CASCADE, related_name="options")
    side_img = CloudinaryField("image", blank=True, null=True)

    def __str__(self):
        return self.heading
    
class About_us(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField("image", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class CMS(models.Model):
    landing_page_id = models.ForeignKey(Landing_page, on_delete=models.CASCADE, related_name="Landing_page")
    about_us_id = models.ForeignKey(About_us, on_delete=models.CASCADE, related_name="About_us")

def __str__(self):
    return f"{self.landing_page_id} - {self.survey.about_us_id}"
