# 4.3.1.10 LAB: Converting fuel consumption

def liters_100km_to_miles_gallon(liters):
    gallon = liters / 3.785411784
    hundredkilometer = 62.137119223733
    answer = hundredkilometer / gallon
    return answer


def miles_gallon_to_liters_100km(miles):
    hundredkilometer = 62.137119223733
    km = hundredkilometer / miles 
    answerkm = km * 3.785411784
    return answerkm

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
