#*****************************************************************************
# Author:       	Ari P.
# Assignment:       Assignment 1
# Date:         	1/24/2025
# Description:  	This program will prompt the user for six D&D character
#                   attributes (strength, dexterity, constitution,
#                   intelligence, wisdom, and charisma), then display the
#                   bonus or penalty to  dice rolls for each of them.
# Input:        	Strength score (int), Dexterity score (int), Constitution
#                   score (int), Intelligence score (int), Wisdom score (int),
#                   Charisma score (int)
# Output:       	Welcome message (string), input prompts (string), result
#                   messages (string), goodbye message (string), Strength
#                   bonus (int), Dexterity bonus (int), Constitution bonus
#                   (int), Intelligence bonus (int), Wisdom bonus (int),
#                   Charisma bonus (int)
# Sources:      	Assignment 1 specifications, assignment 1 sample, python
#                   style guide, W3Schools python reference, freeCodeCamp int
#                   rounding guide
#*****************************************************************************

# Import module for rounding down
import math

def main():
    # Create variables for scores and bonuses of all five attributes
    strScore = 0
    strBonus = 0
    dexScore = 0
    dexBonus = 0
    conScore = 0
    conBonus = 0
    intScore = 0
    intBonus = 0
    wisScore = 0
    wisBonus = 0
    chaScore = 0
    chaBonus = 0

    # Print welcome message
    print(("This program will prompt you for your six D&D (Dungeons and Dragon"
           "s) attributes, then display your bonus or penalty to dice rolls fo"
           "r each of them.\n"))
    print(("Please enter whole numbers between 8 and 20. 10 represents the hum"
           "an average."))
    
    # Prompt for score
    strScore = int(input("Enter Strength (physical power) score: "))
    # Cap to minimum of 8 and maximum of 20
    if strScore < 8:
        strScore = 8
        print("Your Strength score was set to 8.\n")
    if strScore > 20:
        strScore = 20
        print("Your Strength score was set to 20.\n")
    
    dexScore = int(input("Enter Dexterity (agility) score: "))
    if dexScore < 8:
        dexScore = 8
        print("Your Dexterity score was set to 8.\n")
    if dexScore > 20:
        dexScore = 20
        print("Your Dexterity score was set to 20.\n")
    
    conScore = int(input("Enter Constitution (endurance) score: "))
    if conScore < 8:
        conScore = 8
        print("Your Constitution score was set to 8.\n")
    if conScore > 20:
        conScore = 20
        print("Your Constitution score was set to 20.\n")
    
    intScore = int(input("Enter Intelligence (reasoning and memory) score: "))
    if intScore < 8:
        intScore = 8
        print("Your Intelligence score was set to 8.\n")
    if intScore > 20:
        intScore = 20
        print("Your Intelligence score was set to 20.\n")
    
    wisScore = int(input("Enter Wisdom (perception and insight) score: "))
    if wisScore < 8:
        wisScore = 8
        print("Your Wisdom score was set to 8.\n")
    if wisScore > 20:
        wisScore = 20
        print("Your Wisdom score was set to 20.\n")
    
    chaScore = int(input("Enter Charisma (force of personality) score: "))
    if chaScore < 8:
        chaScore = 8
        print("Your Charisma score was set to 8.")
    if chaScore > 20:
        chaScore = 20
        print("Your Charisma score was set to 20.")
    
    # Calculate bonuses, rounded down
    strBonus = math.floor((strScore - 10) / 2)
    dexBonus = math.floor((dexScore - 10) / 2)
    conBonus = math.floor((conScore - 10) / 2)
    intBonus = math.floor((intScore - 10) / 2)
    wisBonus = math.floor((wisScore - 10) / 2)
    chaBonus = math.floor((chaScore - 10) / 2)

    # Print results with varying punctuation
    if strBonus >= 2:
        print("\nYour Strength bonus is +", str(strBonus), "!", sep="")
    elif strBonus < 0:
        print("\nYour Strength penalty is ", str(strBonus), "...", sep="")
    else:
        print("\nYour Strength bonus is +", str(strBonus), ".", sep="")
    
    if dexBonus >= 2:
        print("Your Dexterity bonus is +", str(dexBonus), "!", sep="")
    elif dexBonus < 0:
        print("Your Dexterity penalty is ", str(dexBonus), "...", sep="")
    else:
        print("Your Dexterity bonus is +", str(dexBonus), ".", sep="")
    
    if conBonus >= 2:
        print("Your Constitution bonus is +", str(conBonus), "!", sep="")
    elif conBonus < 0:
        print("Your Constitution penalty is ", str(conBonus), "...", sep="")
    else:
        print("Your Constitution bonus is +", str(conBonus), ".", sep="")
    
    if intBonus >= 2:
        print("Your Intelligence bonus is +", str(intBonus), "!", sep="")
    elif intBonus < 0:
        print("Your Intelligence penalty is ", str(intBonus), "...", sep="")
    else:
        print("Your Intelligence bonus is +", str(intBonus), ".", sep="")
    
    if wisBonus >= 2:
        print("Your Wisdom bonus is +", str(wisBonus), "!", sep="")
    elif wisBonus < 0:
        print("Your Wisdom penalty is ", str(wisBonus), "...", sep="")
    else:
        print("Your Wisdom bonus is +", str(wisBonus), ".", sep="")
    
    if chaBonus >= 2:
        print("Your Charisma bonus is +", str(chaBonus), "!", sep="")
    elif chaBonus < 0:
        print("Your Charisma penalty is ", str(chaBonus), "...", sep="")
    else:
        print("Your Charisma bonus is +", str(chaBonus), ".", sep="")
    
    # Print goodbye message
    print("\nGood luck with your adventures. Farewell!")

main()