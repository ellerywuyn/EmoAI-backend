from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the virtualfriend index page.")

# virtualfriend/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import VirtualFriend
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_virtual_friend(request):
    try:
        # Extract data from request
        mbti_type = request.data.get('mbtiType')
        trait = request.data.get('trait')
        name = request.data.get('virtualFriendName')

        # print(mbti_type, trait, name)
        # Get the user from the request
        user = request.user

        # Create and save the new VirtualFriend object
        virtual_friend = VirtualFriend.objects.create(
            user=user,
            friend_name=name,
            friend_mbti=mbti_type,  # Adjust the field names as per your model
            friend_mbti_variant=trait
        )

        return Response({
            'message': 'Virtual friend created successfully',
            'virtual_friend_id': virtual_friend.id
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
