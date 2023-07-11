import random
from datetime import date


number_digit = 10
min_value = 10 ** (number_digit - 1)
max_value = (10 ** number_digit) - 1


def image_uploader(class_name):
    global wrapper
    def wrapper(instance, filename):
        name , extension = filename.split('.')
        random_number = random.randint(min_value, max_value)
        today = date.today()
        formatted_date = today.strftime("%m-%Y")
        return f'{class_name}_images/{formatted_date}/{instance.id}_{random_number}.{extension}'
    return wrapper

# {instance.user_id.username}