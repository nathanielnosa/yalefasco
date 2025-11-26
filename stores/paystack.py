import requests
from django.conf import settings

class Paystack:
    PAYSTACK_SECRETE_KEY = settings.PAYSTACK_SECRETE_KEY
    base_url = "https://api.paystack.co"

    def verify_payment(self,ref,*args, **kwargs):
        path = f"/transaction/verify/{ref}"
        headers ={
            "Authorization": f"Bearer {self.PAYSTACK_SECRETE_KEY}",
            "Content-Type": "application/json",
        }
        url = self.base_url + path
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("data"):
                return True, response_data["data"]
            else:
                return False, response_data.get("message", "Verification failed")
        else:
            return False, f"HTTP Error: {response.status_code}"
        




        

