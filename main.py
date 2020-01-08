#!/usr/bin/python3

import random


class Card:
    """Simple deck card instance, 
    number is 1 to 13 ( 13 being the king)
    kind is Heards, Spades, Diamonds, Clubs """
    kinds = {1: 'Heart', 2: 'Spade', 3: 'Diamond', 4: 'Club'}
    numbers = {13: 'Ace', 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 'Jack', 11: 'Queen', 12: 'King'}

    def __init__(self, number, kind):
        if number in self.numbers:
            self.number = number
        else:
            print("choice not in available choices. ")

        if kind in self.kinds:
            self.kind = kind
        else:
            print("Choices not in available choices. ")


    def display(self):
        kind = self.kinds.get(self.kind)
        num = self.numbers.get(self.number)
        # print("display")
        print(" %s of %s" %(num, kind))

    def get_kind(self, ):
        kind = self.kinds.get(self.kind)
        return kind

    def get_number(self, ):
        number = self.numbers.get(self.number)
        return number

class CardDeck:
    """Contains 54 cards to have a complete Card Deck. """
    # cards = []

    def __init__(self, ):
        self.cards = []



    def add_card(self, card):
        self.cards.append(card)
        print("Card added to deck succesfully")

    def shuffle(self):
        random.shuffle(self.cards)


    def standard_init(self):
        """Make a standard deck of card without the jockers."""
        for num in range(13):
            # print(num)
            for kind in range(4):
                # print(kind)
                self.cards.append(Card(num+1, kind+1))

class CardGame:
    """docstring for CardGame"""
    def __init__(self, card_deck, player1, player2):

        self.card_deck = card_deck
        self.player1 = player1
        self.player2 = player2

    def init_deal(self):
        """This will make the initialise deal and split the cards through players."""
        k = 0
        for card in self.card_deck.cards:
            if (k % 2) == 0:
                self.player1.cards.append(card)
            else:
                self.player2.cards.append(card)
            k += 1

        print("Init deal completed")

    def show_details(self, temp_card_p1, temp_card_p2):
        print("length player1 now :", len(self.player1.cards))
        print("temp player1 now :", len(temp_card_p1))
        print("length player2 now :", len(self.player2.cards))
        print("temp player2 now :", len(temp_card_p2))

    def play(self):
        print("Starting the game, player1 is %s, player2 is %s." %(self.player1.name, self.player2.name))
        temp_card_p1 = []
        temp_card_p2 = []
        temp_draw = []

        round_no = 0
        while True:
            battle_list = []

            print("Round #%s, %s has %s cards, %s has %s cards." %(round_no+1, self.player1.name, len(self.player1.cards), self.player2.name, len(self.player2.cards)))
            
            
            # self.show_details(temp_card_p1, temp_card_p2)

            random.shuffle(self.player1.cards)
            random.shuffle(self.player2.cards)

            if len(self.player1.cards) == len(self.player2.cards):
                battle_list = zip(self.player1.cards, self.player2.cards)
                self.player1.cards = []
                self.player2.cards = [] 
            
            elif len(self.player1.cards) > len(self.player2.cards):
                battle_list = zip(self.player1.cards[0:len(self.player2.cards)], self.player2.cards)
                self.player1.cards = self.player1.cards[len(self.player2.cards):]
                self.player2.cards = []

            elif len(self.player1.cards) < len(self.player2.cards):
                battle_list = zip(self.player1.cards, self.player2.cards[0:len(self.player1.cards)])
                self.player2.cards = self.player2.cards[len(self.player1.cards):]
                self.player1.cards = []


            for card_p1, card_p2 in battle_list:


                # print("card_p1: ", card_p1)
                # print("card_p2: ", card_p2)

                # card_p1.display()
                print("%s has %s of %s" %(self.player1.name, card_p1.get_number(), card_p1.get_kind()))
                print("%s has %s of %s" %(self.player2.name, card_p2.get_number(), card_p2.get_kind()))
                # card_p2.display()

                if card_p1.number > card_p2.number:
                    print("%s wins! " %(self.player1.name))
                    temp_card_p1.append(card_p1)
                    temp_card_p1.append(card_p2)
                    if len(temp_draw) > 0:
                        temp_card_p1.extend(temp_draw)
                        temp_draw = []
                    # self.show_details(temp_card_p1, temp_card_p2)

                elif card_p1.number < card_p2.number:
                    print("%s wins! " %(self.player2.name))
                    temp_card_p2.append(card_p1)
                    temp_card_p2.append(card_p2)
                    if len(temp_draw) > 0:
                        temp_card_p2.extend(temp_draw)
                        temp_draw = []
                    # self.show_details(temp_card_p1, temp_card_p2)


                else:
                    print("Draw, keep going.")
                    
                    temp_draw.append(card_p1)
                    temp_draw.append(card_p2)
                # data = input("")

            self.player1.cards.extend(temp_card_p1)
            self.player2.cards.extend(temp_card_p2)
            temp_card_p1 = []
            temp_card_p2 = []

            if (len(self.player1.cards) + len(temp_card_p1)) == 0:
                print("%s wins the game!!!" %self.player2.name)
                break
            if (len(self.player2.cards) + len(temp_card_p2)) == 0:
                print("%s wins the game!!!" %self.player1.name)
                break

            round_no += 1








class Player:
    """docstring for Player"""
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.used_cards = []


if __name__ == "__main__":

    deck = CardDeck()
    deck.standard_init()
    deck.shuffle()
    player1 = Player("Francis")
    player2 = Player("Ethan")
    game = CardGame(deck, player1, player2)
    game.init_deal()
    game.play()