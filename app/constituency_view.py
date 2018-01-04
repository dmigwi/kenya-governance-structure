from app.models import Ward, County, Constituency
from app.ward_view import return_ward

def return_constituency(constituency):
    if isinstance(constituency, Constituency) and constituency is not None:
        wards = Ward().get_by_constituency_code(constituency.code)

        return { 
            "code": constituency.code,
            "name": constituency.name, 
            "wards": [return_ward(ward) for ward in wards] 
            }
    else:
        return { "code": "", "name": "", "wards":"[]" }

class ConstituencyData(object):
    
    def __init__(self):
        self.constituency = Constituency()
    
    def fetch_constituency(self, code):
        if not isinstance(code, int):
            return {"error": "Invalid constituency code found"+ str(code)}

        return return_constituency(
            self.constituency.get_one(code))

    def fetch_all_constituencies(self):
        return [return_constituency(constituency) for constituency in self.constituency.get_all()]

    
    def add_new_constituency(self, name, county_code):
        if not isinstance(name, str):
             return {"error": "Invalid constituency name found: "+ str(name)}
        elif not isinstance(county_code, int):
            return {"error": "Invalid county code found: "+ str(county_code)}

        try:
          newconstituency = Constituency(name=name, county_code=county_code).save()
          return return_constituency(newconstituency)
        except:
            raise
            return {"error": "Creating new constituency failed"}

    def update_constituency(self, code, name, county_code):
        if not isinstance(code, int):
            return {"error": "Invalid constituency code found: "+ str(code)}

        elif not isinstance(name, str):
             return {"error": "Invalid constituency name found: "+ str(name)} 

        elif not isinstance(county_code, int):
            return {"error": "Invalid county code found: "+ str(county_code)}

        constituency = self.constituency.get_one(code)
        constituency.name = name if name != "" else constituency.name
        constituency.county_code = county_code if county_code != 0 else constituency.county_code

        try:
          newconstituency = constituency.update()
          return return_constituency(newconstituency)
        except:
            return {"error": "Updating constituency failed"}

    def delete_constituency(self, code):
        if not isinstance(code, int):
            return {"error": "Invalid constituency code found: "+ str(code)}
        
        constituency  = self.constituency.get_one(code)
        constituency.delete()