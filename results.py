import time

def results(x):
    if x > 99:
        print('Wow bro, thats almost average, nice cock!.')
    elif x < 99 and x > 87:
        print('Hey buddy, are you sure that'+"'s not a clitoris? We both know you've never seen one in person, maybe thats whats happening now...")
    elif x < 87 and x > 82:
        print("That's a cock only a father could love.")
    elif x < 82 and x > 76:
        print("That's a cock not even a father could love.")
    elif x < 76 and x > 71:
        print('Oh, you have a micropenis for sure dude.')
    elif x < 71 and x > 69:
        print('I bet you haven'+"'t seen that thing since the last time a prostitute left your musty motel room because they couldn't seeanything other than tic tacs below your belt.")
    elif x < 69 and x > 55:
        print('I bet the first time you go to use that disgrace of a cock, they'"'ll tell you to stop stabbing them with that thumbtack.")
    elif x < 55 and x > 47:
        print('Calling you a pencil dick would be a complement to say the least. You may want to rerun howbig.py to get a more accurate response.')
    elif x < 47 and x > 42:
        print("Don't worry, I'm sure it will grow some more when you hit puberty.")
    elif x < 42 and x > 37:
        print('That'+"'s a cock not even a mother could love.")
    elif x < 37 and x > 35:
        print('This test is a sham made by the developer to insult you repeatedly so that you will send this to your friends to insult them.')
    elif x < 35 and x > 27:
        print('Ok, so you can'"'t do it legally, but I, as would all your "'"future" partners would highly advise some back alley late night penis extenstion services, just make sure you take some valium before you do.')
    elif x < 27 and x > 18:
        print('I would tell you that its pathetic, but we both know you already know that.')
    else:
        print("Look at that, you're perfectly average.")
        time.sleep(2)
        print('...')
        time.sleep(.33)
        print('...')
        time.sleep(.17)
        print('...')
        time.sleep(.17)
        print('...')
        print("Was that implied for human size?")
        time.sleep(.75)
        print('.....................')
        time.sleep(3)
        print('Just to clarify, I meant its average for a shrew, as in the rodent...')
    return x

def save_results(x, name):
    counter = 0
    with open('Correct_Results_Very_Conclusive_My_Most_Notable_Scientific_Contribution.txt', 'w') as f:
        f.write(f'Conclusive Results for {name}')
        while counter < 3:
            f.write('\n...........')
            counter +=1
        counter -= 3
        f.write('\nHello '+ name + '.\n')
        if x > 99:
            f.write('Wow bro, thats almost average, nice cock!.')
        elif x < 99 and x > 87:
            f.write('Hey buddy, are you sure that'+"'s not a clitoris? We both know you've never seen one in person, maybe thats whats happening now...")
        elif x < 87 and x > 82:
            f.write("That's a cock only a father could love.")
        elif x < 82 and x > 76:
            f.write("That's a cock not even a father could love.")
        elif x < 76 and x > 71:
            f.write('Oh, you have a micropenis for sure dude.')
        elif x < 71 and x > 69:
            f.write('I bet you haven'+"'t seen that thing since the last time a prostitute left your musty motel room because they couldn't seeanything other than tic tacs below your belt.")
        elif x < 69 and x > 55:
            f.write('I bet the first time you go to use that disgrace of a cock, they'"'ll tell you to stop stabbing them with that thumbtack.")
        elif x < 55 and x > 47:
            f.write('Calling you a pencil dick would be a complement to say the least. You may want to rerun howbig.py to get a more accurate response.')
        elif x < 47 and x > 42:
            f.write("Don't worry, I'm sure it will grow some more when you hit puberty.")
        elif x < 42 and x > 37:
            f.write('That'+"'s a cock not even a mother could love.")
        elif x < 37 and x > 35:
            f.write('This test is a sham made by the developer to insult you repeatedly so that you will send this to your friends to insult them.')
        elif x < 35 and x > 27:
            f.write('Ok, so you can'"'t do it legally, but I, as would all your "'"future" partners would highly advise some back alley late night penis extenstion services, just make sure you take some valium before you do.')
        elif x < 27 and x > 18:
            f.write('I would tell you that its pathetic, but we both know you already know that.')
        else:
            f.write("Look at that, you're perfectly average.")
            f.write('...')
            f.write('...')
            f.write('...')
            f.write("Was that implied for human size?")
            f.write('.....................')
            f.write('Just to clarify, I meant its average for a shrew, as in the rodent...')
        f.write("\nThank you for taking your time to complete this test.")
        f.write('\nPlease remember that these results are real and authoritative. What follows is an authentic Soggy Doggy Diagnosis\n')
    print('Please leave us a five star review on Yelp!')

