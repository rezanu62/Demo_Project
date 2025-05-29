import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json, os
from dotenv import load_dotenv
from .models import Chat

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# Use correct model name
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt", "")

            if not prompt:
                return JsonResponse({"error": "Prompt is required."}, status=400)

            # Gemini expects this as a list of parts or a string
            response = model.generate_content([prompt])
            reply = response.text.strip()

            # Save to DB
            Chat.objects.create(user_prompt=prompt, bot_response=reply)

            return JsonResponse({"response": reply}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Only POST allowed."}, status=405)


from query_counter.decorators import queries_counter

from django.http import HttpResponse
from query_counter.decorators import queries_counter
from .models import Chat

@queries_counter
def track_queries_view(request):
    chats = Chat.objects.all()[:5]  # 🔥 SELECT query runs here
    return HttpResponse(f"Queried {len(chats)} chat objects.")
