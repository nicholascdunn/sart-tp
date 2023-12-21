# Sustained Attention to Response Task with Thought Probes (SART-TP) in PsychoPy.

## Description
This task was developed based on the Cristoff et al. (2021) study, which used a SART with Thought Probes to assess mindwandering.
We programmed this task for use in an fMRI machine. As such, frame-based timing was used to ensure millisecond accuracy for
the presentation of stimuli, which is necessary for fMRI studies.

*NOTE: This functionality (i.e., frame-based timing, non-slip timing) is difficult to achieve in PsychoPy builder. If all of your trials
are the same length, then it is possible to do, and you can find guides online for how to achieve this. However, our task needed
target and non-target stimuli presentations that were different total durations than our thought probe trials, so coding this task
was the only option (as of this version of PsychoPy). In theory, you could also achieve this via while loops and clock-based timing.
I just learned frame-based timing first.

The task presents a random number between 0 and 9 for 500ms followed by a 1800ms inter-stimulus interval (ISI) for target and non-target
trials. If the stimulus is a non-target trial (any number but 3), the participant is instructed to press the <left> key. If the stimulus is
3, the participant is instructed to without a response. Reaction time (ms) and whether they correctly responded are saved to an excel output.

Occasionally, a thought probe is presented. Probe 1 asks whether the participant's mind was on-task or off-task at the time of presentation. 
It is presented for 500ms, with an ISI of 0ms. If on-task, the participant responds by pressing the <left> key. If off-task, the participant 
responds by pressing the <right> key. The response to probe 1 is saved to the excel output. For probe 2, the participant is presented with
a conditional stimulus, depending on their response to probe 1. If on-task in probe 1, they are instructed to complete an attention check,
wherein they are told either to press the <left> or <right> key. If off-task or did not respond to probe 1, they are asked whether
they were externally distracted (<left>) or daydreaming/mindwandering (<right>). This response is also recorded in the excel output.

There are 5 blocks total, with 1725 total trials. Each block has 297 non-target trials, 16 target trials, and 16 thought probe pairs (probe 1
and probe 2), totaling 345 trials. Targets and thought probe pairs were pseudocounterbalanced to only occur with a random distance between
5-15 non-target trials away from each other (e.g., you receive a target trial --> you will receive another target OR probe between
5 and 15 non-target trials after finishing the target trial). Each block takes about 17 minutes.  
