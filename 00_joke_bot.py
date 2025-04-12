PROMPT = "What do you want? "
JOKE = "Here is a joke for you! A programmer’s wife tells him: 'Go to the store and buy a loaf of bread. If they have eggs, buy a dozen.' The programmer comes back with 13 loaves of bread. The wife asks, 'Why did you buy so much bread?' The programmer replies, 'Because they had eggs!'"
SORRY = "Sorry, I only tell jokes."

def main():
    user_input = input(PROMPT)  
    user_input = user_input.strip().lower()
    
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()




