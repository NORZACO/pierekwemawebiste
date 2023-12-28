
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()



def create_users(range_number_of_users):
    # fields name: username, password, email, first_name, last_name, is_active, is_staff, is_superuser
    for _ in range(range_number_of_users):
        user = User.objects.create_user(
            username=fake.user_name(),
            password=fake.password(),
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
        user.save()
        print(user.username, user.password)