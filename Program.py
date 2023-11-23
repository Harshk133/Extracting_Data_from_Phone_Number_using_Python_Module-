import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Taking User's Phone number as a input!
phone_number = input("Enter Your Phone Number with +..: ")

# Passing the Phone number to `phonenumbers` module function and storing it into a phone variable.
phone = phonenumbers.parse(phone_number)

# Extracting the data such as timezone, carrier
time_zone = timezone.time_zones_for_number(phone)

carrier_data = carrier.name_for_number(phone, "en")

registration_data = geocoder.description_for_number(phone, "en")

# Printing the extracted data to the terminal!
print(f"Your Phone Number is {phone_number}")
print(f"Your Phone Number time zone is {time_zone}")
print(f"Your Phone Number company is {carrier_data}")
print(f"Your Phone Number registration is {registration_data}")