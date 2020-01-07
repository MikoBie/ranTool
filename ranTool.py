from psychopy import visual, core, event, clock, gui
from psychopy.constants import *
import random
import sys
import re
import glob
import pandas

## How many times the red square should display
REPETITION_NUMBER = 5

## How long the red square should be displayed in seconds
RED_SQUARE_DISPLAY_LENGTH = .75

## Time between red square's exposition in seconds
RED_SQUARE_REST_LENGTH = 1.25

## read file with conditions
conditions = pandas.read_csv('conditions.csv', sep = ';')

## Create a pop up which gathers demographic data
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

## Creates a full screen window on MacBook Pro Early 2015 13 inch
win = visual.Window(fullscr=True, size=[1280,800])

## Make the mouse courser invisible
win.mouseVisible = False

# Creates the instruction objects sex specific
if myDlg.data[1] == 'Kobieta':
    instruction = visual.ImageStim(win,image='instrukcja_k/instrukcja.png', size=(1.92,1.2))
    instruction2 = visual.ImageStim(win,image='instrukcja2_k/instrukcja2.png', size=(1.92,1.3969904240766073))
else:
    instruction = visual.ImageStim(win,image='instrukcja_m/instrukcja.png', size=(1.92,1.2))
    instruction2 = visual.ImageStim(win,image='instrukcja2_m/instrukcja2.png', size=(1.92,1.3969904240766073))

## Creates red square object
stim = visual.Rect(win, size = [800,800], lineColor = 'red', fillColor = 'red', units = 'pix')

## Creates objects for displaying history
hist0 = visual.TextStim(win, text='', pos=(1,.8), font='Latin Modern Roman')
hist1 = visual.TextStim(win, text='', pos=(.9,.8), font='Latin Modern Roman')
hist2 = visual.TextStim(win, text='', pos=(.8,.8), font='Latin Modern Roman')
hist3 = visual.TextStim(win, text='', pos=(.7,.8), font='Latin Modern Roman')
hist4 = visual.TextStim(win, text='', pos=(.6,.8), font='Latin Modern Roman')
hist5 = visual.TextStim(win, text='', pos=(.5,.8), font='Latin Modern Roman')
hist6 = visual.TextStim(win, text='', pos=(.4,.8), font='Latin Modern Roman')
hist = [hist6,hist5,hist4,hist3,hist2,hist1,hist0]

## Creates ending object
end = visual.TextStim(win, text='Koniec tej części badania.', pos=(0.5,0), font='Latin Modern Roman')

## Initialize the clock and clear keys buffer
myClock=clock.Clock()
event.clearEvents()


## Display first Instruction
instruction.draw()
win.flip()
event.waitKeys(keyList = ['space'], clearEvents=True)

## Display second instruction
instruction2.draw()
win.flip()
event.waitKeys(keyList = ['space'], clearEvents=True)

## Creates file name
file_name = 'data/' + condition + '_' + myDlg.data[0] + '.csv'

## Opens a file connection
with open(file_name,'w') as file:
    file.write('id;sex;hand;age;faculty;condition;trial;time;key'+'\n')
    
    ## Starts the routine of displaying the red square 
    continueRutine=True
    for trial in range(REPETITION_NUMBER):
        myClock.reset()
        event.clearEvents()
        myKeys=[]
        i = 0

        while continueRutine:
            if myClock.getTime() <= RED_SQUARE_DISPLAY_LENGTH:
                myKeys.append(event.getKeys(keyList=['period','slash'], timeStamped=myClock))
                stim.autoDraw=True
                win.flip()
            if myClock.getTime() > RED_SQUARE_DISPLAY_LENGTH:
                myKeys.append(event.getKeys(keyList=['period','slash'], timeStamped=myClock))
                stim.autoDraw=False
                win.flip()
            if myClock.getTime() > (RED_SQUARE_DISPLAY_LENGTH + RED_SQUARE_REST_LENGTH):
                continueRutine=False
            
            ## Display history if the condition is visible
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

        ## Write out every single button pressed to the file
        for line in myKeys:
            if len(line) > 0:
                output = [myDlg.data[0],myDlg.data[1],myDlg.data[2],myDlg.data[3],myDlg.data[4],condition, trial, line[0][1],line[0][0]]
                file.write(";".join(str(x) for x in output)+'\n')
        

        continueRutine=True

## Display ending information
for h in hist:
    h.autoDraw = False
win.flip()
end.draw()
win.flip()
event.waitKeys(keyList = ['backslash'], clearEvents=True)