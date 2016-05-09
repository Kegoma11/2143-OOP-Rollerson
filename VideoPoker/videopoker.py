"""Keona Rollerson"""
import os
import random   
import time

class Card(object):

    """A card object with a suit and rank."""
    ranks = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    suits = ('Spades','Diamonds','Hearts','Clubs')

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        return ("(suit: %s, rank: %s)") % (self.suit,self.rank)

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        #shuffle the deck
        random.shuffle(self.cards)

    def deal(self):
        if len(self) == 0:
            return None
        else:
            #returns top card
            return self.cards.pop()

    def __len__(self):
        #return num of cards in deck
        return len(self.cards)

    def sort(self):
        random.shuffle(self.cards)

    def __str__(self):
        result = []
        for c in  self.cards:
            result.append(str(c))
        return "".join(result)

class Hand(object):
    def __init__(self, deck):
        if(len(deck) < 5):
            print ("Not enough cards in deck!")
        self.cards = []
        for i in range (5):
            card = deck.deal()
            self.cards.append(card)
        self.rank = [0] * 14
        self.suit = [0] * 4
        self.process()

    def __str__(self):
        result = []
        for card in self.cards:
            result.append(str(card))
        return "".join(result)

    def sortHand(self):
        self.cards = sorted(self.cards)

    def process(self):
        for card in self.cards:
            rank = card.getRank()
            rankIndex = Card.RANKS.index(rank)
            self._myranks[rankIndex] += 1
            suit = card.getSuit()
            suitIndex = Card.SUITS.index(suit)
            self._mysuits[suitIndex] += 1
        return self._myranks[rankIndex]

class VideoPoker(object):
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
        
    #def deal(self, num =5):
     #   self.deck.shuffle()
      # for i in range(0,num):
       #     self.hand.add(self.deal.pop())
        #print(self.hand)
        #return self.hand

    def checkHand(self):
        if royalFlush():
            return 800
        if fourAcesOrEights():
            return 80
        if straightFlush():
            return 50
        if fourSevens():
            return 50
        if fourOfAKind():
            return 25
        if fullHouse():
            return 8
        if flush():
            return 5
        if straight():
            return 4
        if threeOfAKind():
            return 3
        if twoPair():
            return 2
        if pair():
            return 1

        return 0

class game_driver(VideoPoker):
    def __init__(self):
        
        self.totalScore = 0

    def menu(self):
        print("1.New Game")
        print("2.Play Again")
        print("3.Quit")
        return input('')

    def resethand(self):
        self.hand = Hand()

    def resetDeck(self):
        self.deck = Deck()

    def calculate(self):
        playerScore = self.checkHand()
        print ("Earned: ", playerScore)
        self.totalScore += playerScore
        print ("Your total score is: ", self.totalScore, '\n')

    def print(self):
        for card in self.hand.cards:
            print(str(card))

    def loop(self):
        user = int(self.menu())
        if user == 1:
            print("Starting new game")
            self.resetDeck()
            self.totalScore = 0
        elif user == 3:
            print("Game Over")
            return False
            
        if user == 1 or user == 2:
            if len(self.deck.cards) < 5:
                print("\nNot enough cards!")
                print("Total score is: ",self.totalScore)
                print("Starting game")
                self.totalScore =0
                self.resetDeck()
                return True
            self.resethand()
            self.print()

            user = input("Enter position of card(s) wanting to be removed,1-5(seperate with comma)")
            if not user is '':
                user = user.split(",")
                for index in user:
                    cardreplace = self.deck.pop()
                    self.hand.replace(int(index)-1,cardreplace)

            print("\nNew Hand: ")
            self.print()
            self.calculate()
            return True
    
    def Start(self):
        loop = True
        while loop:
            loop = self.loop()
g = game_driver()
g.menu()
