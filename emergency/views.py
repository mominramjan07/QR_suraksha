import qrcode, os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profile


def home(request):
    return render(request, 'home.html')


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('create_profile')
    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def create_profile(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        profile.owner_name = data.get('owner')
        profile.vehicle_number = data.get('vehicle')
        profile.vehicle_model = data.get('model')
        profile.license_number = data.get('license')
        profile.insurance_number = data.get('insurance')
        profile.blood_group = data.get('blood')
        profile.medical_notes = data.get('notes')
        profile.family_name = data.get('fname')
        profile.family_phone = data.get('phone')

        # profile image
        if files.get('profile_image'):
            profile.profile_image = files.get('profile_image')

        # documents
        if files.get('aadhar'):
            profile.aadhar = files.get('aadhar')

        if files.get('rc_book'):
            profile.rc_book = files.get('rc_book')

        if files.get('license_file'):
            profile.license = files.get('license_file')

        if files.get('insurance_file'):
            profile.insurance = files.get('insurance_file')

        profile.save()

        # QR generate
        qr_data = f"https://qr-suraksha-3.onrender.com/emergency/{profile.id}/"
        img = qrcode.make(qr_data)

        os.makedirs("media/qr_codes", exist_ok=True)

        path = f"media/qr_codes/user_{profile.id}.png"
        img.save(path)

        profile.qr_code = f"qr_codes/user_{profile.id}.png"
        profile.save()

        return redirect('dashboard')

    return render(request, 'profile.html')


@login_required
def dashboard(request):
    p = Profile.objects.filter(user=request.user).first()
    return render(request, 'dashboard.html', {'p': p})


def emergency(request, id):
    p = Profile.objects.get(id=id)
    return render(request, 'emergency.html', {'p': p})

def about(request):
    return render(request, "about.html")

@login_required
def edit_profile(request):

    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":

        data = request.POST
        files = request.FILES

        profile.owner_name = data['owner']
        profile.vehicle_number = data['vehicle']
        profile.vehicle_model = data['model']
        profile.license_number = data['license']
        profile.insurance_number = data['insurance']
        profile.blood_group = data['blood']
        profile.medical_notes = data['notes']
        profile.family_name = data['fname']
        profile.family_phone = data['phone']

        if 'profile_image' in files:
            profile.profile_image = files['profile_image']

        if 'aadhar' in files:
            profile.aadhar = files['aadhar']

        if 'rc_book' in files:
            profile.rc_book = files['rc_book']

        if 'license_doc' in files:
            profile.license_doc = files['license_doc']

        if 'insurance_doc' in files:
            profile.insurance_doc = files['insurance_doc']

        profile.save()

        return redirect("dashboard")

    return render(request,"edit_profile.html",{'p':profile})