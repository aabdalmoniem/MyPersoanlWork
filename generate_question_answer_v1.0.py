"""
This project from "automate boring stuff"
it generate exam templates and generate random questions.
for now it generate 10questions and only 1 file ( using j) just for testing
TODO :
1- create_file fn. return does not work as expected
"""


import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


def create_file(i):
    quizFileName,ansFileName = f'capialQuiz{i+1}', f'ansQuiz{i+1}'
    quizFile = open(f'capialQuiz{i+1}', 'w')
    ansFile = open(f'ansQuiz{i+1}', 'w')
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' ' * 20) + f'state capial quiz(Form{i + 1})')
    quizFile.write('\n\n')

    return quizFileName,ansFileName


def gen_quest(i, state_dict):
    states = list(state_dict.keys())
    chosen_state = states[i]
    correct_ans = state_dict[states[i]]
    wrong_ans = list(state_dict.values())
    del wrong_ans[wrong_ans.index(correct_ans)]
    wrong_ans = random.sample(wrong_ans, 3)
    answer_options = wrong_ans + [correct_ans]
    random.shuffle(answer_options)
    return chosen_state, answer_options, correct_ans


def write_questions(i):
    #create_file(i)
    quizFile.write(f'{i + 1}.What is the capital of {quiz[0]}\n\n{quiz[1]}')


if __name__ == '__main__':
    for j in range(1):
        quizFile = open(f'capialQuiz{j + 1}.txt', 'w')
        ansFile = open(f'ansQuiz{j + 1}.txt', 'w')
        quizFile.write('Name:\n\nDate:\n\n')
        quizFile.write((' ' * 20) + f'state capial quiz(Form{j + 1})')
        quizFile.write('\n')
        for i in range(10):
    #create_file(i)
    #gen_quest(i, capitals)
    #quiz_files = create_file(i)
    #print (quiz_files[0])
            quiz = gen_quest(i, capitals)
    #print(quiz[2])
    #print (f'{i + 1}.What is the capital of {quiz[0]}\n\n{quiz[1]}')

    #create_file(i)
            quizFile.write(f'{i + 1}.What is the capital of {quiz[0]}\n\n{quiz[1]}')
            quizFile.write('\n\n')
            ansFile.write(f'state capial Answer (Form{j + 1})')
            ansFile.write(f'state capial Answer (Qestion{i + 1}) :: {quiz[2]}')
            ansFile.write('\n')