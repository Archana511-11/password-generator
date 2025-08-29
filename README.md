# password-generator
This is a Python password generator script that creates passwords of varying complexity based on user input. Here's a detailed breakdown of how it works:
Function Definition
def generating_password(length, strength):
The function takes two parameters:

length: How many characters the password should contain
strength: The complexity level ("weak", "medium", or "strong")

Character Set Selection
The function uses different character sets based on the strength parameter:
Weak passwords (strength == "weak"):

Uses only lowercase letters (a-z)
Character set: string.ascii_lowercase
Example characters: abcdefghijklmnopqrstuvwxyz

Medium passwords (strength == "medium"):

Uses both uppercase and lowercase letters
Character set: string.ascii_letters
Example characters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

Strong passwords (strength == "strong"):

Uses letters, numbers, and special characters
Character set: string.ascii_letters + string.digits + string.punctuation
Example characters: All letters + 0123456789 + !"#$%&'()*+,-./:;<=>?@[]^_`{|}~

Password Generation Process

Creates an empty list password_chars = []
Loops length number of times
Each iteration randomly selects one character from the chosen character set using random.choice(chars)
Appends each selected character to the list
Joins all characters into a single string using ''.join(password_chars)

User Input and Execution

Prompts user for password length (converts to integer)
Prompts user for strength level (converts to lowercase for case-insensitive input)
Calls the function and prints the generated password

Error Handling
If an invalid strength is entered (anything other than "weak", "medium", or "strong"), the function returns "Invalid".
Example Usage
Enter the password length: 12
Enter strength of password: strong
Output: K#9mP@x2N$qL
