**Save list of packages**

```shell
python -m pip freeze > requirements.txt
```

**Reset Django Project**

1. Remove database migrations

```shell
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

2. Drop current database or delete `db.sqlite3`

**Local mail server**
To run a local mail server and testing forgot password functionality, run the following in terminal to start
a SMTP server at http://localhost:1025. It won't send any emails to actual email address but show them in terminal.

```shell
python -m smtpd -n -c DebuggingServer localhost:1025
```

# Snippet

list all table entities

```py
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)
```

Get detail of a specific entry in a table by id

```py
def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)
```

Create a new entry in a table

```py
def listing_create(request):
    form = ListingForm()

    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)
```

Update an entry in a table

```py
def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)
```

Delete an entry in a table

```py
def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")
```
