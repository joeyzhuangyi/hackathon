from abc import ABC, abstractmethod
from flask_login import UserMixin
from datetime import datetime, timedelta
class user:
    def __init__(self,name,gender,rating,related_tag,about,reviews=[],past_tutoring = [],point=10):
        user._name = name
        user._gender= gender
        user._rating = rating
        user._related_tag= related_tag
        user._about = about
        user._reviews = reviews
        user._past_tutoring = past_tutoring
        user._availability = False
        user._point = point

    def add_reviews(self,user_other,review):
        if user_other in self.past_tutoring:
            self._review.append(review)
    def change_availability (self):
        if self._availability == True:
            self._availability= False
        else:
            self._availability = True

