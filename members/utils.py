import string


def get_initials(objects):
    initials = [
        dict(
            value=i,
            disabled=(
                objects.filter(first_name__istartswith=i).count() == 0
            )
        )
        for i in list(string.ascii_uppercase)
    ]
    return initials
