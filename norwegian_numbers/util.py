import re

INVALID_CONTROL_DIGIT = 'Rejected due to invalid control digit.'
INTEGER_PATTERN = re.compile(r'^[0-9]+$')


def make_kid_number(value, mode='MOD10'):
    """Makes a KID-number in either MOD10 or MOD11.
    Valid input lengths are from 1 to 24 characters, inclusive.
    The output length will be one character longer.

    Args:
        value (str): The value to make the KID-number based on
        mode (str): MOD10 (default) or MOD11

    Returns:
        str: The resulting KID-number

    Raises:
        ValueError: If invalid length or non-integer
    """
    _validate_length(value, 1, 24)
    _validate_integer(value)
    if mode.upper() == 'MOD10':
        controlDigit = _make_mod10_control_digit(value)
        return value + str(controlDigit)
    elif mode.upper() == 'MOD11':
        controlDigit = _make_mod11_control_digit(value)
        return value + str(controlDigit)


def verify_kid_number(value, mode='MOD10'):
    """Verifies a KID-number in either MOD10 or MOD11.

    Args:
        value (str): The KID-number value to verify
        mode (str): MOD10 (default) or MOD11

    Returns:
        bool: If the value is a valid KID-number or not
    """
    try:
        return value == make_kid_number(value[:-1], mode)
    except:
        return False


def make_birth_number(value):
    """Makes a birth number.
    Valid input length is 9 characters.
    The output length will be 11 character.

    Args:
        value (str): The value to make the birth number based on

    Returns:
        str: The resulting birth number

    Raises:
        ValueError: If invalid length, non-integer or illegal control digits
    """
    _validate_length(value, 9, 9)
    _validate_integer(value)
    firstControlDigit = _make_mod11_control_digit(value, [2, 5, 4, 9, 8, 1, 6, 7, 3])
    secondControlDigit = _make_mod11_control_digit(value + str(firstControlDigit))
    _validate_integer(str(firstControlDigit), INVALID_CONTROL_DIGIT)
    _validate_integer(str(secondControlDigit), INVALID_CONTROL_DIGIT)
    return value + str(firstControlDigit) + str(secondControlDigit)


def verify_birth_number(value):
    """Verifies a birth number.

    Args:
        value (str): The birth number value to verify

    Returns:
        bool: If the value is a valid birth number or not
    """
    try:
        return value == make_birth_number(value[:-2])
    except:
        return False


def make_account_number(value):
    """Makes an account number.
    Valid input length is 10 characters.
    The output length will be 11 character.

    Args:
        value (str): The value to make the account number based on

    Returns:
        str: The resulting account number

    Raises:
        ValueError: If invalid length, non-integer or illegal control digits
    """
    _validate_length(value, 10, 10)
    _validate_integer(value)
    controlDigit = _make_mod11_control_digit(value)
    _validate_integer(str(controlDigit), INVALID_CONTROL_DIGIT)
    return value + str(controlDigit)


def verify_account_number(value):
    """Verifies an account number.

    Args:
        value (str): The account number value to verify

    Returns:
        bool: If the value is a valid account number or not
    """
    try:
        return value == make_account_number(value[:-1])
    except:
        return False


def make_organisation_number(value):
    """Makes a organisation number.
    Valid input length is 8 characters.
    The output length will be 9 character.

    Args:
        value (str): The value to make the organisation number based on

    Returns:
        str: The resulting organisation number

    Raises:
        ValueError: If invalid length, non-integer or illegal control digits
    """
    _validate_length(value, 8, 8)
    _validate_integer(value)
    controlDigit = _make_mod11_control_digit(value)
    _validate_integer(str(controlDigit), INVALID_CONTROL_DIGIT)
    return value + str(controlDigit)


def verify_organisation_number(value):
    """Verifies an organisation number.

    Args:
        value (str): The organisation number value to verify

    Returns:
        bool: If the value is a valid organisation number or not
    """
    try:
        return value == make_organisation_number(value[:-1])
    except:
        return False


def _make_mod10_control_digit(value, multiplicands = [2, 1]):
    control = 10 - (multiply_digits_by_weight(value, multiplicands, _sum_of_digits) % 10)

    if control == 10:
        return 0

    return control


def _make_mod11_control_digit(value, multiplicands = [2, 3, 4, 5, 6, 7]):
    control = 11 - (multiply_digits_by_weight(value, multiplicands, _do_nothing) % 11)

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


def _validate_integer(value, errorMessage='Value was not an integer.'):
    # https://stackoverflow.com/a/10834843
    result = INTEGER_PATTERN.match(value)
    if not result:
        raise ValueError(errorMessage)


def _validate_length(value, minimum, maximum):
    if len(value) < minimum or len(value) > maximum:
        raise ValueError('Invalid value length for "{}". Must be from {} to {} characters, inclusive.'.format(value, minimum, maximum))


def _sum_of_digits(n):
    # https://stackoverflow.com/a/14940026
    r = 0
    while n > 0:
        r += n % 10
        n = n // 10
    return r


def _do_nothing(n):
    return n
