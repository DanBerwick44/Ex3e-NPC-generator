#   Ex3eNPC ver 0.30
#   By Daniel Berwick
#   Date:       8/29/2020
#   Changes:   Rewritten with object-oriented code. PEP 8 has also been applied.

import random
import csv


class Attribute:
	def __init__(self, category):
		self.category = category
		self.rating = 1
		self.limit = 5
		
		
	#def mortal_limit_check(cls)
		#if active_char.exaltation == 'mortal':
			#self.limit = 4
		#else:
			#self.limit = 5
			

strength = dexterity = stamina = Attribute('physical')
physical_attributes = [strength, dexterity, stamina]

charisma = manipulation = appearance = Attribute('social')
social_attributes = [charisma, manipulation, appearance]

perception = intelligence = wits = Attribute('mental')
mental_attributes = [perception, intelligence, wits]
			
default_attributes = [physical_attributes, social_attributes, mental_attributes]



class Abilities:
	def __init__(self, *args):
		self.rating = 0
		self.limit = 5
		self.favored = False
		self.specialties = []
		for arguments in args:
			self.specialties.append(arguments)
			


default_abilities = ["Archery", "Athletics", "Awareness",
                     "Brawl", "Bureaucracy", "Craft",
                     "Dodge", "Integrity", "Lore",
                     "Martial Arts", "Medicine", "Melee",
                     "Occult", "Performance", "Presence",
                     "Resistance", "Ride", "Sail",
                     "Socialize", "Stealth", "Survival",
                     "Thrown", "War"]

for ability in default_abilities:
	ability = Abilities()


class Character:
	def __init__(self, name, exaltation, background, attributes, abilities, merit_bank, *args):
		self.essence = 1
		self.name = name
		self.exaltation = exaltation
		self.background = background
		self.caste = random.choice(self.exaltation.caste)
		self.attributes = attributes
		self.abilities = abilities
		self.charms = charms
		self.merit_bank = merit_bank
		self.merit_list = []
		
		


	def apply_bonus_points(cls): # Do different exaltations have different bonus points? Might need parameters. Also, note to self, the available points for a point bank need to function with a parameter so that bonus points can be distributed and then re-ran.
		bonus_points = active_char.exaltation.bonus_points
		options = ['buy_attributes', 'buy_abilities', 'buy_charms', 'buy_merits']
				   
				   
class Merits:
	def __init__(self, repeatable, *args):
		self.repeatable = bool(repeatable)
		self.cost = [0]
		for dot_value in args:
			self.cost.append(dot_value)
		self.current_rank = 0
		self.max_rank = len(self.cost) - 1
		
			
	def generate_merits(cls):
		supernatural_allowed = input("Allow Supernatural Merits? ([Y]es/No) \n")
		if supernatural_allowed.lower == 'yes' or supernatural_allowed.lower == 'y':
			supernatural_allowed = True
		else:
			supernatural_allowed = False
		while active_char.merit_points > 0:
			pass
			


class Exaltation:	#Data-type for different exalts
	def __init__(self, primary_attr, secondary_attr, tertiary_attr, attr_limit, favoreds, charm_points, *args):
		self.primary_attr = primary_attr
		self.secondary_attr = secondary_attr
		self.tertiary_attr = tertiary_attr
		self.attr_limit = attr_limit
		self.favoreds = favoreds
		self.charm_points = charm_points
		self.charms_list =[]
		self.caste = []
		for caste in args:
			self.caste.append(caste)
		self.background = background
		self.merits = merits


def terrestrial_background():
	print("Select your background:")
	print("0. Random \n 1. Scarlet Empire \n 2. Lookshy \n 3. Prasad \n 4. Forest Witch \n 5. Outcaste")
	choice = input()
	if choice == "1":
		return "Scarlet Empire"
	elif choice == "2":
		return "Lookshy"
	elif choice == "3":
		return "Prasad"
	elif choice == "4":
		return "Forest Witch"
	elif choice == "5":
		return "Outcaste"
	else:
		roll = random.randrange(0, 101)
		if roll <= 60:
			return "Scarlet Empire"
		elif roll > 60 and roll <= 80:
			return "Outcaste"
		elif roll > 80 and roll <=92:
			return "Lookshy"
		elif roll > 92 and roll <=99:
			return "Prasad"
		else:
			return "Forest Witch"



#class Backgrounds:
		#For most, these are flavor decisions, as well as providing flavor for
		#merits from relevant lists, but Dragonblooded backgrounds come with stats
		#as well


mortal = Exaltation(6, 4, 3, 4, 0, 0,)
terrestrial = Exaltation(8, 6, 4, 5, 3, 15, 'Air', 'Earth', 'Fire', 'Water', 'Wood')
solar = Exaltation(8, 6, 4, 5, 5, 15, 'Dawn', 'Zenith', 'Twilight', 'Night', 'Eclipse')


def choose_exaltation():
	selection = input("Is the NPC a [M]ortal, [T]errestrial exalt, or [S]olar exalt? \n")
	if selection.lower() == "mortal" or selection.lower() == "m":
		print('Creating a mortal...')
		return mortal
	elif selection.lower() == "terrestrial" or selection.lower() == "t":
		print('Creating a scion of the elemental dragons...')
		return terrestrial
	elif selection.lower() == "sidereal":  # or selection.lower() == "s":
		print('\nThe mask is perfect.\n')
		choose_exaltation()
	elif selection.lower() == "lunar":  # or selection.lower() == "l":
		print('\nComing soon ;)\n')
		choose_exaltation()
	elif selection.lower() == "abyssal":  # or selection.lower() == "a":
		print('\nComing soon ;)\n')
		choose_exaltation()
	elif selection.lower() == "solar" or selection.lower() == "s":
		print('Eagerly awaiting the return of Sol\'s chosen heroes...')
		return solar
	else:
		print(' \n Command not understood. \n Please try again. \n')
		choose_exaltation()

active_char = Character('placeholder' + ' ' + 'name', choose_exaltation(), generate_attributes(), generate_abilities(), generate_merits())


#Finish character object
# Randomly assign favoreds if necessary
# Randomly assign attributes
#randomly assign abilities
#Randomly assign charms (create charm object)
#randomly assign merits. (create merit object)
#randomly assign bonus points.
#Print
#Export
#Charm suites
#Lore generator - names, merit descriptions,