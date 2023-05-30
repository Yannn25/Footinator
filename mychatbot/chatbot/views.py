from django.http import JsonResponse

def chatbot(request):
    # Récupérez le message entrant à partir de la requête POST
    incoming_message = request.POST.get('message')

    # Traitez le message en fonction de votre logique de chatbot
    response_message = "Bonjour, comment puis-je vous aider ?"

    # Retournez la réponse au format JSON
    return JsonResponse({'message': response_message})
