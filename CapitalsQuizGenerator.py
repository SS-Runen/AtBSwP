"""
Here is what the program does:

Creates 35 different quizzes
Creates 50 multiple-choice questions for each quiz, in random order
Provides the correct answer and three random wrong answers for each question,
in random order
Writes the quizzes to 35 text files
Writes the answer keys to 35 text files
"""

import os
import pprint
from pathlib import Path
import random
import re
import datetime as dt


def make_identification_questions(
    dict_source,
    questionpatterns={
        "key_first": "\n{0} = {1}",
        "val_first": "\n{1} = {0}"
    },
    n_questions=1
        ):
    questions_made = 0
    items_copy = dict_source.copy()
    lst_questions = []
    lst_answers = []
    dict_qa_pairs = {}

    while questions_made < n_questions:
        keys = list(dict_source.keys())
        index = random.randint(0, (len(keys) - 1))
        pair_key = keys[index]
        lst_question = [
            pair_key,
            dict_source[pair_key]
            ]
        random.shuffle(lst_question)

        lst_questionpatterns_keys = list(questionpatterns.keys())
        index = random.randint(
            0,
            (len(lst_questionpatterns_keys) - 1)
            )
        pattern_key = lst_questionpatterns_keys[index]
        dict_qa_pairs[lst_question[0]] = lst_question[1]
        str_answer = questionpatterns[pattern_key].format(
            lst_question[0],
            lst_question[1]
            )
        lst_answers.append(str_answer)
        str_questions = questionpatterns[pattern_key].format(
            lst_question[0],
            "____"
            )
        lst_questions.append(str_questions)
        questions_made += 1

    return {
        "questions": lst_questions,
        "answers": lst_answers,
        "answer key": dict_qa_pairs
        }


# pprint.pprint(
#     make_identification_questions(
#         dict_source=capitals,
#         n_questions=50
#     )
# )

def make_multiple_choice(
    dict_answerkey,
    question_pattern="{}:\n{}",
    items_per_question=4,
    n_questions=5
        ):
    lst_questions = []
    lst_answers = []
    lst_match_keys = list(dict_answerkey.keys())

    for question_number in range(1, (n_questions + 1)):
        random.seed(random.randint(0, 1024))
        index = random.randint(0, (len(lst_match_keys) - 1))
        question_key = lst_match_keys.pop(index)

        lst_items = [dict_answerkey[question_key]]
        lst_bait = list(dict_answerkey.keys())
        lst_bait.remove(question_key)

        for i in range(0, (items_per_question - 1)):
            bait_index = random.randint(0, (len(lst_bait) - 1))
            bait_key = lst_bait.pop(bait_index)
            lst_items.append(dict_answerkey[bait_key])

        random.shuffle(lst_items)
        # str_questions = question_pattern.format(lst_items)
        str_number = str(question_number) + ".) "

        str_questions = {
            str_number + question_key:
            lst_items
        }

        str_answer = {
            str_number + question_key:
            dict_answerkey[question_key]
        }

        lst_questions.append(str_questions)
        lst_answers.append(str_answer)

    return {
        "answers": lst_answers,
        "questions": lst_questions
    }


def format_asquiz(
    str_body,
    str_header="",
    str_endstring="",
    str_footer=""
        ):

    string = str_header
    string += ("\n\n\n" + str_body)
    string += ('\n' + str_endstring)
    string += ('\n\n\n' + str_footer)

    return string


def write_quizfile(
    dict_quiz: dict,
    quiz_type: ["multiple choice", "identification"] = "multiple choice",
    filename: str = "Quiz.txt",
    str_header: str = "Name:\nSubject:\nDate:\n",
    str_filepath: str = r"C:/Users/Rives/Downloads/Quizzes/"
        ):

    """
    Parameters:
    dict_answerkey: Dictionary of Lists.
    Must contain the keys "questions" and "answers"
    whose values must be aligned/correspoding lists
    of questions and answers.
    """
    lst_answers = dict_quiz["answers"]
    lst_questions = dict_quiz["questions"]

    try:
        # os.mkdir(Path(str_filepath))
        os.mkdir(str_filepath)
    except Exception as e:
        print(
            """Exception occured trying to create folder:
        %s""" % str_filepath
        )
        print(e)

    if not filename.endswith(".txt"):
        filename += ".txt"

    str_questions = format_asquiz(
        str_body=re.sub(r"[{}\]'[]", "", pprint.pformat(lst_questions)),
        str_header=str_header,
        str_endstring="\nEND. Nothing follows."
        )
    file_quiztext = open(
        str(Path(str_filepath + filename)),
        'x'
        )
    file_quiztext.write(str_questions)
    file_quiztext.close()

    str_answerkey = format_asquiz(
        str_header="\nAnswers to " + filename.strip('.txt') + '\n',
        str_body=re.sub(
            r"[{}\]'[]",
            "",
            pprint.pformat(lst_answers)
                ),
        str_endstring="\nEND of Answer Key. Nothing follows."
    )
    file_answers = open(
        str(Path(str_filepath + filename.strip('.txt'))) + " Answer Key.txt",
        'x'
        )
    file_answers.write(str_answerkey)
    file_answers.close()

    return None


def main():

    capitals = {
        'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock', 'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford', 'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
        'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
        'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
        'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe', 'New York': 'Albany',
        'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
        'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
        'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
        'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }
    questions = 50
    quiz_count = 35
    date_created = dt.datetime.now().date()

    for quiz_number in range(1, (quiz_count+1)):
        dict_quiz_qa = make_multiple_choice(
            capitals,
            n_questions=questions
        )

        write_quizfile(
            dict_quiz=dict_quiz_qa,
            # filename=f"Capitals Quiz Number {quiz_number} on {date_created}",
            filename="New Seed per Question {} on {}".format(
                quiz_number, date_created),
            str_header="\nNSpQ Quiz 2\nName:\nTime:%s" % date_created
        )

    return None


if __name__ == "__main__":
    main()
