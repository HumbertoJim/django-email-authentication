from accounts.models import User
from main.tools import generate_code

def generate_username(length=16) -> str:
    username = generate_code()
    while User.objects.filter(username=username):
        username = generate_code(length)
    return username