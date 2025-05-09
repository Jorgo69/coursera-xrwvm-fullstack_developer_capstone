from .models import CarMake, CarModel

def initiate():

    CarModel.objects.all().delete()
    CarMake.objects.all().delete()


    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    car_model_data = [
    {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1},
    {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 2},
    {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 3},
    {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 4},
    {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 5},
    {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 6},
    {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 7},
    {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 8},
    {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 9},
    {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 10},
    {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 11},
    {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 12},
    {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 13},
    {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 14},
    {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 15},
]

    # for data in car_model_data:
    #         CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'])

    # for data in car_model_data:
    #             CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'], dealer_id=data['dealer_id'])

    for data in car_model_data:
        try:
            CarModel.objects.create(
                name=data['name'],
                car_make=data['car_make'],
                type=data['type'],
                year=data['year'],
                dealer_id=data['dealer_id']
            )
        except Exception as e:
            print(f"Error creating CarModel {data['name']}: {e}")