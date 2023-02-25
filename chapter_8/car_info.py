def car_info(manufacturer, model_name, **kwargs):
    """Build a dictionary containing everything we know about a car."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    return kwargs

car1 = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car1)