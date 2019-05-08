# Norwegian numbers

[![Build Status](https://travis-ci.com/Ondkloss/norwegian-numbers.svg?branch=master)](https://travis-ci.com/Ondkloss/norwegian-numbers)

Make and verify official Norwegian numbers:

* KID-nummer: `make_kid_number` and `verify_kid_number`
* Organisasjonsnummer: `make_organisation_number` and `verify_organisation_number`
* Fødselsnummer: `make_birth_number` and `verify_birth_number`
* Kontonummer: `make_account_number` and `verify_account_number`

This currently only concerns itself with the control digits.

## Installation

To install from PyPi as a module in your environment:

    pip install norwegian-numbers

To install from source as a module in your environment:

    python setup.py install

## Code usage from installation

Example code usages after installation:

    >>> import norwegian_numbers as nn
    >>> nn.make_kid_number('1234', 'mod10')
    '12344'
    >>> nn.verify_kid_number('12344', 'mod10')
    True
    >>> nn.make_account_number('1234567890')
    '12345678903'
    >>> nn.make_organisation_number('12345678')
    '123456785'
    >>> nn.make_birth_number('311299567')
    '31129956715'

## Running from command line

Usage from command line:

    $ python -m norwegian_numbers --help
    usage: __main__.py [-h]
                    (-m {kid10,kid11,organisation,birth,account} | -v {kid10,kid11,organisation,birth,account})
                    value

    Generate or verify KID-nummer, organisasjonsnummer, fødselsnummer, kontonummer

    positional arguments:
    value                 The value to make or verify based on

    optional arguments:
    -h, --help            show this help message and exit
    -m {kid10,kid11,organisation,birth,account}, --make {kid10,kid11,organisation,birth,account}
                            Choose what to make
    -v {kid10,kid11,organisation,birth,account}, --verify {kid10,kid11,organisation,birth,account}
                            Choose what to verify

Example usage:

    $ python -m norwegian_numbers -m kid10 1234
    12344
    $ python -m norwegian_numbers -v kid10 12344
    True
    $ python -m norwegian_numbers -m account 1234567890
    12345678903
    $ python -m norwegian_numbers -m organisation 12345678
    123456785
    $ python -m norwegian_numbers -m birth 311299567
    31129956715

## Testing from source

To run the tests:

    python -m unittest discover

Or if you have tox:

    tox

## Sources

Some sources on the background material:

* [KID-nummer](https://no.wikipedia.org/wiki/KID-nummer)
* [Fødselsnummer](https://no.wikipedia.org/wiki/F%C3%B8dselsnummer)
* [Organisasjonsnummer](https://no.wikipedia.org/wiki/Organisasjonsnummer)
* [Kontonummer](https://no.wikipedia.org/wiki/Kontonummer)
* [MOD10](https://no.wikipedia.org/wiki/MOD10)
* [MOD11](https://no.wikipedia.org/wiki/MOD11)

## Distribution

The distribution was created by the following commands:

    python setup.py sdist bdist_wheel
    python -m twine upload dist/*
