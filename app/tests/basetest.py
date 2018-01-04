from app import app as app_test, db
from app.models import County, Ward, Constituency
from flask_testing import TestCase

class BaseTest(TestCase):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    def create_app(self):
        self.app_t = app_test
        return app_test

    def setUp(self):
        db.create_all(app=self.app_t)

        self.http = self.create_app().test_client()

        # Create a new County
        county = County(name="Nakuru").save()

        county = County(name="Turkana").save()

        # create constituencies associated with  Nakuru
        constituency1 = Constituency(name="Kongowea", county_code=county.code)
        constituency2 = Constituency(name="Nairobi", county_code=county.code)

        # create wards associated with Kongowea and Nairobi
        Ward(name="xxxxx", constituency_code=constituency1.code)
        Ward(name="yyyyyy", constituency_code=constituency1.code)

        Ward(name="Hurama", constituency_code=constituency2.code)
        Ward(name="Pangani", constituency_code=constituency2.code)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=self.app_t)