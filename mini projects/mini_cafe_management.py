 '''-------------------------------------------------- Mini Cafe Management ------------------------------------------------------s-----'''

print("Welcome to our Mini Cafe !! \U00002615 \U0001F60A")

# Menu Card
menu_card={
    "PIZZA":130,
    "BURGER":50,
    "DOSA":90,
    "COFFEE":70,
    "TEA":30    
}


print(f"Menu Card - {menu_card} ")

# checking order - available in Menu Card
def check_order(od_itm):
    if od_itm in menu_card.keys():
        return "Yes"
    return "No" 

customer_record={'name':[], 'order':[]}
customer_name=input("Please enter your name: ")


# Storing in our customer record
customer_record['name'].append(customer_name)
total_order={}

# Taking order from customer
def take_order():
    order_itm=input("\U0001F449 What do you want to order? ") 
    return order_itm.upper()

# Processing the order
def process_order(menu_card, total_order):
    total_amount=0
    s_gst=0.05 # 5%
    gst=0.05 #5%
    for item, qty in total_order.items():
        total_amount+=menu_card[item]*qty # total_amount=0+130*3=390
        # total_amount=390+30*2=450
        total_bill=(0.05/total_amount)*100
    print("Congrats! Your order has been processed \U0001F60D")
    print(f"Your total bill amount is {total_amount} ")

while True:
    order_item=take_order() # PIZZA
    print(order_item)
    item_available=check_order(order_item)
    print(item_available) # Yes
    if item_available == "Yes":
        quantity=int(input("Sure, What's the quantity? ")) 
        total_order[order_item]=quantity # d[key]=value
        print(total_order) # {'PIZZA': 3}
        customer_record["order"].append(order_item)
        more_order=input("Your order has been added successfully \U0001F60A\nDo you want anything else? \U0001F914 Yes or No ")
        if more_order!="Yes":
            break
    else:
        other_order=input("Opps!!, Your ordered item is not available in our \U0001F4CB !! \nDo you want something else? \U0001F914 Yes or No ")
        if other_order=="Yes":
            pass
        else:
            print("Have a nice day!!")
            break


if len(total_order)>0:
    process_order(menu_card,total_order)
print("Thank you for visiting !! \U0001F60A")


rating_card={
    1: ["Bad"],
    2:["Average","\U0001F633"],
    3:"Good",
    4:"Very Good",
    5:"Excellent"
}

print(rating_card)
rating=int(input("Please provide a rating between 1 to 5: "))
print(rating_card[rating][0], rating_card[rating][1])

feedback=input("Please provide us feedback..")
print(customer_record)












