from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")


class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using PayPal.")


class BitcoinPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Bitcoin.")


class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


print("=== Payment Processing System ===")

processor = PaymentProcessor(CreditCardPayment())
processor.process_payment(500)

processor.set_strategy(PayPalPayment())
processor.process_payment(1000)

processor.set_strategy(BitcoinPayment())
processor.process_payment(1500)
