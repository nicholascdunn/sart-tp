'''
Nicholas C. Dunn
Sustained Attention to Response Task with Thought Probes (SART-TP)
PsychoPy
12/4/2023
v0.5
'''

from __future__ import absolute_import, division
from ast import withitem

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, monitors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import pandas as pd

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.2'
expName = 'SART-TP'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '1', 'practice': ('No', 'Yes')}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\SART\\sart-tp-frameBased.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.0001  # how close to onset before 'same' frame

#-------------------EXPERIMENT CODE---------------------------------------------

# Setup window
mon = monitors.Monitor('monitor')

win = visual.Window(monitor=mon)

# Store monitor framerate
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

# Set refresh rate
refresh = 1.0/60.0
#refresh = frameDur
# Create default keyboard
defaultKeyboard = keyboard.Keyboard()

# Create default instruction stimulus
instrStim = visual.TextStim(win)

# Create fixation stimulus
fixStim = visual.TextStim(win, text='+', font='Open Sans')

instr1 = 'Welcome to the SART-TP'
instr2 = 'In this task, you will see numbers from 0 to 9. You are to press <spacebar> each time any number EXCEPT 3 appears on the screen. If the number 3 appears, do NOT press <spacebar>.'
instr3 = 'Occasionally, you will be asked whether your mind was on task. If your mind was on task, press <left>. If your mind was off task, press <right>.'
instr4 = 'You will also be asked to occasionally recall the last digit you saw. If the digit is the last number you saw, press <left>. If it was not the last digit you saw, press <right>.'
instr5 = 'You are now ready to complete the task. Before starting, you will see a countdown appear. Once the countdown ends, you will begin the task.'

instrList = [instr1, instr2, instr3, instr4, instr5]
            
# Create default visual stimulus
stim = visual.TextStim(win)

# Create probe 1 response stimuli
probe1Resp1 = visual.TextStim(win, 'On task \n <left>', font='Open Sans', pos=(-.5,-.5))
probe1Resp2 = visual.TextStim(win, 'Off Task \n <right>', font='Open Sans', pos=(.5,-.5))

# Create probe 2 response stimuli
probe2Resp1 = visual.TextStim(win, 'Yes \n <left>', font='Open Sans', pos=(-.5,-.5))
probe2Resp2 = visual.TextStim(win, 'No \n <right>', font='Open Sans', pos=(.5,-.5))

# Set durations (seconds)
numISI = 2
numDur = .5
probeISI = 5
probeDur = 1

# Set frame counts
numFrames = int(numDur / refresh)
numISIFrames = int(numISI / refresh)
probeFrames = int(probeDur / refresh)
probeISIFrames = int(probeISI /refresh)
totalNumFrames = int(numFrames + numISIFrames)
totalProbeFrames = int(probeFrames + probeISIFrames)

# Initialize list of block condition files
blockFiles = ['CDSImagingPilotProtocol_TimingsBlock1.xlsx']
blockCount = 1

# Initialize clocks
globalClock = core.Clock()
trialClock = core.Clock()
countdownTimer = core.CountdownTimer()

win.recordFrameIntervals = True # enables framerate tracking
win.refreshThreshold = 1.0/6.0 + 0.004 # sets the tolerance before considering a frame dropped

for instr in instrList:
    countdownTimer.reset()
    countdownTimer.add(10)
    while countdownTimer.getTime() > 0:
        instrStim.setText(instr)
        instrStim.draw()
        win.flip()

countdownTimer.reset()

countdown = 60
for sec in range(60):
    countdownTimer.add(1)
    while countdownTimer.getTime() > 0:
        instrStim.setText(countdown)
        instrStim.draw()
        win.flip()
    countdown-=1
    

# Experiment loop - opens block condition files sequentially
for block in blockFiles:
    # Initialize trial handler (PsychoPy function)
    trials = data.TrialHandler(nReps=1, method='sequential', trialList=data.importConditions(block))
   
    # Reset global clock to track time across each block
    globalClock.reset()
    
    # Initialize trial count to be added to .csv
    trialCount=0
    
    # Trial loop - loops through trials within a given block (i.e., rows in the condition files)
    for trial in trials:
        # Reset trial clock each loop
        trialClock.reset()
        
        # Logs trial start time
        startTime = trialClock.getTime() * 1000
        logging.log(level=logging.EXP, msg=f"Trial start: {startTime}")
        
        # Clears keyboard events
        event.clearEvents(eventType='keyboard')
        
        # Sets stimulus to be the stimulus from conditions file for the given loop
        stimulus = trial['stimulus']
        stim.setText(stimulus)
        
        stimOnset = None
        subResp=[]
        # corrAns=[]
        corrAns = trial['corrAns']
        correct = 0
        respTime=None
        count=-1
        onTask = 0
        mindwander = ''
        trialType = trial['trialType']
        if trial['trialType'] == 'Target' or trial['trialType'] == 'Non-target':
            for frameN in range(totalNumFrames):
            
                if 0 <= frameN <= (numFrames):
                    stim.draw()
                    win.flip()
                    
                    if frameN == 0:
                        stimOnset = globalClock.getTime()
                
                    if frameN == numFrames:
                        print('End number num frame =', frameN)
            
                if numFrames < frameN < (totalNumFrames):
                    stimOffset = globalClock.getTime()
                    fixStim.draw()
                    win.flip()
                    
                    if frameN == (totalNumFrames-1):
                        print('End ISI frame =', frameN)
            
                keys = event.getKeys(keyList=['space'])
                
                
                if keys:
                    count+=1
                    if count==0:
                        respTime = trialClock.getTime()
                        subResp = keys
                        if subResp[0] == corrAns:
                            print(subResp[0])
                            print(subResp)
                            print(subResp[0] == corrAns)
                            correct = 1     
            trialCount+=1
            print(trialCount, stimulus, subResp, respTime, corrAns)            
        elif trial['trialType'] == "Probe 1":
            for frameN in range(totalProbeFrames):
                
                if 0 <= frameN <= (probeFrames):
                   
                    stim.draw()
                    probe1Resp1.draw()
                    probe1Resp2.draw()
                    win.flip()
                    
                    if frameN == 0:
                         stimOnset = globalClock.getTime()
                    
                    if frameN == probeFrames:
                        print('End probe frame =', frameN)
                        
                
                if probeFrames < frameN < (totalProbeFrames):
                    fixStim.draw()
                    win.flip()
                    
                    if frameN == (totalProbeFrames-1):
                        print('End ISI frame =', frameN)
                
                keys = event.getKeys(keyList=['left', 'right'])
                if keys:
                    count+=1
                    if count==0:
                        respTime = trialClock.getTime()
                        subResp = keys
                        if subResp[0] == 'left':
                            mindwander = 1
                        if subResp[0] == 'right':
                            mindwander = 0
                correct = ''
            trialCount+=1
        else:
            for frameN in range(totalProbeFrames):
                
                if 0 <= frameN <= (probeFrames):
                   
                    stim.draw()
                    probe2Resp1.draw()
                    probe2Resp2.draw()
                    win.flip()
                    
                    if frameN == 0:
                         stimOnset = globalClock.getTime()
                    
                    if frameN == probeFrames:
                        print('End probe frame =', frameN)
                        
                
                if probeFrames < frameN < (totalProbeFrames):
                    fixStim.draw()
                    win.flip()
                    
                    if frameN == (totalProbeFrames-1):
                        print('End ISI frame =', frameN)
                
                keys = event.getKeys(keyList=['left', 'right'])
                if keys:
                    count+=1
                    if count==0:
                        respTime = trialClock.getTime()
                        subResp = keys
                        if subResp[0] == corrAns:
                            correct = 1   
            trialCount+=1
            print(trialCount, stimulus, subResp, respTime, corrAns)
        
        
        # Log the end time of the trial
        endTime = trialClock.getTime() * 1000
        logging.log(level=logging.EXP, msg=f"Trial end: {endTime}")
        logging.log(level=logging.EXP, msg=f"Global Clock:{globalClock.getTime()}")
        
        # Add data to .csv file after each trial loop
        thisExp.addData('block', blockCount)
        thisExp.addData('trial', trialCount)
        thisExp.addData('trialType', trialType)
        thisExp.addData('stimulus', stimulus)
        thisExp.addData('stimulusOnset', stimOnset*1000)
        thisExp.addData('trialDuration', endTime)
        if subResp == []:
            thisExp.addData('key', '')
        else:
            thisExp.addData('key',subResp[0])
        if respTime != None:  # we had a response
            thisExp.addData('rt', respTime)
        thisExp.addData('correct', correct)
        if trial['trialType'] == 'Probe 1':
            thisExp.addData('mindwander', mindwander)
        
        
        # Prepares .csv by going to next row
        thisExp.nextEntry()
        
        print('Overall, %i frames were dropped.' % win.nDroppedFrames)
        if 'escape' in event.getKeys():
            win.close()
            core.quit()
    blockCount+=1



win.flip()

thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()

thisExp.abort()
win.close()
core.quit()
        
        

















