def print_error(parameter):
    print(f'{parameter} is out of range!')

def temperature_in_range(temperature):
    if temperature < 0 or temperature > 45:
        print_error('Temperature')
        return False
    return True

def soc_in_range(soc):
    if soc < 20 or soc > 80:
        print_error('State of Charge')
        return False
    return True

def charge_rate_in_range(charge_rate):
    if charge_rate > 0.8:
        print_error('Charge rate')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    return (temperature_in_range(temperature) and
            soc_in_range(soc) and
            charge_rate_in_range(charge_rate))



if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
