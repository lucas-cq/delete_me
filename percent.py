def percentage() :
    try:
        user_input = input('How many questions did you get correct?: ')
        second_input = input('What was the total ammount of questions?: ')
        final_calc = int(user_input) / int(second_input) * 100
        print('You got ' + str(final_calc) + '%')
    except:
        print('Use a number silly')

percentage()