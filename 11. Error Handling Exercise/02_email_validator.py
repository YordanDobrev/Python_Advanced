import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidSymbols(Exception):
    pass


VALID_DOMAINS = ["com", "bg", "org", "net"]
MIN_CHAR = 4
end_pattern = r"(\.com)|(\.bg)|(\.org)|(\.net)$"
symbol_pattern = r"(^[a-z0-9_]+)@"
the_email = input()

while the_email != "End":

    if "@" not in the_email:
        raise MustContainAtSymbolError('Entered email must contain "@" !')
    elif len(the_email.split("@")[0]) <= MIN_CHAR:
        raise NameTooShortError("Entered name must be more than 4 characters long !")
    elif not re.findall(end_pattern, the_email):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)} !")
    elif not re.findall(symbol_pattern, the_email):
        raise InvalidSymbols(f"Entered name must contain only word characters, digits and underscore !")

    print(f"Email is valid")

    the_email = input()