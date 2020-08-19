#   Version 0.11
#   By Daniel Berwick
#   Date: 8/18/2020
#   Changes: fixed logic error in line 66 which sometimes caused a single attribute set to be completely empty.

import random
#   The exalt-type can be expanded, and may benefit from classes/objects going forward, especially after charms are added.
#   For now, I've made it a simple set of global variables for the process.
def select_exalt_type():
    global primary_attribute_bank
    global attribute_limit
    global primary_attribute_bank
    global secondary_attribute_bank
    global tertiary_attribute_bank
    exalt_type = input("Is the NPC a [M]ortal, [T]errestrial exalt, or [S]olar exalt? \n")
    if exalt_type.lower() == "mortal" or exalt_type.lower() == "m":
        exalt_type = 'mortal'
        print('Creating a puny mortal...')
        attribute_limit = 4
        primary_attribute_bank = 6
        secondary_attribute_bank = 4
        tertiary_attribute_bank = 3
    elif exalt_type.lower() == "terrestrial" or exalt_type.lower() == "t":
        exalt_type = 'terrestrial'
        print('Creating a scion of the elemental dragons...')
        attribute_limit = 5
        primary_attribute_bank = 8
        secondary_attribute_bank = 6
        tertiary_attribute_bank = 4
    elif exalt_type.lower() == "sidereal": #or exalt_type.lower() == "l":
        print('\nThe mask is perfect.\n')
        select_exalt_type()
    elif exalt_type.lower() == "lunar": #or exalt_type.lower() == "l":
        print('\nComing soon ;)\n')
        select_exalt_type()
    elif exalt_type.lower() == "abyssal": #or exalt_type.lower() == "a":
        print('\nComing soon ;)\n')
        select_exalt_type()
    elif exalt_type.lower() == "solar" or exalt_type.lower() == "s":
        exalt_type = 'solar'
        print('Eagerly awaiting the return of Sol\'s chosen heroes...')
        attribute_limit = 5
        primary_attribute_bank = 8
        secondary_attribute_bank = 6
        tertiary_attribute_bank = 4
    else:
        print(' \n Command not undertood. \n Please try again. \n')
        select_exalt_type()


print("Ex3e NPC generator")
print("Let's generate an NPC")
select_exalt_type()

attribute_banks = [primary_attribute_bank, secondary_attribute_bank, tertiary_attribute_bank]

strength_rank = dexterity_rank = stamina_rank = charisma_rank = manipulation_rank = appearance_rank = perception_rank = intelligence_rank = wits_rank = 1
physical_attributes = [strength_rank, dexterity_rank, stamina_rank]
social_attributes = [charisma_rank, manipulation_rank, appearance_rank]
mental_attributes = [perception_rank, intelligence_rank, wits_rank]
attributes = [physical_attributes, social_attributes, mental_attributes]

def attribute_allocation():
    for bank in attribute_banks[0:3]:
        x = random.randrange(0, 3)  # Selects attribute set
        while attributes[x][0] > 2 or attributes[x][1] > 2 or attributes[x][2] > 2: #Checks if we've done this set before
            x = random.randrange(0, 3)  # Selects attribute set
        while bank > 0:
            y = random.randrange(0, 3) # Selects discrete attribute
            if attributes[x][y] > attribute_limit:
                y = random.randrange(0, 3)
            else:
                attributes[x][y] += 1
                bank -= 1
# Debug script used for point allocation: print('ABILITY CAP REACHED FOR ATTRIBUTE' + str(y) + ' IN GROUP' + str(x) + ' using bank ' + str(bank))
attribute_allocation()

def display_character():
    print(" Strength: " + str(attributes[0][0]) + "        Charisma: " + str(attributes[1][0]) + "       Perception: " + str(attributes[2][0]))
    print("Dexterity: " + str(attributes[0][1]) + "    Manipulation: " + str(attributes[1][1]) + "     Intelligence: " + str(attributes[2][1]))
    print("  Stamina: " + str(attributes[0][2]) + "      Appearance: " + str(attributes[1][2]) + "             Wits: " + str(attributes[2][2]))

display_character()
