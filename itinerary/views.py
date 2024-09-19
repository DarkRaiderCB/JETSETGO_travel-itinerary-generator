from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import markdown2
from .utils import *
from .models import *
from .forms import CustomForm


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('itinerary_generate')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomForm()
    return render(request, 'signup.html', {'form': form})


def render_result(response):
    html_content = markdown2.markdown(response)
    return html_content


@login_required
def itinerary_generate(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        no_of_days = request.POST.get('no_of_days')
        budget = request.POST.get('budget')
        activities = request.POST.get('activities')

        if destination and start_date and end_date and no_of_days and activities:
            personalized_content = generate_itinerary(
                destination, start_date, end_date, no_of_days, budget, activities)
            personalized_content = render_result(personalized_content)
            images = scrape_images(destination)

            return render(request, 'destination_detail.html', {
                'user': request.user,
                'destination': destination,
                'start_date': start_date,
                'end_date': end_date,
                'no_of_days': no_of_days,
                'budget': budget,
                'activities': activities,
                'personalized_content': personalized_content,
                'images': images
            })

    return render(request, 'search.html', {'user': request.user})


def guest_mode(request):
    tries = request.session.get('guest_tries', 0)

    if tries >= 2 and not request.user.is_authenticated:
        # Redirect guest users to register after 2 tries
        return redirect('signup')

    if request.method == 'POST':
        destination = request.POST.get('destination')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        no_of_days = request.POST.get('no_of_days')
        budget = request.POST.get('budget')
        activities = request.POST.get('activities')

        personalized_content = generate_itinerary(
            destination, start_date, end_date, no_of_days, budget, activities)
        personalized_content = render_result(personalized_content)
        images = scrape_images(destination)
        request.session['guest_tries'] = tries + 1
        return render(request, 'destination_detail.html', {
            'destination': destination,
            'start_date': start_date,
            'end_date': end_date,
            'no_of_days': no_of_days,
            'budget': budget,
            'activities': activities,
            'personalized_content': personalized_content,
            'images': images
        })

    return render(request, 'search2.html')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')
