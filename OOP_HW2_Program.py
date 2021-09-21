import OOP_HW2_Car as C


def main():
    ye = input('Enter the year of the model: ')
    mo = input('Enter the model: ')
    speed = 0
    car = C.Car(ye, mo, speed)

    print(car.get_make(),car.get_year_model())

    for i in range (0,5):
        car.accelerate()
        print('Your current speed is: ', car.get_speed())

    for n in range (0,5):
        car.brake()
        print('Your current speed is: ', car.get_speed())



main()
