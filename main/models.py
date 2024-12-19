from django.db import models


# Create your models here.
class Cards(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Title")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    address = models.CharField(max_length=50, verbose_name="Address")
    image = models.ImageField(
        upload_to="main_images", blank=True, null=True, verbose_name="Image"
    )
    price = models.DecimalField(
        default=0.00, max_digits=8, decimal_places=1, verbose_name="Price"
    )

    class Meta:
        db_table = "card"

    def __str__(self):
        return self.name
