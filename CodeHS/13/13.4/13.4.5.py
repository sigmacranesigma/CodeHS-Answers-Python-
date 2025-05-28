phones = {}

while True:
    name = input("Enter your name (or press Enter to quit): ").strip()
    if not name:
        break

    if name in phones:
        print(f"{name}'s number is: {phones[name]}")
    else:
        phone = input("Enter Number: ").strip()

        # Remove existing dashes to count digits only
        digits_only = phone.replace("-", "")

        if len(digits_only) == 10 and digits_only.isdigit():
            # Format as XXX-XXX-XXXX
            phone_formatted = digits_only[:3] + '-' + digits_only[3:6] + '-' + digits_only[6:]
        else:
            # Not 10 digits: just strip all dashes
            phone_formatted = digits_only

        phones[name] = phone_formatted
print(phones)
