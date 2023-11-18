import math
import argparse


def calculate_diff_payment(principal, periods, interest):
    i = (interest / 100) / 12
    total_payment = 0

    for month in range(1, periods + 1):
        diff_payment = (principal / periods) + i * (principal - ((principal * (month - 1)) / periods))
        total_payment += math.ceil(diff_payment)
        print(f'Month {str(month)}: payment is {math.ceil(diff_payment)}')

    overpayment = total_payment - principal
    print(f'\nOverpayment = {math.ceil(overpayment)}')


def calculate_annuity_payment(principal, periods, interest):
    i = (interest / 100) / 12
    annuity_payment = principal * (i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1)
    overpayment = (math.ceil(annuity_payment) * periods) - principal

    print(f'Your annuity payment = {math.ceil(annuity_payment)}!')
    print(f'Overpayment = {math.ceil(overpayment)}')


def calculate_loan_principal(payment, periods, interest):
    i = (interest / 100) / 12
    loan_principal = payment / ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))
    overpayment = (payment * periods) - loan_principal

    print(f'Your loan principal = {math.floor(loan_principal)}!')
    print(f'Overpayment = {math.ceil(overpayment)}')


def calculate_how_long_it_will_take(principal, payment, interest):
    i = (interest / 100) / 12
    n = math.log(payment / (payment - i * principal), 1 + i)

    months = math.ceil(n)
    overpayment = (payment * months) - principal
    years = months // 12
    months %= 12

    if years == 0:
        print(f'It will take {months} months to repay the loan')
    elif years == 1 and months == 0:
        print(f'It will take {years} year to repay the loan')
    elif years > 1 and months == 0:
        print(f'It will take {years} years to repay the loan')
    else:
        print(f'It will take {years} years and {months} months to repay the loan!')

    print(f'Overpayment = {math.ceil(overpayment)}')


parser = argparse.ArgumentParser(description='Loan Calculator')

parser.add_argument('--type', help='Choose diff or annuity')
parser.add_argument('--principal', type=int, help='Enter principal')
parser.add_argument('--periods', type=int, help='Enter periods')
parser.add_argument('--payment', type=int, help='Enter payment')
parser.add_argument('--interest', type=float, help='Enter interest')

args = parser.parse_args()


if args.type not in ['diff', 'annuity']:
    print('Incorrect parameters')

else:
    if args.type == 'diff':

        if all([args.principal, args.periods, args.interest]):
            if any([arg < 0 for arg in [args.principal, args.periods, args.interest]]):
                print('Incorrect parameters.')
            else:
                calculate_diff_payment(args.principal, args.periods, args.interest)
        else:
            print('Incorrect parameters')

    elif args.type == 'annuity':

        if all([args.payment, args.periods, args.interest]):
            if any([arg < 0 for arg in [args.payment, args.periods, args.interest]]):
                print('Incorrect parameters')
            else:
                calculate_loan_principal(args.payment, args.periods, args.interest)

        elif all([args.principal, args.payment, args.interest]):
            if any([arg < 0 for arg in [args.principal, args.payment, args.interest]]):
                print('Incorrect parameters')
            else:
                calculate_how_long_it_will_take(args.principal, args.payment, args.interest)

        elif all([args.principal, args.periods, args.interest]):
            if any([arg < 0 for arg in [args.principal, args.periods, args.interest]]):
                print('Incorrect parameters')
            else:
                calculate_annuity_payment(args.principal, args.periods, args.interest)
        else:
            print('Incorrect parameters')
