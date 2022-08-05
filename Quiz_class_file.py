
from questions import prompts
class Quiz_game:
    import json

    def __init__(self, asking):
        self.askings = asking

    def play_quiz(self, asking):
        print("Please only input a letter \n")
        player_name = input("Please type your name: \n")
        responses= {"Dominique" : ["B", "B", "B", "A"]}
        answer = []
        for prompt, choices in asking:
            answer.append(input(prompt, choices).upper())
            responses[player_name] = answer


Quiz_game(prompts)













