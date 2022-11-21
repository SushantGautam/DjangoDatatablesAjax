# install requirements, makemigrations then migrate  and run the code below in manage.py shell:


from faker import Faker

from WebApp.models import TestModel

for i in range(100):
    fake = Faker()
    TestModel.objects.create(
        name=fake.name(),
        email=fake.email(),
        address=fake.address(),
        phone=fake.phone_number(),
        company=fake.company(),
    )
