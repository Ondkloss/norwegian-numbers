import argparse
from .util import make_kid_number, verify_kid_number, make_account_number, verify_account_number, make_birth_number, verify_birth_number, make_organisation_number, verify_organisation_number


def argparser():
    parser = argparse.ArgumentParser(description='Generate or verify KID-nummer, organisasjonsnummer, fødselsnummer, kontonummer')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--make', choices=['kid10', 'kid11', 'organisation', 'birth', 'account'], type=str.lower, help='Choose what to make')
    group.add_argument('-v', '--verify', choices=['kid10', 'kid11', 'organisation', 'birth', 'account'], type=str.lower, help='Choose what to verify')
    parser.add_argument('value', help='The value to make or verify based on')

    return parser.parse_args()


if __name__ == "__main__":
    args = argparser()

    if args.make:
        if args.make == 'kid10':
            print(make_kid_number(args.value, 'mod10'))
        elif args.make == 'kid11':
            print(make_kid_number(args.value, 'mod11'))
        elif args.make == 'organisation':
            print(make_organisation_number(args.value))
        elif args.make == 'birth':
            print(make_birth_number(args.value))
        elif args.make == 'account':
            print(make_account_number(args.value))
    elif args.verify:
        if args.verify == 'kid10':
            print(verify_kid_number(args.value, 'mod10'))
        elif args.verify == 'kid11':
            print(verify_kid_number(args.value, 'mod11'))
        elif args.verify == 'organisation':
            print(verify_organisation_number(args.value))
        elif args.verify == 'birth':
            print(verify_birth_number(args.value))
        elif args.verify == 'account':
            print(verify_account_number(args.value))
