from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the account index page.")

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

import os
from django.conf import settings

def create_user_directory(username):
    user_directory = os.path.join(settings.MEDIA_ROOT, 'user_data', username)
    os.makedirs(user_directory, exist_ok=True)
    return user_directory

@csrf_exempt
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    mbti = request.data.get('mbti')
    gender = request.data.get('gender')
    mbti_variant = request.data.get('mbti_variant')

    user = User.objects.create(
        username=username,
        email=email,
        password=make_password(password),
        first_name=first_name,
        last_name=last_name
    )
    Profile.objects.create(
        user=user,
        mbti=mbti,
        gender=gender,
        mbti_variant=mbti_variant
    )

    # Authenticate the newly created user
    new_user = authenticate(username=username, password=password)
    create_user_directory(new_user.username)

    # Create a token for the user
    if new_user is not None:
        token, created = Token.objects.get_or_create(user=new_user)
        return JsonResponse({
            'token': token.key,
            'username': new_user.username  # or 'username': new_user.username
        }, status=201)
    else:
        # In case authentication fails
        return JsonResponse({'error': 'Authentication failed'}, status=400)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        # Send back the token and the user's unique identifier (e.g., user ID or username)
        return JsonResponse({
            'token': token.key,
            'username': user.username  # Send back the username
        }, status=200)
    else:
        return JsonResponse({'error': 'Invalid Credentials'}, status=400)

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_specific_endpoint(request, user_id):
#     # Make sure the user is requesting their own data
#     if request.user.id != int(user_id):
#         return JsonResponse({'error': 'You do not have permission to access this data.'}, status=403)

    # Fetch and return the user-specific data

# Django view to serve user files
from django.http import HttpResponse
from django.conf import settings
import os

def serve_user_file(request, username, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, username, filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type="image/png") # set appropriate content type
            response['Content-Disposition'] = 'inline; filename=' + filename
            return response
    return HttpResponse("Not Found", status=404)


# @csrf_exempt
# @api_view(['POST'])
# def register_user(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     email = request.data.get('email')
#     first_name = request.data.get('first_name')
#     last_name = request.data.get('last_name')
#     mbti = request.data.get('mbti')
#     gender = request.data.get('gender')

#     user = User.objects.create(
#         username=username,
#         email=email,
#         password=make_password(password),
#         first_name=first_name,
#         last_name=last_name
#     )
#     Profile.objects.create(
#         user=user,
#         mbti=request.data.get('mbti'),
#         gender=request.data.get('gender'),
#         mbti_variant=request.data.get('mbti_variant'),
#     )
#     # profile_defaults = {
#     #     'mbti': request.data.get('mbti'),
#     #     'gender': request.data.get('gender'),
#     #     'mbti_variant': request.data.get('mbti_variant'),
#     # }

#     # user.save(profile_defaults=profile_defaults)
#     # Profile.objects.create(user=user, mbti=mbti, gender=gender)
    
#     return JsonResponse({'message': 'User registered successfully'}, status=201)

# users/views.py


# @api_view(['POST'])
# def login_user(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
    
#     if user:
#         token, _ = Token.objects.get_or_create(user=user)
#         return JsonResponse({'token': token.key}, status=200)
#     else:
#         return JsonResponse({'error': 'Invalid Credentials'}, status=400)

# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view
# from django.http import JsonResponse