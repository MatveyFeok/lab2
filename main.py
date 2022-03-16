import csv


dialog = ('Какой жанр вас интересует?',
          'Какая минимальная оценка?',
          'Какое минимальное количество отзывов должно быть?',
          'Каких предупреждений не должно быть?',
          'Какой формат анимэ вас устроит?',
          'Какое минимальное количество эпизодов?',
          'Анимэ должно быть закончено? Введите True или False.',
          'Какой год начала съемки анимэ вас интересует?',
          'Какой год окончания съемки анимэ вас интересует?',
          'Какой сезон съемки анимэ вам нужен?',
          'Какая студия вас интересует?'
         )

question = (
    'Tags',
    'Rating Score',
    'Number Votes',
    'Content Warning',
    'Type',
    'Episodes',
    'Finished',
    'StartYear',
    'EndYear',
    'Season',
    'Studios'
)
answer_equal = {
    'Type': '',
    'Finished': '',
    'StartYear': '',
    'EndYear': ''
}
answer_more = {
    'Rating Score': '',
    'Number Votes': '',
    'Episodes': ''
}
answer_in = {
    'Tags': '',
    'Season': '',
    'Studios': ''
}
answer_not_in = {
    'Content Warning': ''
}
answers = [answer_in, answer_not_in, answer_more, answer_equal]



def is_equal(answer_in, entry):
    if answer_in in ('', entry):
        return True
    else:
        return False


def is_more(answer_in, entry):
    if answer_in == '':
        answer_in = float(0)
    if entry == 'Unknown':
        entry = float(0)
    if float(answer_in) <= float(entry):
        return True
    else:
        return False


def is_in(answer_in, entry):
    if answer_in in entry:
        return True
    else:
        return False


def is_not_in(answer_in, entry):
    if answer_in in entry:
        return False
    else:
        return True




def save_answer(ans, q_type, answers):
    for answer_gr in answers:
        if q_type in answer_gr:
            answer_gr[q_type] = ans


for k in range(len(dialog)):
    ans = input(dialog[k])
    save_answer(ans, question[k], answers)


answer = []

with open('anime.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        good = True
        for key, val in answer_equal.items():
            good = good and is_equal(val, row[key])

        for key, val in answer_more.items():
            good = good and is_more(val, row[key])

        for key, val in answer_in.items():
            for j in val.split():
                good = good and is_in(j, row[key])

        for key, val in answer_not_in.items():
            for j in val.split():
                good = good and is_not_in(j, row[key])

        if good:
            if row['Rating Score'] == 'Unknown':
                answer.append([float(0), row['Url'], row['Name']])
            else:
                answer.append([float(row['Rating Score']), row['Url'], row['Name']])
answer.sort()
answer.reverse()
f = open('result.txt', 'w', encoding='utf-8')
for i in range(len(answer)):
    f.write(answer[i][2] + ': ' + answer[i][1] + '\n')
f.close()

print('\n' + 'Готово')
