from aggregator import AggregatorFactory


def main():
    try:
        gw = input("Gateway (stripe/razorpay): ").strip().lower()
        agg = AggregatorFactory.get_aggregator_object(gw)

        mode = input("Method (card/upi): ").strip().lower()

        if mode == "card":
            num = input("Card number: ").strip()
            opts = {"card_number": num}
        elif mode == "upi":
            uid = input("UPI ID: ").strip()
            opts = {"upi_id": uid}
        else:
            raise ValueError("Invalid payment method")

        amt = float(input("Amount (Rs): "))
        if amt <= 0:
            raise ValueError("Amount must be positive")

        ok = agg.call_get_payment_object(mode, amt, **opts)
        if ok:
            print("\nPayment Successful!")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
