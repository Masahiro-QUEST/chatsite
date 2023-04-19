from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
# Create your views here.
def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            # stop='.'
        )
        print("API response:", response)  # Add this line
        chatbot_response = response["choices"][0]["text"].strip()
        print("Chatbot response:", chatbot_response)  # Add this line
    return render(request, "chat/frontpage.html",  {"response": chatbot_response})