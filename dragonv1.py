import random

class DragonCasino:
    def __init__(self):
        self.player_balance = 1000
        self.dragon_names = ['Firestorm', 'Nightshade', 'Thunderclap', 'Shadowfing']

    def display_menu(self):
        print("\nDragon Casino")
        print("1. Bet On A Dragon Race")
        print("2. Check Balance")
        print("3. Quit")

    def bet_on_race(self):
        print("\nDragon Race Betting")
        print("Available Dragons:")
        for i, dragon in enumerate(self.dragon_names):
            print(f"{i+1}. {dragon}")

        selected_dragon = int(input("Choose the dragon you want to bet on (1-4): "))
        bet_amount = int(input("Enter your bet amount: "))

        if bet_amount > self.player_balance:
            print("Insufficient Balance!")
            return
        
        winning_dragon = random.choice(self.dragon_names)
        print(f"The race is over! {winning_dragon} won!")

        if selected_dragon == self.dragon_names.index(winning_dragon) + 1:
            winnings = bet_amount * 2
            print(f"Congratulations! You won {winnings}!")
            self.player_balance += winnings
        else:
            print("Better luck next time!")
            self.player_balance -= bet_amount
         
    def check_balance(self):
        print(f"Your current balance: {self.player_balance}")

    def play(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.bet_on_race()
            elif choice == '2':
                self.check_balance()
            elif choice == '3':
                print("Thanks for playing at Dragon Casino!")
                break
            else:
                print("Invalid choice! Please try again.")

# Main program
if __name__ == "__main__":
    casino = DragonCasino()
    casino.play()
