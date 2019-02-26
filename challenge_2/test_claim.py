import unittest

import claim_repo


class TestClaim(unittest.TestCase):

    def test_create_claim_should_return_claim_list(self):
        # arrange
        claimtype = "Auto"
        description = "Car blows up, lame"
        claimamount = 10000
        dateofincident = "12-11-12"
        dateofclaim = "12-12-12"
        isvalid = True
        claim_repo.create_claim(claimtype, description, claimamount, dateofincident, dateofclaim, isvalid)
        actual = len(claim_repo)
        expected = '1'
        self.assertEqual(actual, expected)

    def test_get_claims_should_give_claim_information(self):
        # arrange
        claim_repo.show_claims
        # act
        actual = type(claim_repo.show_claims)
        expected = type([])
        # assert
        self.assertEqual(actual, expected)

    def test_remove_first_claim_from_overall_list(self):
        claim_repo.deal_with_claim()
        actual = len(claim_repo.claim)
        expected = claim_repo.claim.pop()
        self.assertEqual(actual, expected)
