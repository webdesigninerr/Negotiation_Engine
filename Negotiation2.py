import random

class NegotiationEngine:
    def __init__(self, buyer_name, seller_name, initial_price):
        self.buyer_name = buyer_name
        self.seller_name = seller_name
        self.initial_price = initial_price

    def start_negotiation(self):
        print(f"Negotiation between {self.buyer_name} and {self.seller_name} started.")
        print(f"Initial price set by {self.seller_name}: ${self.initial_price}")

        buyer_offer = self.initial_price
        seller_offer = self.initial_price

        while True:
            buyer_offer = float(input(f"{self.buyer_name}, make an offer: Rs"))
            if buyer_offer <= 0:
                print("Invalid offer. Please enter a positive amount.")
                continue

            # Simulate seller's response using AI-generated offer
            seller_offer = self.generate_seller_offer(buyer_offer)
            print(f"{self.seller_name}'s counter offer: Rs{seller_offer}")

            if buyer_offer >= seller_offer:
                print(f"Congratulations! {self.buyer_name} and {self.seller_name} have reached an agreement.")
                print(f"Final price: Rs{buyer_offer}")
                break
            else:
                print(f"{self.seller_name} declines. Counteroffer needed.")

        print("Negotiation ended.")

    def generate_seller_offer(self, buyer_offer):
        # Simple AI to generate seller's offer (can be replaced with more complex logic)
        # For simplicity, let's just generate a random offer within a range of 80% to 120% of the buyer's offer
        min_offer = buyer_offer * 0.8
        max_offer = buyer_offer * 1.2
        return round(random.uniform(min_offer, max_offer), 2)


if __name__ == "__main__":
    buyer_name = input("Enter the buyer's name: ")
    seller_name = input("Enter the seller's name: ")
    initial_price = float(input("Enter the initial price set by the seller: Rs"))

    negotiation_engine = NegotiationEngine(buyer_name, seller_name, initial_price)
    negotiation_engine.start_negotiation()