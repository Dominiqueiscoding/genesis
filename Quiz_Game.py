from Quiz_class_file import Quiz_game
print("Please enter the letter that cooresponds with your answer")
prompts = [
    "What food would you most like to eat? \n A popcorn \n B cookies \n C chips    ",
    "What is your favorite vacation spot? \n A beach \n B mountains \n C desert     ",
    "What color do you like the best? \n A blue \n B green \n C red     ",
    "what would you most want to be? \n A loved \n B respected \n C feared     ",
]
dominique_response = [
    "B",
    "B",
    "B",
    "A",
]

q0 = Quiz_game(prompts[0], dominique_response[0])
q1 = Quiz_game(prompts[1], dominique_response[1])
q2 = Quiz_game(prompts[2], dominique_response[2])
q3 = Quiz_game(prompts[3], dominique_response[3])

lst_of_prompts = [q0, q1, q2, q3]
similarityScore = 0

for questions in lst_of_prompts: 
    answer = input(questions.asking).upper()
    print("your answer is: ", answer)
    if answer == "A" or answer == "B" or answer == "C":
        if answer == questions.dominique_answers:
            similarityScore += 1
    else:
        print("You can only respond with a letter, please restart the quiz")
        break       
    
    # print ("You answered: ", answer)
if similarityScore <= 1 and similarityScore != 0:
    print("You and Dominique are not similar")
elif similarityScore <= 3 and similarityScore != 0:
    print("You and Dominique are kind of similar")
elif similarityScore >= 4 and similarityScore != 0:
    print("You and Dominique are the same!")
else:
    print("")