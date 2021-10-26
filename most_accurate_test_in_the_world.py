# this was the first program I wrote. I'm young and immature so this kind of thing was funny enough to motivate me to 
# code a test which was able to test multiple things i was working on from input to variables to f.write and more
# I was not learning everything in a natural order as you can tell

# This is degenerative insult humor, not meant to be taken seriously. This code is to test input capabilites as well as import and learning variable scope as well as saving results to external files for various purposes
# in future codes I have used this to create a video game with a battle simulator, until I rewrite that I will not be releasing it as the code is bulky and inefficient (as is this one) and there is no real additions to this code, just using it in wierd ways combined with a scoring system I tested in a derivitive of this code but for a different test with a scoring system

# these will import the elements needed for this to work
import time
import random
from results import results
from results import save_results
import os

# variable bank / these are just for the RNG
x = random.randint(0,3)
xxx = random.randint(0,1)
xxxxx = random.randint(0,100)

# I used camel case because this is my first program, give me a break
# question bank
# designed to slowly break away at the point, mislead them a bit at first
shoeSize = 'What size shoe do you wear?'
hairColor = 'What color is your hair?'
eyeColor = 'What color are your eyes?'
hieght = 'How tall are you?'
bodySize = 'What is your body type?'
palmSize = 'How big is your palm?'
fingerFold = 'When folding your fingers down, do any of them extend past your palm?'
pen15 = 'Are you satisfied with your size?'
reallytho = "But honestly, are you really ok with what you're working with?"
noBS = 'Honesty is imperative to an integral result, please do not lie. Are you actually content down there?'
bsFilter = 'If you have had any sexual partners, have they commented negatively on your size?'+'(if you have not had any partners please input 0)'
honesty = 'This is your last chance to get a real answer, have you ever been told it is small?'

# question list to call for function
questions = [shoeSize,hairColor,eyeColor,hieght,bodySize,palmSize,fingerFold,pen15,reallytho,noBS,bsFilter,honesty]


# runs the code
print('Hello and thank you for taking time to advance medical science today.')
print('This will help us advance society into the future as we can more accurately gauge if size matters once and for all and what we can do as a society to mitigate this.')
name_of_user = input('Before we begin here at the Soggy Doggy Medical Center with our test today, can we get a username for you? This will be used to store your data.\nPlease enter your name: ')
for question in questions:
    print(question)
    xx = input('Please Anwser Honestly: ')
    print('We asked', '"' + question + '"' + '. You said', '"' + xx + '"' + '. Is this correct?')
    yesOrNo = input() # doesnt matter what the user says. its easier this way and allows the questions to be anything and everything. much more funny in my humble opinion
    time.sleep(xxx)
    print('I hope that was the right answer, because we are moving forward!')
    response = 'Thank you again for your honest answer, this will advance medical science many years into the future.'
    time.sleep(xxx)
    print(response)
    time.sleep(xxx)

os.system('cls' if os.name == 'nt' else 'clear')
print('The test has concluded. Please prepare for accurate results delivered carefully to you. Remember, we really care about your feelings here at Soggy Doggy Pacer Medical Inc. You have helped so much today with science, thank you noble hero filled with valor.')
print(' ')
time.sleep(xxx)
store_as = results(xxxxx)
input('Would you like to save your results? ')
print('We understand the way you feel. Your results are saved to Correct_Results_Very_Conclusive_My_Most_Notable_Scientific_Contribution.txt')
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')
# Correct_Results_Very_Conclusive_My_Most_Notable_Scientific_Contribution.txt
save_results(store_as, name_of_user)
print('Thank you again for taking the time today to advance medical science. You\'re a hero, just not that much of one...')
time.sleep(x)
# I think overall this program was a success. I could have added more or chosen a more mature theme, but its simple and funny and has the perfect qty of lines.