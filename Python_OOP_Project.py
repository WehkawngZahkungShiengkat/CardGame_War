#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random

# Two useful variables for creating Cards.
#SUITE = 'H D S C'.split()
#RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    WholeDesk = []
    def __init__(self,SUITE = 'H D S C',RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'):
        self.SUITE = SUITE.split()
        self.RANKS = RANKS.split()

    def createDesk(self):
        for r in self.RANKS:
            for s in self.SUITE:
                self.WholeDesk.append((s,r))
        #print("frist created desk: ",self.WholeDesk)

    def shuffleDesk(self):
        random.shuffle(self.WholeDesk)
        #print("shuffled desk: ",self.WholeDesk)
        print("\nThe New deck has shuffled! Let's Start the game!!!\n")
        return self.WholeDesk

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def winHand1(self,in1,in2,betL):
        a,b = in1
        c,d = in2
        pp = []
        pcp = []
        Rnk = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
        for r in Rnk:
            if b == r and d == r:
                betL.append(in1)
                betL.append(in2)
                break
            elif b == r:
                pp = [in1,in2]
                break
            elif d == r:
                pcp = [in1,in2]
                break

        return pp,pcp,betL

    def winHand2(self,in1,in2,betL):
        a,b = in1
        c,d = in2
        pp = []
        pcp = []
        Rnk =["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
        for r in Rnk:
            if b == r and d == r:
                for hdsc in ["H","D","S","C"]:
                    if a == hdsc:
                        pp = [in1,in2] + betL
                        break
                    elif c == hdsc:
                        pcp = [in1,in2] + betL
                        break
            elif b == r:
                pp = [in1,in2] + betL
                break
            elif d == r:
                pcp = [in1,in2] + betL
                break

        return pp,pcp

    def addIn(self,wlin,lsall):
        putattop = [wlin.pop(0)]
        newLs = wlin + lsall + putattop
        return newLs

class Players(Deck):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self,PlayerN = "P1",ComputerN = "PC"):
        self.PlayerN = PlayerN
        self.ComputerN = ComputerN

    def set_Pname(self,Pname):
        self.PlayerN = Pname
        return self.PlayerN

    def checkcards(self,pn,cardsIn):
        print("Currently, {} has total of {} cards left.".format(pn,len(cardsIn)))



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")


Gcards = Deck()
Gcards.createDesk()
Gcards.shuffleDesk()
Gplayers = Players()
ply = Gplayers.set_Pname(input("What's your name?\n"))
plyPC = Gplayers.ComputerN
Pcards = Gplayers.WholeDesk[:26]
Ccards = Gplayers.WholeDesk[26:]
countTime = 0
countWar = 0
while (len(Pcards)!=0 and len(Ccards)!=0):
    countTime += 1
    Gplayers.checkcards(ply,Pcards)
    Gplayers.checkcards(plyPC,Ccards)
    playedCards = []
    Ppop = Pcards.pop()
    Cpop = Ccards.pop()
    print("\nFace up card of {} is {}".format(ply,Ppop))
    print("Face up card of {} is {}\n".format(plyPC,Cpop))
    phand = Hand()
    ptoadd,ctoadd,playedCards = phand.winHand1(Ppop,Cpop,playedCards)
    if ptoadd != []:
        Pcards=phand.addIn(ptoadd,Pcards)
    elif ctoadd != []:
        Ccards=phand.addIn(ctoadd,Ccards)
    else:
        if (len(Pcards)>3 and len(Ccards)>3):
            countWar += 1
            print("There's a war!!!")
            for addPop in range(3):
                playedCards.append(Pcards.pop())
                playedCards.append(Ccards.pop())
            Ppop = Pcards.pop()
            Cpop = Ccards.pop()
            print("Face up card of {} is {}".format(ply,Ppop))
            print("Face up card of {} is {}\n".format(plyPC,Cpop))
            ptoadd,ctoadd = phand.winHand2(Ppop,Cpop,playedCards)
            if ptoadd != []:
                Pcards=phand.addIn(ptoadd,Pcards)
            else:
                Ccards=phand.addIn(ctoadd,Ccards)

print("{} rounds have been played and {} wars has occured.".format(countTime,countWar))
if len(Pcards)!=0:
    print("\nCongradulation! {} has won!".format(ply))
else:
    print("\nCongradulation! {} has won!".format(plyPC))
# Use the 3 classes along with some logic to play a game of war!
