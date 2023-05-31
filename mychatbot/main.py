import json
import csv
from difflib import get_close_matches
import random

# Load the knowledge base from a JSON file
def load_knowledge_base(file_path: str):
    """
    Read the knowledge base from a JSON file.
    :param file_path: The path to the JSON file containing the knowledge base.
    :return: A dictionary with the knowledge base data.
    """
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

# Save the updated knowledge base to the JSON file
def save_knowledge_base(file_path: str, data: dict):
    """
    Write the updated knowledge base to a JSON file.
    :param file_path: The path to the JSON file to save the knowledge base.
    :param data: A dictionary with the knowledge base data.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Find the closest matching question
def find_best_match(user_answer: str, answers: list[str]) -> str | None:
    """
    Find the closest matching question in the knowledge base.
    :param user_question: The user's input question.
    :param questions: A list of questions from the knowledge base.
    :return: The closest matching question or None if no match is found.
    """
    matches: list = get_close_matches(user_answer, answers, n=1, cutoff=0.7)
    return matches[0] if matches else None

def find_closest_words(word: str, word_list: list[str], n: int = 5, cutoff: float = 0.5) -> list[str]:
    """
    Find the closest words in a list to a given word.
    :param word: The word to match.
    :param word_list: A list of words to search through.
    :param n: The maximum number of matches to return (default is 5).
    :param cutoff: The minimum similarity score for a match (default is 0.6).
    :return: A list of closest matching words.
    """
    matches: list = get_close_matches(word, word_list, n=n, cutoff=cutoff)
    return matches

def get_format_for_reponse(reponse: str, knowledge_base: dict) -> str | None:
    """
    Retrieve the answer for a given question from the knowledge base.
    :param question: The matched question from the knowledge base.
    :param knowledge_base: A dictionary containing the knowledge base data.
    :return: The answer to the question or None if the question is not found.
    """
    for q in knowledge_base["formatage"]:
        if q["reponse"] == reponse:
            return q["format"]
    return None

def read_players_data():
    players = []
    with open('../data/final_players.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = {
                'nom': row['name'],
                'club': row['current_club_name'],
                'nationalite': row['country_of_citizenship'],
                'pays_naissance': row['country_of_birth'],
                'age': row['age'],
                'poste': row['position'],
                'position': row['sub_position'],
                'pied': row['foot'],
                'taille': int(row['height_in_cm']),
                'valeur': float(row['market_value_in_eur']),
                'championnat': row['current_club_domestic_competition_id']
            }
            players.append(player)
    
    return players

def keep_digits_only(string):
    digits_only = ""
    for char in string:
        if char.isdigit():
            digits_only += char
    return digits_only

def filter_players(players, filters):
    """
    Filter the list of players based on the given filters.
    :param players: The list of players.
    :param filters: A dictionary containing the filters.
    :return: The filtered list of players.
    """
    filtered_players = []
    for player in players:
        match = True
        for attribute, value in filters.items():
            if value != '' and player.get(attribute) != value:
                match = False
                break
        if match:
            filtered_players.append(player)
    return filtered_players

def filter_in_range(players, filters, range_value=3):
    filtered_players = []
    for player in players:
        for attribute, value in filters.items():
            if float(player.get(attribute)) >= float(value) - range_value and float(player.get(attribute)) <= float(value) + range_value:
                        filtered_players.append(player)
    return filtered_players



def print_help():
    print("\033[92mUsage:")
    print("- Vous pouvez répondre aux questions en tapant les mots-clés correspondants.")
    print("- Si vous ne connaissez pas la réponse à une question, vous pouvez saisir 'je ne sais pas' ou 'passer'.")
    print("- Pour quitter le jeu, tapez 'quitter' ou 'quit'.")
    print("- Pour obtenir de l'aide, tapez 'aide'.\033[0m")


# Main function to handle user input and respond
def chatbot():
    """
    Run the chatbot to interact with the user, answer questions, and learn new information.
    The chatbot does the following:
    1. Load the knowledge base from a JSON file.
    2. Continuously prompt the user for questions.
    3. Find the closest matching question in the knowledge base.
    4. If a match is found, return the answer. Otherwise, ask the user to teach the chatbot.
    5. If the user provides a new answer, add it to the knowledge base and save the updated knowledge base to the JSON file.
    6. Exit the chatbot when the user types 'quit'.
    """
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    players = read_players_data()
    filterdplayers = []
    filter = {}
    asked_questions = []
    
    print("Bienvenue dans footinator, je suis un chatbot qui devienne le joueur au quel vous pensez\nJe vais vous posez plusieurs questions afin trouver le bon joueur\n\033[92mEntrer quitter pour quitter le jeu,ou alors aide si vous avez besoin d'aide, ou je ne sais pas/passer si vous souhaitez passer une question\n\033[0;31mAllons y!!!\033[0m")

    while True:
        
        #On pose une question au hasard a l'utilisateur tant que elle non pas deja eté utiliser 
        for i in range(len(knowledge_base['interactions'])):
            random_question = random.choice(knowledge_base["interactions"])
            critere = random_question['critere']
            if random_question not in asked_questions:
                print(f"\033[0;34mBot: {random_question['question']}\033[0m")
                asked_questions.append(random_question)
                break
            else:
                random_question = random.choice(knowledge_base["interactions"])
        if (len(asked_questions)+1) == (len(knowledge_base["interactions"]) +1 ):
            break
        
        user_input: str = input("-> ").lower()

        if user_input == "aide" or user_input == "":
            print_help()
            #continue
            user_input: str = input("-> ").lower()
        if user_input == 'quit' or user_input == 'quitter':
            print("\033[0;31mAu revoir !")
            break
        if user_input == 'passer' or user_input == 'je ne sais pas':
            continue
        if critere == "age" or critere == "taille" :
            #index: str = keep_digits_only(user_input)
            filter = {critere : keep_digits_only(user_input)}
            print(filter)
            if len(filterdplayers) == 0:                   
                filterdplayers = filter_in_range(players, filter)
            else :
                filterdplayers = filter_in_range(filterdplayers, filter)
            print(filterdplayers)
            continue
            
        best_match: str | None = find_best_match(user_input, [q["reponse"] for q in knowledge_base["formatage"]])

        if best_match:
            format: str = get_format_for_reponse(best_match, knowledge_base)
            filter = {critere : format}
            print(filter)
            if len(filterdplayers) == 0:                   
                filterdplayers = filter_players(players, filter)
            else :
                filterdplayers = filter_players(filterdplayers, filter)
        else:
            print("\033[0;36mBot: Je ne comprends pas votre réponse, selon vous quelle réponse dans la liste matche le mieux avec votre réponse ?")
            list_words = find_closest_words(user_input, [q["reponse"] for q in knowledge_base["formatage"]])
            print(list_words)
            new_answer: str = input("\033[0;36mEntrer la réponse(mot pour mot) ou 'passer' si vous ne savez pas: \033[0m")
            if new_answer != 'passer':
                if new_answer in [q["reponse"] for q in knowledge_base["formatage"]]:
                    format = get_format_for_reponse(new_answer, knowledge_base)
                    knowledge_base["formatage"].append({"reponse": user_input, "format": format})
                else:
                    knowledge_base["formatage"].append({"reponse": user_input, "format": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                #answer: str = get_answer_for_question(new_answer, knowledge_base)
                filter = {critere : new_answer}
                print(filter)
                if len(filterdplayers) == 0:
                    filterdplayers = filter_players(players, filter)
                else :
                    filterdplayers = filter_players(filterdplayers, filter)
                print("\033[0;35mBot: Merci pour votre aide précieuse ! Vous contribuez à mon amélioration :-)\033[0m")
        print(filterdplayers)
        
        if len(filterdplayers) < 4:
            flag: bool = False
            while len(filterdplayers) > 0:
                print(f"\033[0;35mBot: Le joueur auquel vous pensez est-il {filterdplayers[0]['nom']} ? (oui/non)\033[0m")
                user_input: str = input("-> ").lower()
                
                if user_input == "oui":
                    flag = True
                    break
                else:
                    filterdplayers.remove(filterdplayers[0])
            
            if flag:
                print("\033[0;33mSuper merci pour votre participation ;-)")
            else:
                print("\033[0;36mJe n'ai pas réussi à trouver votre joueur, désolé.\n\033[0;31mAu revoir ^_^")
            break
                
                        

if __name__ == "__main__":
    chatbot()