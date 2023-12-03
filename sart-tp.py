from __future__ import absolute_import, division
from ast import withitem

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
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
expInfo = {'participant': '', 'session': '1'}
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
    originPath='C:\\Users\\dun5yn\\OneDrive - cchmc\\Documents\\06 - Neuroimaging Study\\SART\\SART-TP.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

#-------------------EXPERIMENT CODE---------------------------------------------

# Setup window
win = visual.Window(
    size=(2560, 1440), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units='deg')

# Store monitor framerate
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

# Create default keyboard
defaultKeyboard = keyboard.Keyboard()

# Create default visual stimulus
stim = visual.TextStim(win)

# Initialize list of block condition files
blockFiles = ['conditions.xlsx']



# Initialize global clock
globalClock = core.Clock()

# Experiment loop
for block in blockFiles:
    trials = data.TrialHandler(nReps=1, method='sequential', trialList=data.importConditions(block))
    timer = core.CountdownTimer()
    #stimulusOffset = 0
    for trial in trials:
        trialClock = core.MonotonicClock()
        startTime = trialClock.getTime() * 1000
        logging.log(level=logging.EXP, msg=f"Trial start: {startTime}")

        stimulusDuration = trial['stimulusDuration'] / 1000.0
        isi = trial['isi'] / 1000.0
        stimulusOnset = trial['stimulusOnset'] / 1000.0
        #trialDuration = stimulusDuration + isi
        #stimulusOffset += trialDuration
        stimulus = trial['stimulus']

        
        timer.add(stimulusDuration)
        while timer.getTime() > 0:
           stim.setText(stimulus)
           stim.draw()
           win.flip()
        
        timer.add(isi)
        
        while timer.getTime() > 0:
            win.flip()
        

        # Log the end time of the trial
        endTime = trialClock.getTime() * 1000
        logging.log(level=logging.EXP, msg=f"Trial end: {endTime}")
        logging.log(level=logging.EXP, msg=f"Global Clock:{globalClock.getTime()}")
        
        if 'escape' in event.getKeys():
            win.close()
            core.quit()

win.flip()

thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()

thisExp.abort()
win.close()
core.quit()
        
        

















