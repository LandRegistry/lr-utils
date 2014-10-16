import unittest

from address import build_address

class AddressTestCase(unittest.TestCase):

    def setUp(self):
        self.minimal_address = {
                                    "full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ",
                                    "house_no" : "8",
                                    "street_name" : "Miller Way",
                                    "town" : "Plymouth",
                                    "postal_county" :  "Devon",
                                    "region_name" : "",
                                    "country" : "",
                                    "postcode":"PL6 8UQ"
                                }

    def test_structured_address_created_minimal_required_fields_not_empty(self):

        address = build_address(self.minimal_address)
        self.assertEquals("8", address.structured.house_no)
        self.assertEquals("Miller Way", address.structured.street_name)
        self.assertEquals("Plymouth", address.structured.town)
        self.assertEquals("Devon", address.structured.postal_county)


    def test_structured_address_not_created_if_a_required_field_empty(self):

        self.minimal_address["town"] = ""

        address = build_address(self.minimal_address)

        self.assertIsNone(address.structured)


    def test_structured_address_not_created_if_both_postal_country_and_region_name_empty(self):

        self.minimal_address["postal_county"] = ""
        self.minimal_address["region_name"] = "   "

        address = build_address(self.minimal_address)

        self.assertIsNone(address.structured)


    def test_string_address_is_present_even_when_required_field_is_empty(self):

        self.minimal_address["house_no"] = ""

        address = build_address(self.minimal_address)

        self.assertIsNone(address.structured)
        self.assertEquals("8 Miller Way, Plymouth, Devon, PL6 8UQ", address.string.get_string())
        self.assertEquals(["8 Miller Way", "Plymouth", "Devon", "PL6 8UQ"], address.string.get_fields())
