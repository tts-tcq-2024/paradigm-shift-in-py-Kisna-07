def print_error(parameter):
    print(f'{parameter} is out of range!')

def print_warning(parameter, warning_type):
    print(f'Warning: {parameter} - {warning_type}')

def check_limit(value, lower_limit, upper_limit):
    return lower_limit <= value <= upper_limit

def check_warning(value, lower_limit, upper_limit, tolerance, parameter, warning_type_discharge='Approaching discharge', warning_type_peak='Approaching charge-peak'):
    if value <= lower_limit + tolerance:
        print_warning(parameter, warning_type_discharge)
    elif value >= upper_limit - tolerance:
        print_warning(parameter, warning_type_peak)

def temperature_in_range(temperature, warning=True):
    upper_limit = 45
    lower_limit = 0
    tolerance = 0.05 * upper_limit
    
    if not check_limit(temperature, lower_limit, upper_limit):
        print_error('Temperature')
        return False
    
    if warning:
        check_warning(temperature, lower_limit, upper_limit, tolerance, 'Temperature')
    
    return True

def soc_in_range(soc, warning=True):
    upper_limit = 80
    lower_limit = 20
    tolerance = 0.05 * upper_limit
    
    if not check_limit(soc, lower_limit, upper_limit):
        print_error('State of Charge')
        return False
    
    if warning:
        check_warning(soc, lower_limit, upper_limit, tolerance, 'State of Charge')
    
    return True

def charge_rate_in_range(charge_rate, warning=True):
    upper_limit = 0.8
    tolerance = 0.05 * upper_limit
    
    if not check_limit(charge_rate, 0, upper_limit):
        print_error('Charge rate')
        return False
    
    if warning:
        check_warning(charge_rate, 0, upper_limit, tolerance, 'Charge rate', warning_type_discharge='', warning_type_peak='Approaching charge-peak')
    
    return True

def battery_is_ok(temperature, soc, charge_rate, warnings_enabled=True):
    return (temperature_in_range(temperature, warning=warnings_enabled) and
            soc_in_range(soc, warning=warnings_enabled) and
            charge_rate_in_range(charge_rate, warning=warnings_enabled))

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
