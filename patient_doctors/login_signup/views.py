from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import CustomUser


# Create your views here.
def index(request):
    return render(request,'login_signup/index.html')

def login(request):
    return render(request, 'login_signup/login.html')

def signup(request):
    if request.method == 'POST':
 # Extract form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_picture = request.FILES.get('profile_picture')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address_line1 = request.POST.get('address_line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        user_type = request.POST.get('user_type')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'login_signup/signup.html', {'error_message': 'Password and confirm password do not match.'})
        
         # Create new user object
        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            profile_picture=profile_picture,
            username=username,
            email=email,
            address_line1=address_line1,
            city=city,
            state=state,
            pincode=pincode,
            user_type=user_type
        )

        # Set password
        user.set_password(password)
        
        # Save user object to database
        user.save()
        return redirect('login_signup:login')
    return render(request, 'login_signup/signup.html')

def dashboard(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                # User authenticated; proceed to display dashboard
                context = {
                    'user': user
                }
                return render(request, 'login_signup/dashboard.html', context)
            else:
                messages.error(request, 'Incorrect password.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist.')

    return redirect('login_signup:login')  # Redirect to login page on failure