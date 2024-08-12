def print_error(parameter):
    print(f'{parameter} is out of range!')

def print_warning(parameter, warning_type):
    print(f'Warning: {parameter} - {warning_type}')

def temperature_in_range(temperature, warning=True):
    upper_limit = 45
    lower_limit = 0
    tolerance = 0.05 * upper_limit
    
    if temperature < lower_limit or temperature > upper_limit:
        print_error('Temperature')
        return False
    
    if warning:
        if temperature <= lower_limit + tolerance:
            print_warning('Temperature', 'Approaching discharge')
        elif temperature >= upper_limit - tolerance:
            print_warning('Temperature', 'Approaching charge-peak')
    
    return True

def soc_in_range(soc, warning=True):
    upper_limit = 80
    lower_limit = 20
    tolerance = 0.05 * upper_limit
    
    if soc < lower_limit or soc > upper_limit:
        print_error('State of Charge')
        return False
    
    if warning:
        if soc <= lower_limit + tolerance:
            print_warning('State of Charge', 'Approaching discharge')
        elif soc >= upper_limit - tolerance:
            print_warning('State of Charge', 'Approaching charge-peak')
    
    return True

def charge_rate_in_range(charge_rate, warning=True):
    upper_limit = 0.8
    tolerance = 0.05 * upper_limit
    
    if charge_rate > upper_limit:
        print_error('Charge rate')
        return False
    
    if warning:
        if charge_rate >= upper_limit - tolerance:
            print_warning('Charge rate', 'Approaching charge-peak')
    
    return True

def battery_is_ok(temperature, soc, charge_rate, warnings_enabled=True):
    return (temperature_in_range(temperature, warning=warnings_enabled) and
            soc_in_range(soc, warning=warnings_enabled) and
            charge_rate_in_range(charge_rate, warning=warnings_enabled))

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
