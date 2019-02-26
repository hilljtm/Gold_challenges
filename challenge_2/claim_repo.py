from claim import Claim

claim = []
claim_list = []


def create_claim(claim_type, description, amount, accident_date, claim_date, is_valid):
    new_claim = Claim(claim_type, description, amount, accident_date, claim_date, is_valid)
    claim_list.append(new_claim)


def process_next_claim(self):
    process_next_claim


def show_next_claim():
    return claim_list[0]


def deal_with_claim():
    claim_list.pop(0)
    return True


def show_claims():
    return claim_list
