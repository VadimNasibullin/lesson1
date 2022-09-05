data = {
    "city": "Москва", 
    "temperature": "20"
    }
print(data["city"])
temp = int(data["temperature"])
print(temp-5)
print(data)  
print(data.get("country")) 
data["country"]= "Россия"
print(data["country"])
data["date"]="27.05.2019"
print(len(data))
