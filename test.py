class Car():
    def __init__(self,material,proizvoditel,crush):
        self.set_data(material,proizvoditel,crush)
        self.get_status_work()


    def set_data(self,material,proizvoditel,crush):
        if crush<0:
            raise ValueError("ошибка ввода crush их кол-во не может быть отрицательным!!!")
        self.materia=material
        self.proizvoditel=proizvoditel
        self.crush=crush

    def get_status_work(self):
        if self.crush>0:
            self.status_work=False
        else:
            self.status_work=True
        return self.status_work

def main():
    car1 = Car(material="Сталь", proizvoditel="BMW", crush=0)
    car2 = Car(material="Сталь", proizvoditel="toyota", crush=4)


    print(f"статус машины {car1.proizvoditel} равен {car1.status_work}")
    print(f"статус машины {car2.proizvoditel} равен {car2.status_work}")

if __name__ == "__main__":
    main()

