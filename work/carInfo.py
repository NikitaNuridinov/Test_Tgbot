import json


class CarFilter: # фильтр машин
    def __init__(self):
        with open('C:\\Users\\wilda\\python_class\\git_new\\Telegrambot\\carsBase\\car.json', 'r', encoding='utf-8') as f:
            car_f = json.load(f)
        self.carlist = car_f


    def countryfilter(self, country: str): #фильтр по городам
        lt = list()
        for car in self.carlist:
            if car["country"].lower() == country.lower():
                lt.append(car)        
        self.carlist = lt


    def brandfilter(self, brand: str): #фильтр по марке
        lt = list()
        for car in self.carlist:
            if car["brand"].lower() == brand.lower():
                lt.append(car)        
        self.carlist = lt
    

    def modelfilter(self, model: str): #фильтр по модели
        lt = list()
        for car in self.carlist:
            if car["model"].lower() == model.lower():
                lt.append(car)        
        self.carlist = lt

    
    def getCountry(self): #список стран производителей
        lt = set()
        for car in self.carlist:
            lt.add(car["country"].lower())
        return lt


    def getBrand(self): #список марок автомобилей
        lt = set()
        for car in self.carlist:
            lt.add(car["brand"].lower())
        return lt


    def getModel(self): #список моделей автомобилей
        lt = set()
        for car in self.carlist:
            lt.add(car["model"].lower())
        return lt
    





# class SearchError: # проверка на наличие
#     def countryError(x):
#         if x.lower() in CarFilter().getCountry():
#             return True
#         else:
#             return False
        
#     def brandError(x):
#         if x.lower() in CarFilter().getBrand():
#             return True
#         else:
#             return False
        
#     def modelError(x):
#         if x.lower() in CarFilter().getModel():
#             return True
#         else:
#             return False
        




class Car: # запрос информации по машине
    def __init__(self, car) -> None:
        self.car = car

    def country(self):
        return self.car["country"]
    
    def brand(self):
        return self.car["brand"]
    
    def model(self):
        return self.car["model"]
    
    def release(self):
        return self.car["s_y"]
    
    def lastyear(self):
        return self.car["e_y"]
    
    def image(self):
        return self.car["image"]
