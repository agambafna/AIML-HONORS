from abc import ABC, abstractmethod
from payment import RazorpayFactory, StripeFactory


class Aggregator(ABC):

    def __init__(self, name, processing_fee):
        self.name = name
        self.processing_fee = processing_fee

    @abstractmethod
    def get_payment_factory(self):
        pass

    def call_get_payment_object(self, method_type, amount, **kwargs):
        f = self.get_payment_factory()
        p = f.get_payment_object(method_type, **kwargs)

        print("\nPayment Info:", p.get_details())

        fee = amount * self.processing_fee
        total = amount + fee

        print(f"Amount:     Rs.{amount:.2f}")
        print(f"Fee:        Rs.{fee:.2f}")
        print(f"Total:      Rs.{total:.2f}")

        return p.pay(total)


class RazorpayAggregator(Aggregator):

    def __init__(self):
        super().__init__("Razorpay", 0.02)

    def get_payment_factory(self):
        return RazorpayFactory


class StripeAggregator(Aggregator):

    def __init__(self):
        super().__init__("Stripe", 0.029)

    def get_payment_factory(self):
        return StripeFactory


class AggregatorFactory:

    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator
    }

    @classmethod
    def register_aggregator(cls, name, agg_class):
        cls.factory[name.lower()] = agg_class

    @classmethod
    def get_aggregator_object(cls, aggregator_name):
        key = aggregator_name.lower()
        if key not in cls.factory:
            raise ValueError("Invalid aggregator!")
        return cls.factory[key]()
