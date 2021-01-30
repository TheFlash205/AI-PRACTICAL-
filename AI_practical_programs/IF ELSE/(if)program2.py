"""
Create a 3-questions quiz on python, which will print the questions and options to choose from,
and the user should input the option number and get the score accordingly.Ask your friends to play.
"""

import random

questions = {
    'A .py' : ['Which one of the following is the correct extension of the Python file?', [
        'A: .py',
        'B: .python',
        'C: .p',
        'D: None of these']
         ] ,

    'B #' : ['Which character is used in Python to make a single line comment?', [
        'A: /',
        'B: #',
        'C: //',
        'D: !']
         ] ,

    'A C' : ['In which language is Python written?', [
        'A: C',
        'B: English',
        'C: PHP',
        'D: All of the above']
         ]
}

ques = random.choice(list(questions.items()))
answer , question = ques

print(f'Question: {question[0]}')
print('\n'.join(map(str , question[1])))

user_inp = input('Please input the option that you think is correct: ').lower()
ch1 , ch2 = answer.split(' ')

if user_inp in ch1.lower() or user_inp in ch2.lower():
    print('correct answer!')