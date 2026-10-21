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
    pass



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

    new_tx = {
        "type":tx_type,
        "category":category,
        "amount":amount
    }
    data["transactions"].append(new_tx)
    print (f"успешно добавлен: {tx_type} на сумму {amount} руб. в категорию '{category}'!")




def main():
    data=load_data()
    print("=== ДОБРО ПОЖАЛОВАТЬ В МЕНЕДЖЕР ФИНАНСОВ ===")

    while True:
        print("\n1. посмотреть баланс")
        print("2. Добавить операцию")
        print("3. Выход")

        choice = input("выберете действие:")

        if choice=="1":
            print("Вы выбрали баланс (функция в разработке)")
        elif choice =="2":
            add_transactions(data)
            save_data(data)
        elif choice =="3":
            print("До свидания!")
            break
        else:
            print("ввод был совершен не верно введите снова!")




if __name__ == "__main__":
    main()
