#!/usr/bin/python
import pyttsx3
import pyaudio
import speech_recognition as sr

import random
from colorama import init
from termcolor import colored
from playsound import playsound

engine = pyttsx3.init('sapi5') #nitialize speech engine
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    speak("Welcome to the Python versus Java battle.")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        r.pause_threshold = 0.5 #how long it wait for user command
        audio = r.listen(source)
    try:
        print("Recognizing voice...")
        query = r.recognize_google(audio, language='en-US') # where user command is stored after being recognized
        print(query)
    except Exception as e:
        print(e)
        print("Unable to recognize. Try again please.")
        return "None"
    return query

if __name__ == "__main__":
    greeting()
    class Character:
        def __init__(self, name, energy, health, magic, exp=0, level=1):
            self.name = name
            self.energy = energy
            self.health = health
            self.magic = magic
            self.exp = exp
            self.level = level
            self.levelup_counter = exp + 5
        
        def hero_attack(self): # Takes away 5 energy points and adds 1 XP point for every attack
            playsound(r"C:\path\to\file\slash.mp3")
            print(colored(f"You have attacked the {c2.name}!",'green'))
            speak("You attacked the monster!")
            if c1.level >= 2: #this increases the attack strength when player levels up
                c2.health -= 15
            else:
                c2.health -= 10 # takes away monster health
            self.energy -= 5
            self.exp += 1

        def magic(self):
            playsound(r"C:\path\to\file\magic.mp3")
            print(colored(f"You have used magic!",'green'))
            speak("Magic used!")
            self.magic -= 1
            c2.health -= 25

        def monster_attack(self): # Takes away 10 energy points and adds 1 XP point for evert attack
            playsound(r"C:\path\to\file\slash.mp3")
            print(colored(f"The {c2.name} has attacked you!", 'red'))
            speak("The monster attacked you!")
            self.energy -= 10

    # This function prints out both hero and monster stats    
    def stats():
            print("________________________________________________________")
            print("You\t\t\t\tMonster\n--------------------------------------------------------")
            print(f"Your Health: {c1.health}   \t\tMonster's Health: {c2.health}")
            print(f"Your Energy: {c1.energy}   \t\tMonster's Energy: {c2.energy}")
            print(f"Your Level: {c1.level}\t\t        Monster's Level: 4      ")
            print(f"Your Magic: {c1.magic}/1\t\t              ")
            print(f"Your XP: {c1.exp}/{c1.levelup_counter}\t\t         ")


    # Two objects from the Character class
    c1 = Character("Python Hero", 100, 100, 1, 0, 1)
    c2 = Character("Java Monster", 100, 100, 10, 3)

    # This is the main game function
    def play():
        stats() # stats print out

        while True:
            try:
                # Three possible choices for hero
                # choice = int(input("\n[1] Fight [2] Magic [3] Run: "))
                speak("Choose action")

            except ValueError:
                print("Invalid entry. Try again.")
                speak("Invalid entry. Try again.")
            else:
                if take_command() == "fight":
                    if c1.health > 0: # Attack only if health is above 0
                        r = random.choice(['Monster Attack', 'Hero Attack']) # Randomizes between hero or monster

                        if r == "Hero Attack":
                            attack_or_block = random.choice(['attack','block']) #Randomizes successful attack or not
                            if attack_or_block == 'attack':
                                c1.hero_attack()
                                
                                if c1.exp %5 == 0: # increases level for every 5 points
                                    c1.level += 1 # level up counter (increase 1 point for every attack)
                                    c1.exp = 0 # this resets experience counter to zero for every levelup
                                    playsound(r"C:\path\to\file\levelup.mp3")
                                    print(colored(f"You have leveled up!", 'cyan'))
                                    speak("You have leveled up!")
                                stats()
                            else:
                                playsound(r"C:\path\to\file\defend.mp3")
                                print(colored(f"The {c2.name} has blocked your attack!",'magenta'))
                                speak("The monster blocked your attack!")
                                c2.energy -= 2
                                

                        elif r == "Monster Attack":
                            attack_or_block = random.choice(['attack','block']) #Randomizes successful attack or not
                            if attack_or_block == 'attack':
                                c2.monster_attack()
                                c1.health -= 15 # Takes away hero's health
                                stats()
                            else:
                                playsound(r"C:\path\to\file\defend.mp3")
                                print(colored(f"You have blocked the {c2.name}'s attack!", 'magenta'))
                                speak("You blocked the monster's attack!")
                                c1.energy -= 1
                                
                    if c1.energy <= 20: # warning for player to retreat due to low energy
                        playsound(r"C:\path\to\file\no_energy.mp3")
                        print(colored("Your energy is too low! Retreat!", 'red'))
                        speak("Your energy is too low!")
                        

                    if c1.health <= 20: # warning for player to retreat due to low health
                        playsound(r"C:\path\to\file\no_energy.mp3")
                        print(colored("Your health is too low! Retreat!", 'red'))
                        speak("Your health is too low!")

                    if c1.health <= 0: #player death
                        print(colored("You have died!", 'red'))
                        playsound(r"C:\path\to\file\death.mp3")
                        speak("Game over!")
                        break

                    if c2.health <= 0: # monster death
                        print(colored(f"You have killed the {c2.name}! You're a legend!", 'yellow'))
                        playsound(r"C:\path\to\file\victory.mp3")
                        speak("You defetated the monster!")
                        break

                    if c2.energy <= 10: # if enemy's energy reaches 10, it will run away
                        print(colored(f"The {c2.name}'s energy is drained. It ran away.\nYou won!", 'yellow'))
                        playsound(r"C:\path\to\file\victory.mp3")
                        speak("The monster gave up!")
                        break

                    if c2.health <= 15: # if enemy's health reaches 15, it will run away
                        print(colored(f"The {c2.name}'s health is almost depleted. It ran away.\nYou won!", 'yellow'))
                        playsound(r"C:\path\to\file\victory.mp3")
                        speak("The monster gave up!")
                        break

                elif take_command() == "Magic": # magic option
                    if c1.magic == 1: # only works if available
                        playsound(r"C:\path\to\file\magic.mp3")
                        print(colored(f"You have used magic!",'green'))
                        speak("Magic used!")
                        c1.magic -= 1
                        c2.health -= 20
                        c1.exp += 1
                        if c1.exp %5 == 0: # increases level for every 5 points
                            c1.level += 1 # level up counter (increase 1 point for every attack)
                            c1.exp = 0 # this resets experience counter to zero for every levelup
                            print(colored(f"You have leveled up!", 'cyan'))
                            playsound(r"C:\path\to\file\levelup.mp3")
                            speak("You have leveled up!")
                        stats()
                    else:
                        print(colored("You don't have enough magic!", 'red'))
                        playsound(r"C:\path\to\file\error.mp3")
                        speak("Magic not available!")
                        
                elif take_command() == 'run': # run away option
                    print(colored("It's wise to choose your battles. Good bye!", 'blue'))
                    playsound(r"C:\path\to\file\lose.mp3")
                    speak("It's wise to choose your battles. Goodbye.")
                    break

                else:
                    print("Invalid entry. Try again.")
                    speak("Command not executed. Try again.")
                    continue
        
        # again = input("Play again? Y/N: ").capitalize().strip()
        speak("Would you like to play again?")
        if take_command() == 'yes':
            c1.energy, c1.health, c1.magic, c1.exp, c1.level = 100, 100, 1, 1, 1
            c2.energy, c2.health = 100, 100
            play()
        elif take_command() == 'no':
            print("See you next time!")
            speak("See you next time!")
            
    play()


