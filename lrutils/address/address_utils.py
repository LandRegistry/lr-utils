
def build_address(raw_address):
    return AddressBuilder(house_no=raw_address["house_no"],
                                            street_name=raw_address["street_name"],
                                            town=raw_address["town"],
                                            postcode=raw_address["postcode"],
                                            postal_county=raw_address["postal_county"],
                                            region_name=raw_address["region_name"],
                                            country=raw_address["country"],
                                            full_address=raw_address["full_address"]).build()


class Address(object):

    def __init__(self, string_address):
        self.structured = None
        self.string = StringAddress(string_address)


class StructuredAddress(object):

    def __init__(self, house_no, street_name, town, postcode, postal_county, region_name, country):
        self.house_no = house_no
        self.street_name = street_name
        self.town = town
        self.postcode = postcode
        self.postal_county = postal_county
        self.region_name = region_name
        self.country = country


class StringAddress(object):

    def __init__(self, string_address):
        self.string_address = string_address

    def get_fields(self):
        fields = self.string_address.split(',')
        fields = [item.strip() for item in fields]
        return fields

    def get_string(self):
        return self.string_address


class AddressBuilder(object):

    def __init__(self, house_no, street_name, town, postcode, postal_county, region_name, country, full_address):
        self.house_no = house_no
        self.street_name = street_name
        self.town = town
        self.postcode = postcode
        self.postal_county = postal_county
        self.region_name = region_name
        self.country = country
        self.full_address = full_address
        self.minimal_viable_address_fields = ["house_no", "street_name", "town", "postcode"]


    def build(self):

        address = Address(self.full_address)

        have_minimum_required_data = True
        for field in self.minimal_viable_address_fields:
            if not self.__dict__[field] or self.__dict__[field].isspace() :
                have_minimum_required_data = False
                break
        if have_minimum_required_data and self.county_and_region_empty():
            have_minimum_required_data = False

        if have_minimum_required_data:
            address.structured = StructuredAddress(self.house_no, self.street_name, self.town, self.postcode, self.postal_county,
                self.region_name, self.country)

        return address

    def county_and_region_empty(self):
        county = self.postal_county.replace(" ","")
        region = self.region_name.replace(" ","")
        if not county and not region:
            return True
        return False

