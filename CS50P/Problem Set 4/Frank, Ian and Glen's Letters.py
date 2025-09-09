# imports the various fonts to be applied to the input
# i.e. takes figlet class from the pyfiglet module
from pyfiglet import Figlet
figlet = Figlet()
# allows for interaction with the command line inputs from a user
import sys
# ensures that a font is able to be randomly selected if no arguments are passed through the input
import random

# obtains a list of available fonts from figlet class
fonts = figlet.getFonts()

# check when there are no command line arguments
if len(sys.argv) == 1:
    # will select from the fonts variable randomly and apply the font to the text
    figlet.setFont(font=random.choice(figlet.getFonts()))

# checks 2 arguments are passed and a font name
# first argument needs to be 'f' or 'font'
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):

        # Check if the font is valid
        # aims to stop invalid fonts being applied
        if sys.argv[2] not in fonts:
            print('Invalid usage')
            sys.exit(1)

        # Set and render the chosen font
        figlet.setFont(font=sys.argv[2])

else:
    print('Invalid usage')
    sys.exit(1)

# asks for input from a user and gives an output
question = input('Input: ')
# converts input into art using the currently selected set font
print(figlet.renderText(question))

# rationale for the question being at the end is that the input first needs to be validated
# then after validation at the command line level, then looks to input
# then looks to apply the font to the input
