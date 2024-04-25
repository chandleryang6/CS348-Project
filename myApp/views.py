from django.shortcuts import render, redirect
from .forms import ArtistForm, ConcertForm
from .models import Artist, AddConcert

#imports for delete concert button
from django.http import HttpResponseRedirect
from django.urls import reverse

#import for edit concert button
from django.shortcuts import get_object_or_404

#imports for view concerts link
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils.dateparse import parse_date

#import for transactions
from django.db import transaction


#home: Handles the display and processing of forms for adding artists and creating concerts.
#If a POST request is received, it checks for form submissions and processes them accordingly.
#After handling form submissions, it fetches all artist and concert records from the database,
#prepares the context with forms and object lists, and renders the 'home.html' template.
@transaction.atomic
def home(request):
    if request.method == 'POST':
        if 'artist_form' in request.POST:  #Check if the artist form was submitted
            artist_form = ArtistForm(request.POST)
            if artist_form.is_valid():
                artist_form.save()
                return redirect('home')  #Redirect to the homepage after adding the artist
        elif 'concert_form' in request.POST:  #Check if the concert form was submitted
            concert_form = ConcertForm(request.POST)
            if concert_form.is_valid():
                concert_form.save()
                return redirect('home')  #Redirect to the homepage after creating the concert

    artist_form = ArtistForm()
    concert_form = ConcertForm()
    artists = Artist.objects.all()  #Retrieve all artists from the database
    concerts = AddConcert.objects.all()  #Retrieve all concerts from the database

    context = {
        'artist_form': artist_form,
        'concert_form': concert_form,
        'artists': artists,
        'concerts': concerts  #Pass the concerts to the template
    }
    return render(request, 'myApp/home.html', context)


#delete_concert: Processes the deletion of a concert based on its ID. 
#If a POST request is made, it retrieves the concert by ID and deletes it from the database. 
#After deletion, it redirects to the home page.
@transaction.atomic
def delete_concert(request, concert_id):
    if request.method == 'POST':
        concert = AddConcert.objects.get(pk=concert_id)
        concert.delete()
    return HttpResponseRedirect(reverse('home'))  #Redirect to the home page or your list of concerts.


#edit_concert: Handles both displaying a form pre-filled with concert data for editing based on its ID, and processing the form submission to update the concert in the database. 
#After updating, it redirects to the home page.
@transaction.atomic
def edit_concert(request, concert_id):
    concert = get_object_or_404(AddConcert, pk=concert_id)
    if request.method == 'POST':
        form = ConcertForm(request.POST, instance=concert)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ConcertForm(instance=concert)
    return render(request, 'edit_concert.html', {'form': form})


def view_concerts(request):
    descriptions = Artist.objects.values_list('description', flat=True).distinct()

    # Start with an empty queryset
    concerts = AddConcert.objects.none()

    # Check if an artist ID was provided
    artist_id = request.GET.get('artist_id')
    if artist_id:
        try:
            artist_id = int(artist_id)  # Convert artist_id to int, make sure to handle exceptions
            concerts = AddConcert.objects.get_concerts_for_artist(artist_id)
        except ValueError:
            # Handle the exception if the conversion fails
            pass

    # If no artist_id or invalid artist_id was provided, get all concerts
    if not concerts:
        concerts = AddConcert.objects.all()

    # Filter based on the request
    if request.method == 'GET':
        description = request.GET.get('description')
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%m/%d/%Y').date()
                end_date = datetime.strptime(end_date_str, '%m/%d/%Y').date()
                end_date += timedelta(days=1)  # Make the end date inclusive
                concerts = concerts.filter(date__range=(start_date, end_date))
            except ValueError:
                # If there's a ValueError, it will just skip the date filter
                pass

        if description:
            concerts = concerts.filter(artist__description=description)

    return render(request, 'view_concerts.html', {
        'concerts': concerts,
        'descriptions': descriptions,
    })
