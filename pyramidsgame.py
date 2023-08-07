import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        return str(self.value) + self.suit

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for suit in ["♥", "♦", "♣", "♠"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.deal())
        
    def show_hand(self):
        print(self.name + "'s hand:")
        for card in self.hand:
            print(card)
            
    def play_card(self, card):
        self.hand.remove(card)
        
class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.build_pyramid()
        self.current_card = None
        
    def build_pyramid(self):
        self.pyramid = []
        rows = 7
        cols = 7
        for i in range(rows):
            row = []
            for j in range(cols):
                if j >= i:
                    card = self.deck.deal()
                    row.append(card)
                else:
                    row.append(None)
            self.pyramid.append(row)
            
    def print_pyramid(self):
        for row in self.pyramid:
            for card in row:
                if card is None:
                    print("  ", end=" ")
                else:
                    print(card, end=" ")
            print()
        print()
        
    def add_player(self, name):
        self.players.append(Player(name))
        
    def deal_cards(self):
        for player in self.players:
            for i in range(7):
                player.draw(self.deck)
                
    def play_game(self):
        self.deal_cards()
        while True:
            for player in self.players:
                player.show_hand()
                self.print_pyramid()
                print("Current card: ", self.current_card)
                print("It's", player.name + "'s turn.")
                while True:
                    choice = input("Do you want to draw from the deck or take a card from the pyramid? (deck/pyramid): ")
                    if choice == "deck":
                        player.draw(self.deck)
                        break
                    elif choice == "pyramid":
                        row = int(input("Which row? "))
                        col = int(input("Which column? "))
                        if self.pyramid[row][col] is not None:
                            card = self.pyramid[row][col]
                            self.pyramid[row][col] = None
                            player.play_card(card)
                            self.current_card = card
                            break
                        else:
                            print("That card is already taken.")
                    else:
                        print("Invalid choice.")
                if len(player.hand) == 0:
                    print(player.name + " wins!")
                    return
                
game = Game()
game.add_player("Muhammad")
game.add_player("Waseem")
game.play_game()
