from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NowShowingMovie, UpcomingMovie, Contact, Transaction, Reg
from main.forms import RegForm, ContactForm 


# Create your views here.
def index(request):
    #return HttpResponse("Thi is home page!")
    now_showing_movies = NowShowingMovie.objects.all()
    upcoming_movies = UpcomingMovie.objects.all()
    return render(request, 'main/index.html', {'now_showing_movies': now_showing_movies, 'upcoming_movies': upcoming_movies})

def movies(request):
    #return HttpResponse("Thi is movies page!")
    now_showing_movies = NowShowingMovie.objects.all()
    upcoming_movies = UpcomingMovie.objects.all()
    return render(request, 'main/movies.html', {'now_showing_movies': now_showing_movies, 'upcoming_movies': upcoming_movies})

def movie_details(request, movie_id):
    movie = NowShowingMovie.objects.get(id=movie_id)
    return render(request, 'main/movie_details.html', {'movie': movie})

def transaction(request, movie_id):
    # Implement your transaction logic
    # For example, create a new transaction record and redirect to a payment page
    return render(request, 'main/transaction.html', {'movie_id': movie_id})


#def login(request):
    return render(request, 'loginform.html')

#def signup(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/booked")
    else:
        form = RegForm()
    return render(request, 'signup.html', {'form': form})

#def booked(request):
    booked_customers = Reg.objects.all()
    return render(request, 'booked.html', {'booked_customers': booked_customers})

#def about(request):
    return render(request, 'Untitled-1.html')

#def details(request, id):
    movie_details = NowShowingMovie.objects.get(id=id)
    return render(request, 'details.html', {'movie_details': movie_details})

#def updetails(request, id):
    movie_details = UpcomingMovie.objects.get(id=id)
    return render(request, 'updetails.html', {'movie_details': movie_details})

#def aboutmore(request):
    return render(request, 'about.html')

def contact_us(request):
    #return HttpResponse("Thi is contact us page!")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks for your message! We'll get back to you soon.")
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

#def buy_ticket(request):
    if request.method == 'POST':
        # Handle the ticket buying process
        # You can access the form data using request.POST.get('<field_name>')
        # Example: name = request.POST.get('name')
        # Add your ticket buying logic here
        return HttpResponse("Ticket bought successfully!")
    else:
        # Render the buy ticket form
        return render(request, 'buy_ticket.html')
