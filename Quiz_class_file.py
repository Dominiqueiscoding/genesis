# class Quiz_game:
#     def __init__(self, asking, answer, dominique_answers):
#         self.asking = asking
#         self.answer = answer
#         self.dominique_answers = dominique_answers

'''
    Probably should not be a seperate Quiz_game per question, you can use a dictionary. 
    Lets say Tom and Jerry have taken your quiz, couldn't you do a dictionary structured as:
    {
        "Dominique" : ["B", "B", "B", "A],
        "Tom" : ["B", "B", "B", "A],
        "Jerry" : ["A", "A", "A", "B"]
    } ?
''' 
class Quiz_game:
    def __init__(self, asking, dominique_answers):
        self.asking = asking
        self.dominique_answers = dominique_answers