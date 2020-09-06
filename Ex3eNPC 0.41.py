#   Ex3eNPC ver 0.41
#   By Daniel Berwick
#   Date:       9/6/2020
#   Changes:   Wrote in some of the generators. Current version is not functional and desperately needs a cleanup.

import random
import csv
import copy


class Attribute:
	def __init__(self, category):
		self.category = category
		self.rating = 1
		self.limit = 5

	@staticmethod
	def set_mortal_limits():
		for categories in default_attributes:
			for attribute in categories:
				attribute.limit = 4

	@staticmethod
	def set_exalted_limits():
		for categories in default_attributes:
			for attribute in categories:
				attribute.limit = 5


strength = dexterity = stamina = Attribute('physical')
physical_attributes = [strength, dexterity, stamina]

charisma = manipulation = appearance = Attribute('social')
social_attributes = [charisma, manipulation, appearance]

perception = intelligence = wits = Attribute('mental')
mental_attributes = [perception, intelligence, wits]

default_attributes = [physical_attributes, social_attributes, mental_attributes]


class Ability:
	def __init__(self, *args):
		self.rating = 0
		self.limit = 5
		self.favored = False
		self.specialties = []
		for arguments in args:
			self.specialties.append(arguments)


			
# Not sure if all this was necessary but Pycharm was giving me some sass about initiating these variables, so I just
# made strings of them and fed them into a factory.

ability_names = ["Archery", "Athletics", "Awareness",
                     "Brawl", "Bureaucracy", "Craft",
                     "Dodge", "Integrity", "Lore",
                     "Martial Arts", "Medicine", "Melee",
                     "Occult", "Performance", "Presence",
                     "Resistance", "Ride", "Sail",
                     "Socialize", "Stealth", "Survival",
                     "Thrown", "War"]

default_abilities = []

for ability in ability_names:
	ability = Ability()
	default_abilities.append(ability)

class Character:
	# This class exists to hold all variables relating to the active character. Might be useful for save functions.
	def __init__(self, name, exaltation, background, merit_bank, *args):
		self.essence = 1
		self.name = name
		self.exaltation = exaltation
		#if self.exaltation == "mortal":
			#attributes.mortal_limits()
		#else:
			#attributes.exalted_limits()
		self.background = background
		self.caste = random.choice(self.exaltation.castes)
		self.attributes = copy.copy(default_attributes)
		self.abilities = copy.copy(default_abilities)
		charms = []
		self.charms = charms
		self.merit_bank = merit_bank
		self.merit_list = []

	def generate_attributes(self):
		attribute_banks = [self.exaltation.primary_attr, self.exaltation.secondary_attr, self.exaltation.tertiary_attr]
		#  Watch out for problems here down the road. Might need to use copy.copy on the attribute banks for repetition.
		for bank in attribute_banks:
			with random.choice(self.attributes) as selected_category:
				while bank > 0:
					with random.choice(selected_category) as selected_attribute:
						if selected_attribute.rating < selected_attribute.limit:
							selected_attribute.rating += 1
							bank -= 1
		print("Attributes Generated")

	def generate_abilities(self, default_abilities):
		favored_ability_count = self.exaltation.favoreds
		#Again, might call for copy.copy in the future to allow for running multiple times
		while favored_ability_count > 0:
			with random.choice(default_abilities) as ability:
				if not ability.favored:
					ability.favored = True
					favored_ability_count -= 1
		if default_abilities[4].favored or default_abilities[10].favored:  # Brawl & Martial Arts special rule
			default_abilities[4].favored = default_abilities[10].favored = True
		ability_bank = 25
		while ability_bank > 0:
			with random.choice(default_abilities) as selected_ability:
				if selected_ability < 3:
					selected_ability += 1
					ability_bank -= 1
		print("Abilities Generated")

	#def apply_bonus_points():  # Do different exaltations have different bonus points? Might need parameters.
		# Also, note to self, the available points for a point bank need to function with a parameter so that bonus
		# points can be distributed and then re-ran.
		bonus_points = active_char.exaltation.bonus_points
		options = ['buy_attributes', 'buy_abilities', 'buy_charms', 'buy_merits']

	def display_character_sheet(self):
		print("Name: ")
		if self.exaltation == 'terrestrial':
			print('Aspect: ' + self.caste)
		elif self.exaltation == 'solar':
			print("Caste: " + self.caste)
		print("___________________________________________________")
		for category in self.attributes:
			for attribute in category:
				print(attribute + " " + attribute.rating)
			print("")
		print("___________________________________________________")
		for ability in self.abilities:
			print(ability + " " + ability.rating)


class Merit:
	default_merits = []

	def __init__(self, repeatable, supernatural, *args):
		self.repeatable = bool(repeatable)
		self.supernatural = bool(supernatural)
		self.cost = [0]
		for dot_value in args:
			self.cost.append(dot_value)
		self.current_rank = 0
		self.max_rank = len(self.cost) - 1
		Merit.default_merits.append(self)

	@staticmethod
	def import_merits():
		with open('merits.csv', 'r') as raw_merits:
			unsorted_merits = csv.reader(raw_merits)

			next(raw_merits)  # Ignores the first line to allow a spreadsheet header for effective documentation.

			for line in unsorted_merits:
				line[0] = Merit(line[1], line[2], line[3:])
				# In theory, this will pull all the values I need and only that many. In the event of an error, I may
				# have to make each line an individual ranking and rework all the architecture around it. Not as clean,
				# but functional

	@classmethod
	def generate_merits(cls, default_merits, active_char):
		supernatural_allowed = input("Allow Supernatural Merits? ([Y]es/No) \n")
		if supernatural_allowed.lower == 'yes' or supernatural_allowed.lower == 'y':
			supernatural_allowed = True
		else:
			supernatural_allowed = False
		while active_char.merit_bank > 0:
			with random.choice(default_merits) as active_merit:
				if supernatural_allowed == False and active_merit.supernatural == True:
					continue
				elif active_merit.repeatable == False and active_char.merit_list.index(active_merit) >= 1:
					continue
				elif active_char.merit_bank >= active_merit.cost:
					active_char.merit_bank -= active_merit.cost
					active_char.merit_list.append(active_merit)
					continue
		print("Merits Generated.")

class Exaltation:	#Data-type for different exalts
	def __init__(self, primary_attr, secondary_attr, tertiary_attr, attr_limit, favoreds, charm_points, *args):
		self.primary_attr = primary_attr
		self.secondary_attr = secondary_attr
		self.tertiary_attr = tertiary_attr
		self.attr_limit = attr_limit
		self.favoreds = favoreds
		self.charm_points = charm_points
		self.charms_list =[]
		self.castes = []
		for caste in args:
			self.castes.append(caste)

	@staticmethod
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
		elif 60 < roll <= 80:
			return "Outcaste"
		elif 80 < roll <= 92:
			return "Lookshy"
		elif 92 < roll <= 99:
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



active_char = Character('placeholder' + ' ' + 'name', Exaltation.choose_exaltation(),0, 0)
active_char.generate_attributes()
active_char.generate_abilities()
active_char.display_character_sheet()


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