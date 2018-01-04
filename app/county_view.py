from app.models import County, Constituency
from app.constituency_view import return_constituency

def return_county(county):
    if isinstance(county, County) and county not None:
        constituencies = Constituency().get_by_county_code(county.code)

        return { 
            "code": county.code,
            "name": county.name, 
            "Constituencies": [return_constituency(constituency) for constituency in constituencies] 
            }
    else:
        return { "code": "", "name": "", "Constituencies":"[]" }

class CountyData(object):
    
    def __init__(self):
        self.county = County()
    
    def fetch_county(self, code):
        if not isinstance(code, integer):
            return {"error": "Invalid code found"}

        return return_county(self.county.get_one(code))

    def fetch_all_counties(self):
        return [return_county(county) for county in self.county.get_all()]

    
    def add_new_county(self, name):
        if not instance(name, string):
            return {"error": "Invalid name found: "+name}

        try
            return return_county(county(code=code, name=name).save())
        except:
            return {"error": "Creating new county failed"}

    def update_county(self, code, name):
        if not instance(code, integer):
             return {"error": "Invalid code found: "+code}
             
        else if not instance(name, string):
             return {"error": "Invalid name found: "+name} 

        county = self.county.get_one(code)
        county.code = code if code != 0 else county.code
        county.name = name if name != "" else county.name

        try
            return return_county(county.update())
        except:
            return {"error": "Updating county failed"}

    def delete_county(self, code):
        if not instance(code, integer):
            return {"error": "Invalid code found: "+code}
        
        self.county.get_one(code).delete()