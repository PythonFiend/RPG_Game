# RPG_Game
Voice-activated RPG Game

This a very simple game that utilizes the concepts of classes and functions. The character class creates the player (characters) objects, which have six parameters (name, energy, health, magic, experience, and level).

Functions

hero_attack() - this function takes away 5 energy points from the player after each successful attack, but it also increases XP by 1 point with each successful attack. Additionally, each successful attack takes away 10 health points from enemy. If player levels up, an additonal 5 points is taken from enemy's health.

magic() - player has only one magic per round. New magic is added when player levels up. Enemy loses 25 health points with magic attack.

monster_attack() - enemy loses 10 energy points with each successful attack

Game Features

1. Game uses voice recognition for commmands.
2. Games randomizes outcomes. When player attacks enemy, attack may or may not be successful. If not successful, enemy attacks back. If successful, enemy or player may or may not block attack. 
3. XP is acquired with every successful attack.
4. Player levels up with every 5 XP acquired.
5. Player attack strength increases when leveling up.
6. Both player and enemy lose energy points for successful and unsuccessful attacks.
7. Player gets warning message if health reaches 20 points and below.
8. Both player and enemy die if health reaches 0.
9. Enemy gives up and runs away if health reaches 10 points. 
10. Game includes sound effects for attack, block attack, magic, death, low health, level up
11. Game is played using voice-activated commands

How to Play

    1. Speak commands: Fight, Run, Magic
    2. If game-over, speak "yes" to play again, or "no" to exit
    3. Download resources package for mp3 files
    4. Be sure to use correct path for mp3 files for the game to work correctly
    5. Install and import necessary modules
