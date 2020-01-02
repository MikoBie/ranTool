from psychopy import visual, core, event, clock, gui
from psychopy.constants import *
import random
import sys
import re
import glob
import pandas

## read file with conditions
conditions = pandas.read_csv('conditions.csv', sep = ';')

## Create a pop up which gathers demogrphic data
myDlg = gui.Dlg(labelButtonOK='Kontynuuj', labelButtonCancel='Przerwij', size=[800,600])
myDlg.addField(label='Id')
myDlg.addField(label='Płeć', choices=['Kobieta','Mężczyzna'])
myDlg.addField(label='Dominująca ręka', choices=['Lewa', 'Prawa'])
myDlg.addField(label='Wiek')
myDlg.addField(label='Kierunek Studiów')
info = gui.Dlg(title = 'Błąd. Uzupłenij poprawnie wszystkie pola!', size=[800,600])
info2 = gui.Dlg(title = 'Błąd. Zły numer osoby badanej!', size=[800,600])

## Exit the experiment if the participant presses cancel
myDlg.show()
if not myDlg.OK:
    sys.exit(0)

## Show the pop up until the input is correct
while (not (myDlg.data[0].isdigit() and myDlg.data[3].isdigit())) or len(glob.glob(f'data/*_{myDlg.data[0]}.csv'))>0:
    if len(glob.glob(f'data/*_{myDlg.data[0]}.csv'))>0:
        info2.show()
        if info2.OK:
            myDlg.show()
        else:
            sys.exit(0)
    else: 
        info.show()
        if info.OK:
            myDlg.show()
        else:
            sys.exit(0)

## get the condition
condition = conditions.loc[conditions['id']==int(myDlg.data[0])]['condition'].values[0]

## Exit the experiment if the participant presses cancel
if not myDlg.OK:
    sys.exit(0)

## Creates a window
#win = visual.Window(size = [800,600])
## Creates a full screen window
win = visual.Window(fullscr=True, size=[1280,800])
# Creates the stimuli (the red square)
instruction = visual.TextStim(win, pos=(0,0))
stim = visual.Rect(win, size = [200,200], lineColor = 'red', fillColor = 'red', units = 'pix')
hist0 = visual.TextStim(win, text='', pos=(1,.8))
hist1 = visual.TextStim(win, text='', pos=(.9,.8))
hist2 = visual.TextStim(win, text='', pos=(.8,.8))
hist3 = visual.TextStim(win, text='', pos=(.7,.8))
hist4 = visual.TextStim(win, text='', pos=(.6,.8))
hist5 = visual.TextStim(win, text='', pos=(.5,.8))
hist6 = visual.TextStim(win, text='', pos=(.4,.8))
hist = [hist6,hist5,hist4,hist3,hist2,hist1,hist0]
## Opens the otuput file


## Initialize the clock and 
myClock=clock.Clock()

event.clearEvents()
with open('Instrukcja.txt', 'r') as file:
    instruction.text = file.read()
instruction.draw()
win.flip()
event.waitKeys(keyList = ['space'], clearEvents=True)
file_name = 'data/' + condition + '_' + myDlg.data[0] + '.csv'

with open(file_name,'w') as file:
    file.write('id;sex;hand;age;faculty;condition;trial;time;key'+'\n')
    ## Starts the routine of displaying the square 
    continueRutine=True

    for trial in range(5):
        myClock.reset()
        event.clearEvents()
        myKeys=[]
        i = 0

        while continueRutine:
            if myClock.getTime() <= .750:
                myKeys.append(event.getKeys(keyList=['period','slash'], timeStamped=myClock))
                stim.autoDraw=True
                win.flip()
            if myClock.getTime() > .750:
                myKeys.append(event.getKeys(keyList=['period','slash'], timeStamped=myClock))
                stim.autoDraw=False
                win.flip()
            if myClock.getTime() > 2:
                continueRutine=False
            
            if len(myKeys[i])>0 and condition=='visible':
                if myKeys[i][0][0] == 'slash':
                    text = 'R'
                else:
                    text = 'O'
                
                hist6.text = hist5.text
                hist5.text = hist4.text
                hist4.text = hist3.text
                hist3.text = hist2.text
                hist2.text = hist1.text
                hist1.text = hist0.text
                hist0.text = text

                for h in hist:
                    h.autoDraw = True
            i = i + 1

        for line in myKeys:
            if len(line) > 0:
                output = [myDlg.data[0],myDlg.data[1],myDlg.data[2],myDlg.data[3],myDlg.data[4],condition, trial, line[0][1],line[0][0]]
                file.write(";".join(str(x) for x in output)+'\n')
        

        continueRutine=True
