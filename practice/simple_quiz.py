#  To develop a simple quiz system where end user has to answer set of questions
#  the quiz system takes his answers and calculates the grade based on the correct answers

#  Exercise : Simplified Quiz System

no_questions = 0
question_list = []
answer_list = []
counter = 0
correct_ans = 0


def file_reader(filename):
    global no_questions
    fo = open(filename, "r+")
    print("File opened:", fo.name)
    line = fo.readlines()

    # print(f'Reading Line:{line}')
    #  since txt file content fed into line, we can close it
    fo.close()
    for i in line:
        i.split('=')
        # print('Str:{}'.format(i.split('=')))
        no_questions += 1
        question_list.append(i.split('=')[0])
        answer_list.append(i.split('=')[1].split("\n")[0])


def exam_grade_calculator():
    global correct_ans, counter
    print(f'Welcome to the quiz-0')
    print(f'Total Number of Questions:{no_questions}')
    fo = open('result.txt', 'w')
    for counter in range(0, no_questions):
        print(f'Q{counter+1}: {question_list[counter]}')
        student_ans = input()
        if student_ans == answer_list[counter]:
            correct_ans += 1
    final_score = (correct_ans / no_questions)*100
    print('Your final score is {}'.format(final_score))
    fo.write('Your final score is {}'.format(final_score))
    fo.close()
    return final_score


file_reader("questions.txt")
# print(f'List of Questions:{question_list}')
# print(f'List of Expected Answers:{answer_list}')
# print(f'Total No of questions on Exam: {no_questions}')

exam_grade_calculator()





