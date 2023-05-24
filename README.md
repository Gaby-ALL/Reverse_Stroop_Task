# Reverse_Stroop_Task.
The code provided is a Python script that implements the Stroop Task using the Expyriment package. The Stroop Task is a classic cognitive psychology task that measures interference in processing conflicting information.

File Structure:
- reverse_stroop_PCBS.py: The main Python script that runs the Stroop Task experiment.
- reverse_stroop_PCBS.csv: The data file where the participant's responses will be saved.

Dependencies:

The code relies on the following dependencies:
- Python 3.x
- Expyriment package (install using pip install expyriment)
Running the Experiment:

To run the experiment, follow these steps:
1. Make sure you have Python 3.x installed on your machine.
2. Install the Expyriment package by running pip install expyriment in your terminal or command prompt.
3. Save the code in a file named reverse_stroop_PCBS.py.
4. Open a terminal or command prompt and navigate to the directory containing the code file.
5. Run the script by executing python reverse_stroop_PCBS.py.

Description:

1. The code begins by importing the necessary modules from the Expyriment package and defining the experiment's name and variables.
2. The experiment is initialized using control.initialize(exp), which presents the startup screen and starts the experimental clock.
3. The squares and color names for the Stroop Task are defined.
4. The code creates a block for the experiment and iterates through the desired number of trials.
5. For each trial, a random color and position for the squares are selected. The trial stimuli, including the squares and the color word, are created and added to the trial.
6. The trial is then added to the experiment block.
7. The block is added to the experiment.
8. The experiment is started using control.start().
9. The stimuli are presented in succession. Each trial starts with a clear screen, followed by the presentation of the stimuli (squares and color word).
10. The participant is expected to provide a response by pressing any key.
11. After a fixed duration, the stimuli are cleared, and the next trial begins.
12. Once all trials are completed, the data from the experiment are saved to a CSV file named reverse_stroop_PCBS.csv.
13. The experiment is ended using control.end().

Modifications:
- If you want to adjust the number of trials, modify the num_trials variable.
- The code can be customized by changing the color names, colors, and square positions in the colors, color_names, and positions variables, respectively.
- You can modify the duration of stimulus presentation and inter-trial intervals by adjusting the exp.clock.wait() functions.

Note: Make sure to have the Expyriment package installed before running the code
