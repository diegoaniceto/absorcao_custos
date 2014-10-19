import os


def populate():
    dep1 = add_departamento('Dept1')

    # Print out what we have added to the user.
    #for c in Departamento.objects.all():
     #   for p in Page.objects.filter(category=c):
      #      print "- {0} - {1}".format(str(c), str(p))


def add_departamento(nome):
    c = Departamento.objects.get_or_create(nome=nome)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custeio_absorcao.settings')
    from absorcao.models import Departamento
    populate()
