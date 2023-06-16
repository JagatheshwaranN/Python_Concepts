from abc import ABC, abstractmethod


class Payment(ABC):
    def print_invoice(self, amount):
        print("The purchase for", amount, "is done")

    @abstractmethod
    def payment(self, amount):
        pass


class CreditPayment(Payment):
    def payment(self, amount):
        print("The amount", amount, "is done thru Credit Card")


class DebitPayment(Payment):
    def payment(self, amount):
        print("The amount", amount, "is done thru Debit Card")


credit = CreditPayment()
credit.payment(500)
credit.print_invoice(500)

debit = DebitPayment()
debit.payment(1000)
debit.print_invoice(1000)
