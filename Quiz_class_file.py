
from questions import prompts
class Quiz_game:

    def __init__(self, asking):
        self.askings = asking

    def play_quiz(self, asking):
        player_name = input("Please type your name: \n")
        responses= {"Dominique" : ["B", "B" , "B", "A"]}
        answer = []
        print("Please enter the letter that cooresponds with your answer choice")
        for prompt, choices in asking.items():
            print(prompt)
            answer.append(input(choices).upper())
            responses[player_name] = answer
        def turning_json(self):
            import json
            with open('results.json', 'a') as results_json:
                json.dump(responses, results_json)
        turning_json(responses)

                 


starting = Quiz_game(prompts)
starting.play_quiz(prompts)













