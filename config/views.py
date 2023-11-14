from django.http import HttpResponse, HttpResponseNotFound


def handler404(request, exception):
    # return HttpResponse("404: Page not found!")
    return HttpResponseNotFound(
        "404: Page not found! <br><br> <button onClick=" " href='';" "> Go to Homepage"
    )
