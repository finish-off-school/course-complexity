import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        ranks = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        ]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.won_cards = []

    def draw_card(self, deck):
        self.hand.append(deck.deal_card())

    def play_card(self):
        if len(self.hand) == 0:
            self.hand, self.won_cards = self.won_cards, self.hand
        return self.hand.pop(0)

    def add_cards(self, cards):
        self.won_cards.extend(cards)

    def has_cards(self):
        return len(self.hand) > 0 or len(self.won_cards) > 0


class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.opponent = Player("Opponent")
        self.deck = Deck()

    def distribute_cards(self):
        while len(self.deck.cards) > 0:
            self.player.draw_card(self.deck)
            self.opponent.draw_card(self.deck)

    def compare_cards(self, card1, card2):
        ranks = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        return ranks.index(card1.rank) - ranks.index(card2.rank)

    def play_round(self):
        player_card = self.player.play_card()
        opponent_card = self.opponent.play_card()
        print(f"{self.player.name} plays: {player_card}")
        print(f"{self.opponent.name} plays: {opponent_card}")
        comparison = self.compare_cards(player_card, opponent_card)

        if comparison > 0:
            self.player.add_cards([player_card, opponent_card])
            print(f"{self.player.name} wins the round!")
        elif comparison < 0:
            self.opponent.add_cards([player_card, opponent_card])
            print(f"{self.opponent.name} wins the round!")
        else:
            print("*************It's a draw! Playing again...**************")

            token = [player_card, opponent_card]
            # i have problem to write clean code in this part give me ur feedback
            while self.player.has_cards() and self.opponent.has_cards():
                token.extend([self.player.play_card(), self.opponent.play_card()])

                if not self.player.has_cards():
                    self.opponent.add_cards(token)
                    print(f"{self.opponent.name} wins the round!")
                    break

                if not self.opponent.has_cards():
                    self.player.add_cards(token)
                    print(f"{self.player.name} wins the round!")
                    break

                player_card = self.player.play_card()
                opponent_card = self.opponent.play_card()
                token.extend([player_card, opponent_card])
                comparison = self.compare_cards(player_card, opponent_card)

                if comparison > 0:
                    self.player.add_cards(token)
                    print(f"{self.player.name} wins the round!")
                    break
                elif comparison < 0:
                    self.opponent.add_cards(token)
                    print(f"{self.opponent.name} wins the round!")
                    break

    def play_game(self):
        self.distribute_cards()
        while self.player.has_cards() and self.opponent.has_cards():
            self.play_round()

        print(f"\nGame over!")
        if len(self.player.won_cards) > len(self.opponent.won_cards):
            print(f"{self.player.name} wins with {len(self.player.won_cards)} cards!")
        elif len(self.player.won_cards) < len(self.opponent.won_cards):
            print(
                f"{self.opponent.name} wins with {len(self.opponent.won_cards)} cards!"
            )
        else:
            print("It's a tie!")


if __name__ == "__main__":
    game = Game("Anis")
    game.play_game()
