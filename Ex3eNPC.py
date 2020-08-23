#   Ex3eNPC ver 0.20
#   By Daniel Berwick
#   Date:       8/18/2020
#   Changes:    Added simple ability generator and cleaned the readout.
#               Bonus points have been added, but they only add to ability scores right now.

import random
#   The exalt-type can be expanded, and may benefit from classes/objects going forward,
#   especially after charms are added. For now, I've made it a simple set of global variables for the process.
def select_exalt_type():
    global exalt_type
    global primary_attribute_bank
    global attribute_limit
    global primary_attribute_bank
    global secondary_attribute_bank
    global tertiary_attribute_bank
    exalt_type = input("Is the NPC a [M]ortal, [T]errestrial exalt, or [S]olar exalt? \n")
    if exalt_type.lower() == "mortal" or exalt_type.lower() == "m":
        exalt_type = 'mortal'
        print('Creating a mortal...')
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
    elif exalt_type.lower() == "sidereal":  # or exalt_type.lower() == "l":
        print('\nThe mask is perfect.\n')
        select_exalt_type()
    elif exalt_type.lower() == "lunar":     # or exalt_type.lower() == "l":
        print('\nComing soon ;)\n')
        select_exalt_type()
    elif exalt_type.lower() == "abyssal":   # or exalt_type.lower() == "a":
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
            y = random.randrange(0, 3)  # Selects discrete attribute
            if attributes[x][y] >= attribute_limit:
                y = random.randrange(0, 3)
            else:
                attributes[x][y] += 1
                bank -= 1
# Debug script used for point allocation:
# print('ABILITY CAP REACHED FOR ATTRIBUTE' + str(y) + ' IN GROUP' + str(x) + ' using bank ' + str(bank))

attribute_allocation()

def ability_allocation():
    global ability_scores
    global ability_names
    ability_names = ["Archery", "Athletics", "Awareness",
                     "Brawl", "Bureaucracy", "Craft",
                     "Dodge", "Integrity", "Lore",
                     "Martial Arts", "Medicine", "Melee",
                     "Occult", "Performance", "Presence",
                     "Resistance", "Ride", "Sail",
                     "Socialize", "Stealth", "Survival",
                     "Thrown", "War"]
    ability_scores = []
    while ability_scores.count(0 and 1 and 2 and 3 and 4 and 5) < 25:
        ability_scores.append(0)
    ability_bank = 28
    while ability_bank > 0:
        x = random.randrange(1, 25)
        if ability_scores[x] < 3:    #Ability softcap without bonus points
            ability_scores[x] +=1
            ability_bank -=1



ability_allocation()

def bonus_allocation(exalt_type, ability_scores):
    if exalt_type == 'mortal':
        bonus_bank = 21
    elif exalt_type == "terrestrial":
        bonus_bank = 18
    elif exalt_type == "solar":
        bonus_bank = 15
    else:
        return 0
    if ability_scores[10] > 1 and ability_scores[4] < 1:    # Assigns 1 point to Brawl if necessary for Martial Arts
        ability_scores[4] += 1
        bonus_bank -= 1
    while bonus_bank > 0:
        x = random.randrange(1, 25)
        if ability_scores[x] < 5:  # Ability softcap without bonus points
            ability_scores[x] += 1
            bonus_bank -= 1


bonus_allocation(exalt_type, ability_scores)

def finalize_character(ability_scores, ability_names):
    global abilities
    abilities = zip(ability_scores, ability_names)
    choice = input("Sort abilities by [S]core or [A]lphabetically? \n")
    if choice.lower() == "score" or choice.lower() == "s":
        abilities = list(abilities)
        abilities.sort(reverse=True)
        print("")


finalize_character(ability_scores, ability_names)

def display_character(exalt_type):
    print("Name: ")
    if exalt_type == 'terrestrial':
        print('Aspect: ')
    elif exalt_type == 'solar':
        print("Caste: ")
    print("___________________________________________________")
    print(" Strength: " + str(attributes[0][0]) + "        Charisma: " + str(attributes[1][0]) +
          "       Perception: " + str(attributes[2][0]))
    print("Dexterity: " + str(attributes[0][1]) + "    Manipulation: " + str(attributes[1][1]) +
          "     Intelligence: " + str(attributes[2][1]))
    print("  Stamina: " + str(attributes[0][2]) + "      Appearance: " + str(attributes[1][2]) +
          "             Wits: " + str(attributes[2][2]))
    print("\n")
    for item in abilities:
        print(item)

def load_charms(source):
    print("Loading Charms...")
    import csv
    with open(source, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for raw in csv_reader:
            raw[1] = Charm(raw[1], raw[2], raw[3], raw[4], raw[5], raw[6], raw[7], raw[8], raw[9])
            #Note that charms must have 9 parameters. Object initialization handles blanks that are marked with 'N/A'
    print("Load Complete")


load_charms("charms.csv")


class Charm:
    charmlist = []
    def __init__(self, name, book, page, essence_min, ability, ability_min, *args):
        self.name = name
        self.charm_set = book
        self.page = page
        self.essence_min = essence_min
        self.abillity = ability
        self.ability_min = ability_min
        self.prerequisite_charms = []
        for prereq in args:     #applies any number of pre-req charms
            if prereq == "N/A":    #Ignores blanks
                continue
            else:
                self.prerequisite_charms.append(prereq)

        Charm.charmlist.append(self)

    @staticmethod
    def generate_charms(exalt_type):
        if exalt_type == "mortal":
            charm_bank = 0
            print("No charms generated due to lack of exaltation.")
        elif exalt_type == "terrestrial" or exalt_type == "solar":
            global character_charms
            character_charms = []
            print("Generating Charms...")
            charm_bank = 15
        while charm_bank > 0:
            with random.choice(Charm.charmlist) as selected_charm:
                if character_charms.count(selected_charm) == 0 and character_essence >= selected_charm.essence_min and
                    character
                    character_charms.append(selected_charm)
                    charm_bank -= 1





class CharmSuite(Charm):  # Charm suites refer to a practice in 2e's NPC section for clusters of synergistic charms.
                          # Since this excellent idea hasn't been used in 3e, all suites are homebrew by definition.




display_character(exalt_type)
