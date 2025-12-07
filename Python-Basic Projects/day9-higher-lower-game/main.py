import random
from art import logo, vs
from game_data import data

def format_person(person):
    """Returns a formatted string for a person."""
    return f"{person['name']}, a {person['description']}, from {person['country']}"

def choose_two_people(data):
    """Selects two different people from the data."""
    person1 = random.choice(data)
    person2 = random.choice([x for x in data if x != person1])
    return person1, person2

def get_correct_answer(person1, person2):
    """Determines who has more followers."""
    if person1['follower_count'] > person2['follower_count']:
        return 'a'
    else:
        return 'b'

def check_player_answer(player_answer, correct_answer):
    """Checks if the player's answer is correct."""
    return player_answer.lower() == correct_answer

def play_game():
    score = 0
    game_over = False
    print(logo)

    while not game_over:
        person_a, person_b = choose_two_people(data)
        print(f"Compare A: {format_person(person_a)}")
        print(vs)
        print(f"Against B: {format_person(person_b)}")

        correct_answer = get_correct_answer(person_a, person_b)
        player_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        if check_player_answer(player_answer, correct_answer):
            score += 1
            print(f"You're right! Current score: {score}\n")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}\n")

if __name__ == "__main__":
    play_game()
