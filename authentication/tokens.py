from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
	def _make_hash_value(self, user, timestamp):
		return (six.text_type(user.pk) + six.text_type(timestamp))

account_activation_token = AccountActivationTokenGenerator()


# http://127.0.0.1:8000/activate/MTM/aehgcs-87e223361cab1147189e09353c61c748/