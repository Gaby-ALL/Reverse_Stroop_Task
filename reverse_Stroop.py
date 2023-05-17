#import the Expyriment package into Python
import random
from expyriment import design, stimuli, control

#create a new Experiment object by calling the Experiment class and name it “First Experiment”
exp = design.Experiment(name="reverse_stroop_task_PCBS")

# Define a list of color names
colors = [(0, 255, 0),(0, 0, 255), (255, 255, 0), (255, 0, 0)]
color_names = ["Green", "Blue", "Yellow", "Red"]

#initialize this experiment : Present the startup screen, Start an experimental clock...
control.initialize(exp)

#Create the block 1
block_one = design.Block() #creat an experimental block

# Create 5 trials and stimuli
for r in range(5):

    # Randomly select color name and color index
    selected_color_name = random.choice(color_names)
    selected_color_index = random.randint(0, len(colors) - 1)
    selected_color = colors[selected_color_index]

    # Create an experimental trial
    trial_one = design.Trial()

    # Create a TextLine stimulus with the selected color
    stim = stimuli.TextLine(selected_color_name,text_colour=selected_color,text_size=70)
    stim.preload()

    # Create colored squares
    square_color = (255, 0, 0)  # Red color
    square_position = (500, 500)  # Position of the square
    square_size = (100, 100)  # Size of the square
    square = stimuli.Rectangle(size=square_size, position=square_position, colour=square_color)
    square.preload()

    # Add the stimulus and the square to the trial
    trial_one.add_stimulus(stim)
    trial_one.add_stimulus(square)

    # Add the trial to the block
    block_one.add_trial(trial_one) 

# Add the block to the experiment
exp.add_block(block_one)

#start running the currently active (initiated) experiment : Present a screen to ask , Create a data file...
control.start()

# Present the stimulus in sucession
for trial in block_one.trials:
    exp.clock.wait(1000)  # Wait for 1 second before presenting the stimulus
    trial_one.stimuli[0].present()  # Present all stimuli in the trial simultaneously
    exp.clock.wait(1000)  # Wait for 1 second before proceeding to the next trial

#end experiment: automatically save the data and the event file and show the “Ending experiment” screen
control.end()
