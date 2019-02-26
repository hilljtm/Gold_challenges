from datetime import datetime, timedelta

import claim_repo


def Prompt():
    print("""
    Claims Manager\n'
    '1.List claims\n'
    '2.Process next claim\n'
    '3.Create a claim\n'
    '4.exit
    """)

while True:
    Prompt()
    choice = input(" > ")

    if choice == "1":
        x = claim_repo.show_claims()
        print(x)

    elif choice == "2":
        print(claim_repo.show_next_claim())
        a = input('Do you want to deal with this claim now(y/n)?')
    if a == 'y':
        claim_repo.deal_with_claim()

    elif choice == "3":
        claim_valid = True
        claim_id = input('Enter the claim id: ')
        claim_type = input('Enter the claim type: ')
        claim_description = input('Enter a claim description: ')
        amount_damage = input('Amount of damage: ')
        date_accident_year = int(input('Year of accident: '))
        date_accident_month = int(input('Month of accident: '))
        date_accident_day = int(input('Day of accident: '))
        date_claim_year = int(input('Year of claim: '))
        date_claim_month = int(input('Month of claim: '))
        date_claim_day = int(input('Day of claim: '))
        claim_date = datetime(year=date_claim_year, month=date_claim_month, day=date_claim_day)
        accident_date = datetime(year=date_accident_year, month=date_accident_month, day=date_accident_day)
        monthlater = timedelta(days=30)
    if claim_date > accident_date + monthlater:
        claim_valid = False
        claim_repo.create_claim(claim_type, claim_description, amount_damage, accident_date, claim_date, claim_valid)

    elif choice == '4':
        exit()