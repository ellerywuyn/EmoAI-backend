from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the chat index page.")

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# import json
# import openai
# from openai import OpenAI
# import os

# @csrf_exempt
# @require_POST
# def chat_response(request):
#     try:
#         data = json.loads(request.body)
#         user_message = data.get('message')
        
#         openai.api_key = os.getenv('OPENAI_API_KEY')

#         # api_key = "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"
#         # openai.api_key = api_key
        
#         client = OpenAI()
#         response = client.chat.completions.create(
#             model="gpt-4-1106-preview",  # Replace with the correct model
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": user_message}
#             ]
#         )
        
#         # Extract the response - depending on OpenAI's response structure
#         message = response.choices[0].message.content
#         return JsonResponse({'message': message})
#     except Exception as e:
#         # Properly log the error for debugging
#         print(f"Error: {str(e)}")
#         return JsonResponse({'message': "Something."}, status=500)


## Good one!!!
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import openai
import os
from openai import OpenAI
# from config import OPENAI_API_KEY

@csrf_exempt
@require_POST
def chat_response(request):
    try:
        data = json.loads(request.body)
        # user_message = data.get('message', "Hello")  # Default to "Hello" if no message

        print(data)
        user_message = data.get('message')
        if user_message == "":
           user_message = """
            Act as a virtual friend who has a MBTI personality type of ENFJ. 
            Do not explicitly say you are an ENFJ at the beginning, but act like one.
            Keep the greeting and each response brief and engaging.
            And this is actually the first time you meet with your user friend.
            So make the experience memorable.
            Make the conversation relatively casual.
            And your favorite sport is rock climbing.
            """
        os.environ["OPENAI_API_KEY"] = "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"
        # Set the API key from an environment variable
        # openai.api_key = os.getenv('OPENAI_API_KEY')

        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",  # Replace with the correct model
            messages=[
                # {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        
        # Extract the response - depending on OpenAI's response structure
        # The structure of the response should be verified with the latest OpenAI API documentation
        message = response.choices[0].message.content
        return JsonResponse({'message': message})
    except Exception as e:
        # Properly log the error for debugging
        print(f"Error: {str(e)}")
        return JsonResponse({'message': "Something went wrong"}, status=500)


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# import json
# import openai
# import os
# from openai import OpenAI
# # from config import OPENAI_API_KEY

# @csrf_exempt
# @require_POST
# def chat_response(request):
#     try:
#         data = json.loads(request.body)
#         print("Request body:", data)
#         user_message = data.get('message', "Hello")
#         selected_type = data.get('selectedType')  # Get the selectedType from the request
#         print("selected type: ", selected_type)
#         # data = json.loads(request.body)
#         # user_message = data.get('message', "Hello")  # Default to "Hello" if no message

#         print(data)
#         user_message = data.get('message')
#         if user_message == "":
#             # user_message = "Hello"
#             user_message = """
#             Act as a virtual friend who has a MBTI personality type of ENFJ. 
#             Do not explicitly say you are an ENFJ at the beginning, but act like one.
#             Keep the greeting relatively short.
#             And this is actually the first time you meet with your user friend.
#             So make the experience memorable.
#             Make the conversation relatively casual.
#             And your favorite sport is rock climbing.
#             """
#         os.environ["OPENAI_API_KEY"] = "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"
#         # Set the API key from an environment variable
#         # openai.api_key = os.getenv('OPENAI_API_KEY')

#         system_message = f"You are a helpful assistant. MBTI: {selected_type}"
#         print("System message:", system_message)

#         client = OpenAI()
#         response = client.chat.completions.create(
#             model="gpt-4-1106-preview",  # Replace with the correct model
#             messages=[
#                 {"role": "system", "content": f"You are a helpful assistant. MBTI: {selected_type}"},
#                 {"role": "user", "content": user_message}
#             ]
#         )
        
#         # Extract the response - depending on OpenAI's response structure
#         # The structure of the response should be verified with the latest OpenAI API documentation
#         message = response.choices[0].message.content
#         return JsonResponse({'message': message})
#     except Exception as e:
#         # Properly log the error for debugging
#         print(f"Error: {str(e)}")
#         return JsonResponse({'message': "Something went wrong"}, status=500)

