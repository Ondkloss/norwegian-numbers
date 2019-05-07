import re

INVALID_CONTROL_DIGIT = 'Rejected due to invalid control digit.'
INTEGER_PATTERN = re.compile(r'^[0-9]+$')


def make_kid_number(value, mode='MOD10'):
    validate_length(value, 1, 24)
    validate_integer(value)
    if mode.upper() == 'MOD10':
        controlDigit = make_mod10_control_digit(value, [2, 1])
        return value + str(controlDigit)
    elif mode.upper() == 'MOD11':
        controlDigit = make_mod11_control_digit(value, [2, 3, 4, 5, 6, 7])
        return value + str(controlDigit)


def verify_kid_number(value, mode='MOD10'):
    try:
        return value == make_kid_number(value[:-1], mode)
    except:
        return False


def make_birth_number(value):
    validate_length(value, 9, 9)
    validate_integer(value)
    firstControlDigit = make_mod11_control_digit(value, [2, 5, 4, 9, 8, 1, 6, 7, 3])
    secondControlDigit = make_mod11_control_digit(value + str(firstControlDigit), [2, 3, 4, 5, 6, 7])
    validate_integer(str(firstControlDigit), INVALID_CONTROL_DIGIT)
    validate_integer(str(secondControlDigit), INVALID_CONTROL_DIGIT)
    return value + str(firstControlDigit) + str(secondControlDigit)


def verify_birth_number(value):
    try:
        return value == make_birth_number(value[:-2])
    except:
        return False


def make_account_number(value):
    validate_length(value, 10, 10)
    validate_integer(value)
    controlDigit = make_mod11_control_digit(value, [2, 3, 4, 5, 6, 7])
    validate_integer(str(controlDigit), INVALID_CONTROL_DIGIT)
    return value + str(controlDigit)


def verify_account_number(value):
    try:
        return value == make_account_number(value[:-1])
    except:
        return False


def make_organisation_number(value):
    validate_length(value, 8, 8)
    validate_integer(value)
    controlDigit = make_mod11_control_digit(value, [2, 3, 4, 5, 6, 7])
    validate_integer(str(controlDigit), INVALID_CONTROL_DIGIT)
    return value + str(controlDigit)


def verify_organisation_number(value):
    try:
        return value == make_organisation_number(value[:-1])
    except:
        return False


def make_mod10_control_digit(value, multiplicands):
    control = 10 - (multiply_digits_by_weight(value, multiplicands, sum_of_digits) % 10)

    if control == 10:
        return 0

    return control


def make_mod11_control_digit(value, multiplicands):
    control = 11 - (multiply_digits_by_weight(value, multiplicands, do_nothing) % 11)

    if control == 11:
        return 0
    if control == 10:
        return '-'
    return control


def multiply_digits_by_weight(value, multiplicands, operation):
    # While this could be made more dense, maybe this has some hope of being readable
    number = int(value)
    digits = list(str(number))
    index = 0
    total = 0

    for digit in reversed(digits):
        multiplicand = multiplicands[index % len(multiplicands)]
        result = int(digit) * multiplicand
        total += operation(result)
        index += 1

    return total


def validate_integer(value, errorMessage='Value was not an integer.'):
    # https://stackoverflow.com/a/10834843
    result = INTEGER_PATTERN.match(value)
    if not result:
        raise ValueError(errorMessage)


def validate_length(value, minimum, maximum):
    if len(value) < minimum or len(value) > maximum:
        raise ValueError('Invalid value length for "{}". Must be from {} to {} characters, inclusive.'.format(value, minimum, maximum))


def sum_of_digits(n):
    # https://stackoverflow.com/a/14940026
    r = 0
    while n > 0:
        r += n % 10
        n = n // 10
    return r


def do_nothing(n):
    return n
