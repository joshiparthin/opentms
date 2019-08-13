from django.forms import ValidationError
from django.forms import Form


class UsernameInvalidException(ValidationError):pass
class PasswordInvalidException(ValidationError):pass

def is_valid_username_len(username):
    return False if len(username) < 10 else True

def is_valid_password_len(password):
    return False if len(password)<10 else True

def validate_usernames(username):
    if not is_valid_username_len(username):
        return "Username should be more than 10 characters"
    
def validate_password(password):
    if not is_valid_password_len(password):
        return "Password should be more than 10 characters"
        