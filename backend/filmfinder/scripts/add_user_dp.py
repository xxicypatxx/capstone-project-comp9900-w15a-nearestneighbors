from login.models import User
import pandas as pd
import os


def run():
    default_dp = '../movies/user_dp/default.png'
    count = 0
    all_users = User.objects.all()
    

