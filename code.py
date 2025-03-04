import random

def generate_random_text(length=6):
    # Generate a random string of digits of the specified length
    random_text = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return random_text

# Generate and print a random 6-digit string
random_text = generate_random_text()
print(f"Random 6-digit text: {random_text}")
