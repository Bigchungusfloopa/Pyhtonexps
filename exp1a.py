def personalized_greeting():
    name = input("Enter your name: ")
    occasion = input("Enter the occasion (e.g., Birthday, Graduation, etc.): ")
    
    greeting = f"Hello {name}! Wishing you a wonderful {occasion}! May your day be filled with joy and happiness!"
    
    print("\n" + greeting)

# Run the greeting function
personalized_greeting()
