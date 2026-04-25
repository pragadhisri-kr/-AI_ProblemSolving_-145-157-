from data import services

# Decision engine selects service based on emergency type
def get_service_location(emergency_type):
    return services.get(emergency_type, None)
