# Gold Card

import pygame
import sys
import random
import time
from random import randrange


## GLOBAL VARIABLES
FPS = 45
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
GAMEDISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
BOXSIZE = 20
BOARDWIDTH = 24
BOARDHEIGHT = 16
TEXTWIDTH = 20
TEXTHEIGHT = 6
CARDWIDTH = 3
CARDHEIGHT = 3

BLANK = '.'
XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 140
txtXMARGIN = int((WINDOWWIDTH - TEXTWIDTH * BOXSIZE) / 2)
txtTOPMARGIN = WINDOWHEIGHT - (TEXTHEIGHT * BOXSIZE) - 10
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREY = (100, 100, 100)
GREY2 = (90, 80, 80)
BLUE1 = (0,0,200)
BLUE2 = (0,0,100)
GOLD = (125, 125, 0)
GREEN = (0, 255, 0)
YELLOW = (175, 175, 0)
CARDCOLORS = (WHITE, GOLD, BLACK, BLUE1)

# BG COLOR FOR SCREEN
BGCOLOR = BLACK
# COLOR OF TOP BOX
TOPBOXCOLOR = BLACK
# COLOR OF TEXT BOX
TEXTBOXCOLOR = BLUE1
# BORDER COLOR
BORDERCOLOR = WHITE

TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GREY2

class Card():
        # card prototype
    def __init__(self, ctype, cpower, cname, cindex):
        self.cname = cname # Name of card
        self.ctype = ctype # Type, Gold, White or Blue
        self.cpower = cpower # "Strength of the card"
        self.cindex = cindex # Unique card number

    def card_info(self, ctype, cpower, cname):
        print("Card Name:", cname)
        print("Type:", ctype)
        print("Power:", cpower)

# list of cards and attributes
white1 = Card("WHITE", 1 ,"White 1", 0)
white3 = Card("WHITE", 3 ,"White 3", 2)
white4 = Card("WHITE", 4 ,"White 4", 3)
white5 = Card("WHITE", 5 ,"White 5", 4)
gold1 = Card("GOLD", 1 ,"Gold 1", 5)
gold3 = Card("GOLD", 3 ,"Gold 3", 7)
blue1 = Card("BLUE", 0, "Double Power", 10)
blue2 = Card("BLUE", 0, "Block", 11)


# GRAPHICS
cardfront = [
pygame.image.load('graphics\white1.png').convert(),
pygame.image.load('graphics\white2.png').convert(),
pygame.image.load('graphics\white3.png').convert(),
pygame.image.load('graphics\white4.png').convert(),
pygame.image.load('graphics\white5.png').convert(),
pygame.image.load('graphics\gold1.png').convert(),
pygame.image.load('graphics\gold2.png').convert(),
pygame.image.load('graphics\gold3.png').convert(),
pygame.image.load('graphics\cardback.png').convert(),
pygame.image.load('graphics\cardback.png').convert(),
pygame.image.load('graphics\cardback.png').convert(),
pygame.image.load('graphics\cardback.png').convert()
]

cardback = pygame.image.load('graphics\cardback.png').convert()
cursorGfx = pygame.image.load('graphics\cursor.gif').convert()

# list of cards in the decks
# player's base deck:
pDeckCards = [gold1, white1, gold3, gold3, white3, white5, white4]
oDeckCards = [gold1, white1, gold3, gold3, white3, white5, white4]

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption("Gold Card")
    print("main works")
    runGame()

# input loop
    while True:
    
# KEYBOARD FUNCTIONS
        kPressed = pygame.key.get_pressed()

# determine to end the game
    if event.type == pygame.QUIT:
        return
    if event.type.key == pygame.K_w and ctrl_held:
        return
    if event.key == pygame.K_F4 and alt_held:
        return
    if event.key == pygame.K_ESCAPE:
        return

def runGame():
    print("run game works")
    updateText1 = ""
    updateText2 = ""
    updateText3 = ""
    updateText4 = ""
    
    # list of cards in the player's hand
    pHand = []
    oHand = []
    
    # copies of the decks
    pDeckInPlay = pDeckCards
    oDeckInPlay = oDeckCards
    
    # max number of cards in the deck
    pDeck = 7
    oDeck = 7
    
    # most recently drawn card
    drawnCard = 0
    odrawnCard = 0

    # current gold
    pgoldScore = 0
    ogoldScore = 0

    xHand = 100
    yHand = 240
    xCard = 480
    yCard = 40
    cursorx = -100
    cursory = -100
    selected = 1
    
    
    board = getBlankBoard()
    textbox = getTextBox()
    print("blank board works")
    # drawing the screen
    DISPLAYSURF.fill(BGCOLOR)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    print("draw board works")
    drawStatus(pgoldScore, pDeck, ogoldScore, updateText1, updateText2, updateText3, updateText4)
    print("draw status... good")
    pygame.display.update()
    pygame.mixer.music.load('cardmusic.mp3')
    pygame.mixer.music.play(0, 0.0)
    print("Tunes work")

    # update the screen and start the clock
    pygame.display.update()
    FPSCLOCK.tick(FPS)

    cursorMove = 0
    
#### ---------------------------BEGINNING OF THE GAME----------------------------- ####
    
# shuffle the decks
    updateText1="You and your opponent both"
    updateText2="shuffle your decks."
    updateText3=""
    updateText4=""

# shuffle decks
    print("Shuffling the deck...")
    random.shuffle(pDeckInPlay)
    random.shuffle(oDeckInPlay)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)
    
# drawing cards message
    updateText1="You draw your starting hand...."
    updateText2=""
    updateText3=""
    updateText4=""
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)

## drawing a card
    drawnCard = pDeckInPlay.pop(0)
    pDeck = pDeck - 1
    pHand.append(drawnCard)
    i1 = "You draw card 1:"
    i2 = drawnCard.cname
    i3 = "Power:", drawnCard.cpower
    i4 = drawnCard.ctype
    # starting point for hand display
    xHand = 100; # x coordnate of image
    yHand = 240; # y coordinate of image
    updateText1 = str(i1)
    updateText2 = str(i2)
    updateText3 = str(i3)
    updateText4 = str(i4)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)
    
## drawing a card
    drawnCard = pDeckInPlay.pop(0)
    pDeck = pDeck - 1
    pHand.append(drawnCard)
    i1 = "You draw card 2:"
    i2 = drawnCard.cname
    i3 = "Power:", drawnCard.cpower
    i4 = drawnCard.ctype
    updateText1 = str(i1)
    updateText2 = str(i2)
    updateText3 = str(i3)
    updateText4 = str(i4)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)
    
## drawing a card
    drawnCard = pDeckInPlay.pop(0)
    pDeck = pDeck - 1
    pHand.append(drawnCard)
    i1 = "You draw card 3:"
    i2 = drawnCard.cname
    i3 = "Power:", drawnCard.cpower
    i4 = drawnCard.ctype
    updateText1 = str(i1)
    updateText2 = str(i2)
    updateText3 = str(i3)
    updateText4 = str(i4)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)

## drawing a card
    drawnCard = pDeckInPlay.pop(0)
    pDeck = pDeck - 1
    pHand.append(drawnCard)
    i1 = "You draw card 4:"
    i2 = drawnCard.cname
    i3 = "Power:", drawnCard.cpower
    i4 = drawnCard.ctype
    updateText1 = str(i1)
    updateText2 = str(i2)
    updateText3 = str(i3)
    updateText4 = str(i4)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)
    
# opponent also draws 4 cards
    updateText1 = "Your opponent draws 4 cards as well...."
    updateText2=""
    updateText3=""
    updateText4=""
    # starting point for hand display
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)

    drawnCard = oDeckInPlay.pop(0)
    oDeck = oDeck - 1
    oHand.append(drawnCard)
    xCard = 480; # x coordnate of image
    yCard = 40; # y coordinate of image
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    pygame.time.wait(1000)

    drawnCard = oDeckCards.pop(0)
    oDeck = oDeck - 1
    oHand.append(drawnCard)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    pygame.time.wait(1000)

    drawnCard = oDeckCards.pop(0)
    oDeck = oDeck - 1
    oHand.append(drawnCard)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    pygame.time.wait(1000)

    drawnCard = oDeckCards.pop(0)
    oDeck = oDeck - 1
    oHand.append(drawnCard)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    pygame.time.wait(5000)

    xHand = 100
    yHand = 240
    xCard = 480
    yCard = 40
    cursorx = -100
    cursory = -100
    
    # Music begins
    pygame.mixer.music.load('downtime.mp3')
    pygame.mixer.music.play(-1, 0.0)
    updateText1 = "Choose a card to play."
    updateText2 = ""
    updateText3=""
    updateText4=""
    print("End of the intro")
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pcardChoice = selectCard(board, textbox, xCard, yCard, oHand, pHand, xHand, yHand, cursorx, cursory, drawnCard, pDeckInPlay, oDeckInPlay)
    getPlayCard(pcardChoice, oHand, pHand, board, textbox, xCard, yCard, xHand, yHand, cursorx, cursory, pgoldScore, ogoldScore, pDeck, oDeck, pDeckInPlay, oDeckInPlay, updateText1, updateText2, updateText3, updateText4, drawnCard)


####---------------------GAMEPLAY LOOP STARTS HERE ----------------------------####
#### we play until either player has no more cards to draw
    
def getNextTurn(board, updateText1, updateText2, updateText3, updateText4, textbox, pgoldScore, pDeck, oDeck, ogoldScore, pHand, oHand, pDeckInPlay, oDeckInPlay):
    print("getNextTurn begins")

    xHand = 100
    yHand = 240
    xCard = 480
    yCard = 40
    cursorx = -100
    cursory = -100
            
    if pDeck <= 0:
        print("There are no cards left to draw!!")
        updateText1 = "You have no more cards"
        updateText2 = "left to draw!"
        updateText3 = ""
        updateText4 = ""
        drawnCard = 0
    elif pDeck > 0:
        drawnCard = pDeckInPlay.pop(0)
        pDeck = pDeck - 1
        pHand.append(drawnCard)
        i1 = "New turn! You draw a card!"
        i2 = drawnCard.cname
        i3 = "Power:", drawnCard.cpower
        i4 = drawnCard.ctype
        updateText1 = str(i1)
        updateText2 = str(i2)
        updateText3 = str(i3)
        updateText4 = str(i4)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)

    if oDeck <= 0:
        print("They have no more cards left to draw!!")
        updateText1 = "Your opponent is out of"
        updateText2 = "cards to draw!"
        updateText3 = ""
        updateText4 = ""
    elif oDeck > 0:    
        updateText1 = "Your opponent draws a card as well...."
        updateText2=""
        updateText3=""
        updateText4=""
        drawnCard = oDeckInPlay.pop(0)
        oDeck = oDeck - 1
        oHand.append(drawnCard)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)

    if len(pHand) < 1:
        print("There are no more cards left to play!")
        getEndGame(oHand, pHand, board, textbox, xCard, yCard, xHand, yHand, cursorx, cursory, pgoldScore, ogoldScore, pDeck, oDeck, pDeckInPlay, oDeckInPlay, updateText1, updateText2, updateText3, updateText4, drawnCard)
    elif len(oHand) < 1:
        print("There are no more cards left to play!")
        getEndGame(oHand, pHand, board, textbox, xCard, yCard, xHand, yHand, cursorx, cursory, pgoldScore, ogoldScore, pDeck, oDeck, pDeckInPlay, oDeckInPlay, updateText1, updateText2, updateText3, updateText4, drawnCard)
    else:
        updateText1 = "Now choose a card to play"
        updateText2 = ""
        updateText3=""
        updateText4=""
        print("'get next turn' ends... start choosing a card again")
        drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
        drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
        pcardChoice = selectCard(board, textbox, xCard, yCard, oHand, pHand, xHand, yHand, cursorx, cursory, drawnCard, pDeckInPlay, oDeckInPlay)
        getPlayCard(pcardChoice, oHand, pHand, board, textbox, xCard, yCard, xHand, yHand, cursorx, cursory, pgoldScore, ogoldScore, pDeck, oDeck, pDeckInPlay, oDeckInPlay, updateText1, updateText2, updateText3, updateText4, drawnCard)


#### -------------------- PLAYING A CARD -------------------------------####
    
def getPlayCard(pcardChoice, oHand, pHand, board, textbox, xCard, yCard, xHand, yHand, cursorx, cursory, pgoldScore, ogoldScore, pDeck, oDeck, pDeckInPlay, oDeckInPlay, updateText1, updateText2, updateText3, updateText4, drawnCard):
    print("Playing a card turn works")
    print("getPlayCard: You have chosen card #", pcardChoice, "from your hand")
    
    pacqGold = 0
    oacqGold = 0

    # 1 for player victory, 2 for draw, 3 for opponent victory
    victoryType = 0

# here we process the card's vs. stats. The card with the higher number wins the difference in gold    
# compare strength with this if statement

# your opponent selects a random card    
    ocardChoice = randrange(len(oHand))
    patkPwr = pHand[pcardChoice].cpower
    oatkPwr = oHand[ocardChoice].cpower
    print("opponent picks", oHand[ocardChoice].cname)
    print("you picked", pHand[pcardChoice].cname, pHand[pcardChoice].ctype, pHand[pcardChoice].cpower)
    
    i1 = "Your opponent plays"
    i2 = oHand[ocardChoice].cname, oHand[ocardChoice].ctype, oHand[ocardChoice].cpower
    i3 = "Against your"
    i4 = pHand[pcardChoice].cname, pHand[pcardChoice].ctype, pHand[pcardChoice].cpower
    updateText1 = str(i1)
    updateText2 = str(i2)
    updateText3 = str(i3)
    updateText4 = str(i4)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)

    
# IF PLAYER WINS
    if patkPwr > oatkPwr:
        updateText1 = "You win this turn!"
        updateText2 = ''
        updateText3= ''
        updateText4=''
        drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
        drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
        pygame.time.wait(2000)
        victoryType = 1

# IF DRAW
    elif patkPwr == oatkPwr:
        print("It's a draw!!")
        updateText1 = "It's a draw!"
        updateText2 = ""
        updateText3 = ""
        updateText4 = ""
        drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
        drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
        pygame.time.wait(2000)
        victoryType = 2
        
# IF OPPONENT WINS
    elif oatkPwr > patkPwr:
        updateText1 = "Your opponent wins this turn..."
        updateText2 = ''
        updateText3= ''
        updateText4=''
        drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
        drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
        pygame.time.wait(2000)
        victoryType = 3

    if victoryType == 1:
        print("victoryType:", victoryType)
        if pHand[pcardChoice].ctype == "WHITE":
            pacqGold = patkPwr - oatkPwr
            i1 = "You win"
            i2 = patkPwr
            i3 = "minus"
            i4 = oatkPwr
            updateText1 = str(i1)
            updateText2 = str(i2)
            updateText3 = str(i3)
            updateText4 = str(i4)
            effect = pygame.mixer.Sound('plusGold.wav')
            effect.play(pacqGold)
            
        elif pHand[pcardChoice].ctype == "GOLD":
            pacqGold = patkPwr
            i1 = "You win"
            i2 = patkPwr
            i3 = "this turn."
            i4 = ''
            updateText1 = str(i1)
            updateText2 = str(i2)
            updateText3 = str(i3)
            updateText4 = str(i4)
            effect = pygame.mixer.Sound('plusGold.wav')
            effect.play(pacqGold)
            
    elif victoryType == 2:
        print("victoryType:", victoryType)
        if pHand[pcardChoice].ctype and oHand[ocardChoice].ctype == "GOLD":
            pacqGold = patkPwr
            oacqGold = oatkPwr
            i1 = "You both played a gold card"
            i2 = "on a tie, so you still earn"
            i3 = "gold this turn."
            i4 = ''
            updateText1 = str(i1)
            updateText2 = str(i2)
            updateText3 = str(i3)
            updateText4 = str(i4)
            effect = pygame.mixer.Sound('plusGold.wav')
            effect.play(pacqGold)
        elif pHand[pcardChoice].ctype == "GOLD":
            pacqGold = patkPwr
            i1 = "You played a gold card on a tie, "
            i2 = 'so you still earn'
            i3 = pacqGold
            i4 = 'gold'
            updateText1 = str(i1)
            updateText2 = str(i2)
            updateText3 = str(i3)
            updateText4 = str(i4)
        elif oHand[ocardChoice].ctype == "GOLD":
            oacqGold = oatkPwr
            i1 = "Your opponent played a gold card on a  "
            i2 = 'tie, so they still earn'
            i3 = oacqGold
            i4 = 'gold'
            updateText1 = str(i1)
            updateText2 = str(i2)
            updateText3 = str(i3)
            updateText4 = str(i4)
        else:
            i1 = "No gold was earned this turn"
            i2 = ''
            i3 = ''
            i4 = ''
            updateText1 = str(i1)
            updateText2 = str(i2)
            updateText3 = str(i3)
            updateText4 = str(i4)
    elif victoryType == 3:
        print("victoryType:", victoryType)
        if oHand[ocardChoice].ctype == "WHITE":
            oacqGold = oatkPwr - patkPwr
            i1 = "They win"
            i2 = oatkPwr
            i3 = "minus"
            i4 = patkPwr
            updateText1 = str(i1)
            updateText2 = str(i2)
            updateText3 = str(i3)
            updateText4 = str(i4)
            effect = pygame.mixer.Sound('plusGold.wav')
            effect.play(oacqGold)
            
        elif oHand[ocardChoice].ctype == "GOLD":
            oacqGold = oatkPwr
            i1 = "They win"
            i2 = oacqGold
            i3 = "this turn."
            i4 = ''
            updateText1 = str(i1)
            updateText2 = str(i2)
            updateText3 = str(i3)
            updateText4 = str(i4)
            effect = pygame.mixer.Sound('plusGold.wav')
            effect.play(oacqGold)

    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)
# delete the card from play
    pHand.pop(pcardChoice)
    oHand.pop(ocardChoice)
    pgoldScore += pacqGold
    ogoldScore += oacqGold
    print("Cards deleted from hand succesfully")
    updateText1 = "Next Turn!"
    updateText2 = ""
    updateText3 = ""
    updateText4 = ""
    print("Cards have been compared succesfully")
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)
    getNextTurn(board, updateText1, updateText2, updateText3, updateText4, textbox, pgoldScore, pDeck, oDeck, ogoldScore, pHand, oHand, pDeckInPlay, oDeckInPlay)    

#### -------------------- GAMEPLAY LOOP ENDS ---------------------------####

def getEndGame(oHand, pHand, board, textbox, xCard, yCard, xHand, yHand, cursorx, cursory, pgoldScore, ogoldScore, pDeck, oDeck, pDeckInPlay, oDeckInPlay, updateText1, updateText2, updateText3, updateText4, drawnCard):
    updateText1 = "The game has ended!"
    updateText2 = ""
    updateText3 = ""
    updateText4 = ""
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)

    if pgoldScore > ogoldScore:
        i1 = "You win! Your final score:"
        i2 = pgoldScore
        i3 = "Your opponent's final score:"
        i4 = ogoldScore
        updateText1 = str(i1)
        updateText2 = str(i2)
        updateText3 = str(i3)
        updateText4 = str(i4)
    elif ogoldScore > pgoldScore:
        i1 = "You lost! Your final score:"
        i2 = pgoldScore
        i3 = "Your opponent's final score:"
        i4 = ogoldScore
        updateText1 = str(i1)
        updateText2 = str(i2)
        updateText3 = str(i3)
        updateText4 = str(i4)
    elif ogoldScore == pgoldScore:
        i1 = "It was a draw! Your final score:"
        i2 = pgoldScore
        i3 = "Your opponent's final score:"
        i4 = ogoldScore
        updateText1 = str(i1)
        updateText2 = str(i2)
        updateText3 = str(i3)
        updateText4 = str(i4)
    drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
    drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4)
    pygame.time.wait(2000)
        
#### -------------------- DRAWING THE BOARDS -------------------------- ####    

def getBlankBoard():
    board = []
    print("Get blank board works")
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
    return board

def getTextBox():
    textbox = []
    print("Get txtbox works")
    for i in range(TEXTWIDTH):
        textbox.append([BLANK] * TEXTHEIGHT)
    return textbox

#### UPDATE THE TEXTBOX AND GAME STATUS HERE ####
def drawStatus(pgoldScore, ogoldScore, pDeck, updateText1, updateText2, updateText3, updateText4):
# Player stats
    scoreSurf = BASICFONT.render('P1: %s' % pgoldScore, True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 100, 360)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    scoreSurf2 = BASICFONT.render('P2: %s' % ogoldScore, True, TEXTCOLOR)
    scoreRect2 = scoreSurf.get_rect()
    scoreRect2.topleft = (WINDOWWIDTH - 100, 380)
    DISPLAYSURF.blit(scoreSurf2, scoreRect2)

# draw the text box
# line 1
    textSurf1 = BASICFONT.render(updateText1, True, TEXTCOLOR)
    textRect1 = textSurf1.get_rect()
    textRect1.topleft = (WINDOWWIDTH - 510, 365)
#line 2
    textSurf2 = BASICFONT.render(updateText2, True, TEXTCOLOR)
    textRect2 = textSurf2.get_rect()
    textRect2.topleft = (WINDOWWIDTH - 510, 390)
# line 3
    textSurf3 = BASICFONT.render(updateText3, True, TEXTCOLOR)
    textRect3 = textSurf3.get_rect()
    textRect3.topleft = (WINDOWWIDTH - 510, 415)
# line 4
    textSurf4 = BASICFONT.render(updateText4, True, TEXTCOLOR)
    textRect4 = textSurf4.get_rect()
    textRect4.topleft = (WINDOWWIDTH - 510, 440)

# display 4 lines of text
    DISPLAYSURF.blit(textSurf1, textRect1)
    DISPLAYSURF.blit(textSurf2, textRect2)
    DISPLAYSURF.blit(textSurf3, textRect3)
    DISPLAYSURF.blit(textSurf4, textRect4)
    pygame.display.update()

#### TURN TEXT INTO OBJECT   
def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()
    
def drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory):
    GAMEDISPLAY.fill(pygame.Color("BLACK"))
    # draws a border around the board
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 6)

    # fills the bg in
    pygame.draw.rect(DISPLAYSURF, TOPBOXCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))

    # draws a border around text box
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (txtXMARGIN - 3, txtTOPMARGIN - 7, (TEXTWIDTH * BOXSIZE) + 6, (TEXTHEIGHT * BOXSIZE) + 8), 6)

    # fills the bg in
    pygame.draw.rect(DISPLAYSURF, TEXTBOXCOLOR, (txtXMARGIN, txtTOPMARGIN, BOXSIZE * TEXTWIDTH, BOXSIZE * TEXTHEIGHT))

    # draws player hand on field
    x = 0
    while x < len(pHand):
        GAMEDISPLAY.blit(cardfront[pHand[x].cindex], (xHand, yHand))
        x += 1
        xHand += 80
        
    # draws opponent's hand on field
    for card in oHand:
        GAMEDISPLAY.blit(cardback, (xCard, yCard))
        xCard -= 80

    #draws the cursor
        GAMEDISPLAY.blit(cursorGfx, (cursorx, cursory))
        pygame.display.flip()

# update screen
    pygame.display.flip()

def selectCard(board, textbox, xCard, yCard, oHand, pHand, xHand, yHand, cursorx, cursory, drawnCard, pDeckInPlay, oDeckInPlay):
# set cursor locations
    cursorx = 100
    cursory = 240
    pcardChoice = 0

    mode = 0

    # mode that declares a card choice when == 1
    selected = 0
    
    GAMEDISPLAY.blit(cursorGfx, (cursorx, cursory))
    pygame.display.flip()

# KEYBOARD FUNCTIONS
# determine if an arrow key is pressed
# cycle through cards on hand

    while selected == 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if pcardChoice > 0:
                        mode = 'cursorLeft'
                    else:
                        mode = 'noMove'
                elif event.key == pygame.K_d:
                    if pcardChoice < len(pHand) - 1:
                        mode = 'cursorRight'
                    else:
                        mode = 'noMove'
                elif event.key == pygame.K_SPACE:
                    mode = 'selected'
            
                if mode == 'cursorLeft':
                        effect = pygame.mixer.Sound('sound\cursor.wav')
                        effect.play()
                        cursorx -= 80
                        pcardChoice -= 1
                        print("selection:", pcardChoice)
                        drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
                elif mode == 'cursorRight':
                        effect = pygame.mixer.Sound('sound\cursor.wav')
                        effect.play()
                        cursorx += 80
                        pcardChoice += 1
                        print("selection:", pcardChoice)
                        drawBoard(board, textbox, xCard, yCard, oHand, pHand, drawnCard, xHand, yHand, cursorx, cursory)
                elif mode == 'noMove':
                        effect = pygame.mixer.Sound('sound\cursor.wav')
                        effect.play()
                elif mode == 'selected':
                        print("selectCard: You have chosen card #", pcardChoice, "from your hand")
                        return(pcardChoice)
    
# update screen
    pygame.display.flip()
    
if __name__ == '__main__':
        main()
