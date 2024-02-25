def is_palindrome(s):
    s = ''.join(s.split()).lower()
    return s == s[::-1]

num_test_cases = int(input("Enter the number of test cases: "))

for _ in range(num_test_cases):
    user_input = input("Enter a string: ")
    result = "Palindrome!" if is_palindrome(user_input) else "Not a palindrome."
    print(f"{user_input}: {result}")