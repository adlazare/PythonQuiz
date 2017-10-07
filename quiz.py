import random
import sys
import csv
import operator
import os


def user_login():
    # Initialize lists & open .csv file
    user_data = []
    user_name = []
    login_name = []
    login_pass = []

    with open('user_data.csv', 'r') as f:
        readCSV = csv.reader(f, delimiter=',')

        for row in readCSV:
            user_data.append(row)
            # print(row)

    # Generate list of user-names & passwords
    for x in range(len(user_data)):
        user_name.append(user_data[x][0])
        login_name.append(user_data[x][3])
        login_pass.append(user_data[x][4])



    print('Please login\nUsername: ')
    login_check = ''
    pass_actual = ''
    name = ''
    x = 1
    while x == 1:
        login_check = sys.stdin.readline()

        for i in range(len(login_name)):
            if login_name[i] == login_check[:-1]:
                # print('Found it!')
                pass_actual = login_pass[i]
                name = user_name[i]
                login_name2 = login_name[i]
                x = 0
                break
        if x == 1:
            print('Incorrect username.')
            print('Username: ')


    print('Password: ')
    x = 1
    while x == 1:
        pass_check = sys.stdin.readline()
        # print(pass_check)
        # print(pass_actual)

        if pass_check[:-1] != pass_actual:
            print('Incorrect password')
        else:
            x = 0

    print('Welcome %s!\n' % name)
    return(login_name2)


def user_registration():
    # Initialize array
    user_data = []
    # Get user input
    print('What is your name?')
    name = sys.stdin.readline()
    print('What is your age?')
    age = sys.stdin.readline()
    print('What year group are you in?')
    year_group = sys.stdin.readline()

    # creates username
    login = (name[0:3]) + age
    # print(login)

    print('Your username is: %s' % login)
    print('Please create a password:')
    password = sys.stdin.readline()

    user_data.append(name[:-1])
    user_data.append(age[:-1])
    user_data.append(year_group[:-1])
    user_data.append(login[:-1])
    user_data.append(password[:-1])
    # print(user_data)

    with open('user_data.csv', 'a') as f:
        f.write('\n')
        x = 0
        for i in user_data:
            x += 1
            if x < len(user_data):
                f.write(i + ',')
            else:
                f.write(i)


def quiz(username):
    # Initialize list of questions & separate into categories
    question_list = []
    with open('quiz_questions.csv', 'r') as f:
        readCSV = csv.reader(f, delimiter=',')

        for row in readCSV:
            question_list.append(row)

    history_set = question_list[0:4]
    music_set = question_list[4:8]
    compsci_set = question_list[8:12]

    # Quiz prompt
    print("Which topic would you like to take a quiz on: ")
    print(" 1. History")
    print(" 2. Music")
    print(" 3. Computer Science")
    x=1
    while x == 1:
        topic = sys.stdin.readline()
        topic = topic[:-1]

        if topic == '1':
            topic = 'History'
            question_set = history_set
            x = 0
        elif topic == '2':
            topic = 'Music'
            question_set = music_set
            x = 0
        elif topic == '3':
            topic = 'Computer Science'
            question_set = compsci_set
            x = 0
        else:
            print('Please select a valid option...')

    # Difficulty prompt
    print('Choose a quiz difficulty level: ')
    print(' 1. Easy')
    print(' 2. Medium')
    print(' 3. Hard')

    x = 1
    while x == 1:
        difficulty = sys.stdin.readline()
        difficulty = difficulty[:-1]

        if difficulty == '1':
            difficulty = 'Easy'

            # Administer the easy quiz
            score = 0
            print('You are taking the %s quiz on %s difficulty, good luck!\n' % (topic, difficulty))

            for x in range(0, 4):
                print('Question %i: %s' % (x + 1, question_set[x][0]))
                for y in range(0, 2):
                    # This increments the letter # for the answers
                    print('     %s) %s' % ((chr(ord('a') + y)), question_set[x][y + 1]))
                print('Choose an option: ')
                i = 1
                # Check the answer
                while i == 1:
                    answer = sys.stdin.readline()
                    answer = answer[:-1]

                    if answer == 'a':
                        answer_text = question_set[x][1]
                        i = 0
                    elif answer == 'b':
                        answer_text = question_set[x][2]
                        i = 0
                    else:
                        print('Please select a valid option...')

                # check answer - increment the y by 4 here since y is at 2 not 3
                if question_set[x][y + 4] == answer_text:
                    print("Correct!\n")
                    score += 1
                else:
                    print("Sorry, that is incorrect.\n")

            # print('You finished the quiz!\n')
            # print('Your score is %i\n' % score)
            x = 0
            x = 0
        elif difficulty == '2':
            difficulty = 'Medium'

            # Administer the medium quiz
            score = 0
            print('You are taking the %s quiz on %s difficulty, good luck!\n' % (topic, difficulty))

            for x in range(0, 4):
                print('Question %i: %s' % (x + 1, question_set[x][0]))
                for y in range(0, 3):
                    # This increments the letter # for the answers
                    print('     %s) %s' % ((chr(ord('a') + y)), question_set[x][y + 1]))
                print('Choose an option: ')
                i = 1
                # Check the answer
                while i == 1:
                    answer = sys.stdin.readline()
                    answer = answer[:-1]

                    if answer == 'a':
                        answer_text = question_set[x][1]
                        i = 0
                    elif answer == 'b':
                        answer_text = question_set[x][2]
                        i = 0
                    elif answer == 'c':
                        answer_text = question_set[x][3]
                        i = 0
                    else:
                        print('Please select a valid option...')

                # check answer - increment the y by 3 here since y is at 3 not 4
                if question_set[x][y + 3] == answer_text:
                    print("Correct!\n")
                    score += 1
                else:
                    print("Sorry, that is incorrect.\n")

            # print('You finished the quiz!\n')
            # print('Your score is %i\n' % score)
            x = 0
        elif difficulty == '3':
            difficulty = 'Hard'

            # Administer the hard quiz
            score = 0
            print('You are taking the %s quiz on %s difficulty, good luck!\n' % (topic, difficulty))

            for x in range(0, 4):
                print('Question %i: %s' % (x + 1, question_set[x][0]))
                for y in range(0, 4):
                    # This increments the letter # for the answers | I used (4-y) to increment here,
                    # so the correct answer will not always be either a) or b)
                    print('     %s) %s' % ((chr(ord('a') + y)), question_set[x][4-y]))
                print('Choose an option: ')
                i = 1
                # Check the answer
                while i == 1:
                    answer = sys.stdin.readline()
                    answer = answer[:-1]

                    if answer == 'a':
                        answer_text = question_set[x][4]
                        i = 0
                    elif answer == 'b':
                        answer_text = question_set[x][3]
                        i = 0
                    elif answer == 'c':
                        answer_text = question_set[x][2]
                        i = 0
                    elif answer == 'd':
                        answer_text = question_set[x][1]
                        i = 0
                    else:
                        print('Please select a valid option...')

                # check answer
                if question_set[x][y + 2] == answer_text:
                    print("Correct!\n")
                    score += 1
                else:
                    print("Sorry, that is incorrect.\n")

            # print('You finished the quiz!\n')
            # print('Your score is %i\n' % score)
            x = 0
        else:
            print('Please select a valid option...')

    # Print out score & grade & percentage
    print('You finished the quiz! Here are your results:\n')
    print('     Score: %i\n' % score)
    percentage = ((float(score) / 4.0) * 100)
    print('     Percentage: %i %%\n' % percentage)
    grade = ''
    if score == 0:
        grade = 'F'
    elif score == 1:
        grade = 'D'
    elif score == 2:
        grade = 'C'
    elif score == 3:
        grade = 'B'
    elif score == 4:
        grade = 'A'
    print('     Grade: %s\n\n' % grade)

    # Store quiz results in .csv file
    quiz_results = [topic, difficulty, username, str(score)]
    with open('quiz_data.csv', 'a') as f:
        f.write('\n')
        x = 0
        for i in quiz_results:
            x += 1
            if x < len(quiz_results):
                f.write(i + ',')
            else:
                f.write(i)


def quiz_report(history_quizzes, music_quizzes, compsci_quizzes):
    chosen_quiz_list = []
    modified_quiz_list = []
    topic = ''
    difficulty = ''

    # Prompt user to select a quiz topic
    print('Choose a quiz topic to generate a report for: ')
    print('     1. History\n     2. Music\n     3. Computer Science\n')

    i = 1
    while i == 1:
        input = sys.stdin.readline()
        input = input[:-1]

        if input == '1':
            topic = 'History'
            chosen_quiz_list = history_quizzes
            i = 0
        elif input == '2':
            topic = 'Music'
            chosen_quiz_list = music_quizzes
            i = 0
        elif input == '3':
            topic = 'Computer Science'
            chosen_quiz_list = compsci_quizzes
            i = 0
        else:
            print('Please select a valid option...\n')

    # Prompt user to select a quiz difficulty
    print('Choose a difficulty to generate a report for: ')
    print('     1. Easy\n     2. Medium\n     3. Hard\n')

    i = 1
    while i == 1:
        input = sys.stdin.readline()
        input = input[:-1]

        if input == '1':
            difficulty = 'Easy'
            # Separate data into individual lists
            for x in range(len(chosen_quiz_list)):
                if chosen_quiz_list[x][1] == 'Easy':
                    modified_quiz_list.append(chosen_quiz_list[x])
            i = 0
        elif input == '2':
            difficulty = 'Medium'
            # Separate data into individual lists
            for x in range(len(chosen_quiz_list)):
                if chosen_quiz_list[x][1] == 'Medium':
                    modified_quiz_list.append(chosen_quiz_list[x])
            i = 0
        elif input == '3':
            difficulty = 'Hard'
            # Separate data into individual lists
            for x in range(len(chosen_quiz_list)):
                if chosen_quiz_list[x][1] == 'Hard':
                    modified_quiz_list.append(chosen_quiz_list[x])
            i = 0
        else:
            print('Please select a valid option...\n')

    highscore = 0
    average_score = 0.0
    # Find the high score & username of the high scorer
    for x in range(len(modified_quiz_list)):
        score = int(modified_quiz_list[x][3])
        if score > highscore:
            highscore = score
            highscorer = modified_quiz_list[x][2]

    for x in range(len(modified_quiz_list)):
        average_score += int(modified_quiz_list[x][3])

        if (x + 1) == int(len(modified_quiz_list)):
            average_score = float(average_score) / float(x+1)

    print('Here is the report for the %s quiz on %s difficulty: ' % (topic, difficulty))
    print('     High Score: %s\n     High Scorer: %s\n     Average Score: %s\n' % (highscore, highscorer, average_score))

    generate_report()


def user_report(quiz_data):
    print('Inside user_report')
    user_list = []
    unique_users = []
    selected_user_quiz_data = []
    selected_user = ''

    # Extract the list of users from the data set
    for x in range(len(quiz_data)):
        user_list.append(quiz_data[x][2])

    # Convert list to a set & back to list to create a list of unique user names
    unique_users = list(set(user_list))

    # Prompt user to select a username
    print('Type the username of the user you want to generate a report for: ')
    for x in range(len(unique_users)):
        print('     %s' % unique_users[x])

    # Check users input & store selected username
    i = 1
    while i == 1:
        input = sys.stdin.readline()
        input = input[:-1]

        for x in range(len(unique_users)):
            if input == unique_users[x]:
                selected_user = unique_users[x]
                print('Selected user: %s' % selected_user)
                i = 0
        if selected_user == '':
            print('Please select a valid option...\n')

    # Print out user report
    print('Here is the quiz report for \'%s\':' % selected_user)

    # Filter the quiz_data list for the selected users quizzes
    for x in range(len(quiz_data)):
        if quiz_data[x][2] == selected_user:
            selected_user_quiz_data.append(quiz_data[x])

    for x in range(len(selected_user_quiz_data)):
        print('   Quiz #%i' % (x + 1))
        print('     Topic:      %s\n     Difficulty: %s\n     Score:      %s\n' % (selected_user_quiz_data[x][0], selected_user_quiz_data[x][1], selected_user_quiz_data[x][3]))

    generate_report()


def generate_report():
    # Store quiz results in .csv file
    quiz_data = []

    history_quizzes = []
    music_quizzes = []
    compsci_quizzes = []

    with open('quiz_data.csv', 'r') as f:
        readCSV = csv.reader(f, delimiter=',')

        for row in readCSV:
            quiz_data.append(row)
            # print(row)

    # Separate data into individual lists
    for x in range(len(quiz_data)):
        if quiz_data[x][0] == 'History':
            history_quizzes.append(quiz_data[x])
        if quiz_data[x][0] == 'Music':
            music_quizzes.append(quiz_data[x])
        if quiz_data[x][0] == 'Computer Science':
            compsci_quizzes.append(quiz_data[x])

    # Prompt user to select an option
    print('Choose an option: ')
    print('     1. Generate a quiz report\n     2. Generate a user report\n     3. Exit\n')

    i = 1
    while i == 1:
        input = sys.stdin.readline()
        input = input[:-1]

        if input == '1':
            quiz_report(history_quizzes, music_quizzes, compsci_quizzes)
            i = 0
        elif input == '2':
            user_report(quiz_data)
            i = 0
        elif input == '3':
            exit()
            i = 0
        else:
            print('Please select a valid option...\n')


def homebase(username):
    # Prompt user for input
    i = 1
    while i == 1:
        print('Please select an option (type 1, 2 or 3): ')
        print('     1. Take a Quiz\n     2. Generate Report\n     3. Exit')
        input = sys.stdin.readline()
        input = input[:-1]

        if input == '1':
            quiz(username)
        elif input == '2':
            generate_report()
        elif input == '3':
            exit()
        else:
            print('Please select a valid option...\n')


# Begin program
print('Welcome! Please select an option (type 1, 2 or 3):')
print('     1. Login\n     2. Register\n     3. Generate Report')

# Check input & run respective function
i = 1
while i == 1:
    input = sys.stdin.readline()
    input = input[:-1]

    if input == '1':
        username = user_login()
        homebase(username)
        i = 0
    elif input == '2':
        user_registration()
        username = user_login()
        homebase(username)
        i = 0
    elif input == '3':
        generate_report()
        i = 0
    else:
        print('Please select a valid option...\n')
