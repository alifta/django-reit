from django.db import models


# class Ptype(models.Model):
#     class Type(models.TextChoices):
#         HOUSE = "house", "House"
#         TOWNHOUSE = "townhouse", "Townhouse"
#         BUNGALOW = "bungalow", "Bungalow"  # Small single story
#         SINGLEFAMILY = "singlefamily", "Singlefamily"  # Detached single story
#         MULTIFAMILY = "multifamily", "Multifamily"
#         MANSION = "mansion", "Mansion"
#         APARTMENT = "apartment", "Apartment"
#         CONDO = "condo", "Condo"
#         FLAT = "flat", "Flat"
#         CABIN = "cabin", "Cabin"
#         FARMHOUSE = "farmhouse", "Farmhouse"
#         RANCH = "ranch", "Ranch"
#         LAND = "land", "Land"
#         OFFICE = "office", "Office"
#         RETAIL = "retail", "Retail"
#         HOTEL = "hotel", "Hotel"
#         WAREHOUSE = "warehouse", "Warehouse"
#         OTHER = "other", "Other"

#     description = models.CharField(max_length=50, choices=Type.choices)


# class Property(models.Model):
#     title = models.CharField(max_length=100, blank=True)
#     price = models.IntegerField(null=False, blank=False)
#     address_line1 = models.CharField(max_length=150, blank=False)
#     address_line2 = models.CharField(max_length=150, blank=True)
#     address_line3 = models.CharField(max_length=150, blank=True)
#     city = models.CharField(max_length=50, blank=False)
#     region = models.CharField(max_length=50, blank=False)
#     country = models.CharField(max_length=50, blank=False)
#     property_size = models.IntegerField(null=False, blank=False)
#     block_size = models.IntegerField(null=False, blank=False)
#     bedroom = models.IntegerField(null=False, blank=False)
#     bathroom = models.IntegerField(null=False, blank=False)
#     parking = models.IntegerField(null=False, blank=False)
#     description = models.TextField(blank=True)
#     slug = models.SlugField()
#     is_active = models.BooleanField(default=True)
#     is_commercial = models.BooleanField(default=False)
#     date_added = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     # property_type = models.ForeignKey(Ptype, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.title} {self.city}"


class OfferStatus(models.Model):
    offer_description = models.CharField("description", max_length=10)
    value = models.IntegerField()


class Offer(models.Model):
    # Choices
    IN_REVIEW = "in_review"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
    CLOSED = "closed"
    OFFER_STATUS_CHOICES = (
        (IN_REVIEW, "In Review"),
        (REJECTED, "Rejected"),
        (ACCEPTED, "Accepted"),
        (CLOSED, "Closed"),
    )

    # Fields
    price = models.IntegerField()
    deposit = models.IntegerField()
    conditions = models.TextField()
    date_closing = models.DateTimeField()
    client_id = models.IntegerField()  # Foreign key
    realtor_id = models.IntegerField()  # Foreign key
    property_id = models.IntegerField()  # Foreign key
    offer_status = models.CharField(
        "status", max_length=10, choices=OFFER_STATUS_CHOICES
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_closed = models.DateTimeField(auto_now=False, auto_now_add=False)
    # Testing
    ofs = models.ForeignKey(OfferStatus, on_delete=models.CASCADE, related_name="ofss")

    # Managers
    objects = models.Manager()  # Replace objects with "offers"

    # Meta
    class Meta:
        verbose_name = "offer"
        verbose_name_plural = "offers"

    # String
    def __str__(self):
        return self.name

    # Save
    # def save(self, *args, **kwargs):
    # do_something()
    # super().save(*args, **kwargs)  # Call the original save() method
    # do_something_else()

    # Absolute URL
    # def get_absolute_url(self):
    # return reverse('offer_details', kwargs={'pk': self.id})
