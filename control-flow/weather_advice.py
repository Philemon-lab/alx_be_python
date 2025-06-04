weather= input("What's the weather like today? (sunny, rainy, snowy):").lower()
if weather == "sunny":
    print("wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Dont't forget your umbrella and wear a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarg.")
else:
    print("Sorry, I dont't have recommendations for that weather.")