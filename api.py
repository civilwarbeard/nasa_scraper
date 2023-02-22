#Nasa-Updated
import requests
import json
import csv


#base URL - No key needed. Request format for category listing: https://technology.nasa.gov/api/query/patent/category/{category}
#format for individual records. https://technology.nasa.gov/api/query/patent/geturl/{tech_id}

url = "https://technology.nasa.gov/api/query/patent/"
tech_url = url + "geturl/"
category_url = url + "category/"

count = len(deduped_tech_ids)
nasa_tech_ids = []
nasa_individual_tech_ids = []

# Keys for each of the 15 NASA Patent Portfolio categories.
categories = [
    "communications",
    "electrical%20and%20electronics",
    "environment",
    "health%20medicine%20and%20biotechnology",
    "mechanical%20and%20fluid%20systems",
    "aerospace",
    "instrumentation",
    "manufacturing",
    "materials%20and%20coatings",
    "sensors",
    "optics",
    "information%20technology%20and%20software",
    "power%20generation%20and%20storage",
    "propulsion",
    "robotics%20automation%20and%20control"
]


#Get "tops ID" from the general category listing responses
for category in categories: 
    #request to NASA api
    new_url = url + category
    api_response = requests.get(new_url, allow_redirects=True)

    #Store response as raw data
    technologies = api_response.json()
    #store as list
    results = technologies["results"]
        
    nasa_tech_ids.append([ dict[1] for dict in results ])

#turn list of lists into one list
for element in nasa_tech_ids:
    if type(element) is list:
        # If the element is of type list, iterate through the sublist
        for item in element:
            nasa_individual_tech_ids.append(item)
    else:
        nasa_individual_tech_ids.append(element)

#De-dupe the list of Tech-IDs. (Nasa tech can have multiple categories but we just want to list them once for FLC Business)
deduped_tech_ids = [*set(nasa_individual_tech_ids)]

#Get full listings from nasa_record_id
with open("nasa.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(
        [
            "_id",
            "subtitle",
            "tech_desc",
            "publications",
            "cname",
            "cphone",
            "cemail",
            "application",
            "benefit",
            "trl",
            "id",
            "type",
            "center",
            "client_record_id",
            "reference_number",
            "patent_number",
            "license_fee",
            "annual_royalty",
            "license_term",
            "evaluation_fee",
            "evaluation_lic_term",
            "case_number",
            "title",
            "abstract",
            "category",
            "subcategory",
            "img1",
            "img2",
            "img3",
            "img4",
            "fig1",
            "fig2",
            "fig3",
            "fig4",
            "push_date",
            "erelations",
            
        ]
    )

	for nasa_id in deduped_tech_ids: 
    	new_url = url + nasa_id

    	api_response = requests.get(new_url, allow_redirects=True)
    
    	technology = api_response.json()
    	individual_tech = technology["results"]

    	writer.writerows(individual_tech)
    	print("Looks good! Record: " + nasa_id)

    print("All done! " + str(count))
