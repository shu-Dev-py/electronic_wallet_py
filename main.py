from datetime import datetime
import json
import os


def load_data():
    if not os.path.exists("walet.jason"):
        return {"balance":0,"transactions":[],"goals":[]}
    with open("walet.json","r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open("walet.json","w", encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)



def calculate_balance(data):
    total=0
    for tx in data["transactions"]:
        if tx["type"]=="доходы":
            total+=tx["amount"]
        if tx["type"]=="расходы":
            total-=tx["amount"]
    return total



def add_transactions(data):
    print("\n==Добавление транзакции==")
    print("1. доход(заработал)")
    print("2. Расходы(потратил)")
    tx_type_choice=input("выберите тип операции 1/2 :")
    if tx_type_choice == "1":
        tx_type="доходы"
    elif tx_type_choice =="2":
        tx_type="расходы"
    else:
        print("не верный ввод попробуй снова")
        return

    category = input("введите категорию(например: продукты, зарплата,кино): ")

    try:
        amount = float(input("введите сумму транзакции:"))
    except ValueError:
        print("ошибка: сумма должна быть числом!")
        return

    today_str = datetime.today().strftime("%d.%m.%y")
    print(f"операция совершена сегодня{today_str}?")
    print("yes/no")
    date_choice=input("введите y/n:")
    if date_choice=="y":
        tx_date=today_str
    elif date_choice=="n":
        day_input=input("введите день в который была совершена операция:")
        current_month_year=datetime.now().strftime(".%m.%y")

        if len(day_input)==1:
            day_input="o"+day_input

        tx_date=day_input+current_month_year
    else:
        print("неверный выбор ставим сегодняшнюю дату")
        tx_date=today_str

    new_tx = {
        "type":tx_type,
        "category":category,
        "amount":amount,
        "date":tx_date
    }
    data["transactions"].append(new_tx)
    print (f"успешно добавлен: {tx_type} на сумму {amount} руб. в категорию '{category}' выполненная {tx_date} !!!")

def find_most_expensive_day(data):
    daily_expenses = {}

    for tx in data["transactions"]:
        if tx["type"] == "расходы":
            date = tx["date"]
            amount = tx["amount"]

            if date not in daily_expenses:
                daily_expenses[date] = 0
            daily_expenses[date] += amount

    if not daily_expenses:
        return None
    most_expensive_day = max(daily_expenses, key=daily_expenses.get)
    max_amount = daily_expenses[most_expensive_day]
    return most_expensive_day, max_amount



def main():
    data=load_data()
    print("=== ДОБРО ПОЖАЛОВАТЬ В МЕНЕДЖЕР ФИНАНСОВ ===")

    while True:
        print("\n1. посмотреть баланс")
        print("2. Добавить операцию")
        print("3. Выход")
        print("4. Аналитика расходов")

        choice = input("выберете действие:")

        if choice=="1":
            current_balance=calculate_balance(data)
            print(f"текущий баланс равен ={current_balance} руб!")
        elif choice =="2":
            add_transactions(data)
            save_data(data)
        elif choice =="3":
            print("До свидания!")
            break
        elif choice == "4":
            result = find_most_expensive_day(data)

            print("\n=====================================")
            print("         АНАЛИТИКА РАСХОДОВ          ")
            print("=====================================")

            if result is None:
                print("У вас пока нет расходов за этот месяц!")
            else:
                # Распаковываем кортеж, который вернула функция, в две переменные
                best_date, total_spent = result
                print(f" Самый дорогой день: {best_date}")
                print(f" Сумма трат в этот день: {total_spent} руб.")

            print("=====================================")
        else:
            print("ввод был совершен не верно введите снова!")


if __name__ == "__main__":
    main()
