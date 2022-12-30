

class Vehicle:
    def vehicle_info(self, marque: str = "BMW", tipe: str = "320D"):
        print('--- Inside Vehicle class ---')
        print('Marque:', marque, "\tType:", tipe)


class Car:
    def car_info(self, company: str = 'PIRELLI', location: str = 'Italie'):
        print('--- Inside Car class ---')
        print('Company:', company, "\tLocation:", location)


class Bus(Vehicle, Car):
    def bus_info(self, size: float = 0.0, fonction: str = 'Postal'):
        print('--- Inside Bus class ---')
        print('Company:', size, "\tLocation:", fonction)


class Truck(Vehicle):
    def truck_info(self, road_size: int = 0, name: str = ''):
        print('--- Inside Bus class ---')
        print('Company:', road_size, "\tLocation:", name)


class Google:
    def show_google(self):
        return 'Google Company'


class GoogleName(Google):
    def info(self):
        c_name = super().show_google()
        print('What is the company ? ', c_name)


def boulot():
    print('Boulot Boulot')


bus1 = Bus()
bus1.bus_info(15.55, 'Poste')
bus1.car_info('Farina', 'Italie')
bus1.vehicle_info('ALFA', '280I')

trk = Truck()
trk.vehicle_info()  # with defaults args
trk.truck_info(12, 'TruckMan')

goo = Google()
resultat = goo.show_google()
print(resultat)

gooC = GoogleName()
gooC.info()

bl = boulot
bl()
