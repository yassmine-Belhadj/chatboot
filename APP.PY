import random

# Liste de réponses possibles du chatbot
responses = {
    "Bonjour": ["Bonjour! Comment puis-je vous aider aujourd'hui?", "Salut! Comment puis-je vous aider aujourd'hui?"],
    "Quels sont vos produits?": ["Nous offrons une large gamme de produits cosmétiques, des produits pour la peau aux produits capillaires. Quel type de produit vous intéresse?"],
    "Pouvez-vous m'aider à trouver le produit qui me convient le mieux?": ["Bien sûr! Pouvez-vous me donner plus d'informations sur votre type de peau / vos cheveux?"],
    "Quels sont vos horaires d'ouverture?": ["Nous sommes ouverts de 9h à 18h du lundi au vendredi. Nous sommes fermés les week-ends."],
    "Comment puis-je passer une commande?": ["Vous pouvez passer une commande directement sur notre site web. Si vous avez des problèmes pour passer votre commande, n'hésitez pas à me demander de l'aide."],
    "Je rencontre des problèmes avec ma commande": ["Je suis désolé d'entendre cela. Pouvez-vous me donner plus d'informations sur le problème que vous rencontrez?"],
    "Merci": ["De rien! N'hésitez pas à me contacter si vous avez besoin d'aide supplémentaire."]
}

# Fonction qui retourne une réponse aléatoire de la liste de réponses possibles
def get_response(message):
    if message in responses:
        return random.choice(responses[message])
    else:
        return "Je ne comprends pas. Pouvez-vous reformuler votre question?"

# Boucle principale qui écoute les messages de l'utilisateur et renvoie une réponse
while True:
    user_message = input("Vous: ")
    chatbot_response = get_response(user_message)
    print("Bot: " + chatbot_response)
