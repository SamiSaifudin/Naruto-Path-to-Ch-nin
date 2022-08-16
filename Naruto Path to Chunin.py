from time import sleep
import sys
import random
from random import randint,choice

def greeting_user():
 print("Naruto: Path to Chunin\n")
 name = input("Enter your first name here: ")
 print(f"Hello {name}, welcome to the Hidden Leaf Village.\n")
 sleep(2.0)
 print("Currently, you are just a measily genin with no respect.\n")
 sleep(2.0)
 print("Do not worry, your opportunity to shine is here with the Chunin Exams!\n")
 sleep(2.0)

def user_customization():
 print("Before we get started, lets customize your experience.\n")
 sleep(2.0)
 while True:
   clan = input("Choose your clan! [Uchiha, Nara, Uzumaki, Hyuga, Aburame, Akimichi, Yamanaka, Inuzuka] Enter here: ").upper()
   sleep(2.0)
   if clan == "UCHIHA":
       print("How much can you see with those Sharingan of yours?\n")
       break
   elif clan == "NARA":
       print("This process must be a drag for you.\n")
       break
   elif clan == "UZUMAKI":
       print("Full of Chakra and energy, you know!\n")
       break
   elif clan == "HYUGA":
       print("Can you live up to your family's name with those eyes?\n")
       break
   elif clan == "ABURAME":
       print("Bugs? Really? Guess its your type.\n")
       break
   elif clan == "AKIMICHI":
       print("You just came back from lunch, didn't you?\n")
       break
   elif clan == "YAMANAKA":
       print("Are you reading my mind right now?\n")
       break
   elif clan == "INUZUKA":
       print("Dogs>Cats huh? Debatable.\n")
       break
   else:
       print("Invalid Operator")
       continue

def pick_friends():
 print("You will now get to pick your Sensei and Teammates.\n")
 sleep(2.0)
 while True:
   sensei = input("Choose your sensei! [Kakashi Hatake, Might Guy, Asuma Sarutobi, Kurenai Yuhi] Enter Here: ").upper()
   sleep(2.0)
   if sensei == "KAKASHI HATAKE" or sensei == "KAKASHI":
       print("The Leaf's top Jonin. High expectations will be placed on you.\n")
       break
   elif sensei == "MIGHT GUY" or sensei == "GUY":
       print("Get ready to swim in the fountain of youth.\n")
       break
   elif sensei == "ASUMA SARUTOBI" or sensei == "ASUMA":
       print("Laid back but always down for a game of Shogi.\n")
       break
   elif sensei == "KURENAI YUHI" or sensei == "KURENAI":
       print("Be careful not to get caught in her genjutsu.\n")
       break
   else:
       print("Invalid Operator")
       continue
 sleep(2.0)
 while True:
   teamate_1 = input("Choose your first teamate. [Sasuke Uchiha, Naruto Uzumaki, Sakura Haruno, Shikamaru Nara, Choji Akimichi, Ino Yamanaka, Hinata Hyuga, Kiba Inuzuka, Shino Aburame, Rock Lee, Neji Hyuga, Tenten] Enter here: ").upper()
   sleep(2.0)
   if teamate_1 == "SASUKE UCHIHA" or teamate_1 == "SASUKE":
       print("The Leaf's top Rookie and a last of his kind.\n")
       break
   elif teamate_1 == "NARUTO UZUMAKI" or teamate_1 == "NARUTO":
       print("No need to worry about motivating this guy. This kid has eyes set on big things.\n")
       break
   elif teamate_1 == "SAKURA HARUNO" or teamate_1 == "SAKURA":
       print("Just don't try to get on her nerves.\n")
       break
   elif teamate_1 == "SHIKAMARU NARA" or teamate_1 == "SHIKAMARU":
       print("This guy may need a little motivating, but his strategic mind will be beneficial in battle.\n")
       break
   elif teamate_1 == "CHOJI AKIMICHI" or teamate_1 == "CHOJI":
       print("Your going to have to share your lunch from now on.\n")
       break
   elif teamate_1 == "INO YAMANAKA" or teamate_1 == "INO":
       print("Set her up, and you got a battle won with her mind transfer jutsu.\n")
       break
   elif teamate_1 == "HINATA HYUGA" or teamate_1 == "HINATA":
       print("Shy but is suprisingly skilled.\n")
       break
   elif teamate_1 == "KIBA INUZUKA" or teamate_1 == "KIBA":
       print("Your a dog person from now on.\n")
       break
   elif teamate_1 == "SHINO ABURAME" or teamate_1 == "SHINO":
       print("Quiet and reserved but reliable in battle.\n")
       break
   elif teamate_1 == "ROCK LEE" or teamate_1 == "LEE":
       print("Hard work is the motto.\n")
       break
   elif teamate_1 == "NEJI HYUGA" or teamate_1 == "NEJI":
       print("The Leaf's top Genin. You will have to earn his respect.\n")
       break
   elif teamate_1 == "TENTEN" or teamate_1 == "TEN TEN" or teamate_1 == "TEN-TEN":
       print("Weapons Specialist with a lot to offer.\n")
       break
   else:
       print("Invalid Operator")
       continue
 sleep(2.0)
 while True:
   teamate_2 = input("Choose your second teamate. [Sasuke Uchiha, Naruto Uzumaki, Sakura Haruno, Shikamaru Nara, Choji Akimichi, Ino Yamanaka, Hinata Hyuga, Kiba Inuzuka, Shino Aburame, Rock Lee, Neji Hyuga, Tenten] Enter here: ").upper()
   sleep(2.0)
   if teamate_2 == teamate_1:
       print("Sorry. Can't pick the same teamate twice!\n")
       continue
   elif teamate_2 == "SASUKE UCHIHA" or teamate_2 == "SASUKE":
       print("The Leaf's top Rookie and a last of his kind.\n")
       break
   elif teamate_2 == "NARUTO UZUMAKI" or teamate_2 == "NARUTO":
       print("No need to worry about motivating this guy. This kid has eyes set on big things.\n")
       break
   elif teamate_2 == "SAKURA HARUNO" or teamate_2 == "SAKURA":
       print("Just don't try to get on her nerves.\n")
       break
   elif teamate_2 == "SHIKAMARU NARA" or teamate_2 == "SHIKAMARU":
       print("This guy may need a little motivating, but his strategic mind will be beneficial in battle.\n")
       break
   elif teamate_2 == "CHOJI AKIMICHI" or teamate_2 == "CHOJI":
       print("Your going to have to share your lunch from now on.\n")
       break
   elif teamate_2 == "INO YAMANAKA" or teamate_2 == "INO":
       print("Set her up, and you got a battle won with her mind transfer jutsu.\n")
       break
   elif teamate_2 == "HINATA HYUGA" or teamate_2 == "HINATA":
       print("Shy but is suprisingly skilled.\n")
       break
   elif teamate_2 == "KIBA INUZUKA" or teamate_2 == "KIBA":
       print("Your a dog person from now on.\n")
       break
   elif teamate_2 == "SHINO ABURAME" or teamate_2 == "SHINO":
       print("Quiet and reserved but reliable in battle.\n")
       break
   elif teamate_2 == "ROCK LEE" or teamate_2 == "LEE":
       print("Hard work is the motto.\n")
       break
   elif teamate_2 == "NEJI HYUGA" or teamate_2 == "NEJI":
       print("The Leaf's top Genin. You will have to earn his respect.\n")
       break
   elif teamate_2 == "TENTEN" or teamate_2 == "TEN TEN" or teamate_2 == "TEN-TEN":
       print("Weapons Specialist with a lot to offer.\n")
       break
   else:
       print("Invalid Operator")
       continue

 sleep(2.0)
 print(f"Welcome to team {sensei} with {teamate_1} and {teamate_2}!\n")

def written_exam():
   print("The stage is set and the teams are ready, now lets head to the first round: The Written Exam.\n")
   sleep(2.0)
   print("You will be asked a series of questions testing your knowledge of the Shinobi world.\n")
   sleep(2.0)
   print("The exam consists of 8 questions and you must get 6/8 correct in order to advance.\n")
   sleep(2.0)
   print("This written exam isn't a walk in a park. Don't get caught cheating or else that is an automatic disqualification.\n")
   sleep(5.0)
   while True:
       ready = input("Are you ready? Yes or No. Enter Here: ").upper()
       if ready == "YES":
           print("ALRIGHT!\n")
           break
       if ready == "NO":
           print("HURRY UP!\n")
           continue
       else:
           print("Invalid Operator")
           continue
   sleep(2.0)
   print("1")
   sleep(1.0)
   print("2")
   sleep(1.0)
   print("3")
   sleep(1.0)
   print("GO!")

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is the title name of the leader of the Hidden Leaf Village?\n(a) Hokage\n(b) Kazekage\n(c) Tsuchikage\n(d) Raikage\n\n",
    "What is the ninja rank after chunin?\n(a) Hokage\n(b) Genin\n(c) Jonin\n(d) Anbu\n\n",
    "Who is the second hokage?\n(a) Tobirama Senju\n(b) Hiruzen Sarutobi\n(c) Danzo\n(d) Hashirama Senju\n\n",
    "Who is responsible for creating the rule that every squad must be accompanied by a medical ninjutsu user?\n(a) Jiraiya\n(b) Danzo\n(c) Hiruzen Sarutobi\n(d) Tsunade\n\n",
    "Who is not a member of the three legendary Sanin?\n(a) Jiraiya\n(b) Kakashi\n(c) Orochimaru\n(d) Tsunade\n\n",
    "So far, how many great ninja wars have occured in history?\n(a) 5\n(b) 3\n(c) 2\n(d) 4\n\n",
    "What current Hidden leaf clan is endangered?\n(a) Uchiha\n(b) Nara\n(c) Inuzuka\n(d) Aburame\n\n",
    "Who is the greatest prodigy to come out of the academy?\n(a) Hiruzen Sarutobi\n(b) Neji Hyuga\n(c) Itachi Uchiha\n(d) Hashirama Senju\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct")
    while True:
        if score < 6:
            print("You have failed the written exam. Try again next year.\n")
            return sys.exit()
        if score >= 6:
            print("Congrats. You have ALMOST passed the written exam. There is one more question for you to answer which will decide your fate.\n")
            break
    while True:
        do_or_die = input("Did you cheat on this exam?\n(a) Yes\n(b) No\n\n").upper()
        if do_or_die == "A":
            print("YOU PASS! This written exam was made for you to cheat. We created it to test your ability to strategize in difficult situations as this is an important skill for a squad leader to have.\n")
            break
        if do_or_die == "B":
            print("YOU FAIL! This written exam was made for you to cheat. If you did not, you have not displayed the current skills we are looking for in a Chunin. Come back next year!")
            return sys.exit()

def round_2():
    print("Welcome to the second round of the Chunin Exams: The Forest of Death.\n")
    sleep(2.0) 
    print("The rules are simple, your three man squad along with the other three man squads will be dropped into the forest with either a heaven or earth scroll.\n")
    sleep(2.0)
    print("In order to advance, you must reach the clock tower located in the middle of the forest with both a heaven and earth scroll.\n")
    sleep(2.0)
    print("In order to attain the other scroll you need, you will have to defeat enemies until you find one that so happens to have your opposite scroll.\n")
    sleep(2.0)
    print("Battles will work similarly to the game Rock/Paper/Scissors but instead with Ninjutsu/Taijutsu/Genjutsu.\n")
    sleep(2.0)
    print("Ninjutsu is weak against Genjutsu and strong against Taijutsu.\n")
    sleep(2.0)
    print("Genjutsu is weak against Taijutsu and strong against Ninjutsu.\n")
    sleep(2.0)
    print("Taijutsu is weak against Ninjutsu and strong against Genjutsu.\n")
    sleep(2.0)
    print("A match with an enemy will be a best out of three. If you defeat the enemy, you can take their scroll and check if it's the scroll you need.\n")
    sleep(2.0)
    while True:
        ready = input("Are you ready? Yes or No: ").upper()
        if ready == "YES":
            break
        elif ready == "NO":
            sleep(2.0)
            print("Well Hurry Up and understand the rules. We don't have all day here!\n")
            continue
        else:
            print("Invalid Operator")
            continue
    sleep(2.0)
    scrolls = ["Heaven", "Earth"]
    user_scroll = random.choice(scrolls)
    enemy_scroll = random.choice(scrolls)
    win_count = 0
    enemy_win_count = 0 
    wins_needed = 2    
    print(f"You are assigned an {user_scroll} scroll\n")
    sleep(2.0)
    print("Enemy Founded!!!\n")
    sleep(2.0)
    while True:
        enemy_scroll = random.choice(scrolls)
        user_pick = input("Choose Ninjutsu, Taijutsu, or Genjutsu: ").upper()
        print(f"Your Pick: {user_pick}")
        aI_pick = ["NINJUTSU", "TAIJUTSU", "GENJUTSU"]
        random_index = random.randrange(len(aI_pick))
        if user_pick == "NINJUTSU" and aI_pick[random_index]== "GENJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick[random_index]}")
            sleep(2.0)
            print("YOU LOSE THIS ROUND")
            sleep(2.0)
            enemy_win_count += 1
            print(f"Your enemy has {enemy_win_count}/2 wins and you have {win_count}/2 wins\n")
        elif user_pick == "NINJUTSU" and aI_pick[random_index]== "TAIJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick[random_index]}")
            sleep(2.0)
            print("YOU WIN THIS ROUND")
            sleep(2.0)
            win_count += 1
            print(f"Your enemy has {enemy_win_count}/2 wins and you have {win_count}/2 wins\n")
        elif user_pick == "NINJUTSU" and aI_pick[random_index]== "NINJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick[random_index]}")
            sleep(2.0)
            print("TIE")
            sleep(2.0)
            print(f"Your enemy has {enemy_win_count}/2 wins and you have {win_count}/2 wins\n")
        elif user_pick == "TAIJUTSU" and aI_pick[random_index]== "TAIJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick[random_index]}")
            sleep(2.0)
            print("TIE")
            sleep(2.0)
            print(f"Your enemy has {enemy_win_count}/2 wins and you have {win_count}/2 wins\n")
        elif user_pick == "TAIJUTSU" and aI_pick[random_index]== "GENJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick[random_index]}")
            sleep(2.0)
            print("YOU WIN THIS ROUND")
            sleep(2.0)
            win_count += 1
            print(f"Your enemy has {enemy_win_count}/2 wins and you have {win_count}/2 wins\n")
        elif user_pick == "TAIJUTSU" and aI_pick[random_index]== "NINJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick[random_index]}")
            sleep(2.0)
            print("YOU LOSE THIS ROUND")
            sleep(2.0)
            enemy_win_count += 1
            print(f"Your enemy has {enemy_win_count}/2 wins and you have {win_count}/2 wins\n")
        elif user_pick == "GENJUTSU" and aI_pick[random_index]== "GENJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick[random_index]}")
            sleep(2.0)
            print("TIE")
            sleep(2.0)
            print(f"Your enemy has {enemy_win_count}/2 wins and you have {win_count}/2 wins\n")
        elif user_pick == "GENJUTSU" and aI_pick[random_index]== "TAIJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick[random_index]}")
            sleep(2.0)
            print("YOU LOSE THIS ROUND")
            sleep(2.0)
            enemy_win_count += 1
            print(f"Your enemy has {enemy_win_count}/2 wins and you have {win_count}/2 wins\n")
        elif user_pick == "GENJUTSU" and aI_pick[random_index]== "NINJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick[random_index]}")
            sleep(2.0)
            print("YOU WIN THIS ROUND")
            sleep(2.0)
            win_count += 1
            print(f"Your enemy has {enemy_win_count}/2 wins and you have {win_count}/2 wins\n")
        else:
            sleep(2.0)
            print("Invalid Operator")
            sleep(2.0)
            continue
        sleep(2.0)
        if win_count == wins_needed and win_count>enemy_win_count:
            print("Congrats, you have defeated this enemy. Now lets take a look to see if they have the scroll you need.\n")
            sleep(2.0)
            print(f"This enemy had a {enemy_scroll} scroll.\n")
            sleep(2.0)
            if enemy_scroll == user_scroll:
                print("Looks like they do not have the scroll you need. Keep exploring and find new enemies that might have your scroll.\n")
                sleep(5.0)
                while True:
                    new_enemy = input("New Enemy Founded. Are you ready? Yes or No: ").upper()
                    if new_enemy == "YES":
                        break 
                    elif new_enemy == "NO":
                        sleep(2.0)
                        print("The enemy is waiting.\n")
                        sleep(2.0)
                        continue 
                    else:
                        print("Invalid Operator")
                        continue
                enemy_win_count -= enemy_win_count
                win_count -= win_count
                sleep(3.0)
                continue
            if enemy_scroll != user_scroll:
                print("Congrats, you now have both scrolls needed to advance!\n")
                break
        if enemy_win_count == wins_needed and enemy_win_count>win_count:
            print("Looks like you lost to this enemy. We can still check to see if they had the scroll you needed.\n")
            sleep(2.0)
            print(f"This enemy had a {enemy_scroll} scroll.\n")
            sleep(2.0)
            if enemy_scroll == user_scroll:
                print("Looks like they do not have the scroll you needed. Keep exploring and find new enemies that might have your scroll.\n")
                sleep(5.0)
                while True:
                    new_enemy = input("New Enemy Founded. Are you ready? Yes or No: ").upper()
                    if new_enemy == "YES":
                        break 
                    elif new_enemy == "NO":
                        sleep(2.0)
                        print("The enemy is waiting.\n")
                        sleep(2.0)
                        continue 
                    else:
                        print("Invalid Operator")
                        continue
                enemy_win_count -= enemy_win_count
                win_count -= win_count
                sleep(3.0)
                continue
            if enemy_scroll != user_scroll:
                print("Tough break. Keep exploring and try to find new enemies to challenge.\n")
                sleep(5.0)
                while True:
                    new_enemy = input("New Enemy Founded. Are you ready? Yes or No: ").upper()
                    if new_enemy == "YES":
                        break 
                    elif new_enemy == "NO":
                        sleep(2.0)
                        print("The enemy is waiting.\n")
                        sleep(2.0)
                        continue 
                    else:
                        print("Invalid Operator")
                        continue
                enemy_win_count -= enemy_win_count
                win_count -= win_count
                sleep(3.0)
                continue
            
def round2_boss():
    print("Good Job on defeating that enemy by the way. It should be smooth sailing from here on out.\n")
    sleep(2.0) 
    print("KABOOOOOOOOM!!!!\n")
    sleep(2.0)
    print("Oh no! It's an ambush from the Sound Village Ninja!\n")
    sleep(2.0)
    print("These shinobi are quite fierce and skilled and are looking to take one of your scrolls.\n")
    sleep(2.0)
    while True: 
        reminder = input("Do you need a quick reminder on the rules of how a battle works? Yes or No: ").upper() 
        if reminder == "YES":
            sleep(2.0)
            print("Battles will work similarly to the game Rock/Paper/Scissors but instead with Ninjutsu/Taijutsu/Genjutsu.\n")
            sleep(2.0)
            print("Ninjutsu is weak against Genjutsu and strong against Taijutsu.\n")
            sleep(2.0)
            print("Genjutsu is weak against Taijutsu and strong against Ninjutsu.\n")
            sleep(2.0)
            print("Taijutsu is weak against Ninjutsu and strong against Genjutsu.\n")
            sleep(5.0)
            break 
        elif reminder == "NO":
            break
        else:
            print("Invalid Operator")
            continue
    print("Due to this team being much stronger than the team you faught earlier, this battle will be a best out of seven rather than a best out of three.\n")        
    sleep(2.0)
    while True:
        ready = input("Are you ready? Yes or No: ").upper()
        if ready == "YES":
            break
        elif ready == "NO":
            sleep(2.0)
            print("Well Hurry Up. We don't have all day here!\n")
            continue
        else:
            print("Invalid Operator")
            continue
    sleep(2.0)
    boss_overall_win_count = 0 
    win_count_forboss = 0
    boss_win_count = 0 
    boss_wins_needed = 4
    while True:
        user_pick2 = input("Choose Ninjutsu, Taijutsu, or Genjutsu: ").upper()
        print(f"Your Pick: {user_pick2}")
        aI_pick2 = ["NINJUTSU", "TAIJUTSU", "GENJUTSU"]
        random_index2 = random.randrange(len(aI_pick2))
        if user_pick2 == "NINJUTSU" and aI_pick2[random_index2]== "GENJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick2[random_index2]}")
            sleep(2.0)
            print("YOU LOSE THIS ROUND")
            sleep(2.0)
            boss_win_count += 1
            print(f"Your enemy has {boss_win_count}/4 wins and you have {win_count_forboss}/4 wins\n")
        elif user_pick2 == "NINJUTSU" and aI_pick2[random_index2]== "TAIJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick2[random_index2]}")
            sleep(2.0)
            print("YOU WIN THIS ROUND")
            sleep(2.0)
            win_count_forboss += 1
            print(f"Your enemy has {boss_win_count}/4 wins and you have {win_count_forboss}/4 wins\n")
        elif user_pick2 == "NINJUTSU" and aI_pick2[random_index2]== "NINJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick2[random_index2]}")
            sleep(2.0)
            print("TIE")
            sleep(2.0)
            print(f"Your enemy has {boss_win_count}/4 wins and you have {win_count_forboss}/4 wins\n")
        elif user_pick2 == "TAIJUTSU" and aI_pick2[random_index2]== "TAIJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick2[random_index2]}")
            sleep(2.0)
            print("TIE")
            sleep(2.0)
            print(f"Your enemy has {boss_win_count}/4 wins and you have {win_count_forboss}/4 wins\n")
        elif user_pick2 == "TAIJUTSU" and aI_pick2[random_index2]== "GENJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick2[random_index2]}")
            sleep(2.0)
            print("YOU WIN THIS ROUND")
            sleep(2.0)
            win_count_forboss += 1
            print(f"Your enemy has {boss_win_count}/4 wins and you have {win_count_forboss}/4 wins\n")
        elif user_pick2 == "TAIJUTSU" and aI_pick2[random_index2]== "NINJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick2[random_index2]}")
            sleep(2.0)
            print("YOU LOSE THIS ROUND")
            sleep(2.0)
            boss_win_count += 1
            print(f"Your enemy has {boss_win_count}/4 wins and you have {win_count_forboss}/4 wins\n")
        elif user_pick2 == "GENJUTSU" and aI_pick2[random_index2]== "GENJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick2[random_index2]}")
            sleep(2.0)
            print("TIE")
            sleep(2.0)
            print(f"Your enemy has {boss_win_count}/4 wins and you have {win_count_forboss}/4 wins\n")
        elif user_pick2 == "GENJUTSU" and aI_pick2[random_index2]== "TAIJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick2[random_index2]}")
            sleep(2.0)
            print("YOU LOSE THIS ROUND")
            sleep(2.0)
            boss_win_count += 1
            print(f"Your enemy has {boss_win_count}/4 wins and you have {win_count_forboss}/4 wins\n")
        elif user_pick2 == "GENJUTSU" and aI_pick2[random_index2]== "NINJUTSU":
            sleep(2.0)
            print(f"Enemy pick: {aI_pick2[random_index2]}")
            sleep(2.0)
            print("YOU WIN THIS ROUND")
            sleep(2.0)
            win_count_forboss += 1
            print(f"Your enemy has {boss_win_count}/4 wins and you have {win_count_forboss}/4 wins\n")
        else:
            sleep(2.0)
            print("Invalid Operator")
            sleep(2.0)
            continue
        sleep(2.0)
        if boss_win_count == boss_wins_needed and boss_win_count>win_count_forboss:
            boss_overall_win_count += 1
        if boss_overall_win_count == 2:
            print("TIME IS UP. YOU WILL NOT BE MOVING ON AS YOU HAVE SHOWN NO ABILITY TO GET PAST THE FOREST OF DEATH") 
            return sys.exit()
        if boss_win_count == boss_wins_needed and boss_win_count>win_count_forboss and boss_overall_win_count<2:
            print("Looks like you lost to this enemy. That's alright. Retreat with both of your scrolls and come back to face this enemy tommorow.\n")
            sleep(2.0)
            print("However, if you lose to this enemy once more, you will have run out of time to reach the clock tower. SO DON'T LOSE AGAIN.\n")
            boss_win_count -= 4 
            win_count_forboss -= win_count_forboss
            sleep(5.0)
            while True:
                new_enemy = input("New Day. Are you ready? Yes or No: ").upper()
                if new_enemy == "YES":
                    break 
                elif new_enemy == "NO":
                    sleep(2.0)
                    print("The enemy is waiting.\n")
                    sleep(2.0)
                    continue 
                else:
                    print("Invalid Operator")
                    continue
            continue
        if win_count_forboss == boss_wins_needed and win_count_forboss>boss_win_count:
            print("Congrats, you have defeated this enemy and have a free pathway to the clocktower. You have now completed the Forest of Death and advanced to the final round of the Chunin Exams!\n")
            break

greeting_user()
sleep(5.0)
user_customization()
sleep(5.0)
pick_friends()
sleep(5.0)
written_exam()
run_test(questions)
sleep(5.0)
round_2()
sleep(5.0)
round2_boss()
sleep(2.0)

class Weapons:
    
    def __init__(self):
        self.arsenal = ["NINJUTSU", "TAIJUTSU", "GENJUTSU", "SUPER MOVE", "SHIELD"]
        self.arsenalpwr = {"NINJUTSU": 5, "TAIJUTSU": 5, "GENJUTSU": 5, "SUPER MOVE": 20, "SHIELD": 0}
        self.arsenalbreak = {"NINJUTSU": False, "TAIJUTSU": False, "GENJUTSU": False, "SUPER MOVE": False, "SHIELD": False}
        self.shielduses = 3
        self.supermoveuses = 1 
        
        
    def arsenalstatus(self):
        print("\tShield Uses:", self.shielduses)
        print("\tSuper Move Uses:", self.supermoveuses) 
  
    def shield(self, player, otherplayerweapon, otherplayer): 
        if otherplayerweapon == "SHIELD":
            player.subhp(0)  
        else:
            player.addhp(0)  
        self.shielduses -= 1
        if self.shielduses == 0:
            self.arsenalbreak["SHIELD"] = True
            
    def supermove(self, player, otherplayerweapon, otherplayer): 
        if otherplayerweapon == "SUPER MOVE":
            otherplayer.subhp(self.arsenalpwr["SUPER MOVE"] - 20) 
        if otherplayerweapon == "TAIJUTSU":
            otherplayer.subhp(self.arsenalpwr["SUPER MOVE"])
        elif otherplayerweapon == "GENJUTSU":
            otherplayer.subhp(self.arsenalpwr["SUPER MOVE"])
        elif otherplayerweapon == "NINJUTSU":
            otherplayer.subhp(self.arsenalpwr["SUPER MOVE"])
        elif otherplayerweapon == "SHIELD":
            otherplayer.subhp(self.arsenalpwr["SUPER MOVE"] - 20) 
        self.supermoveuses -= 1
        if self.supermoveuses == 0:
            self.arsenalbreak["SUPER MOVE"] = True
            
    def ninjutsu(self, player, otherplayerweapon, otherplayer):  
        if otherplayerweapon == "TAIJUTSU":
            otherplayer.subhp(self.arsenalpwr["NINJUTSU"])
        elif otherplayerweapon == "GENJUTSU":
            otherplayer.subhp(self.arsenalpwr["NINJUTSU"] - 2)
        elif otherplayerweapon == "NINJUTSU":
            otherplayer.subhp(self.arsenalpwr["NINJUTSU"] - 5)
        elif otherplayerweapon == "SHIELD":
            otherplayer.subhp(self.arsenalpwr["NINJUTSU"] - 5)
        else:
            otherplayer.subhp(self.arsenalpwr["NINJUTSU"])
            
    def genjutsu(self, player, otherplayerweapon, otherplayer):  
        if otherplayerweapon == "TAIJUTSU":
            otherplayer.subhp(self.arsenalpwr["GENJUTSU"] - 2)
        elif otherplayerweapon == "NINJUTSU":
            otherplayer.subhp(self.arsenalpwr["GENJUTSU"])
        elif otherplayerweapon == "GENJUTSU":
            otherplayer.subhp(self.arsenalpwr["GENJUTSU"] - 5)
        elif otherplayerweapon == "SHIELD":
            otherplayer.subhp(self.arsenalpwr["GENJUTSU"] - 5)
        else:
            otherplayer.subhp(self.arsenalpwr["GENJUTSU"])
            
    def taijutsu(self, player, otherplayerweapon, otherplayer):  
        if otherplayerweapon == "NINJUTSU":
            otherplayer.subhp(self.arsenalpwr["TAIJUTSU"] - 2)
        elif otherplayerweapon == "GENJUTSU":
            otherplayer.subhp(self.arsenalpwr["TAIJUTSU"])
        elif otherplayerweapon == "TAIJUTSU":
            otherplayer.subhp(self.arsenalpwr["TAIJUTSU"] - 5)
        elif otherplayerweapon == "SHIELD":
            otherplayer.subhp(self.arsenalpwr["TAIJUTSU"] - 5)
        else:
            otherplayer.subhp(self.arsenalpwr["TAIJUTSU"])

class Player:
    
    def __init__(self, weapons):
        self.weapons = weapons
        self.hp = 100

    def addhp(self, dmgvalue):
        self.hp += dmgvalue
        if self.hp >= 100:
            self.hp = 100

    def subhp(self, dmgvalue):
        self.hp -= dmgvalue
        if self.hp <= 0:
            self.hp = 0

    def getplayermove(self):
        playerchoice = input("Player, pick your technique! [Ninjutsu, Genjutsu, Taijutsu, Shield, Super Move]: ").upper()
        if playerchoice == "STATUS":
            return playerchoice 
        while playerchoice not in self.weapons.arsenal or self.weapons.arsenalbreak[playerchoice] or (playerchoice == "SHIELD" and self.weapons.shielduses == 0) or (playerchoice == "SUPER MOVE" and self.weapons.supermoveuses == 0):
            print("Try Again! You either typed something incorrectly or tried to use a shield/supermove when you don't have any left.\n")
            sleep(2.0)
            playerchoice = input("Player, pick your technique! [Ninjutsu, Genjutsu, Taijutsu, Shield, Super Move]: ").upper()
            if playerchoice == "STATUS":
                return playerchoice
        return (playerchoice)

    def getcompmove(self):
        compmove = choice(self.weapons.arsenal)
        while compmove not in self.weapons.arsenal or self.weapons.arsenalbreak[compmove] or (
                compmove == "SHIELD" and self.weapons.shielduses == 0) or (
                compmove == "SUPER MOVE" and self.weapons.supermoveuses == 0):
            compmove = choice(self.weapons.arsenal)
        return (compmove)
    
def intro():
    while True:
        print("Welcome to the third round of the Chunin Exams: 1v1s\n")
        sleep(2.0)
        print("You will be going up against the one and only Gaara, of the sand.\n")
        sleep(2.0)
        print("Battles will work similarly to those from the Forest of Death.\n")
        sleep(2.0)
        print("However, this time you will be assigned HP (100 HP) instead of rounds. First to ZERO HP loses.\n")
        sleep(2.0)
        print("In addition, you will also have the option of using shield and a super move.\n")
        sleep(2.0)
        print("Shield allows you to block your enemy's attack. If both you and Gaara use your shield at the same time, no damage will be dealt to either of you.\n")
        sleep(2.0)
        print("If one of you uses shield and the other doesn't, no damage is done to either of you. You get 3 shield uses in total.\n")
        sleep(2.0)
        print("A super move allows you to deal heavy damage to your enemy (20 Damage). Because of this, you are limited to only one use.\n")
        sleep(2.0)
        print("If a player uses shield against a super move, no damage is dealt for either player.\n")
        sleep(2.0)
        print("If both players use super move, no damage is dealt for either side.\n")
        sleep(2.0)
        print("To check how many shield or super moves you have left in your arsenal, just type \"Status\".")
        response = input("Do you understand the rules? Yes or No: ").upper()
        if response == "YES":
            break
        else:
            print("We don't have all day here!!!!")
            sleep(4.0)
            continue
    print("Now the battle will begin!!!")
    sleep(3.0)    
    
def main():
    
    intro()

    roundnum = 1

    Player1 = Player(Weapons())
    Player2 = Player(Weapons())

    while Player1.hp > 0 and Player2.hp > 0:
        print(f"Round {roundnum}")
        Player1move = Player1.getplayermove()
        Player2move = Player2.getcompmove()

        
        if Player1move == "STATUS":
            Player1.weapons.arsenalstatus()
            continue
        
        if Player1move == "NINJUTSU":
            Player1.weapons.ninjutsu(Player1, Player2move, Player2)
            
        elif Player1move == "SHIELD":
            Player1.weapons.shield(Player1, Player2move, Player2)
            
        elif Player1move == "TAIJUTSU":
            Player1.weapons.taijutsu(Player1, Player2move, Player2)
            
        elif Player1move == "GENJUTSU":
            Player1.weapons.genjutsu(Player1, Player2move, Player2)

        elif Player1move == "SUPER MOVE":
            Player1.weapons.supermove(Player1, Player2move, Player2)

        if Player2move == "NINJUTSU":
            Player2.weapons.ninjutsu(Player2, Player1move, Player1)
            roundnum += 1

        elif Player2move == "SHIELD":
            Player2.weapons.shield(Player2, Player1move, Player1)
            roundnum += 1

        elif Player2move == "TAIJUTSU":
            Player2.weapons.taijutsu(Player2, Player1move, Player1)
            roundnum += 1

        elif Player2move == "GENJUTSU":
            Player2.weapons.genjutsu(Player2, Player1move, Player1)
            roundnum += 1

        elif Player2move == "SUPER MOVE":
            Player2.weapons.supermove(Player2, Player1move, Player1)
            roundnum += 1

        print(f"You chose:", Player1move)
        print("Gaara chose:", Player2move)
        print(f"Your HP", Player1.hp)
        print("Gaara's HP", Player2.hp, "\n")
        sleep(2.0)
        continue

    if Player1.hp <= 0 and Player2.hp <= 0:
        print("It seems that both you and Gaara have met their match... It's a Draw")
    elif Player1.hp <= 0:
        print("Lik always, Gaara is victorious. YOU LOST!! Therefore, you have failed the Chunin exams!\n")
        print("Not fair, cry about it. Come back next year and prove your worth.\n")
    else:
        print("Congratulations, you have defeated this enemy and have proved your worth to the Ninja World.\n") 
        sleep(2.0)
        print("Lord Hokage himself higly praised you match and your efforts throughout the entire Chunin exams.\n")
        sleep(2.0)
        print("The lords of other lands who observed you match and the proctors were of the same opinion as well.\n")
        sleep(2.0)
        print("We hope you that you will strive to perform in a manner that is worthy of that headband.\n")
        sleep(2.0)
        print("Congratulations, as of today you're a Chunin!\n")
        sleep(2.0)

if __name__ == "__main__":
    main()    