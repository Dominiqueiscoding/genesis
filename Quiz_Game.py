from Quiz_class_file import Quiz_game

prompts = [
    "Question1 \n answera \n answerb \n answerc",
    "Question2 \n answera \n answerb \n answerc",
    "Question3 \n answera \n answerb \n answerc",
    "Question4 \n answera \n answerb \n answerc",
]
dominique_response = [
    "answer1",
    "answer2",
    "answer2",
    "answer4",
]

q0 = Quiz_game(prompts[0], dominique_response[0])
q1 = Quiz_game(prompts[1], dominique_response[1])
q2 = Quiz_game(prompts[2], dominique_response[2])
q3 = Quiz_game(prompts[3], dominique_response[3])

lst_of_prompts = [q0, q1, q2, q3]
similarityScore = 0

for questions in lst_of_prompts: 
    questions.answer = input(questions.asking).upper()
    if questions.answer == questions.dominique_answers:
        similarityScore += 1
    print ("You answered: ", questions.answer, " the answer was: ", questions.dominique_answers)

print("Your score is: ", similarityScore)

print("poopy")

# def comparison(answer, dominique_response):
#     similarity_score = 0
#     for answers in answer:
#         if answers == dominique_response:
#             similarity_score += 1
#         return similarity_score

# def genesis(lst_of_prompts):
    # for question in lst_of_prompts:
        # print(question)
    #     person_answer = input(question.asking)
    #     answer = question.answer.append(person_answer)
    #     answer.upper()
    # def comparison(answer, dominique_response):
    #     similarity_score = 0
    #     for answers in answer:
    #         if answers == dominique_response:
    #             similarity_score += 1
    #     return similarity_score
    # return answer

# genesis(prompts)