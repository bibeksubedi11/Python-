money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000,
         10000000]


# function to print the money
def win_money(correct_answer):
    print(money[correct_answer - 1])
    if money[correct_answer - 1] == 10000:
        print("Congrats!you have completed first round.")
    elif money[correct_answer - 1] == 320000:
        print("Congrats! You have completed second roound.")
    elif money[correct_answer - 1] == 10000000:
        print("Congrats! you have won 1 corror rupees.")


def start():
    name = str(input("your name is = :"))
    print("Hello ",name ,"lets play ko bancha cororpati")
    # Question list for bibek
    question = [
        "By what abbreviation is a compact disc commonly known?",
        "Which colour is used as a term to describe an illegal market in rare goods?",
        "In which country would you expect to be greeted with the word 'bonjour'?",
        "Which country is not an island?",
        "What is the name of the instrument panel in a car?",
        "What copy can be said to describe something identical?",
        "Which country is not crossed by the Arctic Circle?",
        "According to the saying, which of these is 'a dish best served cold'?",
        "With which activity is the phrase 'going, going, gone' most associated?",
        "Which of these is a theory about the creation of the universe?",
        "What would be used to boost an electrical signal?",
        "What term is used for the whole of the background of a flag?",
        "Which creatures are traditionally kept in an aviary?",
        "By what name is sodium carbonate commonly known?",
        "Which of these is not a European river?",
        "In football who is the word GOAT reffered to?",

    ]
    # Option for the game
    first_option = [
        "CD", "Blue", "Italy", "Madagascar", "Chargeboard", "Oxygen", "Norway", "Revenge", "An auction", "Big Bong",
        "Ambrosia", "Meadow", "Birds", "Soda biscuit", "Danube", "Ronaldo"

    ]
    second_option = [
        "COD", "Red", "France", "Cuba", "Sprintboard", "Hydrogen", "Finland", "Cottage pie", "Gardening", "Big Bang",
        "Amphitheatre", "Lea", "Fish", "Soda bread", "Rhine", "pele"

    ]
    third_option = [

        "CDIS", "Black", "Spain", "Germany", "Dashboard", "Nitrogen", "Greece", "Custard", "Horse racing", "Big Ben",
        "Amphetamine", "Pasture", "Reptiles", "Washing soda", "Seine", "Messi"
    ]
    fourth_option = [

        "COMPD", "White", "Wales", "Jamaica", "Jogboard", "Carbon", "Sweeden", "Stew", "Boxing", "Big Bertha",
        "Amplifier", "Field", "Insects", "Lime and soda", "Missouri", "Maradona"
    ]
    # All option are kept in it for easy use
    all_option = [
        first_option, second_option,
        third_option, fourth_option
    ]
    # For iterating till user doesn't gives wrong answer
    wrong_answer = False
    # For counting at which level the user is
    correct_answer = 0
    # List for keeping record of all answer in sequence wise
    ans_key = [0, 2, 1, 2, 2, 3, 2, 0, 0, 1, 3, 3, 0, 2, 3, 2]
    stage = 0

    # Games  begins from here
    while (wrong_answer != True):
        # variable used to pick the questions from the list

        # prints the question from the list
        print("Q." + question[stage])

        # prints the option
        for Number, option in enumerate(all_option):
            print(str(Number + 1) + ". " + option[stage])
        # Takes the input of the user
        answer = int(input("Please give your answer: "))

        key = (ans_key[stage] + 1)
        # checks if the answer is correct or not
        if key == answer:
            print("Congrats!",name,"your answer is correct. You have won : Rs", end="")
            correct_answer += 1
            win_money(correct_answer)
        else:
            print("Sorry! Wrong answer. You can go home now with the money you won!!! ")
            correct_answer = 0
            wrong_answer = True
        # checks if it is the last level or not
        if (correct_answer == 15):
            break
        stage += 1


def main():
    start()
    while input("Play again? (y/n) : ").upper() == "Y":
        start()
    print("See you again")

if __name__ == '__main__':
    main()
