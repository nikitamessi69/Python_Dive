import logging

transactions = []


def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposit: {amount} у.е.")


def withdraw(amount):
    global balance
    if amount > balance:
        logging.error("Недостаточно средств на счете.")
        return
    if balance > 5000000:
        tax = balance * 0.1
        balance -= tax
        transactions.append(f"Tax: {tax} у.е.")
    if amount > 600:
        amount = min(amount, balance)
        fee = max(amount * 0.015, 30)
        balance -= amount + fee
        transactions.append(f"Withdrawal: {amount} у.е. (Fee: {fee} у.е.)")
    else:
        balance -= amount
        transactions.append(f"Withdrawal: {amount} у.е.")


def atm():
    global balance
    balance = 0
    count = 0

    while True:
        action = input("Выберите действие (пополнить, снять, выйти): ")
        if action == "пополнить":
            amount = int(input("Введите сумму для пополнения: "))
            if amount % 50 != 0:
                logging.error("Сумма пополнения должна быть кратна 50 у.е.")
                continue
            deposit(amount)
            count += 1
        elif action == "снять":
            amount = int(input("Введите сумму для снятия: "))
            if amount % 50 != 0:
                logging.error("Сумма снятия должна быть кратна 50 у.е.")
                continue
            withdraw(amount)
            count += 1
        elif action == "выйти":
            break
        else:
            logging.error("Неверное действие. Попробуйте еще раз.")
            continue

        if count % 3 == 0:
            interest = balance * 0.03
            balance += interest
            transactions.append(f"Interest: {interest} у.е.")

        if balance > 5000000:
            tax = balance * 0.1
            balance -= tax
            transactions.append(f"Tax: {tax} у.е.")

        print(f"Текущий баланс: {balance} у.е.")

    print("Операции:")
    for transaction in transactions:
        print(transaction)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Запуск программы для работы с банкоматом."
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    atm()
