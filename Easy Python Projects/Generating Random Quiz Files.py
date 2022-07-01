import random

# quiz data, keys are states and values are their capitals
capitals = {
    'Himachal Pradesh'      : 'Shimla',
    'Punjab'                : 'Chandigarh',
    'Haryana'               : 'Chandigarh',
    'Uttarakhand'           : 'Dehradun',
    'Rajasthan'             : 'Jaipur',
    'Madhya Pradesh'        : 'Bhopal',
    'Uttar Pradesh'         : 'Lucknow',
    'Gujarat'               : 'Gandhinagar',
    'Chhatisgarh'           : 'Raipur',
    'Orissa'                : 'Bhubaneswar',
    'Bihar'                 : 'Patna',
    'Jharkhand'             : 'Ranchi',
    'West Bengal'           : 'Kolkata',
    'Sikkim'                : 'Gangtok',
    'Assam'                 : 'Dispur',
    'Meghalaya'             : 'Shillong',
    'Arunachal Pradesh'     : 'Itanagar',
    'Nagaland'              : 'Kohima',
    'Manipur'               : 'Imphal',
    'Mizoram'               : 'Aizwal',
    'Tripura'               : 'Agartala',
    'Maharashtra'           : 'Mumbai',
    'Telangana'             : 'Hyderabad',
    'Andhra Pradesh'        : 'Amravati',
    'Goa'                   : 'Panji',
    'Karnataka'             : 'Bengaluru',
    'Tamil Nadu'            : 'Chennai',
    'Kerala'                : 'Tiruvananthpuram'
}

# generate 10 quiz files
for quizNum in range(5):
    # create quiz file and answer key file
    quizFile = open('Capitals Quiz %s.txt' % (quizNum + 1), 'w')
    answerkeyFile = open(f'Capitals Quiz %s Answers.txt' % (quizNum + 1), 'w')

    # write down the header for quiz file
    quizFile.write('Name :\n\nDate :\n\nPeriod :\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz - Set %s' % (quizNum + 1))
    quizFile.write('\n\n')

    # shuffle the order of states
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all the 28 states, making a question for each
    for questionNum in range(28):
        # get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # write the question and the answer options to the quiz file
        quizFile.write('%s. What is the capital of %s ?\n' % (questionNum + 1, states[questionNum]))

        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # write the answer to the answerkey file
        answerkeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerkeyFile.close()
