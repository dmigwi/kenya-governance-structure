from app.models import Ward

def return_ward(ward):
    if isinstance(ward, Ward) and ward is not None:
        return { "code": ward.code, "name": ward.name }
    else:
        return { "code": "", "name": ""}

class WardData(object):
    def __init__(self):
        self.ward = Ward()

    def fetch_ward(self, code):
        if not isinstance(code, int):
            return {"error": "Invalid ward code found"+ str(code)}

        return return_ward(
            self.ward.get_one(code))

    def fetch_all_wards(self):
        return [return_ward(ward) for ward in self.ward.get_all()]

    
    def add_new_ward(self, name, constituency_code):
        if not isinstance(name, str):
             return {"error": "Invalid ward name found: " + str(name)}

        elif not isinstance(constituency_code, int):
            return {"error": "Invalid constituency code found: "+ str(constituency_code)}

        try:
          newWard = Ward(name=name, constituency_code=constituency_code).save()
          return return_ward(newWard)
        except:
            return {"error": "Creating new ward failed"}

    def update_ward(self, code, name, constituency_code):
        if not isinstance(code, int):
            return {"error": "Invalid ward code found: "+ str(code)}
            
        elif not isinstance(name, str):
             return {"error": "Invalid ward name found: "+ str(name)} 

        elif not isinstance(constituency_code, int):
            return {"error": "Invalid constituency code found: "+ str(constituency_code)}

        ward = self.ward.get_one(code)
        ward.name = name if name != "" else ward.name
        ward.constituency_code = name if name != "" else ward.constituency_code

        try:
          newWard = ward.update()
          return return_ward(newWard)
        except:
            return {"error": "Updating ward failed"}

    def delete_ward(self, code):
        if not isinstance(code, int):
            return {"error": "Invalid ward code found: "+ str(code)}
        
        ward  = self.ward.get_one(code)
        ward.delete()