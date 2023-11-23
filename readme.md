# Extracting Information from Phone Number using Python!

The main object that the library deals with is a PhoneNumber object. You can create this from a string representing a phone number using the parse function, but you also need to specify the country that the phone number is being dialled from (unless the number is in E.164 format, which is globally unique).

![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

## Installation

Install the Require modules of python!
<br/>
*Note*: You Must have Python installed in your computer!!

```
  pip install phonenumbers
```


## Usage/Examples

```python
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

print("Hello, world programmer!")

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
```

Run the Code and See the Output! 😉

Thank You 🙏, Please Give Star 🌟 to this Repository!
