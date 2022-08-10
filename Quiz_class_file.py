
from questions import prompts
class Quiz_game:

    def __init__(self, asking):
        self.askings = asking

    def play_quiz(self, asking):
        player_name = input("Please type your name: \n")
        answer = []
        print("Please enter the letter that cooresponds with your answer choice")
        for prompt, choices in asking.items():
            print(prompt)
            answer.append(input(choices).upper())
        def json_stuffs(results, filename = "results.json"):
            import json
            with open (filename, "w") as f:
                json.dump(results, f)
        with open('results.json') as results_json:
            import json
            results = json.load(results_json)
            results.update({player_name : answer})
            print(results)
        json_stuffs(results)
                 


starting = Quiz_game(prompts)
starting.play_quiz(prompts)














