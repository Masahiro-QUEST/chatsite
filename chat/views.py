from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
# Create your views here.
def frontpage(request):
    chatbot_responce = None
    if api_key is not None and request.method == 'POST':
        open.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt=prompt,
            max_token=256,
            # stop='.'
        )
        print(response)
    return render(request, "chat/frontpage.html",  {})