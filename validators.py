def add_contractor_validator(contractor):
    name = contractor['name'].get()
    street = contractor['street'].get()
    city = contractor['city'].get()
    zip = contractor['zip'].get()
    nip = contractor['nip'].get()

    if len(name) == 0: return False
    if len(street) == 0: return False
    if len(city) == 0: return False
    if len(zip) == 0: return False
    if len(nip) != 10 or not nip.isdecimal():
        return False

    return True
