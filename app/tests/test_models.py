from basetest import BaseTest
from app.models import County, Ward, Constituency

class TestModels(BaseTest):
    
    def test_save_county(self):
        '''Test if a new County is saved'''
        county = County.query.filter_by(name='Kisumu').first()
        self.assertIsNone(county)

        County(name='Kisumu').save()

        new_county = County.query.filter_by(name='Kisumu').first()
        self.assertEqual('Kisumu', new_county.name)

    def test_update_county(self):
        '''Test if the Update County works'''
        county = County.query.filter_by(name='Turkana').first()
        self.assertIsNot(county.code, 0)

        county.name = 'sample_name'
        county.update()

        updated_county = County.query.filter_by(name='sample_name').first()
        self.assertIsNotNone(updated_county)

    def test_delete_county(self):
        '''Test delete county works'''
        county = County.query.filter_by(name='Nakuru').first()
        self.assertIsNotNone(county)

        county.delete()
        deleted_county = County.query.filter_by(name='Nakuru').first()
        self.assertIsNone(deleted_county)
