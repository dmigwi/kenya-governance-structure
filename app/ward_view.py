from app.models import Ward

def return_ward(ward):
    if isinstance(ward, Ward) and ward not None:
        return { "code": ward.code, "name": ward.name }
    else:
        return { "code": "", "name": ""}

class WardData(object):
    def __init__():
        self.ward = Ward()

    def fetch_ward(self, code):
        if not isinstance(code, integer):
            return {"error": "Invalid ward code found"}

        return return_ward(
            self.ward.get_one(code))

    def fetch_all_wards(self):
        return [return_ward(ward) for ward in self.ward.get_all()]

    
    def add_new_ward(self, name, constituency_code):
        if not instance(name, string):
             return {"error": "Invalid ward name found: "+name}

        else if not instance(constituency_code, integer):
            return {"error": "Invalid constituency code found: "+constituency_code}

        try
          newWard = Ward(code=code, name=name, 
          constituency_code=constituency_code).save()
          return return_ward(newWard)
        except:
            return {"error": "Creating new ward failed"}

    def update_ward(self, code, name, constituency_code):
        if not instance(code, integer):
            return {"error": "Invalid ward code found: "+code}
            
        else if not instance(name, string):
             return {"error": "Invalid ward name found: "+name} 

        else if not instance(constituency_code, integer):
            return {"error": "Invalid constituency code found: "+constituency_code}

        ward = self.ward.get_one(code)
        ward.code = code if code != 0 else ward.code
        ward.name = name if name != "" else ward.name
        ward.constituency_code = name if name != "" else ward.constituency_code

        try
          newWard = ward.update()
          return return_ward(newWard)
        except:
            return {"error": "Updating ward failed"}

    def delete_ward(self, code):
        if not instance(code, integer):
            return {"error": "Invalid ward code found: "+code}
        
        ward  = self.ward.get_one(code)
        ward.delete()