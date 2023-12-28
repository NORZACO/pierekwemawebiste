from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six

class CustomPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def make_token(self, user):
        # Customize the token generation here if needed
        return super().make_token(user)

# generate_token = CustomPasswordResetTokenGenerator()
token_generator = CustomPasswordResetTokenGenerator() 
 # Use your custom class if applicable
# user = YourUserModel.objects.get(username='example_user')  # Replace 'YourUserModel' and 'example_user' with your user model and username

# Generate the token for the user
# token = token_generator.make_token(user)
