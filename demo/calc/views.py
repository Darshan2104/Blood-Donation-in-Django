from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from Doner.models import Donerinfo, ReqDonerinfo, BloodBankinfo, Hospital
# Create your views here.


def show(request):
    dests = Donerinfo.objects.all().order_by('-id')[:5]
    x = BloodBankinfo.objects.all().order_by('-id')[:3]
    y = Hospital.objects.all().order_by('-id')[:3]
    return render(request, 'index.html', {'dests': dests, 'x': x, 'y': y})


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = auth.authenticate(username=username, password=password)

        if user1 is not None:
            auth.login(request, user1)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials !!!')
            return redirect('login')
    else:
        return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is already taken !!!!')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is already taken !!!!')
                return redirect('registration')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                user.save()
                messages.info(request, 'created')
                return redirect('login')
        else:
            messages.info(request, 'password are not same !!!')
            return redirect('registration')
    else:
        return render(request, 'regs.html')

# main home page.....


def alldoner(request):
    q = Donerinfo.objects.all()
    return render(request, "alldoner.html", {'q': q})


def allreq(request):
    q = ReqDonerinfo.objects.all()
    return render(request, "allreq.html", {'q': q})


def allbb(request):
    q = BloodBankinfo.objects.all()
    return render(request, 'allbb.html', {'q': q})


def allhospital(request):
    q = Hospital.objects.all()
    return render(request, "allhospital.html", {'q': q})


def mail(request):
    return render(request, "mail.html")


def donate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            img = request.POST['img']
            name = request.POST['name'].upper()
            email = request.POST['email']
            mobile = request.POST['mobile']
            country = request.POST['country'].upper()
            state = request.POST['state'].upper()
            city = request.POST['city'].upper()
            pincode = request.POST['pincode']
            address = request.POST['address'].upper()
            bloodgrp = request.POST['bloodgrp']

            don = Donerinfo(img=img, name=name, email=email, mobile=mobile, country=country,
                            state=state, city=city, pincode=pincode, address=address, bloodgrp=bloodgrp)
            don.save()
            return redirect('/')
        else:
            return render(request, 'donerform.html')
    else:
        return render(request, 'login.html')


def req(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            patient_name = request.POST['pname'].upper()
            doctor_name = request.POST['dname'].upper()
            bloodgrp = request.POST['bloodgrp']
            country = request.POST['country'].upper()
            state = request.POST['state'].upper()
            city = request.POST['city'].upper()
            hospital_address = request.POST['address'].upper()
            c_name = request.POST['cname'].upper()
            c_mobile = request.POST['mobile']
            c_email = request.POST['email']

            donr = ReqDonerinfo(patient_name=patient_name, doctor_name=doctor_name, c_name=c_name, c_email=c_email, c_mobile=c_mobile, country=country,
                                state=state, city=city, hospital_address=hospital_address, bloodgrp=bloodgrp)
            donr.save()
            return redirect('/')
        else:
            return render(request, 'requestblood.html')
    else:
        return render(request, 'login.html')


def bbank(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            img = request.POST['img']
            name = request.POST['name'].upper()
            bb_email = request.POST['email']
            bb_mobile = request.POST['mobile']
            country = request.POST['country'].upper()
            state = request.POST['state'].upper()
            city = request.POST['city'].upper()
            bb_address = request.POST['address'.upper()]
            pincode = request.POST['pincode']
            about = request.POST['about'].upper()
            bb = BloodBankinfo(img=img, name=name, bb_email=bb_email, bb_mobile=bb_mobile, country=country,
                               state=state, city=city, bb_address=bb_address, pincode=pincode, about=about)
            bb.save()
            return redirect('/')
        else:
            return render(request, 'bloodbank.html')
    else:
        return render(request, 'login.html')


def hp(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            img = request.POST['img']
            name = request.POST['name'].upper()
            email = request.POST['email']
            mobile = request.POST['mobile']
            country = request.POST['country'].upper()
            state = request.POST['state'].upper()
            city = request.POST['city'].upper()
            pincode = request.POST['pincode']
            address = request.POST['address'].upper()
            bloodgrp = request.POST['bloodgrp']

            don = Hospital(img=img, name=name, email=email, mobile=mobile, country=country,
                           state=state, city=city, pincode=pincode, address=address, bloodgrp=bloodgrp)
            don.save()
            return redirect('/')
        else:
            return render(request, 'hospital.html')
    else:
        return render(request, 'login.html')


# Need to change !!!!!!!!!!1111

def finddoner(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            state = request.POST['state'].upper()
            city = request.POST['city'].upper()
            bloodgrp = request.POST['bloodgrp']
            query = Donerinfo.objects.all()
            #     state=state, city=city, bloodgrp=bloodgrp)
            return render(request, "outputDoner.html", {'query': query, 'state': state, 'city': city, 'bloodgrp': bloodgrp})
        else:
            return render(request, 'finddoner.html')
    else:
        return render(request, 'login.html')


def findbloodbank(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            state = request.POST['state'].upper()
            city = request.POST['city'].upper()
            query = BloodBankinfo.objects.all()
            return render(request, "outputbb.html", {'query': query, 'state': state, 'city': city})
        else:
            return render(request, 'findbb.html')
    else:
        return render(request, 'login.html')


def findhp(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            state = request.POST['state'].upper()
            city = request.POST['city'].upper()
            query = Hospital.objects.all()
            return render(request, "outputHP.html", {'query': query, 'state': state, 'city': city})
        else:
            return render(request, 'findh.html')
    else:
        return render(request, 'login.html')


def look(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            state = request.POST['state'].upper()
            city = request.POST['city'].upper()
            bloodgrp = request.POST['bloodgrp']
            # listView
            query = Donerinfo.objects.get(
                state=state, city=city, bloodgrp=bloodgrp)
            return redirect('display', query)
        else:
            return render(request, 'finddoner.html')
    else:
        return render(request, 'login.html')
