
class Claim:

    id_number = 0

    def __init__(self, claim_type, description, amount, accident_date, claim_date, is_valid):
        Claim.id_number += 1
        self.id = Claim.id_number
        self.claim = claim_type
        self.description = description
        self.amount = amount
        self.accident_date = accident_date
        self.claim_date = claim_date
        self.is_valid = is_valid

    def __repr__(self):
        return f'{self.id}, {self.claim},{self.description}, {self.amount}, {self.accident_date}, {self.claim_date}, {self.is_valid}'
