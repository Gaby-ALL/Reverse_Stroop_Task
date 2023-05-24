# Import the Expyriment package into Python
import random
from expyriment import design, stimuli, control, misc

# Create a new Experiment 
exp = design.Experiment(name="stroop_task_PCBS")

# Define a list of color names

colors = [(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0)]
color_names = ["Green", "Blue", "Yellow", "Red"]

# Initialize this experiment
control.initialize(exp)
exp.mouse.show_cursor()
exp.keyboard.wait()


# Create squares
screen_size = exp.screen.surface.get_size()
square_size = 150

positions = [(400, 300), (-400, 300), (400, -300), (-400, -300)]  # top right, bottom right, top left, bottom left


# Create the block 
block_one = design.Block() #creat an experimental block

# Create multiple trials 
num_trials = 10  

# Create instruction screen
instruction_text = """
Welcome to the Reverse Stroop Task!
In this task, you will see colored squares and words.
Your task is to indicate the color of the word by clicking on the corresponding Square.You have to ignore the word itself.
Press any space bar to start the task.
"""

instruction_screen = stimuli.TextScreen("Instructions", instruction_text)
instruction_screen.present()
exp.keyboard.wait_char(' ')

#exp.keyboard.wait(expyriment.misc.constants.K_ANY)


for trial_number in range(num_trials):

    # Randomly select color name and color indix
    selected_color_name = random.choice(color_names)
    selected_color_index = random.randint(0, len(colors) - 1)
    selected_color = colors[selected_color_index]
    trial_positions = positions.copy()
    random.shuffle(trial_positions)

    # Create square stimuli with shuffled positions for the trial
    squares = [
        stimuli.Rectangle(size=(square_size, square_size), position=trial_positions[0], colour=(255, 0, 0)),   # top-left
        stimuli.Rectangle(size=(square_size, square_size), position=trial_positions[1], colour=(0, 255, 0)),   # top-right
        stimuli.Rectangle(size=(square_size, square_size), position=trial_positions[2], colour=(0, 0, 255)),   # bottom-left
        stimuli.Rectangle(size=(square_size, square_size), position=trial_positions[3], colour=(255, 255, 0))  # bottom-right
    ]

    # Create the trial
    trial = design.Trial()

    # Add the squares as stimuli for the trial
    for square in squares:
        trial.add_stimulus(square)

    # Create the text stimulus
    text_stimulus = stimuli.TextLine(selected_color_name, text_colour=selected_color, text_size=70)

    # Preload the text stimulus
    text_stimulus.preload()

    # Add the stimulus to the trial
    trial.add_stimulus(text_stimulus)

    # Add the trial to the block
    block_one.add_trial(trial) 

# Add the block to the experiment
exp.add_block(block_one)

# Start the experiment
control.start()

# Present the stimulus in sucession

for block in exp.blocks:
    for trial in block.trials:
       
        # Clear the screen and update
        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(2000)

        # Present all stimuli in the trial
        for stimulus in trial.stimuli:
            stimulus.preload()

        # Present all stimuli simultaneously
        for stimulus in trial.stimuli:
            stimulus.present(clear=False)  # Set clear=False to present stimuli simultaneously

        # Wait for participant response
        button, position, _ = exp.mouse.wait_press()
        
        participant_response = None


        for square in squares:
            if square.overlapping_with_position(position):
                participant_response = square.colour

        exp.data.add([trial_number, selected_color_name, participant_response]) 

        exp.clock.wait(1000) 


#end experiment
#exp.data.save("reverse_stroop_PCBS.csv")
#control.end()
exp.data.save("reverse_stroop_PCBS.csv")
control.end()
