from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of {amount}...")

class PayPalPayment(Payment):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of {amount}...")

class StripePayment(Payment):
    def process_payment(self, amount: float) -> None:
        print(f"Processing Stripe payment of {amount}...")

def main():
    credit_card = CreditCardPayment()
    