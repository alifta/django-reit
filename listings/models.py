from django.db import models


class Feature(models.Model):
    # Fields
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # Meta
    class Meta:
        verbose_name = "feature"
        verbose_name_plural = "features"

    # String
    def __str__(self):
        return f"{self.name}"


"""
# TODO: Need an appraisal table
- Appraiser
- Employer
- Date
- Price
- Cost
    - Residential 250-400 CAD
    - Commercial 1000-2500 CAD
    - 
- Years of experience
- Credibility
"""


class Property(models.Model):
    # Fields
    title = models.CharField(max_length=100, blank=True)
    address_line1 = models.CharField(max_length=150)
    address_line2 = models.CharField(max_length=150, blank=True)
    address_line3 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    building_size = models.IntegerField()
    floor_size = models.IntegerField()
    lot_size = models.IntegerField()
    block_size = models.IntegerField(null=True, blank=True)
    bedroom_number = models.IntegerField()
    bathroom_number = models.IntegerField()
    parking_number = models.IntegerField()
    market_value = models.IntegerField()
    description = models.TextField(blank=True)
    slug = models.SlugField(null=True)
    is_commercial = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_built = models.DateField(null=True, blank=True)
    date_activated = models.DateTimeField(null=True, blank=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    features = models.ManyToManyField(
        Feature,
        help_text="Select a feature for the property",
    )

    # Choices
    PROPERTY_TYPE = (
        ("ho", "House"),
        ("th", "Townhouse"),
        ("bu", "Bungalow"),  # Small single story
        ("sf", "Singlefamily"),  # Detached single story
        ("mf", "Multifamily"),
        ("ma", "Mansion"),
        ("ap", "Apartment"),
        ("co", "Condo"),
        ("fl", "Flat"),
        ("ca", "Cabin"),
        ("fm", "Farmhouse"),
        ("ra", "Ranch"),
        ("la", "Land"),
        ("of", "Office"),
        ("re", "Retail"),
        ("ht", "Hotel"),
        ("we", "Warehouse"),
        ("ot", "Other"),
    )

    property_type = models.CharField(
        "type",
        max_length=2,
        choices=PROPERTY_TYPE,
        default="ho",
        blank=True,
        help_text="Property type",
    )

    # Meta
    class Meta:
        verbose_name = "property"
        verbose_name_plural = "properties"
        ordering = ["-date_added"]

    # String
    def __str__(self):
        return f"{self.title} | {self.city}"


class Agent(models.Model):
    # Fields
    email = models.EmailField()
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=250)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)
    phone = models.CharField(max_length=150)
    slug = models.SlugField(null=True)
    is_active = models.BooleanField(default=True)
    date_activated = models.DateTimeField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # Office/Real Estate Company - FK

    # Choices
    AGENT_TYPE = (
        ("a", "Agent"),
        ("b", "Broker"),
    )

    AGENT_SIDE = (
        ("s", "Seller"),
        ("b", "Buyer"),
    )

    agent_type = models.CharField(
        "type",
        max_length=1,
        choices=AGENT_TYPE,
        default="a",
        blank=True,
        help_text="Agent type",
    )

    agent_side = models.CharField(
        "side",
        max_length=1,
        choices=AGENT_SIDE,
        default="s",
        blank=True,
        help_text="Agent side",
    )

    # Meta
    class Meta:
        verbose_name = "agent"
        verbose_name_plural = "agents"
        ordering = ["username"]

    # String
    def __str__(self):
        return f"{self.username} | {self.email}"


class RealEstate(models.Model):
    # Fields
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # Meta
    class Meta:
        verbose_name = "real estate"
        verbose_name_plural = "real estates"

    # String
    def __str__(self):
        return f"{self.name}"


class Listing(models.Model):
    # Fields
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    days_on_market = models.IntegerField()
    slug = models.SlugField(null=True)
    is_active = models.BooleanField(default=True)
    date_activated = models.DateTimeField(null=True, blank=True)
    date_available = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="listings"
    )
    agents = models.ManyToManyField(
        Agent,
        through="ListingAgent",
        through_fields=["listing", "agent"],
        help_text="Select an agent for the listing",
    )

    # Choices
    LISTING_TYPE = (
        ("s", "Sale"),
        ("r", "Rent"),
    )
    LISTING_STATUS = (
        ("r", "Created"),
        ("a", "Active"),
        ("c", "Cancelled"),
        ("e", "Ended"),
    )

    listing_type = models.CharField(
        "type",
        max_length=1,
        choices=LISTING_TYPE,
        default="r",
        blank=True,
        help_text="Listing type",
    )

    listing_status = models.CharField(
        "status",
        max_length=1,
        choices=LISTING_STATUS,
        default="r",
        blank=True,
        help_text="Listing type",
    )

    # Meta
    class Meta:
        verbose_name = "listing"
        verbose_name_plural = "listings"
        ordering = ["-date_added"]

    # String
    def __str__(self):
        return f"{self.title} | {self.price}"


class ListingAgent(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)


class Offer(models.Model):
    # Fields
    price = models.IntegerField()
    deposit = models.IntegerField()
    conditions = models.TextField()
    date_closing = models.DateTimeField()
    client_id = models.IntegerField()  # Foreign key
    realtor_id = models.IntegerField()  # Foreign key
    property_id = models.IntegerField()  # Foreign key
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_closed = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    # Choices
    OFFER_STATUS = (
        ("ir", "In Review"),
        ("re", "Rejected"),
        ("ac", "Accepted"),
        ("cl", "Closed"),
    )

    offer_status = models.CharField(
        "status",
        max_length=2,
        choices=OFFER_STATUS,
        default="ir",
        blank=True,
        help_text="Offer status",
    )

    # Managers
    objects = models.Manager()  # Replace objects with "offers"

    # Meta
    class Meta:
        verbose_name = "offer"
        verbose_name_plural = "offers"

    # String
    def __str__(self):
        return f"{self.client_id} | {self.property_id} | {self.price}"


# class Temp(models.Model):
#     # Choices
#     CH = "choice"
#     TEMP_CHOICES = ((CH, "Choice"),)

#     # Fields
#     name = models.CharField("name", max_length=20, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)

#     # Managers
#     objects = models.Manager()  # Replace objects with "temps"

#     # Meta
#     class Meta:
#         verbose_name = "temp"
#         verbose_name_plural = "temps"

#     # String
#     def __str__(self):
#         return f"{self.name}"

#     # Save
#     def save(self, *args, **kwargs):
#         # do_something()
#         super().save(*args, **kwargs)  # Call the original save() method
#         # do_something_else()

#     # Absolute URL
#     def get_absolute_url(self):
#         return reverse('offer_details', kwargs={'pk': self.id})
