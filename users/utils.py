import secrets
from users.models import *
from datetime import datetime
import pytz
from django.utils import timezone

def generate_token():
    token = secrets.token_hex(32)
    return token
 
def update_token(self,employee_id,api_token):
    token = Employees.objects.filter(id=employee_id).update(api_token=api_token) 
    return token

def login_update(self,employee_id):
   timezone = pytz.timezone('Asia/Kolkata')
   date=datetime.today()
   time =datetime.now(timezone)
   obj = TblEmployeeLogin.objects.create(employee_id=employee_id,login_date=date,login_time=time,created_at=time,updated_at=time)
   return obj



