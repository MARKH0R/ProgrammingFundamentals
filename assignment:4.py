companyList = [ 
    {
        "Company Name": "Roshan",
        "Company Motto": "Roshan began operations in 2003 in an environment where there was virtually no telecommunications infrastructure.",
        "City": "Kabul",
        "Country": "Afghanistan",
        "Contact": {
            "Phone Number": "+93 79 997 1333",
            "Email": "roshanca@roshan.af",
            "Website": "http://www.roshan.af/"
        },
        "Social Accounts": {
            "Facebook": "https://www.facebook.com/RoshanConnects",
            "Twitter": "https://www.twitter.com/roshanconnects",
            "LinkedIn": "https://www.linkedin.com/company/roshan"
        }
    }, 
    {
        "Company Name": "Gjirafa",
        "Company Motto": "Gjirafa is a video content and e-commerce platform for the Balkans built on top of an Albanian language specialized search engine.",
        "City": "Tirana",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "37744991206",
            "Email": "info@gjirafa.com",
            "Website": "http://www.gjirafa.com/"
        },
        "Social Accounts": {
            "Facebook": "http://www.facebook.com/gjirafa",
            "Twitter": "https://twitter.com/gjirafashqip",
            "LinkedIn": "https://www.linkedin.com/company/gjirafa-inc-"
        }
    },
    {
        "Company Name": "Shqiperia Com",
        "Company Motto": "ShqiperiaCom primarily provides web developing services and consultancy in the region of Balkan.",
        "City": "Tirana",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "35542403910",
            "Email": "mandi@shqiperia.com",
            "Website": "http://www.shqiperiacom.info"
        },
        "Social Accounts": {
            "Facebook": "https://www.facebook.com/shqiperiacom",
            "Twitter": "http://twitter.com/ShqiperiaCom",
            "LinkedIn": "https://www.linkedin.com/company/shqiperiacom"
        }
    }
]







# Your code for get_companies_names goes here
def get_companies_names(x):
    z=[]
    if x==[]:
    	return []
    for i in range(0,len(x)) :
        a=x[i]['Company Name']
        z.append(a)
    return z







# Your code for get_countries goes here
def get_countries (companyList):
    if companyList==[] :
        return {}
    b=0
    a = 0
    counting=0
    count =0                           # this function if fale for get_countries(companyList) == {'Afghanistan': 1, 'Albania': 2}
    for i in companyList:              # but pass for index list only  
        if i["Country"]   and i["Company Name"]:
            a= i["Country"]
            counting += 1
        if i["Country"] and i["Company Name"]:
            b= i["Country"]
            count += 1
    return {a:counting,b:count}




# Your code for get_companies goes here
def get_companies(companyList, location):
    
    city_list= []
    
    for i in companyList:
        if location["city"] == i["City"]:
            city_list.append(i["Company Name"])
    if len(city_list) ==0:
        return None
    else:
    	return city_list
    	
    	
    	
