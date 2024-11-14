# Predefined phone number and ID for validation
valid_phone_number = "0112284093"
valid_id = "123456789"

# Loop for user input and validation
while True:
    # Prompt user for phone number and ID
    phone_number = input("Enter your phone number: ")
    user_id = input("Enter your ID: ")

    # Check if the entered phone number and ID match the valid ones
    if phone_number == valid_phone_number and user_id == valid_id:
        print("Access granted.")
        break  # Exit the loop if access is granted
    else:
        print("Incorrect, please try again.")
