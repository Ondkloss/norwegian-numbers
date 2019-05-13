import sys
import argparse
from .util import make_kid_number, verify_kid_number, make_account_number, verify_account_number, make_birth_number, verify_birth_number, make_organisation_number, verify_organisation_number


def argparser(args):
    parser = argparse.ArgumentParser(description='Generate or verify KID-nummer, organisasjonsnummer, fødselsnummer, kontonummer')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--make', choices=['kid10', 'kid11', 'organisation', 'birth', 'account'], type=str.lower, help='Choose what to make')
    group.add_argument('-v', '--verify', choices=['kid10', 'kid11', 'organisation', 'birth', 'account'], type=str.lower, help='Choose what to verify')
    parser.add_argument('value', help='The value to make or verify based on')

    return parser.parse_args(args)


def main(args):
    parsed = argparser(args)

    if parsed.make:
        if parsed.make == 'kid10':
            return make_kid_number(parsed.value, 'mod10')
        elif parsed.make == 'kid11':
            return make_kid_number(parsed.value, 'mod11')
        elif parsed.make == 'organisation':
            return make_organisation_number(parsed.value)
        elif parsed.make == 'birth':
            return make_birth_number(parsed.value)
        elif parsed.make == 'account':
            return make_account_number(parsed.value)
    elif parsed.verify:
        if parsed.verify == 'kid10':
            return verify_kid_number(parsed.value, 'mod10')
        elif parsed.verify == 'kid11':
            return verify_kid_number(parsed.value, 'mod11')
        elif parsed.verify == 'organisation':
            return verify_organisation_number(parsed.value)
        elif parsed.verify == 'birth':
            return verify_birth_number(parsed.value)
        elif parsed.verify == 'account':
            return verify_account_number(parsed.value)


if __name__ == "__main__":
    print(main(sys.argv[1:]))
