import random
def cars():
    print('Toyota')

    cars_list = ['Toyota', 'Nissan', 'Dodge', 'GMC', 'BMW']
    return random.choice(cars_list)

def model():
    models = ['2020', '2012', '2025', '2023', '2014', '2024', '2022']
    return random.choice(models)

print(f'car: {cars()} model: {model()}')