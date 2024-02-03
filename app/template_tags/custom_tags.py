from django.template.defaulttags import register
from django.template import Library
import datetime
from django.db.models import Sum


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_extra_digits(number, digits):
    number = str(number).zfill(digits)
    return number

@register.filter
def return_list(start, finish):
    list = []
    for i in range(start, finish):
        list.append(i)
    return list
    # register = Library()

@register.filter(expects_localtime=True)
def parse_iso(value):
    return datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

@register.filter()
def promocode_count_users(users, promo_code):
    promo_users = users.filter(profile__promo_code__code=promo_code.code)
    return len(promo_users)

@register.filter()
def promocode_total_value(users, promo_code):
    promo_users = users.filter(profile__promo_code__code=promo_code.code)
    total_paid_amount = 0
    for user in promo_users:
        if user.profile.paid_amount is not None:
            total_paid_amount += float(user.profile.paid_amount)
    return total_paid_amount

@register.filter()
def is_value_between(value, i):
    if value >= i:
        return 1
    elif value >= i - 0.25:
        return 2
    elif value >= i - 0.5:
        return 3
    elif value >= i - 0.75:
        return 4

@register.filter()
def summary_keys(stars):
    if stars == 0:
        return SUMMARY_KEYS[0]
    elif 0 < stars <= 1:
        return SUMMARY_KEYS[1]
    elif 1 < stars <= 1.5:
        return SUMMARY_KEYS[2]
    elif 1.5 < stars <= 2:
        return SUMMARY_KEYS[3]
    elif 2 < stars <= 2.5:
        return SUMMARY_KEYS[4]
    elif 2.5 < stars <= 3:
        return SUMMARY_KEYS[5]
    elif 3 < stars <= 3.5:
        return SUMMARY_KEYS[6]
    elif 3.5 < stars <= 4:
        return SUMMARY_KEYS[7]
    elif 4 < stars < 5:
        return SUMMARY_KEYS[8]
    elif stars == 5:
        return SUMMARY_KEYS[9]
    