from app.models import County, Constituency
from app.constituency_view import return_constituency

def return_county(county):
    if isinstance(county, County) and county is not None:
        constituencies = Constituency().get_by_county_code(county.code)

        return { 
            "code": county.code,
            "name": county.name, 
            "constituencies": [return_constituency(constituency) for constituency in constituencies] 
            }
    else:
        return { "code": "", "name": "", "constituencies":"[]" }

class CountyData(object):
    
    def __init__(self):
        self.county = County()
    
    def fetch_county(self, code):
        if not isinstance(code, int):
            return {"error": "Invalid code found :" + str(code)}

        return return_county(self.county.get_one(code))

    def fetch_all_counties(self):
        return [return_county(county) for county in self.county.get_all()]

    
    def add_new_county(self, name):
        if not isinstance(name, str):
            return {"error": "Invalid name found: "+ str(name)}

        try:
            return return_county(County(name=name).save())
        except:
            raise
            return {"error": "Creating new county failed"}

    def update_county(self, code, name):
        if not isinstance(code, int):
             return {"error": "Invalid code found: "+ str(code)}
             
        elif not isinstance(name, str):
             return {"error": "Invalid name found: "+ str(name)} 

        county = self.county.get_one(code)
        county.name = name if name != "" else county.name

        try:
            return return_county(county.update())
        except:
            raise
            return {"error": "Updating county failed"}

    def delete_county(self, code):
        if not isinstance(code, int):
            return {"error": "Invalid code found: "+ str(code)}
        
        self.county.get_one(code).delete()