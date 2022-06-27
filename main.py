import tkinter as tk 
import time 
import random 

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=600, bg='#87CEEB')

canvas.pack()

numframes = 100
back = canvas.create_rectangle(0,0,800,600, fill='black')

#Introduction 
introscreen = canvas.create_rectangle(0,0,800,600, fill='black')

#Outputs texts
for f in range(400):
  introtext1 = canvas.create_text(400, 600-f, text='The US President', font='Arial 50', fill='#ffe81f')

  introtext2 = canvas.create_text(400, 700-f, text='A (very) short film', font='Arial 30', fill='#ffe81f')

  introtext3 = canvas.create_text(400, 800-f, text='Credits to Donald J. Trump for Acting.', font='Arial 30', fill='#ffe81f')

  canvas.update()
  time.sleep(0.005)
  f += 3
  canvas.delete(introtext1, introtext2, introtext3)
  

#Date  
for frame in range(0,numframes+1):
  monthDay = canvas.create_text(400,300-frame/2, text='NOVEMBER 07', font=('Arial','50'), fill='#ffe81f')

  if frame == 100:
    year = canvas.create_text(400,300+frame, text='2020', font=('Arial','40'), fill='white')
    canvas.update() 
    time.sleep(1.5) 
    canvas.delete(year) 

  canvas.update()
  time.sleep(0.01)
  canvas.delete(monthDay) 
  

canvas.delete(back) 

canvas.update()

##White house
#White house walls
canvas.create_rectangle(0,0,800,600, fill='#fefff5')

#Door
canvas.create_rectangle(250,600,550,300, fill='#696969')

#Horizontal door frames
turns = 0
spacing = 0

while turns < 3:
  canvas.create_rectangle(250,300+spacing,550,310+spacing, fill='#DCDCDC', outline='')

  spacing += 145
  turns += 1

canvas.update() 
#Vertical door frames 
turn = 0
spacing = 0

while turn < 4:
  canvas.create_rectangle(250+spacing,300,260+spacing,600, fill='#DCDCDC', outline='') 

  if turn == 1:
    spacing += 10 

  else:
    spacing += 140

  turn +=1

canvas.create_line(400,300,400,600, fill='black') 

#Window above door 
canvas.create_rectangle(250,300,550,225, fill='#8a8a8a', outline='') 
canvas.create_rectangle(260,290,540,235, fill='#696969', outline='') 

#White house text 
canvas.create_text(400,200, text='The White House', font='Arial 25')

#Arched Window with frames 
canvas.create_arc(250, 100, 550, 250, start=0, extent=180, fill='#696969', outline='')

spacing=20
#Creates the frames
for i in range(6):
  canvas.create_arc(250, 100, 550, 250, start=0, extent=spacing, outline='#f0e8aa', width=2)
  spacing += 30

#Donald trump walking animation

headstartx = 50 ; headstarty = 325 ; scaler=7
numframes=400

for i in range(numframes):

  #Creates donald trump's head
  head1 = canvas.create_polygon(headstartx, headstarty, headstartx+5*scaler, headstarty, headstartx+10*scaler, headstarty, headstartx+11*scaler, headstarty+3*scaler, headstartx+11*scaler, headstarty+7.5*scaler, headstartx+11*scaler, headstarty+11*scaler, headstartx+7*scaler, headstarty+10.7*scaler, headstartx+4*scaler, headstarty+10.35*scaler, headstartx-1*scaler, headstarty+10, headstartx-0.7, headstarty+7, headstartx-0.4, headstarty+4, headstartx, headstarty, smooth=True, fill='#faa23e')

  head2 = canvas.create_polygon(headstartx, headstarty, headstartx+1*scaler, headstarty+10*scaler, headstartx+3*scaler, headstarty+10.25*scaler, headstartx+7*scaler, headstarty+10.7*scaler, fill='#faa23e', smooth=True)

  hair = canvas.create_polygon(headstartx, headstarty, headstartx-1*scaler, headstarty+1*scaler, headstartx+5, headstarty+2*scaler, headstartx+8*scaler, headstarty, headstartx+10*scaler, headstarty, headstartx+10*scaler, headstarty-1*scaler, headstartx+5*scaler, headstarty, headstartx, headstarty, smooth=True, fill='#FFEAAE') 

  #Eyes, iris, and eyebrows
  Leye = canvas.create_oval(headstartx+1*scaler, headstarty+3*scaler, headstartx+3*scaler, headstarty+4*scaler, fill='white', outline='') 

  Liris = canvas.create_oval(headstartx+1.5*scaler, headstarty+3*scaler, headstartx+2.5*scaler, headstarty+4*scaler, fill='#29465B') 

  Leyebrow = canvas.create_polygon(headstartx+0.5*scaler, headstarty+2*scaler, headstartx+3.5*scaler, headstarty+2.5*scaler, headstartx+3.5*scaler, headstarty+3*scaler, headstartx+0.5*scaler, headstarty+2.5*scaler, fill='#FFEAAE', outline='') 

  Reye = canvas.create_oval(headstartx+7*scaler, headstarty+3*scaler, headstartx+9*scaler, headstarty+4*scaler, fill='white', outline='') 

  Riris = canvas.create_oval(headstartx+7.5*scaler, headstarty+3*scaler, headstartx+8.5*scaler, headstarty+4*scaler, fill='#29465B') 

  Reyebrow = canvas.create_polygon(headstartx+9.5*scaler, headstarty+2*scaler, headstartx+6.5*scaler, headstarty+2.5*scaler, headstartx+6.5*scaler, headstarty+3*scaler, headstartx+9.5*scaler, headstarty+2.5*scaler, fill='#FFEAAE', outline='') 

  #nose outline
  nose1 = canvas.create_oval(headstartx+4*scaler, headstarty+4.5*scaler, headstartx+6*scaler, headstarty+6*scaler, fill='#faa23e', width=2)

  nose2 = canvas.create_rectangle(headstartx+4.5*scaler, headstarty+4.5*scaler, headstartx+5.5*scaler, headstarty+5*scaler, fill='#faa23e', outline='') 

  nose3 = canvas.create_line(headstartx+4.5*scaler, headstarty+3.5*scaler, headstartx+4.5*scaler, headstarty+4.7*scaler, width=2) 

  nose4 = canvas.create_line(headstartx+5.5*scaler, headstarty+3.5*scaler, headstartx+5.5*scaler, headstarty+4.7*scaler, width=2) 

  #mouth
  mouth = canvas.create_arc(headstartx+4.5*scaler, headstarty+7*scaler, headstartx+6.5*scaler, headstarty+9*scaler, start=0, extent=180, fill='#eec1ad', outline='') 

  #suit  
  suit = canvas.create_polygon(headstartx+5.5*scaler, headstarty+10*scaler, headstartx+11*scaler, headstarty+11*scaler, headstartx+11*scaler, headstarty+25*scaler, headstartx, headstarty+25*scaler, headstartx, headstarty+11*scaler, fill='#00084d', outline='')

  #tie and collar  
  dressShirt = canvas.create_polygon(headstartx+5.5*scaler,headstarty+13*scaler, headstartx+3.5*scaler, headstarty+10*scaler, headstartx+5.5*scaler, headstarty+10*scaler, headstartx+7.5*scaler, headstarty+10.25*scaler, fill='white') 

  tieKnot = canvas.create_oval(headstartx+5*scaler, headstarty+10*scaler, headstartx+6*scaler, headstarty+11*scaler, fill='red',outline='')

  tie = canvas.create_polygon(headstartx+11*scaler, headstarty+11*scaler, headstartx+6.5*scaler, headstarty+11.5*scaler, headstartx+5.5*scaler, headstarty+13*scaler, headstartx+4.5*scaler, headstarty+11.5*scaler, fill='red', outline='') 

  #Arms
  Larm = canvas.create_polygon(headstartx, headstarty+11*scaler, headstartx-2*scaler, headstarty+16*scaler, headstartx-2.5*scaler, headstarty+25*scaler, headstartx-0.5*scaler, headstarty+25*scaler, fill='#00084d', outline='')  

  Rarm = canvas.create_polygon(headstartx+10.7*scaler, headstarty+11*scaler, headstartx+13*scaler, headstarty+16*scaler, headstartx+13.5*scaler, headstarty+25*scaler, headstartx+11.1*scaler, headstarty+25*scaler, fill='#00084d', outline='')  

  #Hands
  Lhand = canvas.create_oval(headstartx-2*scaler, headstarty+25*scaler, headstartx-1*scaler, headstarty+26*scaler, fill='#faa23e', outline='')

  Rhand = canvas.create_oval(headstartx+11.5*scaler, headstarty+25*scaler, headstartx+12.5*scaler, headstarty+26*scaler, fill='#faa23e', outline='')

  #Pants 
  pants = canvas.create_polygon(headstartx, headstarty+25*scaler, headstartx+11*scaler, headstarty+25*scaler, headstartx+11*scaler, headstarty+39*scaler, headstartx+6*scaler, headstarty+39*scaler, headstartx+5.5*scaler, headstarty+27*scaler, headstartx+5*scaler, headstarty+39*scaler, headstartx, headstarty+39*scaler, fill='black', outline='') 

  if i == 200: 
    #Creates text bubble
    text1 = canvas.create_oval(headstartx+12*scaler, headstarty-1*scaler, headstartx+45*scaler, headstarty-15*scaler, fill='white')

    text2 = canvas.create_polygon(headstartx+15*scaler, headstarty-6*scaler, headstartx+17*scaler, headstarty-5*scaler, headstartx+11*scaler, headstarty, fill='white') 

    phrases = ['I wonder...', 'what should I do today?', 'Should I manage the pandemic?', 'or hold a rally against Biden?', 'Instead, I think I will...', 'GO GOLFING!!', 'Such BEAUTIFUL weather today!'] 

    #text inside 
    for x in range(len(phrases)): 
      text = canvas.create_text(headstartx+28.5*scaler, headstarty-8*scaler, text=phrases[x], font='Arial 10')

      canvas.update()
      time.sleep(1.5)
      canvas.delete(text)

    canvas.delete(text1, text2)

  canvas.update()
  time.sleep(0.01) 
  canvas.delete(head1, head2, hair, Leye, Reye, Leyebrow, Reyebrow, Liris, Riris, nose1, nose2, nose3, nose4, mouth, suit, dressShirt, tieKnot, tie, Larm, Rarm, Lhand, Rhand, pants)

  headstartx += 2


##Creates new Golfing scenery 
#Creates the sky 
canvas.create_rectangle(0,0,800,600, fill='#87CEEB')

#Creates ground
canvas.create_rectangle(0,200,800,600, fill='#96a63c')

#Left boundary
canvas.create_polygon(75,425, 20,600, 0, 600, 0, 200, 250, 200, fill='darkgreen')

#Right boundary
canvas.create_polygon(800,600, 800, 200, 550, 200, 650, 450, fill='darkgreen')

#Hole
canvas.create_oval(375, 275, 400, 300, fill='black')

#flag
canvas.create_rectangle(400, 275, 390, 240, fill='saddlebrown', outline='')

canvas.create_polygon(390, 240, 390, 250, 360, 245, fill='red', outline='')

#water hole
canvas.create_oval(650, 300, 725, 425, fill='#87d7ee', outline='')

##creates clouds
for clouds in range(3):
  x = random.randint(0, 800)
  y = random.randint(0, 200) 

  #Left piece
  canvas.create_oval(x, y, x+10, y+10, fill="white", outline = "") 

  #Middle piece 
  canvas.create_oval(x+5, y-10, x+25, y+10, fill="white", outline = "")

  #Right piece
  canvas.create_oval(x+20, y, x+30, y+10, fill="white", outline = "") 


#Random trees on the sides 
for i in range(3): 
  posx = [random.randint(625,780), random.randint(0, 125)]
  x = random.choice(posx)

  #Makes sure there are no trees in the water
  while 650 < x < 725: 
    x = random.randint(600, 780)

  y = random.randint(225, 500)

  canvas.create_rectangle(x, y, x+20, y-40, fill='saddlebrown', outline='')
  canvas.create_oval(x-10, y-30, x+30, y-70, fill='#288b22', outline='')

#Hill
canvas.create_arc(0, 375, 325, 1000, start=0, extent=180, fill='#b2c358')

#Ball holder
canvas.create_rectangle(200,400, 210, 430, fill='#f2c074', outline='')

canvas.create_polygon(200, 400, 197, 397, 213, 397, 210, 400, fill='#f2c074', outline='')

#Golf ball 
golfball = canvas.create_oval(200, 397, 210, 387, fill='#cfbea4', outline='') 

#New coordinates and variables needed for the next scene
numFrames = 91 ; headstartx = 0 ; headstarty = 350 ; scaler = 7 ;startxpos = 0 ; startypos = 100

##Donald trump again, climbing up the hill 
for y in range(-30, numFrames):
  
  #Creates donald trump's head
  head1 = canvas.create_polygon(headstartx, headstarty, headstartx+5*scaler, headstarty, headstartx+10*scaler, headstarty, headstartx+11*scaler, headstarty+3*scaler, headstartx+11*scaler, headstarty+7.5*scaler, headstartx+11*scaler, headstarty+11*scaler, headstartx+7*scaler, headstarty+10.7*scaler, headstartx+4*scaler, headstarty+10.35*scaler, headstartx-1*scaler, headstarty+10, headstartx-0.7, headstarty+7, headstartx-0.4, headstarty+4, headstartx, headstarty, smooth=True, fill='#faa23e')

  head2 = canvas.create_polygon(headstartx, headstarty, headstartx+1*scaler, headstarty+10*scaler, headstartx+3*scaler, headstarty+10.25*scaler, headstartx+7*scaler, headstarty+10.7*scaler, fill='#faa23e', smooth=True)

  hair = canvas.create_polygon(headstartx, headstarty, headstartx-1*scaler, headstarty+1*scaler, headstartx+5, headstarty+2*scaler, headstartx+8*scaler, headstarty, headstartx+10*scaler, headstarty, headstartx+10*scaler, headstarty-1*scaler, headstartx+5*scaler, headstarty, headstartx, headstarty, smooth=True, fill='#FFEAAE') 

  #Eyes, iris, and eyebrows
  Leye = canvas.create_oval(headstartx+1*scaler, headstarty+3*scaler, headstartx+3*scaler, headstarty+4*scaler, fill='white', outline='') 

  Liris = canvas.create_oval(headstartx+1.5*scaler, headstarty+3*scaler, headstartx+2.5*scaler, headstarty+4*scaler, fill='#29465B') 

  Leyebrow = canvas.create_polygon(headstartx+0.5*scaler, headstarty+2*scaler, headstartx+3.5*scaler, headstarty+2.5*scaler, headstartx+3.5*scaler, headstarty+3*scaler, headstartx+0.5*scaler, headstarty+2.5*scaler, fill='#FFEAAE', outline='') 

  Reye = canvas.create_oval(headstartx+7*scaler, headstarty+3*scaler, headstartx+9*scaler, headstarty+4*scaler, fill='white', outline='') 

  Riris = canvas.create_oval(headstartx+7.5*scaler, headstarty+3*scaler, headstartx+8.5*scaler, headstarty+4*scaler, fill='#29465B') 

  Reyebrow = canvas.create_polygon(headstartx+9.5*scaler, headstarty+2*scaler, headstartx+6.5*scaler, headstarty+2.5*scaler, headstartx+6.5*scaler, headstarty+3*scaler, headstartx+9.5*scaler, headstarty+2.5*scaler, fill='#FFEAAE', outline='') 

  #nose outline
  nose1 = canvas.create_oval(headstartx+4*scaler, headstarty+4.5*scaler, headstartx+6*scaler, headstarty+6*scaler, fill='#faa23e', width=2)

  nose2 = canvas.create_rectangle(headstartx+4.5*scaler, headstarty+4.5*scaler, headstartx+5.5*scaler, headstarty+5*scaler, fill='#faa23e', outline='') 

  nose3 = canvas.create_line(headstartx+4.5*scaler, headstarty+3.5*scaler, headstartx+4.5*scaler, headstarty+4.7*scaler, width=2) 

  nose4 = canvas.create_line(headstartx+5.5*scaler, headstarty+3.5*scaler, headstartx+5.5*scaler, headstarty+4.7*scaler, width=2) 

  #mouth
  mouth = canvas.create_arc(headstartx+4.5*scaler, headstarty+7*scaler, headstartx+6.5*scaler, headstarty+9*scaler, start=0, extent=180, fill='#eec1ad', outline='') 

  #suit  
  suit = canvas.create_polygon(headstartx+5.5*scaler, headstarty+10*scaler, headstartx+11*scaler, headstarty+11*scaler, headstartx+11*scaler, headstarty+25*scaler, headstartx, headstarty+25*scaler, headstartx, headstarty+11*scaler, fill='#00084d', outline='')

  #tie and collar  
  dressShirt = canvas.create_polygon(headstartx+5.5*scaler,headstarty+13*scaler, headstartx+3.5*scaler, headstarty+10*scaler, headstartx+5.5*scaler, headstarty+10*scaler, headstartx+7.5*scaler, headstarty+10.25*scaler, fill='white') 

  tieKnot = canvas.create_oval(headstartx+5*scaler, headstarty+10*scaler, headstartx+6*scaler, headstarty+11*scaler, fill='red',outline='')

  tie = canvas.create_polygon(headstartx+11*scaler, headstarty+11*scaler, headstartx+6.5*scaler, headstarty+11.5*scaler, headstartx+5.5*scaler, headstarty+13*scaler, headstartx+4.5*scaler, headstarty+11.5*scaler, fill='red', outline='') 

  #Arms
  Larm = canvas.create_polygon(headstartx, headstarty+11*scaler, headstartx-2*scaler, headstarty+16*scaler, headstartx-2.5*scaler, headstarty+25*scaler, headstartx-0.5*scaler, headstarty+25*scaler, fill='#00084d', outline='')  

  Rarm = canvas.create_polygon(headstartx+10.7*scaler, headstarty+11*scaler, headstartx+13*scaler, headstarty+16*scaler, headstartx+13.5*scaler, headstarty+25*scaler, headstartx+11.1*scaler, headstarty+25*scaler, fill='#00084d', outline='')  

  #Hands
  Lhand = canvas.create_oval(headstartx-2*scaler, headstarty+25*scaler, headstartx-1*scaler, headstarty+26*scaler, fill='#faa23e', outline='')

  Rhand = canvas.create_oval(headstartx+11.5*scaler, headstarty+25*scaler, headstartx+12.5*scaler, headstarty+26*scaler, fill='#faa23e', outline='')

  #Pants 
  pants = canvas.create_polygon(headstartx, headstarty+25*scaler, headstartx+11*scaler, headstarty+25*scaler, headstartx+11*scaler, headstarty+39*scaler, headstartx+6*scaler, headstarty+39*scaler, headstartx+5.5*scaler, headstarty+27*scaler, headstartx+5*scaler, headstarty+39*scaler, headstartx, headstarty+39*scaler, fill='black', outline='') 

  #Golf club 
  clubHandle = canvas.create_rectangle(headstartx-1*scaler, headstarty+25*scaler, headstartx+13.5*scaler, headstarty+26*scaler, fill='#c0c0c0')

  clubHitter = canvas.create_oval(headstartx+13.5*scaler, headstarty+24*scaler, headstartx+15*scaler, headstarty+26*scaler, fill='black') 

  #Sun movement 
  sun = canvas.create_oval(startxpos, startypos, startxpos+75, startypos+75, fill='#F1D71C', outline='')

  if y > 80:
    startxpos = 220
    startypos = 72
  
  else:
    startxpos += 2
    startypos = y**2/3200-3*y/8+100

  if y > 60:
    headstarty = 120
    headstartx = 90

  else:
    headstarty = (y**2)/90-(19*y/6)+250
    headstartx += 1
  
  #Conversation 
  if y == 90:
    #Trump text box
    text1 = canvas.create_oval(headstartx+12*scaler, headstarty-3*scaler, headstartx+45*scaler, headstarty+11*scaler, fill='white')

    text2 = canvas.create_polygon(headstartx+15*scaler, headstarty+6*scaler, headstartx+17*scaler, headstarty+7*scaler, headstartx+11*scaler, headstarty+9*scaler, fill='white') 

    #Mike Pence text box
    text3 = canvas.create_oval(headstartx+70*scaler, headstarty+10*scaler, headstartx+103*scaler, headstarty+24*scaler, fill='white')

    text4 = canvas.create_polygon(headstartx+90*scaler, headstarty+20*scaler, headstartx+95*scaler, headstarty+20*scaler, headstartx+102*scaler, headstarty+27*scaler, fill='white')

    #What they say
    trumpPhrase = ['Say Mike,',"Isn't it a great day?",'Ready to lose?', 'I hit first!']
    mikePhrase = ['Yes Donald?','Indeed.','.....', 'Ok Mr. President...']

    for i in range(len(trumpPhrase)):
      trumpSays = canvas.create_text(headstartx+28.5*scaler, headstarty+4*scaler, text=trumpPhrase[i], font='Arial 10') 
      canvas.update()
      time.sleep(1.5)

      mikeSays = canvas.create_text(headstartx+86.5*scaler, headstarty+17*scaler, text=mikePhrase[i], font='Arial 10') 
      canvas.update()
      time.sleep(1.5)
      canvas.delete(mikeSays, trumpSays) 
    
    canvas.delete(text1, text2, text3, text4) 
  
  canvas.update()
  time.sleep(0.01)
  canvas.delete(head1, head2, hair, Leye, Reye, Leyebrow, Reyebrow, Liris, Riris, nose1, nose2, nose3, nose4, mouth, suit, dressShirt, tieKnot, tie, Larm, Rarm, Lhand, Rhand, pants, sun, clubHandle, clubHitter)

##Create new animation block/background
golfBG = canvas.create_rectangle(0,200, 800, 600, fill='#87CEEB')

#Creates the golf ball and stand
stand1 = canvas.create_rectangle(325, 600, 475, 400, fill='#f2c074', outline='')

stand2 = canvas.create_polygon(325, 400, 275, 350, 525, 350, 475, 400, fill='#f2c074', outline='') 

ball = canvas.create_oval(325, 350, 475, 200, fill='#cfbea4', outline='')

balltext = canvas.create_text(400, 275, text='Golf Ball Inc.', font=('Arial' '20'))

#Golf club hitting animation 
frames = 140 ; startposx = 387.5 ; startposy = 0 ; xincrement = 25 ; yincrement = 200 ; ycircincr = 5 ; xcircincr = 5
time.sleep(1)

for i in range(frames):
  #Creates the club handle
  clubHandle = canvas.create_rectangle(startposx+25-xincrement, startposy, startposx+xincrement, startposy+yincrement, fill='#c0c0c0', outline='')

  #Animates 'ball hitting the camera' effect
  if i > 70:

    bangText = canvas.create_text(650, 350, text='BANG!', font='Arial 50', fill='red') 

    ball = canvas.create_oval(325-xcircincr, 350+ycircincr, 475
    +xcircincr, 200-ycircincr, fill='#cfbea4', outline='')

    xcircincr +=8 ; ycircincr += 8
    canvas.update()
    canvas.delete(stand1, stand2) 

  canvas.update()
  time.sleep(0.01)
  if i > 70:
    canvas.delete(clubHandle, balltext, ball) 
  
  else:
    canvas.delete(clubHandle, balltext) 

  xincrement += 0.5

canvas.delete(bangText, stand1, stand2, golfBG) 

#Ball flying background
canvas.create_rectangle(0, 200, 800, 600, fill='#87CEEB', outline='')

startposx = 0 ; startposy = 525 ; frame = 900
for i in range(frame):
  startposy = i**2/4800-19*i/24+600 

  ball = canvas.create_oval(startposx, startposy, startposx+50, startposy+50, fill='#cfbea4', outline='')

  canvas.update()
  time.sleep(0.001)
  canvas.delete(ball) 

  if startposx > 800:
    canvas.delete(ball)
    break
  startposx += 1

#Ball flying into water hole
canvas.create_rectangle(0, 200, 800, 600, fill='darkgreen', outline='')

#water hole
canvas.create_oval(250, 550, 575, 325, fill='#87d7ee', outline='')

startposx = 0 ; startposy = 525 ; frame = 800
#Ball flying into water
for i in range(frame):
  startposy = i**2/450+i/18+425/9

  ball = canvas.create_oval(startposx, startposy, startposx+50, startposy+50, fill='#cfbea4', outline='')

  canvas.update()
  time.sleep(0.001)
  canvas.delete(ball) 

  if startposx > 400:
    canvas.delete(ball)
    break

  startposx += 1

#Talking animation between trump and mike 
headstartx = 0 ; headstarty = 350 ; scaler = 7

#What they say in the conversation
trumpPhrase = ['I win Mike!','Thats called a hole in ONE.','what?'] 
mikePhrase = ['It landed in water...','I just got word Donald:','You LOST the election.'] 

for sentence in range(len(trumpPhrase)):
  #Trump text box
    text1 = canvas.create_oval(headstartx+7*scaler, headstarty-3*scaler, headstartx+40*scaler, headstarty+11*scaler, fill='white')

    text2 = canvas.create_polygon(headstartx+10*scaler, headstarty+6*scaler, headstartx+12*scaler, headstarty+7*scaler, headstartx+6*scaler, headstarty+9*scaler, fill='white') 

    #Mike Pence text box
    text3 = canvas.create_oval(headstartx+70*scaler, headstarty+10*scaler, headstartx+103*scaler, headstarty+24*scaler, fill='white')

    text4 = canvas.create_polygon(headstartx+90*scaler, headstarty+20*scaler, headstartx+95*scaler, headstarty+20*scaler, headstartx+102*scaler, headstarty+27*scaler, fill='white')

    #Output sentences 
    trumpSays = canvas.create_text(headstartx+23.5*scaler, headstarty+4*scaler, text=trumpPhrase[sentence], font='Arial 10')

    canvas.update()
    time.sleep(1.5)
    canvas.delete(trumpSays)

    mikeSays = canvas.create_text(headstartx+86.5*scaler, headstarty+17*scaler, text=mikePhrase[sentence], font='Arial 15', fill='red') 

    canvas.update()
    time.sleep(1.5)
    canvas.delete(mikeSays) 

##End animation of trump looking mad 
headstartx=200 ; headstarty = 100 ; scaler = 100

#Creates donald trump's head
head1 = canvas.create_polygon(headstartx, headstarty, headstartx+5*scaler, headstarty, headstartx+10*scaler, headstarty, headstartx+11*scaler, headstarty+3*scaler, headstartx+11*scaler, headstarty+7.5*scaler, headstartx+11*scaler, headstarty+11*scaler, headstartx+7*scaler, headstarty+10.7*scaler, headstartx+4*scaler, headstarty+10.35*scaler, headstartx-1*scaler, headstarty+10, headstartx-0.7, headstarty+7, headstartx-0.4, headstarty+4, headstartx, headstarty, smooth=True, fill='#faa23e')

head2 = canvas.create_polygon(headstartx, headstarty, headstartx+1*scaler, headstarty+10*scaler, headstartx+3*scaler, headstarty+10.25*scaler, headstartx+7*scaler, headstarty+10.7*scaler, fill='#faa23e', smooth=True)

hair = canvas.create_polygon(headstartx, headstarty, headstartx-1*scaler, headstarty+1*scaler, headstartx+5, headstarty+2*scaler, headstartx+8*scaler, headstarty, headstartx+10*scaler, headstarty, headstartx+10*scaler, headstarty-1*scaler, headstartx+5*scaler, headstarty, headstartx, headstarty, smooth=True, fill='#FFEAAE') 

#Eyes, iris, and eyebrows
Leye = canvas.create_oval(headstartx+1*scaler, headstarty+3*scaler, headstartx+3*scaler, headstarty+4*scaler, fill='white', outline='') 

Liris = canvas.create_oval(headstartx+1.5*scaler, headstarty+3*scaler, headstartx+2.5*scaler, headstarty+4*scaler, fill='#29465B') 

Leyebrow = canvas.create_polygon(headstartx+0.5*scaler, headstarty+2*scaler, headstartx+3.5*scaler, headstarty+2.5*scaler, headstartx+3.5*scaler, headstarty+3*scaler, headstartx+0.5*scaler, headstarty+2.5*scaler, fill='#FFEAAE', outline='') 

Reye = canvas.create_oval(headstartx+7*scaler, headstarty+3*scaler, headstartx+9*scaler, headstarty+4*scaler, fill='white', outline='') 

Riris = canvas.create_oval(headstartx+7.5*scaler, headstarty+3*scaler, headstartx+8.5*scaler, headstarty+4*scaler, fill='#29465B') 

Reyebrow = canvas.create_polygon(headstartx+9.5*scaler, headstarty+2*scaler, headstartx+6.5*scaler, headstarty+2.5*scaler, headstartx+6.5*scaler, headstarty+3*scaler, headstartx+9.5*scaler, headstarty+2.5*scaler, fill='#FFEAAE', outline='') 

#nose outline
nose1 = canvas.create_oval(headstartx+4*scaler, headstarty+4.5*scaler, headstartx+6*scaler, headstarty+6*scaler, fill='#faa23e', width=2)

nose2 = canvas.create_rectangle(headstartx+4.5*scaler, headstarty+4.5*scaler, headstartx+5.5*scaler, headstarty+5*scaler, fill='#faa23e', outline='') 

nose3 = canvas.create_line(headstartx+4.5*scaler, headstarty+3.5*scaler, headstartx+4.5*scaler, headstarty+4.7*scaler, width=2) 

nose4 = canvas.create_line(headstartx+5.5*scaler, headstarty+3.5*scaler, headstartx+5.5*scaler, headstarty+4.7*scaler, width=2) 

#mouth
mouth = canvas.create_arc(headstartx+4.5*scaler, headstarty+7*scaler, headstartx+6.5*scaler, headstarty+9*scaler, start=0, extent=180, fill='#eec1ad', outline='') 

##End animation of trump looking mad 
headstartx=150 ; headstarty = 75 ; scaler = 47

eyeSwitchColors = ['#f5d287', '#f5b787', '#fc9647', '#fa5a41', '#f23a1d', '#ff2300']

backgroundColor = ['#009fe8', '#006594', '#004463', '#300012', '#030101', '#000000']

g = 0

for i in range(501):
  if i%100 == 0:
    eyecolor = eyeSwitchColors[g]
    bgcolor = backgroundColor[g]

    background = canvas.create_rectangle(0,0,800,600, fill=bgcolor)

    #Creates donald trump's head
    head1 = canvas.create_polygon(headstartx, headstarty, headstartx+5*scaler, headstarty, headstartx+10*scaler, headstarty, headstartx+11*scaler, headstarty+3*scaler, headstartx+11*scaler, headstarty+7.5*scaler, headstartx+11*scaler, headstarty+11*scaler, headstartx+7*scaler, headstarty+10.7*scaler, headstartx+4*scaler, headstarty+10.35*scaler, headstartx-1*scaler, headstarty+10, headstartx-0.7, headstarty+7, headstartx-0.4, headstarty+4, headstartx, headstarty, smooth=True, fill='#faa23e')

    head2 = canvas.create_polygon(headstartx, headstarty, headstartx+1*scaler, headstarty+10*scaler, headstartx+3*scaler, headstarty+10.25*scaler, headstartx+7*scaler, headstarty+10.7*scaler, fill='#faa23e', smooth=True)

    hair = canvas.create_polygon(headstartx, headstarty, headstartx-1*scaler, headstarty+1*scaler, headstartx+5, headstarty+2*scaler, headstartx+8*scaler, headstarty, headstartx+10*scaler, headstarty, headstartx+10*scaler, headstarty-1*scaler, headstartx+5*scaler, headstarty, headstartx, headstarty, smooth=True, fill='#FFEAAE') 

    #Eyes, iris, and eyebrows
    Leye = canvas.create_oval(headstartx+1*scaler, headstarty+3*scaler, headstartx+3*scaler, headstarty+4*scaler, fill='white', outline='')

    Leyebrow = canvas.create_polygon(headstartx+0.5*scaler, headstarty+2*scaler, headstartx+3.5*scaler, headstarty+2.5*scaler, headstartx+3.5*scaler, headstarty+3*scaler, headstartx+0.5*scaler, headstarty+2.5*scaler, fill='#FFEAAE', outline='') 

    Reye = canvas.create_oval(headstartx+7*scaler, headstarty+3*scaler, headstartx+9*scaler, headstarty+4*scaler, fill='white', outline='') 

    Reyebrow = canvas.create_polygon(headstartx+9.5*scaler, headstarty+2*scaler, headstartx+6.5*scaler, headstarty+2.5*scaler, headstartx+6.5*scaler, headstarty+3*scaler, headstartx+9.5*scaler, headstarty+2.5*scaler, fill='#FFEAAE', outline='') 

    Liris = canvas.create_oval(headstartx+1.5*scaler, headstarty+3*scaler, headstartx+2.5*scaler, headstarty+4*scaler, fill=eyecolor, outline='') 

    Riris = canvas.create_oval(headstartx+7.5*scaler, headstarty+3*scaler, headstartx+8.5*scaler, headstarty+4*scaler, fill=eyecolor, outline='') 

    #nose outline
    nose1 = canvas.create_oval(headstartx+4*scaler, headstarty+4.5*scaler, headstartx+6*scaler, headstarty+6*scaler, fill='#faa23e', width=2)

    nose2 = canvas.create_rectangle(headstartx+4.5*scaler, headstarty+4.5*scaler, headstartx+5.5*scaler, headstarty+5*scaler, fill='#faa23e', outline='') 

    nose3 = canvas.create_line(headstartx+4.5*scaler, headstarty+3.5*scaler, headstartx+4.5*scaler, headstarty+4.7*scaler, width=2) 

    nose4 = canvas.create_line(headstartx+5.5*scaler, headstarty+3.5*scaler, headstartx+5.5*scaler, headstarty+4.7*scaler, width=2) 

    #mouth
    mouth = canvas.create_arc(headstartx+4.5*scaler, headstarty+7*scaler, headstartx+6.5*scaler, headstarty+9*scaler, start=0, extent=180, fill='#eec1ad', outline='') 
    canvas.update()
    time.sleep(0.2)

    g += 1

time.sleep(2)

#To be continued
canvas.create_rectangle(0,0,800,600, fill='black')

canvas.create_text(400,300, fill='Red', text='TO BE CONTINUED...', font='Arial 50') 

canvas.update()
