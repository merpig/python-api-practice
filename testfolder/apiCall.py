import requests
import json

class ApiCall:
    def get_data(self,api,parameters):
        response = requests.get(f"{api}",params=parameters)
        if response.status_code == 200:
            print("successfully fetched data")
            self.formatted_print(response.json())
        else:
            print(f"Error: {response.status_code}")

    def get_link(self,gif):
        return gif["embed_url"]

    def formatted_print(self, obj):
        data = obj['data']
        mapped_data = list(map(self.get_link,data))
        text = json.dumps(mapped_data, sort_keys=True, indent=4)
        print(text)
        self.mapped_data = mapped_data
    
    def __init__(self,api,parameters):
        self.get_data(api,parameters)

    # def __call__(self):
    #     return self.mapped_data