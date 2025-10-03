from pyscript import display

#list
resto_name = "Snorlet" #string
owner = 'Althea Francisco'       #string
year_founded = 1992              #integer
popular_item_price = "₱230"      #string
has_delivery = True              #Boolean
food_names = ["Pesto Pasta", "Tomato Premium Pasta", "Scallop Salad", "Leche Flan Special", "Grape Juice"] # List of Strings
business_hours = "6:00 AM to 12:00 AM"   #string
common_allergens = ["Seafood(Scallops)", "Dairy", "Tomato"] #list
tax_rate = 0.8 #float

menu_prices = {                    #prices of each product
    "Pesto Pasta": 170,
    "Tomato Premium Pasta": 220,
    "Scallop Pasta": 230,
    "Leche Flan Special": 60.00,
    "Grape Juice": 40.00
}
#display code
display(resto_name, target="storeName")
display(f"Owner: {owner}", target="ownerName")
display(f"Est. {year_founded}", target="yearFounded")
display(f"Popular Item Price: {popular_item_price}", target="popularPrice")
display(f"Business Hours: {business_hours}", target="storeHours")

