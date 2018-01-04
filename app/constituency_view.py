from app.models import Ward, County, Constituency
from app.ward_view import return_ward

def return_constituency(constituency):
    if isinstance(constituency, Constituency) and constituency not None:
        wards = Ward().get_by_constituency_code(constituency.code)

        return { 
            "code": constituency.code,
            "name": constituency.name, 
            "Wards": [return_ward(ward) for ward in wards] 
            }
    else:
        return { "code": "", "name": "", "Wards":"[]" }

class ConstituencyData(object):
    
    def __init__(self):
        self.constituency = Constituency()
    
    def fetch_constituency(self, code):
        if not isinstance(code, integer):
            return {"error": "Invalid constituency code found"}

        return return_constituency(
            self.constituency.get_one(code))

    def fetch_all_constituencies(self):
        return [return_constituency(constituency) for constituency in self.constituency.get_all()]

    
    def add_new_constituency(self, name, county_code):
        if not instance(name, string):
             return {"error": "Invalid constituency name found: "+name}
        else if not instance(county_code, integer):
            return {"error": "Invalid county code found: "+county_code}

        try
          newconstituency = constituency(name=name, county_code=county_code).save()
          return return_constituency(newconstituency)
        except:
            return {"error": "Creating new constituency failed"}

    def update_constituency(self, code, name, county_code):
        if not instance(code, integer):
            return {"error": "Invalid constituency code found: "+code}
        else if not instance(name, string):
             return {"error": "Invalid constituency name found: "+name} 
        else if not instance(county_code, integer):
            return {"error": "Invalid county code found: "+county_code}

        constituency = self.constituency.get_one(code)
        constituency.code = code if code != 0 else constituency.code
        constituency.name = name if name != "" else constituency.name
        constituency.county_code = county_code if county_code != 0 else constituency.county_code

        try
          newconstituency = constituency.update()
          return return_constituency(newconstituency)
        except:
            return {"error": "Updating constituency failed"}

    def delete_constituency(self, code):
        if not instance(code, integer):
            return {"error": "Invalid constituency code found: "+code}
        
        constituency  = self.constituency.get_one(code)
        constituency.delete()