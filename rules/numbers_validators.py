from django.core.validators import RegexValidator


# This regular expression for a phone number to ensure that it is in the Egyptian phone number pattern
PHONE_NUMBER_PATTERN = RegexValidator(
regex = r'^01(0|1|2|5)\d{8}$',
message = "This field must contain a valid phone number in the format 01(1 or 2 or 5 or 0)XXXXXXXX",
code = 'invalid_phone_number'
)


# A ZIP code is a postal code are made up of five digits
ZIP_CODE_VALIDATOR = RegexValidator(
    regex = r'^\d{5}$',
    message = 'The postal code must be only five digits of numbers',
    code = 'invalid_code'
)


COLOR_HEXA_VALIDATOR = RegexValidator(
    regex = r'^(#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})(,|$))+',
    message = 'This field must contain at least one color and at most 3 colors in hexa format #XXXXXX',
    code='ivalid_hexa_number'
)