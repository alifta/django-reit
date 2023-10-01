from django.contrib import admin

from listings.models import (
    Property,
    Feature,
    RealEstate,
    Agent,
    Listing,
    ListingAgent,
    Offer,
)


class ListingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Property)
admin.site.register(Feature)
admin.site.register(RealEstate)
admin.site.register(Agent)
admin.site.register(Listing)
admin.site.register(ListingAgent)
admin.site.register(Offer)
