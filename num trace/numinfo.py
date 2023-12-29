import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def get_phone_number_info(phone_number):
    phone_number = phonenumbers.parse(phone_number)
    if phonenumbers.is_valid_number(phone_number):
        print('Phone Number: {}'.format(phone_number.national_number))
        print('Region: {}'.format(timezone.time_zones_for_number(phone_number)[0]))
        print('Service Provider: {}'.format(carrier.name_for_number(phone_number, "en")))
        print('Country: {}'.format(geocoder.description_for_number(phone_number, "en")))
        print('Number Type: {}'.format('Mobile' if phonenumbers.is_possible_number(phone_number) else 'Fixed line'))
    else:
        print("Invalid phone number. Please enter a valid mobile number.")

if __name__ == '__main__':
    mobile_no = input("Enter Phone number with country code (+xx xxxxxxxxx): ")
    get_phone_number_info(mobile_no)
