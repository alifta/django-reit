from django.shortcuts import render
from django.views.generic import ListView

from listings.models import Listing, Agent


def listing_index(request):
    listings = Listing.objects.all()
    context = {"listings": listings}
    return render(request, "listings/listing_index.html", context)


def listing_detail(request, pk):
    listing = Listing.objects.get(pk=pk)
    context = {"listing": listing}
    return render(request, "listings/listing_detail.html", context)


class AgentListView(ListView):
    model = Agent
    template_name = "listings/agent_list.html"

    def get_queryset(self):
        return Agent.objects.filter(real_estate_id=self.kwargs["real_estate_id"])

    def get_context_data(self):
        context = super().get_context_data()
        agent = context["object"]
        real_estates = agent.real_estates.all()
        context["real_estates"] = real_estates

        # Example from RealPython "https://realpython.com/django-user-management"
        # context["real_estates"] = Agent.objects.get(id=self.kwargs["agent_id"])

        return context
