
def upload_to(instance, filename):
    class_name = instance.__class__.__name__
    return '{0}/{1}/{2}'.format(class_name, instance.id, filename)
