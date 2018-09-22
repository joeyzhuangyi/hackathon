from abc import ABC, abstractmethod
from flask_login import UserMixin
from datetime import datetime, timedelta
class user:
    def __init__(self,name,gender,rating,related_tag,about,reviews,past_tutoring = []):
        user._name = name
        user._gender= gender
        user._rating = rating
        user._related_tag= related_tag
        user._about = about
        user._reviews = reviews
        user._past_tutoring = past_tutoring

    def add_reviews(self,user_other):
        pass
