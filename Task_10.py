# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposit: {amount} у.е.")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Недостаточно средств на счете.")
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
                print("Сумма пополнения должна быть кратна 50 у.е.")
                continue
            deposit(amount)
            count += 1
        elif action == "снять":
            amount = int(input("Введите сумму для снятия: "))
            if amount % 50 != 0:
                print("Сумма снятия должна быть кратна 50 у.е.")
                continue
            withdraw(amount)
            count += 1
        elif action == "выйти":
            break
        else:
            print("Неверное действие. Попробуйте еще раз.")
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

atm()
