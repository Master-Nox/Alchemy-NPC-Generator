# Design Notes #
# This program should be able to take in a multitude of csv files including Species, Class, Gender, Alignment, Attitude, CR, Goal/Motivation, and more.
# This program should take values from the listed CSV files and combine them into Unique and memorable NPCs.
# This program should be able to then take these generated NPCs and export them to a json file that is compatible with Alchemy.

# Extended Features #
# A GUI that allows for editing of any of the generated values.
# Name Generation. 
# Stat Generation. DONE
# interpreting personality from Species, Class, and Alignment.

# Notes #
# Would like to implement Skills/Proficiencies sooner rather than later. DONE
# Proficiency Bonus, HP based on level and Class, AC based on level dex score and pb? Initative Bonus. DONE (Although AC is simplified, may want to change later)
# Set Tracker HP to match NPC HP. DONE (Maybe alter die size based on class later) DONE
# Saving throw proficiencies. DONE
# Auto-Generate a set of actions based on class?
# Make Species actually respect their rarity. DONE
# Make a setting to force a certain level or level range. 

# Bugs #
# Direct editing a class will result in N/A saving throws.
# Direct editing a class will result in inaccurate HP generation(?).
# Alchemy update broke HP generation. 

# Imports #
import csv
import random
import json
import time
import math

# Species #
def SpeciesGen(Classification, PHBCLASSES):
    if PHBCLASSES == False:
        if Classification == "":
            ClassificationRandom = random.randint(1, 12)
        elif Classification == "Naturalborn":
            ClassificationRandom = 5
        elif Classification == "Oddity":
            ClassificationRandom = 10
        elif Classification == "Outlander":
            ClassificationRandom = 15

        if ClassificationRandom < 7:
            NaturalbornRandom = random.randint(1, 200)
            if NaturalbornRandom <= 3:
                SPECIES = "Aasimar"
            elif NaturalbornRandom <= 11:
                SPECIES = "Dragonborn (Chromatic)"
            elif NaturalbornRandom <= 19:
                SPECIES = "Dragonborn (Metallic)"
            elif NaturalbornRandom <= 22:
                SPECIES = "Dwarf (Gray)(Duergar)"
            elif NaturalbornRandom <= 26:
                SPECIES = "Dwarf (Hill)"
            elif NaturalbornRandom <= 30:
                SPECIES = "Dwarf (Mountain)"
            elif NaturalbornRandom <= 32:
                SPECIES = "Dwarf (Seaborn)"
            elif NaturalbornRandom <= 35:
                SPECIES = "Dwarf (Strongblood)"
            elif NaturalbornRandom <= 37:
                SPECIES = "Elf (Ash)"
            elif NaturalbornRandom <= 40:
                SPECIES = "Elf (Dark)(Drow)"
            elif NaturalbornRandom <= 45:
                SPECIES = "Elf (High)"
            elif NaturalbornRandom <= 47:
                SPECIES = "Elf (Sea)"
            elif NaturalbornRandom <= 52:
                SPECIES = "Elf (Wood)"
            elif NaturalbornRandom <= 53:
                SPECIES = "Faunus (Bear)"
            elif NaturalbornRandom <= 54:
                SPECIES = "Faunus (Bird)"
            elif NaturalbornRandom <= 55:
                SPECIES = "Faunus (Cat)"
            elif NaturalbornRandom <= 56:
                SPECIES = "Faunus (Cow/Bull)"
            elif NaturalbornRandom <= 57:
                SPECIES = "Faunus (Deer)"
            elif NaturalbornRandom <= 58:
                SPECIES = "Faunus (Dog)"
            elif NaturalbornRandom <= 59:
                SPECIES = "Faunus (Fox)"
            elif NaturalbornRandom <= 60:
                SPECIES = "Faunus (Horse)"
            elif NaturalbornRandom <= 61:
                SPECIES = "Faunus (Pig)"
            elif NaturalbornRandom <= 62:
                SPECIES = "Faunus (Rabbit)"
            elif NaturalbornRandom <= 63:
                SPECIES = "Faunus (Raccoon)"
            elif NaturalbornRandom <= 64:
                SPECIES = "Faunus (Sheep)"
            elif NaturalbornRandom <= 65:
                SPECIES = "Faunus (Wolf)"
            elif NaturalbornRandom <= 69:
                SPECIES = "Gnome (Deep)"
            elif NaturalbornRandom <= 74:
                SPECIES = "Gnome (Forest)"
            elif NaturalbornRandom <= 78:
                SPECIES = "Gnome (Rock)"
            elif NaturalbornRandom <= 81:
                SPECIES = "Goblin"
            elif NaturalbornRandom <= 84:
                SPECIES = "Goblin (Hoardshine)"
            elif NaturalbornRandom <= 86:
                SPECIES = "Goliath"
            elif NaturalbornRandom <= 87:
                SPECIES = "Goliath (Cloudborn)"
            elif NaturalbornRandom <= 88:
                SPECIES = "Goliath (Fireborn)"
            elif NaturalbornRandom <= 89:
                SPECIES = "Goliath (Frostborn)"
            elif NaturalbornRandom <= 90:
                SPECIES = "Goliath (Hillborn)"
            elif NaturalbornRandom <= 91:
                SPECIES = "Goliath (Stoneborn)"
            elif NaturalbornRandom <= 104:
                SPECIES = "Half-Elf"
            elif NaturalbornRandom <= 110:
                SPECIES = "Half-Orc"
            elif NaturalbornRandom <= 113:
                SPECIES = "Half-Orc (Coldheart)"
            elif NaturalbornRandom <= 118:
                SPECIES = "Halfling (Lightfoot)"
            elif NaturalbornRandom <= 121:
                SPECIES = "Halfling (Lotusden)"
            elif NaturalbornRandom <= 125:
                SPECIES = "Halfling (Stout)"
            elif NaturalbornRandom <= 141:
                SPECIES = "Human"
            elif NaturalbornRandom <= 147:
                SPECIES = "Kobold"
            elif NaturalbornRandom <= 156:
                SPECIES = "Leonin"
            elif NaturalbornRandom <= 169:
                SPECIES = "Orc"
            elif NaturalbornRandom <= 175:
                SPECIES = "Tabaxi"
            elif NaturalbornRandom <= 178:
                SPECIES = "Tabaxi (Softpaw)"
            elif NaturalbornRandom <= 191:
                SPECIES = "Tiefling"
            elif NaturalbornRandom <= 200:
                SPECIES = "Tortle"
            # csvfile = open(r"Lists\Naturalborn.csv", "r")
            # SPECIES = list(csv.reader(csvfile, delimiter=','))
            # selected_row = random.choice(SPECIES)  # Select a random row (list)
            # SPECIES = ','.join(selected_row)  # Convert the list to a comma-separated string
            # if SPECIES == 'ï»¿Aasimar':
            #     SPECIES = 'Aasimar'
        elif ClassificationRandom < 11:
            OddityRandom = random.randint(1, 200)
            if OddityRandom <= 12:
                SPECIES = "Aarakocra"
            elif OddityRandom <= 18:
                SPECIES = "Aasimar (Mystic)"
            elif OddityRandom <= 26:
                SPECIES = "Dragonborn (Gem)"
            elif OddityRandom <= 32:
                SPECIES = "Dragonborn (Radiant)"
            elif OddityRandom <= 40:
                SPECIES = "Elf (Pallid)"
            elif OddityRandom <= 46:
                SPECIES = "Halfling (Jinx)"
            elif OddityRandom <= 52:
                SPECIES = "Kalashtar"
            elif OddityRandom <= 57:
                SPECIES = "Kenku"
            elif OddityRandom <= 60:
                SPECIES = "Kenku (Harrowfeather)"
            elif OddityRandom <= 63:
                SPECIES = "Kenku (Shroudeye)"
            elif OddityRandom <= 64:
                SPECIES = "Lineage (Dhampir)"
            elif OddityRandom <= 65:
                SPECIES = "Lineage (Disembodied)"
            elif OddityRandom <= 66:
                SPECIES = "Lineage (Hexblood)"
            elif OddityRandom <= 68:
                SPECIES = "Lineage (Reborn)"
            elif OddityRandom <= 71:
                SPECIES = "Lupin (Fabled)"
            elif OddityRandom <= 74:
                SPECIES = "Lupin (Isolated)"
            elif OddityRandom <= 77:
                SPECIES = "Lupin (Leader)"
            elif OddityRandom <= 84:
                SPECIES = "Lupin (Pack)"
            elif OddityRandom <= 85:
                SPECIES = "Lustrous (Ore)"
            elif OddityRandom <= 87:
                SPECIES = "Lustrous (Precious)"
            elif OddityRandom <= 89:
                SPECIES = "Lustrous (Semi-Precious)"
            elif OddityRandom <= 101:
                SPECIES = "Macawkra"
            elif OddityRandom <= 103:
                SPECIES = "Nymph (Alseid)"
            elif OddityRandom <= 105:
                SPECIES = "Nymph (Asteria)"
            elif OddityRandom <= 108:
                SPECIES = "Nymph (Aurae)"
            elif OddityRandom <= 110:
                SPECIES = "Nymph (Dryad)"
            elif OddityRandom <= 112:
                SPECIES = "Nymph (Lampad)"
            elif OddityRandom <= 114:
                SPECIES = "Nymph (Naiad)"
            elif OddityRandom <= 116:
                SPECIES = "Nymph (Oread)"
            elif OddityRandom <= 128:
                SPECIES = "Owlin"
            elif OddityRandom <= 134:
                SPECIES = "Rakin (Posskin)"
            elif OddityRandom <= 140:
                SPECIES = "Rakin (Tanukin)"
            elif OddityRandom <= 146:
                SPECIES = "Rakin (Urkin)"
            elif OddityRandom <= 152:
                SPECIES = "Ratfolk (Packrat)"
            elif OddityRandom <= 158:
                SPECIES = "Ratfolk (Ratical)"
            elif OddityRandom <= 164:
                SPECIES = "Ratfolk (Scourgerat)"
            elif OddityRandom <= 170:
                SPECIES = "Tengu"
            elif OddityRandom <= 182:
                SPECIES = "Tiefling (Amethyst Bloodline)"
            elif OddityRandom <= 194:
                SPECIES = "Tiefling (Gold Bloodline)"
            elif OddityRandom <= 200:
                SPECIES = "Warforged" 
            # csvfile = open(r"Lists\Oddity.csv", "r")
            # SPECIES = list(csv.reader(csvfile, delimiter=','))
            # selected_row = random.choice(SPECIES)  # Select a random row (list)
            # SPECIES = ','.join(selected_row)  # Convert the list to a comma-separated string
            # if SPECIES == 'ï»¿Aarakocra':
            #     SPECIES = 'Aarakocra'
        else:
            OutlanderRandom = random.randint(1, 200)
            if OutlanderRandom <= 9:
                SPECIES = "Aasimar (Cosmic)"
            elif OutlanderRandom <= 17:
                SPECIES = "Aasimar (Elfriche)"
            elif OutlanderRandom <= 28:
                SPECIES = "Changeling"
            elif OutlanderRandom <= 44:
                SPECIES = "Dragonborn (Faerie)"
            elif OutlanderRandom <= 55:
                SPECIES = "Dragonborn (Moonstone)"
            elif OutlanderRandom <= 71:
                SPECIES = "Elf (Eladrin)"
            elif OutlanderRandom <= 87:
                SPECIES = "Elf (Shadar-kai)"
            elif OutlanderRandom <= 93:
                SPECIES = "Elf (Snow)"
            elif OutlanderRandom <= 104:
                SPECIES = "Firbolg"
            elif OutlanderRandom <= 110:
                SPECIES = "Genasi (Air)"
            elif OutlanderRandom <= 116:
                SPECIES = "Genasi (Earth)"
            elif OutlanderRandom <= 122:
                SPECIES = "Genasi (Fire)"
            elif OutlanderRandom <= 128:
                SPECIES = "Genasi (Water)"
            elif OutlanderRandom <= 131:
                SPECIES = "Lunarran (Bloodmoon)"
            elif OutlanderRandom <= 134:
                SPECIES = "Lunarran (Bluemoon)"
            elif OutlanderRandom <= 137:
                SPECIES = "Lunarran (Crescent)"
            elif OutlanderRandom <= 140:
                SPECIES = "Lunarran (Waning)"
            elif OutlanderRandom <= 148:
                SPECIES = "Metallus (Alloy)"
            elif OutlanderRandom <= 156:
                SPECIES = "Metallus (Gold)"
            elif OutlanderRandom <= 164:
                SPECIES = "Opteran (Cityborn)"
            elif OutlanderRandom <= 172:
                SPECIES = "Opteran (Natureborn)"
            elif OutlanderRandom <= 181:
                SPECIES = "Tlakah (High Senye)"
            elif OutlanderRandom <= 190:
                SPECIES = "Tlakah (Low Senye)"
            elif OutlanderRandom <= 200:
                SPECIES = "Tlakah (Mid Senye)"
            # csvfile = open(r"Lists\Outlander.csv", "r")
            # SPECIES = list(csv.reader(csvfile, delimiter=','))
            # selected_row = random.choice(SPECIES)  # Select a random row (list)
            # SPECIES = ','.join(selected_row)  # Convert the list to a comma-separated string
            # if SPECIES == 'ï»¿Aasimar (Cosmic)':
            #     SPECIES = 'Aasimar (Cosmic)'
    else:
        PHBList = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
        SPECIES = random.choice(PHBList)
    return SPECIES

# Class #
def ClassGen(CLASSTOGGLE, INCLUDEHOMEBREWCLASSES):
    if CLASSTOGGLE == False:
        ClassRandom = random.randint(1, 20)
    else:
        ClassRandom = 20
    SAVE1 = "N/A"
    SAVE2 = "N/A"
    
    if ClassRandom < 19:
        CommonerRandom = random.randint(1, 100)
        if ClassRandom < 80:
            CLASS = "Commoner"
            MAINSTAT = "RAND"
            SECONDSTAT = "RAND"
            HITDIE = 4
        else:
            if CommonerRandom < 80:
                CLASS = "Commoner"
                MAINSTAT = "RAND"
                SECONDSTAT = "RAND"
                HITDIE = 4
            elif CommonerRandom == 80:
                CLASS = "Alchemist"
                if random.randint(1, 2) == 1:
                    MAINSTAT = "wis"
                else:
                    MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 81:
                CLASS = "Artificer"
                MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 82:
                CLASS = "Blacksmith"
                MAINSTAT = "str"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 83:
                CLASS = "Brewer"
                MAINSTAT = "wis"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 84:
                CLASS = "Carpenter"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 85:
                CLASS = "Cobbler"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 86:
                CLASS = "Cook"
                MAINSTAT = "wis"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 87:
                CLASS = "Enchanter"
                MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 88:
                CLASS = "Engineer"
                MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 89:
                CLASS = "Glassblower"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 90:
                CLASS = "Jeweler"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 91:
                CLASS = "Leatherworker"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 92:
                CLASS = "Mason"
                MAINSTAT = "str"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 93:
                CLASS = "Painter"
                MAINSTAT = "wis"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 94:
                CLASS = "Poisoner"
                if random.randint(1, 2) == 1:
                    MAINSTAT = "wis"
                else:
                    MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 95:
                CLASS = "Scroll Scriber"
                MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 96:
                CLASS = "Tailor"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 97:
                CLASS = "Tinkerer"
                MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 98:
                CLASS = "Wand Whittler"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 99:
                CLASS = "Weaver"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 6
            elif CommonerRandom == 100:
                CLASS = "Wood Carver"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 6
    else:
        if INCLUDEHOMEBREWCLASSES == False:
            PClassRandom = random.randint(1, 14)
            if PClassRandom == 1:
                CLASS = "Artificer"
                MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Constitution"
                SAVE2 = "Intelligence"
            elif PClassRandom == 2:
                CLASS = "Barbarian"
                MAINSTAT = "str"
                SECONDSTAT = "con"
                HITDIE = 12
                SAVE1 = "Strength"
                SAVE2 = "Constitution"
            elif PClassRandom == 3:
                CLASS = "Bard"
                MAINSTAT = "cha"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Dexterity"
                SAVE2 = "Charisma"
            elif PClassRandom == 4:
                CLASS = "Bloodhunter"
                MAINSTAT = "dex"
                SECONDSTAT = "int"
                HITDIE = 10
                SAVE1 = "Dexterity"
                SAVE2 = "Intelligence"
            elif PClassRandom == 5:
                CLASS = "Cleric"
                MAINSTAT = "wis"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Wisdom"
                SAVE2 = "Charisma"
            elif PClassRandom == 6:
                CLASS = "Druid"
                MAINSTAT = "wis"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Intelligence"
                SAVE2 = "Wisdom"
            elif PClassRandom == 7:
                CLASS = "Fighter"
                if random.randint(1, 2) == 1:
                    MAINSTAT = "str"
                else:
                    MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 10
                SAVE1 = "Strength"
                SAVE2 = "Constitution"
            elif PClassRandom == 8:
                CLASS = "Monk"
                MAINSTAT = "dex"
                SECONDSTAT = "wis"
                HITDIE = 8
                SAVE1 = "Strength"
                SAVE2 = "Dexterity"
            elif PClassRandom == 9:
                CLASS = "Paladin"
                MAINSTAT = "cha"
                SECONDSTAT = "str"
                HITDIE = 10
                SAVE1 = "Wisdom"
                SAVE2 = "Charisma"
            elif PClassRandom == 10:
                CLASS = "Ranger"
                MAINSTAT = "dex"
                SECONDSTAT = "wis"
                HITDIE = 10
                SAVE1 = "Strength"
                SAVE2 = "Dexterity"
            elif PClassRandom == 11:
                CLASS = "Rogue"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Dexterity"
                SAVE2 = "Intelligence"
            elif PClassRandom == 12:
                CLASS = "Sorcerer"
                MAINSTAT = "cha"
                SECONDSTAT = "RAND"
                HITDIE = 6
                SAVE1 = "Constitution"
                SAVE2 = "Charisma"
            elif PClassRandom == 13:
                CLASS = "Warlock"
                MAINSTAT = "cha"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Wisdom"
                SAVE2 = "Charisma"
            elif PClassRandom == 14:
                CLASS = "Wizard"
                MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 6
                SAVE1 = "Intelligence"
                SAVE2 = "Wisdom"
        else:
            PClassRandom = random.randint(1, 20)
            if PClassRandom == 1:
                CLASS = "Artificer"
                MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Constitution"
                SAVE2 = "Intelligence"
            elif PClassRandom == 2:
                CLASS = "Barbarian"
                MAINSTAT = "str"
                SECONDSTAT = "con"
                HITDIE = 12
                SAVE1 = "Strength"
                SAVE2 = "Constitution"
            elif PClassRandom == 3:
                CLASS = "Bard"
                MAINSTAT = "cha"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Dexterity"
                SAVE2 = "Charisma"
            elif PClassRandom == 4:
                CLASS = "Bloodhunter"
                MAINSTAT = "dex"
                SECONDSTAT = "int"
                HITDIE = 10
                SAVE1 = "Dexterity"
                SAVE2 = "Intelligence"
            elif PClassRandom == 5:
                CLASS = "Cleric"
                MAINSTAT = "wis"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Wisdom"
                SAVE2 = "Charisma"
            elif PClassRandom == 6:
                CLASS = "Druid"
                MAINSTAT = "wis"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Intelligence"
                SAVE2 = "Wisdom"
            elif PClassRandom == 7:
                CLASS = "Falconer"
                MAINSTAT = "dex"
                SECONDSTAT = "wis"
                HITDIE = 8
                SAVE1 = "Strength"
                SAVE2 = "Dexterity"
            elif PClassRandom == 8:
                CLASS = "Fighter"
                if random.randint(1, 2) == 1:
                    MAINSTAT = "str"
                else:
                    MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 10
                SAVE1 = "Strength"
                SAVE2 = "Constitution"
            elif PClassRandom == 9:
                CLASS = "Guardian"
                MAINSTAT = "str"
                if random.randint(1, 2) == 1:
                    SECONDSTAT = "con"
                else:
                    SECONDSTAT = "cha"
                HITDIE = 12
                SAVE1 = "Constitution"
                SAVE2 = "Charisma"
            elif PClassRandom == 10:
                CLASS = "Keeper"
                MAINSTAT = "cha"
                if random.randint(1, 2) == 1:
                    SECONDSTAT = "con"
                else:
                    if random.randint(1, 2) == 1:
                        SECONDSTAT = "str"
                    else:
                        SECONDSTAT = "dex"
                HITDIE = 8
                SAVE1 = "Constitution"
                SAVE2 = "Charisma"
            elif PClassRandom == 11:
                CLASS = "Magus"
                if random.randint(1, 2) == 1:
                    MAINSTAT = "str"
                else:
                    MAINSTAT = "dex"
                SECONDSTAT = "int"
                HITDIE = 10
                SAVE1 = "Constitution"
                SAVE2 = "Intelligence"
            elif PClassRandom == 12:
                CLASS = "Monk"
                MAINSTAT = "dex"
                SECONDSTAT = "wis"
                HITDIE = 8
                SAVE1 = "Strength"
                SAVE2 = "Dexterity"
            elif PClassRandom == 13:
                CLASS = "Paladin"
                MAINSTAT = "cha"
                SECONDSTAT = "str"
                HITDIE = 10
                SAVE1 = "Wisdom"
                SAVE2 = "Charisma"
            elif PClassRandom == 14:
                CLASS = "Pugilist"
                MAINSTAT = "str"
                SECONDSTAT = "con"
                HITDIE = 8
                SAVE1 = "Strength"
                SAVE2 = "Constitution"
            elif PClassRandom == 15:
                CLASS = "Ranger"
                MAINSTAT = "dex"
                SECONDSTAT = "wis"
                HITDIE = 10
                SAVE1 = "Strength"
                SAVE2 = "Dexterity"
            elif PClassRandom == 16:
                CLASS = "Rogue"
                MAINSTAT = "dex"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Dexterity"
                SAVE2 = "Intelligence"
            elif PClassRandom == 17:
                CLASS = "Sorcerer"
                MAINSTAT = "cha"
                SECONDSTAT = "RAND"
                HITDIE = 6
                SAVE1 = "Constitution"
                SAVE2 = "Charisma"
            elif PClassRandom == 18:
                CLASS = "Warlock"
                MAINSTAT = "cha"
                SECONDSTAT = "RAND"
                HITDIE = 8
                SAVE1 = "Wisdom"
                SAVE2 = "Charisma"
            elif PClassRandom == 19:
                CLASS = "Warlord"
                MAINSTAT = "str"
                if random.randint(1, 2) == 1:
                    SECONDSTAT = "wis"
                else:
                    SECONDSTAT = "cha"
                HITDIE = 8
                SAVE1 = "Wisdom"
                SAVE2 = "Charisma"
            elif PClassRandom == 20:
                CLASS = "Wizard"
                MAINSTAT = "int"
                SECONDSTAT = "RAND"
                HITDIE = 6
                SAVE1 = "Intelligence"
                SAVE2 = "Wisdom"

    Abilities = ["str", "dex", "con", "int", "wis", "cha"]
    
    if MAINSTAT == "RAND":
            MAINSTAT = Abilities.pop(random.randint(0, len(Abilities)-1))
            
    if SECONDSTAT == "RAND":
        SECONDSTAT = Abilities.pop(random.randint(0, len(Abilities)-1))
        if SECONDSTAT == MAINSTAT:
            SECONDSTAT = Abilities.pop(random.randint(0, len(Abilities)-1))
    
    if MAINSTAT == "RAND":
        randomstat = random.randint(1, 6)
        if randomstat == 1:
            MAINSTAT = "str"
        elif randomstat == 2:
            MAINSTAT = "dex"
        elif randomstat == 3:
            MAINSTAT = "con"
        elif randomstat == 4:
            MAINSTAT = "int"
        elif randomstat == 5:
            MAINSTAT = "wis"
        else:
            MAINSTAT = "cha"

    if SECONDSTAT == "RAND":
        randomstat = random.randint(1, 6)
        if randomstat == 1:
            SECONDSTAT = "str"
        elif randomstat == 2:
            SECONDSTAT = "dex"
        elif randomstat == 3:
            SECONDSTAT = "con"
        elif randomstat == 4:
            SECONDSTAT = "int"
        elif randomstat == 5:
            SECONDSTAT = "wis"
        else:
            SECONDSTAT = "cha"
    return CLASS, MAINSTAT, SECONDSTAT, ClassRandom, HITDIE, SAVE1, SAVE2

# Level/challenge Rating #
def LevelCRGen(ClassRandom):
    
    LEVEL = 0
    if ClassRandom >= 18:
        Leveling = 1
        while Leveling == 1:
            Leveling = random.randint(1,2) # 50% chance to level up
            LEVEL += 1

    CHALLENGERATING = "Party CR"
    if ClassRandom >= 18:
        CHALLENGERATING = random.randint(1, 6)

        if CHALLENGERATING == 1:
            CHALLENGERATING = "Party CR-2"
        elif CHALLENGERATING == 2:
            CHALLENGERATING = "Party CR-1"
        elif CHALLENGERATING == 3:
            CHALLENGERATING = "Party CR"
        elif CHALLENGERATING == 4:
            CHALLENGERATING = "Party CR"
        elif CHALLENGERATING == 5:
            CHALLENGERATING = "Party CR+1"
        else:
            CHALLENGERATING = "Party CR+2"
    
    PROFICIENCYBONUS = 0    
    if LEVEL < 5:
        PROFICIENCYBONUS = 2
    elif LEVEL < 9:
        PROFICIENCYBONUS = 3
    elif LEVEL < 13:
        PROFICIENCYBONUS = 4
    elif LEVEL < 17:
        PROFICIENCYBONUS = 5
    else:
        PROFICIENCYBONUS = 6
        
    return LEVEL, CHALLENGERATING, PROFICIENCYBONUS
# Gender #
def GenderGen():
    GENDER = random.randint(1, 100)

    if GENDER <= 40:
        GENDER = "Male"
    elif GENDER <= 80:
        GENDER = "Female"
    elif GENDER <= 90:
        GENDER = "Androgynous"
    elif GENDER <= 95:
        GENDER = "Effeminate Male"
    elif GENDER <= 100:
        GENDER = "Masculine Female"
    return GENDER

# Disposition #
def DispositionGen():
    DISPOSITION = random.randint(1, 6)

    if DISPOSITION == 1:
        DISPOSITION = "Hostile"
    elif DISPOSITION == 2:
        DISPOSITION = "Friendly"
    elif DISPOSITION == 3:
        DISPOSITION = "Friendly"
    elif DISPOSITION == 4:
        DISPOSITION = "Indifferent"
    elif DISPOSITION == 5:
        DISPOSITION = "Indifferent"
    else:
        DISPOSITION = "Indifferent"
    return DISPOSITION

# Alignment #
def AlignmentGen():
    ALIGNMENT = random.randint(1, 10)

    # Disposition altering alignment may not be necessarily what I'm looking for, but the idea holds merit for later use.
    # if DISPOSITION == "Hostile":
    #     ALIGNMENT += 3
    # elif DISPOSITION == "Friendly":
    #     ALIGNMENT -= 3

    if ALIGNMENT == 1:
        ALIGNMENT = "Lawful Good"
    elif ALIGNMENT == 2:
        ALIGNMENT = "Lawful Neutral"
    elif ALIGNMENT == 3:
        ALIGNMENT = "Lawful Evil"
    elif ALIGNMENT == 4:
        ALIGNMENT = "Neutral Good"
    elif ALIGNMENT == 5:
        ALIGNMENT = "True Neutral"
    elif ALIGNMENT == 6:
        ALIGNMENT = "True Neutral"
    elif ALIGNMENT == 7:
        ALIGNMENT = "Neutral Evil"
    elif ALIGNMENT == 8:
        ALIGNMENT = "Chaotic Good"
    elif ALIGNMENT == 9:
        ALIGNMENT = "Chaotic Neutral"
    else:
        ALIGNMENT = "Chaotic Evil"
    return ALIGNMENT

# Goal/Motivation #
def GoalGen():
    with open(r"Lists\Goals.csv", "r", encoding="utf-8") as csvfile:
        GOAL = list(csv.reader(csvfile, delimiter=','))
    selected_row = random.choice(GOAL)  # Select a random row (list)
    GOAL = ','.join(selected_row)  # Convert the list to a comma-separated string
    return GOAL

def GenerateNPC(CLASSTOGGLE, Classification, INCLUDEHOMEBREWCLASSES):
    SPECIES = SpeciesGen(Classification, PHBCLASSES)
    CLASS, MAINSTAT, SECONDSTAT, ClassRandom, HITDIE, SAVE1, SAVE2 = ClassGen(CLASSTOGGLE, INCLUDEHOMEBREWCLASSES)
    LEVEL, CHALLENGERATING, PROFICIENCYBONUS = LevelCRGen(ClassRandom)
    GENDER = GenderGen()
    DISPOSITION = DispositionGen()
    ALIGNMENT = AlignmentGen()
    GOAL = GoalGen()
    
    return SPECIES, CLASS, MAINSTAT, SECONDSTAT, LEVEL, CHALLENGERATING, GENDER, DISPOSITION, ALIGNMENT, GOAL, PROFICIENCYBONUS, HITDIE, SAVE1, SAVE2

def PrintResults():
    print(f"\nGender: {GENDER}\nSpecies: {SPECIES}\nClass: {CLASS}\nLevel: {LEVEL}\nChallenge Rating: {CHALLENGERATING}\nDisposition: {DISPOSITION}\nAlignment: {ALIGNMENT}\n\nGoal: {GOAL}")
    
def ExportNPC(HITDIE, SAVE1, SAVE2):
    with open(r'Lists\template-character.json', 'r') as json_file:
        template_json = json.load(json_file)

        # Ability Scores
        
        ability_scores = template_json["abilityScores"]
        
        StandardArray = [13, 12, 10, 8]
        Count = 0
        for ability in ability_scores:
            if ability['name'] == MAINSTAT:
                ability['value'] = 15
            elif ability['name'] == SECONDSTAT:
                ability['value'] = 14
            else:
                if ability['name'] != MAINSTAT or ability['name'] != SECONDSTAT:
                    ability['value'] = StandardArray.pop(random.randint(0, len(StandardArray)-1))
            if Count == 0:
                ability['value'] += 2
            if Count == 4:
                ability['value'] += 1
            if ability['name'] == "dex":    # Initative Bonus
                template_json["initiativeBonus"] = math.floor((int(ability['value'])-10)/2)
            if ability['name'] == "con":    # HP
                for tracker in template_json["trackers"]:
                    if tracker['name'] == "HP": # HP
                        HPROLLING = LEVEL -1
                        tracker['max'] = 0
                        while HPROLLING > 0:
                            HPROLLING -= 1
                            tracker['max'] += random.randint(1, HITDIE) + math.floor((int(ability['value'])-10)/2)
                        tracker['max'] = tracker['max'] + HITDIE + math.floor((int(ability['value'])-10)/2) # First Level Max HP
                        tracker['value'] = tracker['max']
            Count += 1
        
        # Skills
        SkillList = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
        Skills = template_json["skills"]
        NumberofSkills = random.randint(3, 5)
        
        while NumberofSkills > 0:
            ChosenSkill = SkillList.pop(random.randint(0, len(SkillList)-1))
            for skill in Skills:
                if skill['name'] == ChosenSkill:
                    skill['proficient'] = True
                    NumberofSkills -= 1
                    break
        
        # Proficiencies
        Proficiencies = template_json["proficiencies"]
        for entry in Proficiencies:
            if entry['name'] == "SAVE1":
                entry['name'] = SAVE1
            elif entry['name'] == "SAVE2":
                entry['name'] = SAVE2
        
        
        
        # Name
        
        # Define a variable with a new value
        new_name = SPECIES+" "+CLASS

        # Update the 'name' field in the dictionary with the new value
        template_json["name"] = new_name
        
        # Alignment
        
        template_json["alignment"] = ALIGNMENT
        
        # Class & Level
        
        for entry in template_json["classes"]:
            entry["class"] = CLASS
            entry["level"] = LEVEL

        # Challenge Rating/Proficiency Bonus
        
        template_json["challengeRating"] = CHALLENGERATING
        template_json["proficiencyBonus"] = PROFICIENCYBONUS
        
        # Armor Class
        ClassACMOD = 0
        if CLASS == "Artificer":
            ClassACMOD = 0
        elif CLASS == "Barbarian":
            ClassACMOD = 1
        elif CLASS == "Bard":
            ClassACMOD = 0
        elif CLASS == "Bloodhunter":
            ClassACMOD = 0
        elif CLASS == "Cleric":
            ClassACMOD = 0
        elif CLASS == "Paladin":
            ClassACMOD = 1
        template_json["armorClass"] = 12 + math.floor((random.randint(15,22)/10)*PROFICIENCYBONUS)+ClassACMOD
        
        # Race
        
        template_json["race"] = SPECIES
        
        # Description
        
        template_json["description"] = f"# Visual\nRace: {SPECIES}\nGender: {GENDER}\nHeight: \nHair Color: \nNotable Features: \n\n# Brief\nThis section should be 2-3 sentences long and briefly describe the character's physical appearance and personality regarding the party.\n\n# Relation\n## Party\nHow the party knows/met the NPC and how they affect them.\n\n## World\nHow the NPC knows/interacts with various organizations and or other NPCs throughout the world.\n\n# Background\nThis section should vary in length substantially, revealing more about an NPC's past as the players continue to learn about them. Should be written in the past tense.\n\n# Important Notes\nWhen this NPC mentions something important to them or to the party, it should be put here in a list format.\n\n![# DM Section]()\n![## Voice]()\n![A description of this character's voice when appropriate should be described here.]()\n\n![## Current Goals]()\n![This should be the NPC's CURRENT Goals, likely in a list format, with older goals crossed out.]()\n\n![## Motivations]()\n![This motivation should inform the NPC's current and longterm goals, what they strive for.]()\n\n![## Secrets]()\n![Anything this NPC attempts to keep from the party or the world in general.]()\n\n![## Other]()\n![Misc that I have not yet catagorized.]()"
        
    # Export the modified dictionary as a JSON file
    outputfilename = "NPCs\\"+ str(int(time.time()))+GENDER+" "+SPECIES+" "+CLASS+'.json'
    with open(outputfilename, 'w') as json_file:
        json.dump(template_json, json_file, indent=4)
        
    print("Exported NPC to "+outputfilename)

print("Welcome to Nox's NPC Generator.")
SPECIES = ""
CLASSTOGGLE = False
INCLUDEHOMEBREWCLASSES = False
PHBCLASSES = False
Classification = ""
Choice = "1"
while Choice != "5":
    Choice = input("\n1. Generate New NPC\n2. Edit NPC\n3. Export NPC\n4. Settings\n5. Exit\n\nInput: ")
    print("----------------------------------------")
    if Choice == "1":
        SPECIES, CLASS, MAINSTAT, SECONDSTAT, LEVEL, CHALLENGERATING, GENDER, DISPOSITION, ALIGNMENT, GOAL, PROFICIENCYBONUS, HITDIE, SAVE1, SAVE2 = GenerateNPC(CLASSTOGGLE, Classification, INCLUDEHOMEBREWCLASSES)
        
        PrintResults()
        
    elif Choice == "2":
        if SPECIES == "":
            print("No NPC Generated. Please Generate an NPC first.\n")
        else:
            EditChoice = input("\n1. Random Generate\n2. Direct Edit\n\nInput: ")
            if EditChoice == "1":
                GenerateChoice = input("\n1. Species\n2. Class\n3. Level\n4. Gender\n5. Disposition\n6. Alignment\n7. Goal\n\nInput: ")
                print("----------------------------------------")
                if GenerateChoice == "1":
                    SPECIES = SpeciesGen(Classification, PHBCLASSES)
                elif GenerateChoice == "2":
                    CLASS, MAINSTAT, SECONDSTAT, ClassRandom, HITDIE = ClassGen(CLASSTOGGLE, INCLUDEHOMEBREWCLASSES)
                elif GenerateChoice == "3":
                    LEVEL, CHALLENGERATING, PROFICIENCYBONUS = LevelCRGen(20)
                elif GenerateChoice == "4":
                    GENDER = GenderGen()
                elif GenerateChoice == "5":
                    DISPOSITION = DispositionGen()
                elif GenerateChoice == "6":
                    ALIGNMENT = AlignmentGen()
                elif GenerateChoice == "7":
                    GOAL = GoalGen()
                else:
                    print("Invalid Input.")
                
                PrintResults()
            
            elif EditChoice == "2":
                DirectChoice = input("\n1. Species\n2. Class\n3. Level\n4. Gender\n5. Disposition\n6. Alignment\n7. Goal\n\nInput: ")
                print("----------------------------------------")
                if DirectChoice == "1":
                    SPECIES = input("Enter Species: ")
                elif DirectChoice == "2":
                    CLASS = input("Enter Class: ")
                    MAINSTAT = input("Enter Main Stat: ")
                    SECONDSTAT = input("Enter Secondary Stat: ")
                elif DirectChoice == "3":
                    LEVEL = int(input("Enter Level: "))
                    CHALLENGERATING = input("Enter Challenge Rating: ")
                    PROFICIENCYBONUS = 0
                    
                    if LEVEL < 5:
                        PROFICIENCYBONUS = 2
                    elif LEVEL < 9:
                        PROFICIENCYBONUS = 3
                    elif LEVEL < 13:
                        PROFICIENCYBONUS = 4
                    elif LEVEL < 17:
                        PROFICIENCYBONUS = 5
                    else:
                        PROFICIENCYBONUS = 6
                    LEVEL = int(LEVEL)
                    
                elif DirectChoice == "4":
                    GENDER = input("Enter Gender: ")
                elif DirectChoice == "5":
                    DISPOSITION = input("Enter Disposition: ")
                elif DirectChoice == "6":
                    ALIGNMENT = input("Enter Alignment: ")
                elif DirectChoice == "7":
                    GOAL = input("Enter Goal: ")
                else:
                    print("Invalid Input.")
                
                PrintResults()
            
    elif Choice == "3":
        if SPECIES == "":
            print("No NPC Generated. Please Generate an NPC first.\n")
        else:
            ExportNPC(HITDIE, SAVE1, SAVE2)
        
    elif Choice == "4":
        SettingsChoice = input("\n1. Toggle Player Class\n2. Toggle Homebrew Classes\n3. Set Species Classification\n4. Toggle PHB Species Only\n\nInput: ")
        print("----------------------------------------")
        if SettingsChoice == "1":
            if CLASSTOGGLE == True:
                CLASSTOGGLE = False
                print("Player Class Toggled Off.")
            else:
                CLASSTOGGLE = True
                print("Player Class Toggled On.")
        elif SettingsChoice == "2":
            if INCLUDEHOMEBREWCLASSES == True:
                INCLUDEHOMEBREWCLASSES = False
                print("Homebrew Classes Toggled Off.")
            else:
                INCLUDEHOMEBREWCLASSES = True
                print("Homebrew Classes Toggled On.")
        elif SettingsChoice == "3":
            ClassificationChoice = input("\n1. Naturalborn\n2. Oddity\n3. Outlander\n4. Random\n\nInput: ")
            print("----------------------------------------")
            if ClassificationChoice == "1":
                Classification = "Naturalborn"
            elif ClassificationChoice == "2":
                Classification = "Oddity"
            elif ClassificationChoice == "3":
                Classification = "Outlander"
            elif ClassificationChoice == "4":
                Classification = ""
            else:
                print("Invalid Input.")
        elif SettingsChoice == "4":
            if PHBCLASSES == True:
                PHBCLASSES = False
                print("PHB Only Species Toggled Off.")
            else:
                PHBCLASSES = True
                print("PHB Only Species Toggled On.")
        else:
            print("Invalid Input.")
        
    elif Choice == "5":
        print("Exiting.")
    else:
        print("Invalid Input.")
