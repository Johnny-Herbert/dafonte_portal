from portal.models import OpportunityRole


def run():
    ROLES = [
        {'name': 'Advogado', 'role_type': 'LAWYER'},
        {'name': 'Estagiário', 'role_type': 'INTERN'},
        {'name': 'Trainee', 'role_type': 'TRAINEE'},
    ]
    for role in ROLES:
        name, role_type = role['name'], role['role_type']
        obj, created = OpportunityRole.objects.get_or_create(
            name=name, role_type=role_type, defaults=role
        )
        if created:
            print(f'{obj} criado')
        else:
            print(f'{obj} já existe')
