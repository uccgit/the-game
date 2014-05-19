# Defines all the areas in the game
# I would like access of them to be based on level

area_names = {
    'Elysium': 'Ruled by Cronus and home to the most deserving dead',
    'Tartarus': 'The dungeon of torment and sufferings',
    'Asphodel Fields': 'The meadow of asphodel where abide the souls and phantoms of those whose work is done',
    'Elysian Fields': 'Reserved those chosen by the gods, the righteous, and heroic'
}


river_names = {
    'Acheron': 'The river of woe',
    'Cocytus': 'The River of wailing',
    'Lethe': 'The River of unmindfulness',
    'Phlegethon': 'The River of Flames',
    'Styx': 'The Hades River. Formed a boundary between Earth and the Underworld'
}

town_names = {
    'Home': 'Your House'
}



# Test Loops
print "Current Areas"
for word in area_names:
    print "-", word

print "Current Rivers"
for word in river_names:
    print "#", word

for word in town_names:
    print "$", word



