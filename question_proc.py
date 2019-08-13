import random

questions_per_chapter = {
    4: 11,
    5: 20,
    6: 13,
    7: 13,
    8: 9,
    9: 16,
    10: 6,
    11: 10,
    12: 12,
    13: 12,
    14: 11,
    15: 10,
    16: 12,
    17: 8,
    18: 8
}

done = {
    4: [],
    5: [7, 13],
    6: [],
    7: [4],
    8: [3, 9],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [9],
    14: [],
    15: [],
    16: [],
    17: [6],
    18: []
}


def random_question(questions_per_chapter, done):
    available_questions = []
    for chapter, max in questions_per_chapter.items():
        for question in range(1, max + 1):
            if question not in done[chapter]:
                available_questions.append(str(chapter) + '.' + str(question))

    print('not done: ', len(available_questions))
    return random.choice(available_questions)


print(random_question(questions_per_chapter, done))



