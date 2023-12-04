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

# Create default visual stimulus
stim = visual.TextStim(win)

# Set durations
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

# Initialize global clock
globalClock = core.Clock()
trialClock = core.Clock()

win.recordFrameIntervals = True
win.refreshThreshold = 1.0/6.0 + 0.004

# Experiment loop
for block in blockFiles:
    trials = data.TrialHandler(nReps=1, method='sequential', trialList=data.importConditions(block))
    globalClock.reset()
    trialCount=0
    for trial in trials:
        trialClock.reset()
        startTime = trialClock.getTime() * 1000
        logging.log(level=logging.EXP, msg=f"Trial start: {startTime}")
        event.clearEvents(eventType='keyboard')

        stimulus = trial['stimulus']
        stim.setText(stimulus)
        
        stimOnset = None
        subResp=[]
        corrAns=[]
        respTime=None
        count=-1
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
                    win.flip()
                    
                    if frameN == (totalNumFrames-1):
                        print('End ISI frame =', frameN)
            
                keys = event.getKeys(keyList=['space'])
                if keys:
                    count+=1
                    if count==0:
                        respTime = trialClock.getTime()
                        subResp = keys
                        if trial['stimulus'] != 3 and subResp[0] == 'space':
                            corrAns=1
                        else:
                            corrAns=0
            trialCount+=1
            print(trialCount, stimulus, subResp, respTime, corrAns)
        else:
            for frameN in range(totalProbeFrames):
                
                if 0 <= frameN <= (probeFrames):
                   
                    stim.draw()
                    win.flip()
                    
                    if frameN == 0:
                         stimOnset = globalClock.getTime()
                    
                    if frameN == probeFrames:
                        print('End probe frame =', frameN)
                        
                
                if probeFrames < frameN < (totalProbeFrames):
                    win.flip()
                    
                    if frameN == (totalProbeFrames-1):
                        print('End ISI frame =', frameN)
                
                keys = event.getKeys(keyList=['y', 'n'])
                if keys:
                    count+=1
                    if count==0:
                        respTime = trialClock.getTime()
                        subResp = keys
                        corrAns = ''   
            trialCount+=1
            print(trialCount, stimulus, subResp, respTime, corrAns)
        
        
        # Log the end time of the trial
        endTime = trialClock.getTime() * 1000
        logging.log(level=logging.EXP, msg=f"Trial end: {endTime}")
        logging.log(level=logging.EXP, msg=f"Global Clock:{globalClock.getTime()}")
        thisExp.addData('block', blockCount)
        thisExp.addData('trial', trialCount)
        thisExp.addData('trialType', trialType)
        thisExp.addData('stimulus', stimulus)
        thisExp.addData('stimulusOnset', stimOnset*1000)
        thisExp.addData('trialDuration', endTime)
        if subResp == []:
            thisExp.addData('subResp', '')
        else:
            thisExp.addData('subResp',subResp[0])
        if corrAns == []:  # we had a response
            thisExp.addData('corrAns', '')
        else:
            thisExp.addData('corrAns', corrAns)
        if respTime != None:  # we had a response
            thisExp.addData('rt', respTime)
        
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
        
        

















