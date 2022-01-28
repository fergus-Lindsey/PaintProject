#lindsey ferguson paint project

#INDIVIDUAL FEATURES
#when tool is hoverd over it changes colour
#spraypaint tool
#choose your own colour/ current colour
#music
#increaseing/decreasing the size with keys
#undo
#semi working polygon tool???
#not having to move the window everytime
#text/ quotes tool
#undo and redo
#canvas background
#tells you what size, where your mouse is and what tool your using
#------------------------------------------------------------------------------------------
from pygame import *
from math import *
from random import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from glob import *
root = Tk()            
root.withdraw()

#this imports and initializes my font
font.init()
comicFont = font.SysFont("Comic Sans MS",20)
screen = display.set_mode((800,600))

#opening 
import os
init() #this makes sure you dont have to move the window everytime
inf=display.Info()
w,h=inf.current_w,inf.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,50'

#colours
#just so i didnt have to write them everytime
white = (255,255,255)
black = (0,0,0)
blue = (16,52,166)
red = (255,0,0)
darkblue = (25,25,112)
lightgrey = (211,211,211)
darkgrey = (169,169,169)

#these allow you to chose your own colours, one for leftclick and one for right click 
draw_colour_left = black
draw_colour_right = white 

#---------------------------------------------------------
#BACKGROUND/CANVAS/DECORATIONS
#background
background = image.load("images/wallpaper.jpg")
background1 = transform.smoothscale(background,(800,600))
screen.blit(background1,(0,0))

#canvas background
#when using the left and right arrow keys these change the
#canvas into pictures to draw on
smallcast = image.load("images/b9999999.png")
smallcastB = transform.smoothscale(smallcast,(600,450))
bigcast = image.load("images/background3.jpg")
bigcastB = transform.smoothscale(bigcast,(600,450))
jakepic = image.load("images/background2.jpg")
jakepicB = transform.smoothscale(jakepic,(600,450))
b9 = image.load("images/b9.jpg")
b9B = transform.smoothscale(b9,(600,450))
b999 = image.load("images/b999.jpg")
b999B = transform.smoothscale(b999,(600,450))

#decoration
#this adds a sheild by the title
sheild = image.load("images/nypd.png")
sheild2 = transform.smoothscale(sheild,(60,60))
screen.blit(sheild2,(660,10,60,60))

#canvas
#this makes the canvas and adds a border
canvasB = draw.rect(screen,black,(190,143,600,450),5)
canvas = draw.rect(screen,white,(190,143,600,450))

#title
#this imports the title picture
titleA = image.load("images/Brooklyn_nine-nine_logo.png")
titleB = transform.smoothscale(titleA,(400,70))
titleRect = Rect(250,5,400,70)
screen.blit(titleB,titleRect)
#--------------------------------------------------------
#music
mixer.music.load("images/b99.mp3")
mixer.music.play(+5)

#-----------------------------------------------------------------------
#PICTURES
#here is where i import/resize all my images and add a white background

#pencil picture
tool = "pencil"
#this just sets the variable so it always starts off with pencil
pencil_box_fill = draw.rect(screen,white,(25,10,60,60))
pencilA= image.load("images/pencil.png")
pencilB= transform.scale(pencilA,(60,60))
pencilRect = Rect(25,10,60,60)
screen.blit(pencilB,pencilRect)

#eraser picture
eraser_box_fill = draw.rect(screen,white,(110,10,60,60))
eraserA= image.load("images/eraser.png")
eraserB= transform.scale(eraserA,(60,60))
eraserRect = Rect(110,10,60,60)
screen.blit(eraserB,eraserRect)

#marker picture
marker_box_fill = draw.rect(screen,white,(110,80,60,60))
markerA= image.load("images/marker.jpeg")
markerB= transform.scale(markerA,(60,60))
markerRect = Rect(110,80,60,60)
screen.blit(markerB,markerRect)

#fill picture
fill_box_fill = draw.rect(screen,white,(25,80,60,60))
fillA= image.load("images/fillicon.png")
fillB= transform.scale(fillA,(60,60))
fillRect = Rect(25,80,60,60)
screen.blit(fillB,fillRect)

#spray paint
spraypaint_box_fill = draw.rect(screen,white,(110,221,60,60))
spraypaintA= image.load("images/spraypaint.png")
spraypaintB= transform.scale(spraypaintA,(60,60))
spraypaintRect = Rect(110,221,60,60)
screen.blit(spraypaintB,spraypaintRect)

#line
line_box_fill = draw.rect(screen,white,(110,150,60,60))
lineA= image.load("images/line.jpg")
lineB= transform.scale(lineA,(60,60))
lineRect = Rect(110,150,60,60)
screen.blit(lineB,lineRect)

#brush
brush_box_fill = draw.rect(screen,white,(25,150,60,60))
brushA= image.load("images/brush.jpg")
brushB= transform.scale(brushA,(60,60))
brushRect = Rect(25,150,60,60)
screen.blit(brushB,brushRect)

#highlighter
highlight_box_fill = draw.rect(screen,white,(25,221,60,60))
highlightA= image.load("images/highlighter.jpg")
highlightB= transform.scale(highlightA,(60,60))
highlightRect = Rect(25,221,60,60)
screen.blit(highlightB,highlightRect)

#polygon
poly_fill = draw.rect(screen,white,(25,361,60,60))
polyA = image.load("images/polygon.png")
polyB = transform.scale(polyA,(60,60))
poly_rect = Rect(25,361,60,60)
screen.blit(polyB,poly_rect)

#text
text_fill = draw.rect(screen,white,(110,361,60,60))
textA = image.load("images/letters.png")
textB = transform.scale(textA,(60,60))
text_rect = Rect(110,361,60,60)
screen.blit(textB,text_rect)

#undo
draw.rect(screen,white,(728,77,30,30))
draw.rect(screen,black,(728,77,30,30),2) 
undoA= image.load("images/undo.png")
undoB = transform.smoothscale(undoA,(25,25))
undo_Rect = Rect(730,79,930,40)
screen.blit(undoB,undo_Rect)

#redo
draw.rect(screen,black,(760,77,30,30),2) 
redoA= image.load("images/redo.png")
redoB = transform.smoothscale(redoA,(26,26))
redo_Rect = Rect(762,79,960,40)
screen.blit(redoB,redo_Rect)

#load
draw.rect(screen,white,(760,109,30,30))
loadA = image.load("images/hi.png")
loadB = transform.scale(loadA,(24,24))
openRect = Rect(760,109,30,30)
screen.blit(loadB, openRect)
draw.rect(screen,black,openRect,2)

#SAVE
draw.rect(screen,white,(728,109,30,30)) 
saveA= image.load("images/saveicon.png")
saveB = transform.scale(saveA,(24,24))
saveRect = Rect(728,109,30,30)
screen.blit(saveB,saveRect)
draw.rect(screen,black,saveRect,2)

#new
draw.rect(screen,white,(765,15,22,15))
newA= image.load("images/newicon.png")
newB = transform.scale(newA,(50,40))
new_Rect = Rect(750,5,50,40)
screen.blit(newB,new_Rect)

#quotes
#a list of some iconic quotes
quotes = ["Noice!","NINE NINE!","Smort","cool cool cool cool cool","i love your butt","your butt is the bomb",
          "no doubt no doubt, no doubt","not now boyle","toit","Amazing Detective/Genius"]
quotes_fill = draw.rect(screen,white,(125,540,60,25))
quoteA = image.load("images/quotes.jpg")
quoteB = transform.smoothscale(quoteA,(60,25))
quote_Rect = Rect(125,540,60,25)
screen.blit(quoteB,quote_Rect)

#colour dropper
#allows you to find a colour previously used on the canvas
CD_fill = draw.rect(screen,white,(125,510,60,25))
CD = image.load("images/eyedropper.png")
CDb = transform.scale(CD,(60,25))
CD_Rect = Rect(125,510,60,25)
screen.blit(CDb,CD_Rect)

#RECTANGLE
#this draws the rectangle box, as it was easier just to
#draw them rather than import
rectangle_fill = draw.rect(screen,white,(110,291,60,60))
rectangleAfill = draw.rect(screen,white,(123,303,35,35))
rectangleBfill = draw.rect(screen,black,(110,291,60,60),2)
rectangleCfill = draw.rect(screen,black,(123,303,35,35),2)


#ELLISP
#this draws the ellisp box, as it was easier just to draw them
#rather than import
rectangle_fill = draw.rect(screen,white,(110,291,60,60))
eclisp_fill = draw.rect(screen,white,(25,291,60,60))
eclisp = draw.circle(screen,white,(55,320),20)
eclisp = draw.circle(screen,black,(55,320),20,2)
            
#-------------------------------------------------------------------------
#STICKERS
#heres where i import/resize all my stickers also adding a white background
jake_sticker_fill = draw.rect(screen,white,(188,77,58,58))
jake_stickerA = image.load("images/jakesticker.png")
jake_stickerB = transform.smoothscale(jake_stickerA,(55,55))
jake_sticker_Rect = Rect(190,80,40,40)  
screen.blit(jake_stickerB,jake_sticker_Rect)

amy_sticker_fill=draw.rect(screen,white,(248,77,58,58))
amy_stickerA= image.load("images/amysticker.png")
amy_stickerB = transform.smoothscale(amy_stickerA,(55,55))
amy_sticker_Rect = Rect(250,78,40,40)
screen.blit(amy_stickerB,amy_sticker_Rect)

holt_sticker_fill= draw.rect(screen,white,(308,77,58,58))
holt_stickerA= image.load("images/captainholtsticker.png")
holt_stickerB = transform.smoothscale(holt_stickerA,(55,55))
holt_sticker_Rect = Rect(310,80,40,40)
screen.blit(holt_stickerB,holt_sticker_Rect)

chedder_sticker_fill=draw.rect(screen,white,(368,77,58,58))
chedder_stickerA= image.load("images/cheddersticker.png")
chedder_stickerB = transform.smoothscale(chedder_stickerA,(55,55))
chedder_sticker_Rect = Rect(370,80,40,40)
screen.blit(chedder_stickerB,chedder_sticker_Rect)

hitchcock_and_scully_fill=draw.rect(screen,white,(428,77,58,58))
hitchcock_and_scully_stickerA= image.load("images/hitchcockandscullysticker.png")
hitchcock_and_scully_stickerB = transform.smoothscale(hitchcock_and_scully_stickerA,(55,55))
hitchcock_and_scully_sticker_Rect = Rect(430,80,40,40)
screen.blit(hitchcock_and_scully_stickerB,hitchcock_and_scully_sticker_Rect)

terry_sticker_fill=draw.rect(screen,white,(488,77,58,58)) 
terry_stickerA= image.load("images/terrysticker.png")
terry_stickerB = transform.smoothscale(terry_stickerA,(55,55))
terry_sticker_Rect = Rect(490,80,40,40)
screen.blit(terry_stickerB,terry_sticker_Rect)

charles_sticker_fill=draw.rect(screen,white,(548,77,58,58))   
charles_stickerA= image.load("images/charlessticker.jpg")
charles_stickerB = transform.smoothscale(charles_stickerA,(55,55))
charles_sticker_Rect = Rect(550,78,40,40)
screen.blit(charles_stickerB,charles_sticker_Rect)

rosa_sticker_fill=draw.rect(screen,white,(608,77,58,58)) 
rosa_stickerA= image.load("images/rosasticker.png")
rosa_stickerB = transform.smoothscale(rosa_stickerA,(55,55))
rosa_sticker_Rect = Rect(610,78,40,40)
screen.blit(rosa_stickerB,rosa_sticker_Rect)

ap_sticker_fill=draw.rect(screen,white,(668,77,58,58))   
ap_stickerA= image.load("images/ap.png")
ap_stickerB = transform.smoothscale(ap_stickerA,(55,55))
ap_sticker_Rect = Rect(670,78,40,40)
screen.blit(ap_stickerB,ap_sticker_Rect)

#colour wheel pictures
#import the colour wheel/resizing
colour_wheelA = image.load("images/colour.jpg")
colour_wheelB = transform.scale(colour_wheelA,(100,120))
colour_wheelC = (1,480)
screen.blit(colour_wheelB,colour_wheelC)
#this is the black to white gradient colour bar allowing for more shades
gradientA = image.load("images/gradient.jpg")
gradientB = transform.scale(gradientA,(20,120))
gradientC = (100,480)
screen.blit(gradientB,gradientC)
#---------------------------------------------------------------------------------
#IMPORTANT VARIABLES

#this is my size variable when ever the up or down key is pressed the size will increase or decrease
size = 1
keys = key.get_pressed()

#this is the list that allows redo and undo to properly work
#once a screen shot of the canvas has been taken (button up)it gets added onto the undo list
#once the button ir pressed it blits the old image back onto the canas and then adding the screenshot onto the redo list
undo = [screen.subsurface(canvas).copy()]
redo = []

#mx,my is mouse position and the omx,omy is the "old" pos allowinga line to be formed
mx,my =0,0
omx,omy = 0,0

#these are my polygon variables all starting at 0 so they can be in "start mode"
poly_button = 0
poly_start = 0
poly_end = 0
poly_mid = 0

#this allows the text tool to be of use, the message would then get typed and then added to the mx,my they desried
message = ""

#this is the list of canvas background
BackgroundList = ["smallcastB","bigcastB","jakepicB","b9B","b999B"]

#these are the sizes that allow rectangle
#and ellisp to be filled (when you press 1) or unfilled (when you press 0)
rectangle_size = 2
ellisp_size = 1
#--------------------------------------------------------------------------
#running
running = True
while running :
    click = False
    button_clicked = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            click = True
            poly_button = 1 #sets the polygon button 
            if evt.button ==1:
                start = evt.pos #this is used for the line tool, it sets the first point then allows the user to drag the line
            if tool == "filling" or tool == "rectangle":  #this sets the position of the users ellisp 
                rmx,rmy = mx,my                           #and rectangle allowing them to draw it themselves
            if tool == "filling" or tool == "eclisp":
                emx,emy = mx,my
                ellispRect=(emx,emy,mx-emx,my-emy)            # this is the box for the ellisp
            if evt.button == 3:
                poly_button = 2#sets the polygon button
            back = screen.copy()        
            button_clicked = True
        if evt.type == MOUSEBUTTONUP:
            click = True
            pic = screen.subsurface(canvas).copy() #when the mouse button (mb) comes up or no longer clicked a screen shot is taken of the canvas
            if click and canvas.collidepoint(mx,my):  
                undo.append(pic) #this adds the the picture to the undo list 
            if undo_Rect.collidepoint(mx,my): #if undo is clicked and has more than 1 pic it can undo
                if len(undo)>1: 
                    undopic = undo.pop() #this removes it from the undo list
                    redo.append(undopic) #this adds it back onto the redo list 
                screen.blit(undo[-1],(190,143)) #this puts the screen shot back to the canvas
            if click and canvas.collidepoint(mx,my):
                undo.append(pic) 
            running = True
while running :
    click = False
    button_clicked = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            click = True
            poly_button = 1 #sets the polygon button 
            if evt.button ==1:
                start = evt.pos #this is used for the line tool, it sets the first point then allows the user to drag the line
            if tool == "filling" or tool == "rectangle":  #this sets the position of the users ellisp 
                rmx,rmy = mx,my                           #and rectangle allowing them to draw it themselves
            if tool == "filling" or tool == "eclisp":
                emx,emy = mx,my
                ellispRect=(emx,emy,mx-emx,my-emy)            # this is the box for the ellisp
            if evt.button == 3:
                poly_button = 2#sets the polygon button
            back = screen.copy()        
            button_clicked = True
        if evt.type == MOUSEBUTTONUP:
            click = True
            pic = screen.subsurface(canvas).copy() #when the mouse button (mb) comes up or no longer clicked a screen shot is taken of the canvas
            if click and canvas.collidepoint(mx,my):  
                undo.append(pic) #this adds the the picture to the undo list 
            if undo_Rect.collidepoint(mx,my): #if undo is clicked and has more than 1 pic it can undo
                if len(undo)>1: 
                    undopic = undo.pop() #this removes it from the undo list
                    redo.append(undopic) #this adds it back onto the redo list 
                screen.blit(undo[-1],(190,143)) #this puts the screen shot back to the canvas
            if click and canvas.collidepoint(mx,my):
                undo.append(pic) 
   #unicode is where each letter is assigned a number
                textPic = comicFont.render(message,True,draw_colour_left)
            if evt.key == K_RIGHT:
                #this allows users to change the background of their canvad,
                #going to the right theres 5 different options, but when you click
                #to the left you just get a plain canvas
                backgroundS = choice(BackgroundList)
                if backgroundS == "smallcastB":
                    screen.blit(smallcastB,(190,143))
                if backgroundS == "bigcastB":
                    screen.blit(bigcastB,(190,143))
                if backgroundS == "jakepicB":
                    screen.blit(jakepicB,(190,143))
                if backgroundS == "b9B":
                    screen.blit(b9B,(190,143))
                if backgroundS == "b999B":
                    screen.blit(b999B,(190,143))
            if evt.key == K_LEFT:
                draw.rect(screen,white,(190,143,600,450))
    #--------------------------------------------------------------------
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    #this draws the blue box where mouse pos, sizze, and tool indicators stay
    instruction = draw.rect(screen,blue,(25,425,145,50))
    instructionB = draw.rect(screen,black,(25,425,145,50),3)
    
    #these tell the user: where the mouse is, the tool there using,
    #the size there using and if its filled or unfilled
    myfont = font.SysFont("Comic Sans SM",20)
    mousePOS = myfont.render("mouse pos: "+str(mx)+(", ")+str(my),True, black)
    screen.blit(mousePOS, (30,428))
    toolindicator = myfont.render("tool: "+str(tool),True,black)
    screen.blit(toolindicator,(30,442))
    sizeindicator = myfont.render("size: "+str(size),True,black)
    screen.blit(sizeindicator,(30,455))
    #-------------------------------------------------------------------------
    #this draws the rectangle for the rectangle tool box
    rectangleBfill = draw.rect(screen,black,(110,291,60,60),2)
    rectangleCfill = draw.rect(screen,black,(123,303,35,35),2)

    #----------------------------------------------------------------------------   
    #load/save
    #heres my load and save, when saving it only saves a
    #picture of the canvas and adds a png to the end
    #for my load you can load any photo from your comptuer
    if mb[0] ==1 and openRect.collidepoint(mx,my):    
        loadname = askopenfilename()
        loadpic = image.load(loadname)            
        load = transform.scale(loadpic, (600,450))
        screen.blit(load, (190,143))
       
    if mb[0]==1 and saveRect.collidepoint(mx,my):
        savepic = asksaveasfilename()
        image.save(screen.subsurface(canvas),savepic+".png")
    #-------------------------------------------------------------------------------      
    #colour wheel code
    #here i have my ability to choose colour 
    #left click
    square = draw.rect(screen,black,(1,480,100,120),3)
    square2 = draw.rect(screen,black,(100,480,20,120),3)
    square3 = draw.rect(screen,black,(1,480,120,120),3)
    if square3.collidepoint(mx,my)and mb[0] == 1:
        draw_colour_left = screen.get_at((mx,my))
        highlighter_colour_left = draw_colour_left[:3]+(35,)
    left_colour_boxA = draw.rect(screen,draw_colour_left,(123,568,30,30))
    left_colour_boxB = draw.rect(screen,black,(123,568,30,30),2)
    
    #right click
    if square3.collidepoint(mx,my)and mb[2] == 1:
        draw_colour_right = screen.get_at((mx,my))
        highlighter_colour_right = draw_colour_right[:3]+(35,)
    right_colour_boxA = draw.rect(screen,draw_colour_right,(155,568,30,30))
    right_colour_boxB = draw.rect(screen,black,(155,568,30,30),2)
    #----------------------------------------------------------------------------
    #BORDERS
    #this sets a nice black border around each tool
    pencil_box_border = draw.rect(screen,black,(25,10,60,60),3)
    eraser_box_border = draw.rect(screen,black,(110,10,60,60),3)
    highlight_box_border = draw.rect(screen,black,(25,221,60,60),3)
    brush_box_border = draw.rect(screen,black,(25,150,60,60),3)
    marker_box_border = draw.rect(screen,black,(110,80,60,60),3)
    line_box_border = draw.rect(screen,black,(110,150,60,60),3)
    spraypaint_box_border = draw.rect(screen,black,(110,221,60,60),3)
    fill_box_border = draw.rect(screen,black,(25,80,60,60),3)
    rectangle_border = draw.rect(screen,black,(110,291,60,60),3)
    eclisp_border = draw.rect(screen,black,(25,291,60,60),3)
    quotes_border = draw.rect(screen,black,(125,540,60,25),3)
    poly_border = draw.rect(screen,black,(25,361,60,60),3)
    text_border = draw.rect(screen,black,(110,361,60,60),3)
    CD_border = draw.rect(screen,black,(125,510,60,25),3)
    
    #this sets a nice border around all the stickers
    ap_sticker_border= draw.rect(screen,black,(668,77,58,58),3) 
    jake_sticker_border = draw.rect(screen,black,(188,77,58,58),3)
    amy_sticker_border = draw.rect(screen,black,(248,77,58,58),3)
    holt_sticker_border = draw.rect(screen,black,(308,77,58,58),3)
    chedder_sticker_border = draw.rect(screen,black,(368,77,58,58),3)
    hitchcock_and_scully_sticker_border = draw.rect(screen,black,(428,77,58,58),3)
    terry_sticker_border = draw.rect(screen,black,(488,77,58,58),3)
    rosa_sticker_border = draw.rect(screen,black,(608,77,58,58),3)   
    charles_sticker_border = draw.rect(screen,black,(548,77,58,58),3)

    #HIGHLIGHT TOOL
    #this allows users to hover over each tool option and a blue border temporarily appearing,
    #only when the tool is selected the border will fully turn blue,
    #going back to black when a new tool has been chosen
    if pencilRect.collidepoint(mx,my) or tool=="pencil":     
        draw.rect(screen,blue,pencilRect,3)
    if eraserRect.collidepoint(mx,my) or tool=="eraser":     
        draw.rect(screen,blue,eraserRect,3)
    if markerRect.collidepoint(mx,my) or tool=="marker":     
        draw.rect(screen,blue,markerRect,3)
    if fillRect.collidepoint(mx,my) or tool=="fill":     
        draw.rect(screen,blue,fillRect,3)
    if spraypaintRect.collidepoint(mx,my) or tool=="spray paint":     
        draw.rect(screen,blue,spraypaintRect,3)
    if highlightRect.collidepoint(mx,my) or tool=="highlight":     
        draw.rect(screen,blue,(25,221,60,60),3)
    if lineRect.collidepoint(mx,my) or tool=="line":     
        draw.rect(screen,blue,lineRect,3)
    if brushRect.collidepoint(mx,my) or tool=="brush":     
        draw.rect(screen,blue,brushRect,3)
    if rectangle_fill.collidepoint(mx,my) or tool == "rectangle":
        draw.rect(screen,blue,rectangle_fill,3)
    if eclisp_fill.collidepoint(mx,my) or tool == "eclisp":
        draw.rect(screen,blue,eclisp_fill,3)
    if poly_rect.collidepoint(mx,my) or tool == "polygon":
        draw.rect(screen,blue,poly_fill,3)
    if text_border.collidepoint(mx,my) or tool == "text":
        draw.rect(screen,blue,text_fill,3)
    if CD_border.collidepoint(mx,my) or tool == "colour dropper":
        draw.rect(screen,blue,CD_fill,3)
    if quotes_border.collidepoint(mx,my) or tool == "quotes":
        draw.rect(screen,blue,quotes_fill,3)
    
    #HIGHLIGHT STICKERS
    #this allows users to hover over each sticker and a blue border temporarily appearing,
    #only when the sticker is selected the border will fully turn blue,
    #going back to black when a new sticker/tool has been chosen
    if jake_sticker_fill.collidepoint(mx,my) or tool == "jake sticker":
        draw.rect(screen,blue,jake_sticker_fill,3)
    if amy_sticker_fill.collidepoint(mx,my) or tool == "amy sticker":
        draw.rect(screen,blue,amy_sticker_fill,3)
    if terry_sticker_fill.collidepoint(mx,my) or tool == "terry sticker":
        draw.rect(screen,blue,terry_sticker_fill,3)
    if rosa_sticker_fill.collidepoint(mx,my) or tool == "rosa sticker":
        draw.rect(screen,blue,rosa_sticker_fill,3)
    if holt_sticker_fill.collidepoint(mx,my) or tool == "holt sticker":
        draw.rect(screen,blue,holt_sticker_fill,3)
    if chedder_sticker_fill.collidepoint(mx,my) or tool == "chedder sticker":
        draw.rect(screen,blue,chedder_sticker_fill,3)
    if ap_sticker_fill.collidepoint(mx,my) or tool == "ap sticker":
        draw.rect(screen,blue,ap_sticker_fill,3)
    if hitchcock_and_scully_fill.collidepoint(mx,my) or tool == "hitchcock & scully sticker":
        draw.rect(screen,blue,hitchcock_and_scully_fill,3)
    if charles_sticker_fill.collidepoint(mx,my) or tool == "charles sticker":
        draw.rect(screen,blue,charles_sticker_fill,3)
#---------------------------------------------------------------------------        
    #SELECTING TOOLS/STICKERS
        
    #this is all the selecting tools happend,
    #if the user clicks on the box where the tool
    #are it will set the tool to the correct tool allowing the user to use it
    if mb[0]== 1:
        if pencilRect.collidepoint(mx,my):   
            tool = "pencil"
        if eraserRect.collidepoint(mx,my):
            tool = "eraser"
        if markerRect.collidepoint(mx,my):
            tool = "marker"
        if fillRect.collidepoint(mx,my):
            tool = "fill"
        if spraypaintRect.collidepoint(mx,my):
            tool = "spray paint"
        if brushRect.collidepoint(mx,my):
            tool = "brush"
        if lineRect.collidepoint(mx,my):
            tool = "line"
        if highlightRect.collidepoint(mx,my):
            tool = "highlighter"
        if new_Rect.collidepoint(mx,my):
            tool = "new"
        if undo_Rect.collidepoint(mx,my):
            tool = "undo"
        if redo_Rect.collidepoint(mx,my):
            tool = "redo"
        if rectangle_fill.collidepoint(mx,my) or rectangleAfill.collidepoint(mx,my):
            tool =  "rectangle"
        if eclisp_fill.collidepoint(mx,my) or eclisp_fill.collidepoint(mx,my):
            tool = "eclisp"
        if quote_Rect.collidepoint(mx,my):
            tool = "random quotes"
        if poly_rect.collidepoint(mx,my):
            tool = "polygon"
        if text_rect.collidepoint(mx,my):
            tool = "text"
        if CD_Rect.collidepoint(mx,my):
            tool = "colour dropper"
    
        #this is all the selecting tools for the sticker,
        #if the user clicks on the box where the stickers
        #are it will set the tool to it allowing the user to use the sticker
        if jake_sticker_Rect.collidepoint(mx,my):
            tool = "jake sticker"
        if amy_sticker_Rect.collidepoint(mx,my):
            tool = "amy sticker"
        if rosa_sticker_Rect.collidepoint(mx,my):
            tool = "rosa sticker"
        if holt_sticker_Rect.collidepoint(mx,my):
            tool = "holt sticker"
        if ap_sticker_Rect.collidepoint(mx,my):
            tool = "adrien sticker"
        if chedder_sticker_Rect.collidepoint(mx,my):
            tool = "chedder sticker"
        if hitchcock_and_scully_sticker_Rect.collidepoint(mx,my):
            tool = "hitchcock and scully sticker"
        if terry_sticker_Rect.collidepoint(mx,my):
            tool = "terry sticker"
        if charles_sticker_Rect.collidepoint(mx,my):
            tool = "charles sticker"
            
    #NEW TOOL
    #since the new tool isnt on the canvas it had to be moved away
    #from all the other tool selections, this allows users to start over
    #to the begining so they dont have to restart the program
    if tool == "new":
        canvas = draw.rect(screen,white,(190,143,600,450))
        tool == "pencil"
        
    #TOOL CODEING FOR LEFT CLICK
    #this is where the actal tool code is...
    if mb[0]== 1 and canvas.collidepoint(mx,my):
        screen.set_clip(canvas)
        if tool == "pencil":
            draw.line(screen,draw_colour_left,(omx,omy),(mx,my),size) #this draws a line anywhere the mouse follows
        if tool == "eraser":
            draw.rect(screen,white,(mx-10,my-5,60,50)) #this erases everything
        if tool == "marker":
            draw.line(screen,draw_colour_left,(omx,omy),(mx,my),size+3) #a thicker version of a pencil giving the appearance of a marker
        if tool == "fill":
            screen.fill(draw_colour_left) #fills the canas any colour 
        if  tool == "spray paint":
            for i in range(15):
               x2=randint(-(size+3)*5,(size+3)*5)                
               y2=randint(-(size+3)*5,(size+3)*5)  #these make random little circles appear 
               if (((x2)**2+(y2)**2)**0.5) <=25:               
                   draw.circle(screen,draw_colour_left,(mx+x2,my+y2),0) # a circleular spraypaint effect
        if tool == "line":
            screen.blit(back,(0,0))
            draw.line(screen,draw_colour_left,start,(mx,my),size) #draws a straight line 
        if tool == "brush":
            draw.line(screen,draw_colour_left,(omx+5,omy+3),(mx+5,my+3),size+1)
            draw.line(screen,draw_colour_left,(omx+2,omy+17),(mx+2,my+17),size)
            draw.line(screen,draw_colour_left,(omx,omy+2),(mx,my+2),size)
            draw.line(screen,draw_colour_left,(omx,omy+12),(mx,my+12),size+1)     #gives the appearance of a paintbrush
            draw.line(screen,draw_colour_left,(omx-8,omy+8),(mx-8,my+8),size+1)
            draw.line(screen,draw_colour_left,(omx+6,omy+16),(mx+6,my+16),size)
            draw.line(screen,draw_colour_left,(omx-12,omy+3),(mx-12,my+3),size)
        if tool == "rectangle":
            screen.blit(back,(0,0))
            draw.rect(screen,draw_colour_left,(rmx,rmy,mx-rmy,my-rmy),rectangle_size) #draws a rectangle (press 1 to be filled)
        if tool == "highlighter":
            highlight = Surface((20,20),SRCALPHA)
            draw.circle(highlight,(highlighter_colour_left),(10,10),10)#gives a more transparent colour of your colour selected
            if mx!=omx or my!=omy:
                if mb[0]==1:
                    screen.blit(highlight,(mx-10,my-10))
        if tool == "eclisp": #draws an ellisp (press 1 to fill)
           screen.blit(back,(0,0))                                
           ellispRect= Rect(emx,emy,mx-emx,my-emy) #this draws the box the ellisp is in (also set in loop)
           ellispRect.normalize()                                   
           if ellispRect.width>1 and ellispRect.height>1:
               draw.ellipse(screen,draw_colour_left,ellispRect, ellisp_size)
        if tool == "random quotes":
            if click:
                txtPic = comicFont.render(choice(quotes), True, draw_colour_left)
                screen.blit(txtPic,(mx-txtPic.get_width()/2, my-txtPic.get_height()/2)) #using a list of quotes they randomly appear when right or left clicked on canvas
        if tool == "polygon":                                           #the tool first starts in start mode setting the first mx,my 
            if poly_button == 2 and poly_start !=0 and poly_end !=0:   #when the vaiables are all not equal to 0 the program will draw the first line
                draw.line(screen,draw_colour_left,poly_end,poly_start,2)  
                poly_start = 0
                poly_end = 0
            elif poly_button == 1 and poly_start == 0: 
                poly_start = mx,my
            elif poly_button ==1 and poly_mid == 0 and poly_start != (mx,my):
                if poly_end == 0:
                    poly_mid = mx,my
                    draw.line(screen,draw_colour_left,poly_start,poly_mid,2)#this also draws the middles 
                    poly_end = poly_mid
                    poly_mid = 0
                    poly_button = 0
                else:
                    poly_mid = mx,my
                    draw.line(screen,draw_colour_left,poly_end,poly_mid,2) # this draws the middles lines AS WELL as it was supposed to end but unfortunally it doesent  
                    poly_end = poly_mid
                    poly_mid = 0
                    poly_button = 0
        if tool == "text":
            screen.blit(back,(0,0))
            screen.blit(textPic,(mx,my))
        if tool == "colour dropper":
            draw_colour_left = screen.get_at((mx,my))
        
        screen.set_clip(None)
       
    #TOOL CODEING FOR RIGHT CLICK
    #since it required to different mouse buttons i decided just to copy and paste my code
    #and set it as mb[2] ==1 instead of mb[0] ==1: so they can left and right click different colours
    #this is where the actal tool code is...
    if mb[2]== 1 and canvas.collidepoint(mx,my):
        screen.set_clip(canvas)
        if tool == "pencil":
            draw.line(screen,draw_colour_right,(omx,omy),(mx,my),size)
        if tool == "eraser":
            draw.rect(screen,white,(mx-10,my-5,60,50))
        if tool == "marker":
            draw.line(screen,draw_colour_right,(omx,omy),(mx,my),size+3)
        if tool == "fill":
            screen.fill(draw_colourR)
        if  tool == "spray paint":
            for i in range(15):                              
               x2=randint(-size*15,size*15)                
               y2=randint(-size*15,size*15)
            if (((x2)**2+(y2)**2)**0.5) <=25:               
                   draw.circle(screen,draw_colour_right,(mx+x2,my+y2),0)
        if tool == "line":
            screen.blit(back,(0,0))
            draw.line(screen,draw_colour_right,start,(mx,my),size)
        if tool == "brush":
            draw.line(screen,draw_colour_right,(omx+5,omy+3),(mx+5,my+3),size+1)
            draw.line(screen,draw_colour_right,(omx+2,omy+17),(mx+2,my+17),size+1)
            draw.line(screen,draw_colour_right,(omx,omy+2),(mx,my+2),size+5)
            draw.line(screen,draw_colour_right,(omx,omy+12),(mx,my+12),size+1)
            draw.line(screen,draw_colour_right,(omx-8,omy+8),(mx-8,my+8),size+1)
            draw.line(screen,draw_colour_right,(omx+6,omy+16),(mx+6,my+16),size+3)
            draw.line(screen,draw_colour_right,(omx-12,omy+3),(mx-12,my+3),size+3)
            draw.line(screen,draw_colour_right,(omx-3,omy+8),(mx-3,my+8),size+1)
        if tool == "rectangle":
            screen.blit(back,(0,0))
            draw.rect(screen,draw_colour_right,(rmx,rmy,mx-rmy,my-rmy),rectangle_size)
        if tool == "highlighter":
            highlightR = Surface((20,20),SRCALPHA)
            draw.circle(highlightR,(highlighter_colour_right),(10,10),10)
            if mx!=omx or my!=omy:
                if mb[0]==1:
                    screen.blit(highlight_right,(mx-10,my-10))
        if tool == "eclisp":
           screen.blit(back,(0,0))                                
           ellispRect= Rect(emx,emy,mx-emx,my-emy)
           ellispRect.normalize()                                   
           if ellispRect.width>1 and ellsipRect.height>1:
               draw.ellipse(screen,draw_colour_right,ellispRect,ellisp_size)
        if tool == "polygon":
            if poly_button == 2 and poly_start !=0 and poly_end !=0:
                draw.line(screen,draw_colour_right,poly_end,poly_start,2)
                poly_start = 0
                poly_end = 0
            elif poly_button == 1 and poly_start == 0:
                poly_start = mx,my
            elif poly_button ==1 and poly_mid == 0 and poly_start != (mx,my):
                if poly_end == 0:
                    poly_mid = mx,my
                    draw.line(screen,draw_colour_right,poly_start,poly_mid,2)
                    poly_end = poly_mid
                    poly_mid = 0
                    poly_button = 0
                else:
                    poly_mid = mx,my
                    draw.line(screen,draw_colour_right,poly_end,poly_mid,2)
                    poly_end = poly_mid
                    poly_mid = 0
                    poly_button = 0
        if tool == "text":
            screen.blit(back,(0,0))
            screen.blit(txtPic,(mx,my))
        if tool == "colour dropper":
            draw_colour_right = screen.get_at((mx,my))
        screen.set_clip(None)
#--------------------------------------------------------------------------------------------------------------------------------
    #sticker function
    #This alloww=s the user to make stamps bigger and smaller
    #when pressing the keys on keyboard up and down
    if mb[0]==1 and canvas.collidepoint(mx,my):
        r = (size+5)/10
        screen.set_clip(canvas)
        if tool=="jake sticker":
            jake_stickerB = transform.scale(jake_stickerA,(int(jake_stickerA.get_width()*r),int(jake_stickerA.get_height()*r)))
            screen.blit(jake_stickerB, (mx-jake_stickerB.get_width()//2,my-jake_stickerB.get_height()//2))
        if tool=="amy sticker":                               
            amy_stickerB = transform.scale(amy_stickerA,(int(amy_stickerA.get_width()*r),int(amy_stickerA.get_height()*r)))
            screen.blit(amy_stickerB, (mx-amy_stickerB.get_width()//2,my-amy_stickerB.get_height()//2))
        if tool=="terry sticker":                               
            terry_stickerB = transform.scale(terry_stickerA,(int(terry_stickerA.get_width()*r),int(terry_stickerA.get_height()*r)))
            screen.blit(terry_stickerB, (mx-terry_stickerB.get_width()//2,my-terry_stickerB.get_height()//2))
        if tool=="chedder sticker":                               
            chedder_stickerB = transform.scale(chedder_stickerA,(int(chedder_stickerA.get_width()*r),int(chedder_stickerA.get_height()*r)))
            screen.blit(chedder_stickerB, (mx-chedder_stickerB.get_width()//2,my-chedder_stickerB.get_height()//2))
        if tool=="charles sticker":                               
            charles_stickerB = transform.scale(charles_stickerA,(int(charles_stickerA.get_width()*r),int(charles_stickerA.get_height()*r)))
            screen.blit(charles_stickerB, (mx-charles_stickerB.get_width()//2,my-charles_stickerB.get_height()//2))
        if tool=="holt sticker":                               
            holt_stickerB = transform.scale(holt_stickerA,(int(holt_stickerA.get_width()*r),int(holt_stickerA.get_height()*r)))
            screen.blit(holt_stickerB, (mx-holt_stickerB.get_width()//2,my-holt_stickerB.get_height()//2))
        if tool=="hitchcock and scully sticker":                               
            hitchcock_and_scully_stickerB = transform.scale(hitchcock_and_scully_stickerA,(int(hitchcock_and_scully_stickerA.get_width()*r),int(hitchcock_and_scully_stickerA.get_height()*r)))
            screen.blit(hitchcock_and_scully_stickerB, (mx-hitchcock_and_scully_stickerB.get_width()//2,my-hitchcock_and_scully_stickerB.get_height()//2))
        if tool=="rosa sticker":                               
            rosa_stickerB = transform.scale(rosa_stickerA,(int(rosa_stickerA.get_width()*r),int(rosa_stickerA.get_height()*r)))
            screen.blit(rosa_stickerB, (mx-rosa_stickerB.get_width()//2,my-rosa_stickerB.get_height()//2))
        if tool=="adrien sticker":                               
            ap_stickerB = transform.scale(ap_stickerA,(int(ap_stickerA.get_width()*r),int(ap_stickerA.get_height()*r)))
            screen.blit(ap_stickerB, (mx-ap_stickerB.get_width()//2,my-ap_stickerB.get_height()//2))
        screen.set_clip(None)

  
    omx,omy = mx,my
    #---------------------------
    display.flip()
font.quit()
del comicFont
quit()
