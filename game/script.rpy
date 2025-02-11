# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")

image hunted_overlay = Movie(play="sc_overlay.webm", loop=True)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black default

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    n "The sound of the leaves rushing past barely even register as you dash forward, your heart thundering in your chest as you keep your eyes focused ahead of you. Every step seems to jolt you with the force of an explosion."

    scene bg hunted with dissolve 
    
    n "It's as if you can feel yourself growing weaker with each step but you don't have any choice other than to keep moving. Moving forward, moving away, because behind you is danger... no... more than danger..."

    n "Behind you is death, it hunts you as a wolf does a doe and just like that wounded and dying deer you can feel yourself being worn down."

    n "With every beat of your heart you feel a little less alive and a little more afraid, but there is no stopping now. You just need a chance, a sign, anything to help you escape!"

    n "A light burns in the distance, if you could just reach it you could make it to safety, you could finally be free... but it's... it's just so..."

    n "You collapse, tumbling in a violent burst of leaves and dust, your breath coming in desperate and panicked gasps."

    n """
    You're... 
    
    You're... going to die here...

    You're... going to die here... Your skin grows cold, your breath ragged...

    You're... going to die here... Your skin grows cold, your breath ragged... the haunting blue eyes of your pursuer growing closer...
    """

    n "The world around you fades to black and the last thing you feel before the sweet embrace of death is the gentle touch of a small, furred hand."

    n '"Woah, hey mister! Are you alright?! Hey! Hey guys, someone-"'

    n "The words grow more distant as the world slips further away and then it is gone completely."

    # This ends the game.

    return
