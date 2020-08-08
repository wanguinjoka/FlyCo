from django.shortcuts import render
from django.http import HttpResponse

listing = [
    {
        'author': 'JCrew',
        'title': 'Dine with Crew',
        'description': 'Get to see Summer collection',
        'date_of_event': 'Sept 20,2020'

    },
    {
        'author': 'Mobis',
        'title': 'car crunch',
        'description': 'mud to dust',
        'date_of_event': 'Aug 20,2020'

    },
    {
        'author': 'lolu',
        'title': 'sing user heart out',
        'description': 'kareoki night',
        'date_of_event': 'Aug 14,2020'

    },
]

# Create your views here.
def home(request):
    context ={
        'listing': listing
    }
    return render(request, 'event/home.html', context)

def about(request):
    return render(request,'event/about.html', {'title': 'About'})