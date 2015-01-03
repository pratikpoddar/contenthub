from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import logging
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from flip.models import *


logger = logging.getLogger(__name__)

def user_register(request):
    context = RequestContext(request)

    logger.debug('user_register')

    if request.method == 'POST':
        userfirstname = request.POST['first_name']
        userlastname = request.POST['last_name']
        userID = request.POST['username']
        userEmail = request.POST['email']
        userPass = request.POST['password']

        checkuser = User.objects.filter(username=userID)
        if not checkuser:
            user = User.objects.create_user(
                                            username=userID,
                                            email=userEmail,
                                            password=userPass,
                                            first_name=userfirstname,
                                            last_name=userlastname,
                                            )

            userauth = authenticate(username=userID, password=userPass)
            if userauth:
                login(request, userauth)
                logger.debug('register_login ' + userID)
                return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'User ID already exist')
            return render_to_response('flip/register.html', {'page':'register'}, context)

    return render_to_response('flip/register.html', {'page':'register'}, context)

def user_login(request):
    context = RequestContext(request)
    logger.debug('user_login request')

    next_page = request.GET.get('next', '')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                logger.debug('user_login ' + username)

                next_page = request.POST.get('next_page', '')
                if next_page:
                    return HttpResponseRedirect(next_page)

                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Flip account is disabled.")
        else:
            logger.debug("Invalid login details: {0}, {1}".format(username, password))
            logger.debug('user_login ' + username + 'unable to login')
            messages.warning(request, 'Invalid Login Details')
            return render_to_response('flip/login.html', {'page' : 'login'}, context)
    else:
        return render_to_response('flip/login.html', {'page' : 'login', 'next_page': next_page }, context)


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    logger.debug('user_logout ' + request.user.username)
    return HttpResponseRedirect('/login/')