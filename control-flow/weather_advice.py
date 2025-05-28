respoanses =  input("Enter the weather condition (sunny, rainy, snowy): ").strip().lower()
if respoanses == "sunny":
    print("wear a t-shirt and sunglasses.")
elif respoanses == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif respoanses == "cold":
    print("Make sure to wear a warm coat and a scarf.") 
else:
    print("Sorry, I don't have recommendations for this weather. ")