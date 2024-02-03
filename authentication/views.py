# -*- encoding: utf-8 -*-

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from authentication.tokens import account_activation_token
from django.utils.http import urlsafe_base64_decode

from django.utils.encoding import force_str
from validate_email import validate_email


def login_view(request):
	if request.user.is_authenticated:
		return redirect("dashboard")
	else:
		if request.method == "POST":
			current_site = get_current_site(request)
			email = request.POST['email'].lower()
			temp_username = email.split("@")[0]
			username = "".join(e for e in temp_username if e.isalnum())
			is_valid = validate_email(email_address=email,check_smtp=False)

			if(is_valid):
				try:
					user = User.objects.get(email=email)
				except:
					for i in range(1000):          
						username_check = User.objects.filter(username=username)
						if len(username_check) == 0:
							user = User.objects.create(email=email, username=username)
							break
						else:
							username = f"{username}{i}"
						
				subject = 'Log Into Your Dilanu App Account'
				message = render_to_string('accounts/activation.html', {
						'user': user,
						'domain': current_site.domain,
						'uid': urlsafe_base64_encode(force_bytes(user.pk)),
						'token': account_activation_token.make_token(user),
				})
				user.email_user(subject, message="", html_message=message)
				context = {
					"email": email,
					# "button_text": "Return to Sign In",
					"heading": "Email Successfully Sent", 
					"msg": f'''An email has been sent to: {email}. 
					
					You can now close this window and click the link in the email to log into your Dilanu account.'''
					}
				return render(request, "message.html", context=context)
			else:
				context = {
					"email": email,
					"heading": "Invalid email entered", 
					"msg": f"{email} is an invalid email. Kindly try again with correct email address."
				}
				return render(request, "message.html", context=context)
		context = {}
		return render(request, "accounts/login.html", context=context)


def activate(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		# user.profile.save()
		user.save()
		login(request, user)
		return redirect('home')
	else:
		return redirect('home')
