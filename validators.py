def add_contractor_validator(contractor):
    name = contractor['name'].get()
    street = contractor['street'].get()
    city = contractor['city'].get()
    zip = contractor['zip'].get()
    nip = contractor['nip'].get()

    if len(name) == 0: return "name"
    if len(street) == 0: return "street"
    if len(city) == 0: return "city"
    if len(zip) == 0: return "zip-code"
    if len(nip) != 10 or not nip.isdecimal():
        return "NIP"

    return True
