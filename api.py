##NASA API req's
import requests
import json
import csv


#base URL - No key needed. Request format: http://technology.nasa.gov/api/query/patent/{category}
url = "http://technology.nasa.gov/api/query/patent/"

#categories probably won't be updated often but potentially will need updating in future
categories = ["rocket", "communications", "electronics", "environment", "medicine", "mechanical", "aerospace",
			  "instrumentation", "manufacturing", "materials", "sensors", "optics", "instrumenation", "software", 
			  "power", "propulsion", "robotics"]

#open blank csv file loop through categories and write to file
with open("nasa.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "internal_ref", "name", "abstract", "another_ref",
                    "categories", "unsure", "unsure", "unsure", "code", "url", 
                     "unsure"])
    
    for category in categories: 
        #request to NASA api
        new_url = url + category
        api_response = requests.get(new_url, allow_redirects=True)

        #Store response as raw data
        technologies = api_response.json()
        print(new_url)

        #turn dict into list of lists to iterate through
        list_technologies = technologies["results"]

    writer.writerows(list_technologies)
