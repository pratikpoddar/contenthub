import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import logout
from dateutil.parser import parse
from flip.models import *
import datetime

logger = logging.getLogger(__name__)

def get_client_ip(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

    except:
        ip = ''
    return ip

def get_user_name(request):
    try:
        return request.user.username
    except:
        return 'no-username'

def get_account_name(request):
    try:
        return request.user.userprofile.account
    except:
        return 'no-accountname'

class error500Middleware(object):
        def process_exception(self, request, exception):
                logger.exception('spiral_project.middleware.error500Middleware' + ' userlogin:' + get_user_name(request) + ' ip:' + get_client_ip(request) + ' uri:' + request.build_absolute_uri())
                return None

class log_requests_Middleware(object):
        def process_request(self, request):
                try:
                        logger.debug('session_key:'+request.session.session_key + ' uri:' + request.build_absolute_uri() + ' ip:' + get_client_ip(request) + ' userlogin:' + get_user_name(request) + ' accountlogin:' +  get_account_name(request) + ' -- ACCESS LOGGING')
                except:
                        pass
                return None



class logout_all_users(object):
    def process_response(self, request, response):
            user = request.user
            if str(user) == 'AnonymousUser':
                return response

            last_login_time = parse(str(user.last_login)).replace(tzinfo=None)
            logout_time = parse(settings.LOGOUT_TIME).replace(tzinfo=None)

            if last_login_time < logout_time:
                logout(request)

            return response


class BasicAuthMiddleware(object):


    def unauthed(self):
        response = HttpResponse("""<html><title>Auth required</title><body>
                                <h1>Authorization Required</h1></body></html>""", mimetype="text/html")
        response['WWW-Authenticate'] = 'Basic realm="Development"'
        response.status_code = 401
        return response

    def process_request(self, request):
        if not request.META.has_key('HTTP_AUTHORIZATION'):

            return self.unauthed()
        else:
            authentication = request.META['HTTP_AUTHORIZATION']
            (authmeth, auth) = authentication.split(' ', 1)
            if 'basic' != authmeth.lower():
                return self.unauthed()
            auth = auth.strip().decode('base64')
            username, password = auth.split(':', 1)
            if username == settings.BASICAUTH_USERNAME and password == settings.BASICAUTH_PASSWORD:
                return None

            return self.unauthed()

